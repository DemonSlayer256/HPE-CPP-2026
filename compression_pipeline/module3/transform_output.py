"""
Module 3 — Output Transformer

Reads integration_output.json and transforms the level_4_sections into a
clean, structured hierarchical summarization format with:
  - Duplicate sentence removal
  - Boilerplate stripping
  - UUID assignment
  - Compression ratio calculation
  - AKU deduplication

Usage:
    python module3/transform_output.py
    python module3/transform_output.py --input integration_output.json --output structured_output.json
"""

import json
import uuid
import re
import argparse
import os
from typing import Any, Dict, List


# ---------------------------------------------------------------------------
# Boilerplate patterns to remove
# ---------------------------------------------------------------------------
BOILERPLATE_PATTERNS = [
    r"Amazon S3 Amazon Simple Storage Service API Reference\.?",
    r"Amazon Simple Storage Service API Reference\.?",
    r"Storage Service API Reference",
    r"These endpoints support\b.*?\.",
    r"Request Syntax\b.*?\.",
    r"Response Syntax\b.*?\.",
    r"See Also\b.*?\.",
    r"Welcome Welcome to the",
    r"For more information,?\s*see\s+[A-Z][^.]*\.",
    r"For information about\s+[^.]*\.",
    r"The following\s+(?:example|table|diagram)\s+[^.]*\.",
]

COMPILED_BOILERPLATE = [re.compile(p, re.IGNORECASE) for p in BOILERPLATE_PATTERNS]

# Category keywords for classifying sections
CATEGORY_KEYWORDS = {
    "security": ["permission", "iam", "policy", "encrypt", "auth", "access control", "credential", "acl"],
    "storage": ["bucket", "object", "storage class", "glacier", "s3 standard", "tier"],
    "networking": ["endpoint", "vpc", "dns", "hostname", "region", "transfer"],
    "api": ["api", "request", "response", "header", "http", "rest", "sdk"],
    "configuration": ["config", "setting", "lifecycle", "versioning", "replication", "logging"],
    "operational": ["copy", "delete", "put", "get", "list", "upload", "download", "multipart"],
    "contextual": [],  # default fallback
}


# ---------------------------------------------------------------------------
# Text cleaning helpers
# ---------------------------------------------------------------------------

def _split_sentences(text: str) -> List[str]:
    """Split text into sentences using regex."""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in sentences if s.strip()]


def _remove_boilerplate(text: str) -> str:
    """Strip known boilerplate patterns."""
    for pattern in COMPILED_BOILERPLATE:
        text = pattern.sub("", text)
    return text.strip()


def _deduplicate_sentences(sentences: List[str]) -> List[str]:
    """Remove exact duplicate sentences, preserving order."""
    seen = set()
    result = []
    for s in sentences:
        normalized = re.sub(r'\s+', ' ', s.strip().lower())
        if normalized not in seen and len(normalized) > 5:
            seen.add(normalized)
            result.append(s.strip())
    return result


def _merge_similar_sentences(sentences: List[str], threshold: float = 0.85) -> List[str]:
    """Remove near-duplicate sentences using word overlap ratio."""
    if not sentences:
        return []

    result = [sentences[0]]
    for s in sentences[1:]:
        s_words = set(s.lower().split())
        is_duplicate = False
        for existing in result:
            e_words = set(existing.lower().split())
            if not s_words or not e_words:
                continue
            overlap = len(s_words & e_words) / max(len(s_words), len(e_words))
            if overlap >= threshold:
                # Keep the longer one
                if len(s) > len(existing):
                    result.remove(existing)
                    result.append(s)
                is_duplicate = True
                break
        if not is_duplicate:
            result.append(s)
    return result


def _filter_noise_sentences(sentences: List[str]) -> List[str]:
    """Remove short fragments, headers, and non-informative sentences."""
    noise_patterns = [
        r'^\s*$',
        r'^(Required|Optional|Type|Default|Valid Values|Constraints):?\s*$',
        r'^\d+\s*$',
        r'^[A-Z][a-z]+\s*$',  # Single word headers
    ]
    compiled = [re.compile(p) for p in noise_patterns]
    result = []
    for s in sentences:
        if len(s.split()) < 3:
            continue
        if any(p.match(s) for p in compiled):
            continue
        result.append(s)
    return result


def _classify_category(text: str) -> str:
    """Classify section into a category based on keyword matching."""
    lower = text.lower()
    scores = {}
    for cat, keywords in CATEGORY_KEYWORDS.items():
        if not keywords:
            continue
        scores[cat] = sum(1 for kw in keywords if kw in lower)
    if not scores or max(scores.values()) == 0:
        return "contextual"
    return max(scores, key=scores.get)


def clean_summary_text(raw_text: str) -> str:
    """Full cleaning pipeline: boilerplate → split → dedup → noise → merge → rejoin."""
    # Step 1: Remove boilerplate
    text = _remove_boilerplate(raw_text)

    # Step 2: Split into sentences
    sentences = _split_sentences(text)

    # Step 3: Remove exact duplicates
    sentences = _deduplicate_sentences(sentences)

    # Step 4: Filter noise/fragments
    sentences = _filter_noise_sentences(sentences)

    # Step 5: Remove near-duplicates (redundancy merging)
    sentences = _merge_similar_sentences(sentences, threshold=0.75)

    # Step 6: Rejoin
    cleaned = " ".join(sentences)

    # Step 7: Clean up extra whitespace
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()

    return cleaned


# ---------------------------------------------------------------------------
# AKU cleaning
# ---------------------------------------------------------------------------

def clean_akus(akus: List) -> List:
    """Deduplicate AKUs and format them consistently."""
    seen = set()
    cleaned = []
    for aku in akus:
        if isinstance(aku, list):
            key = tuple(str(x).lower().strip() for x in aku)
            if key not in seen:
                seen.add(key)
                cleaned.append(aku)
        elif isinstance(aku, dict):
            key = (
                aku.get("subject", "").lower().strip(),
                aku.get("predicate", "").lower().strip(),
                aku.get("object", "").lower().strip(),
            )
            if key not in seen:
                seen.add(key)
                cleaned.append(aku)
    return cleaned


# ---------------------------------------------------------------------------
# Entity / AKU ID generation
# ---------------------------------------------------------------------------

_entity_id_cache: Dict[str, str] = {}
_aku_counter = 0


def _entity_to_id(entity: str) -> str:
    """Convert entity name to a stable short ID like 'ent_s3'."""
    if entity in _entity_id_cache:
        return _entity_id_cache[entity]
    # Create readable ID from entity name
    slug = re.sub(r'[^a-z0-9]+', '_', entity.lower()).strip('_')
    eid = f"ent_{slug}"
    _entity_id_cache[entity] = eid
    return eid


def _aku_to_id(index: int) -> str:
    """Generate AKU ID like 'aku_0', 'aku_1', etc."""
    return f"aku_{index}"


# ---------------------------------------------------------------------------
# Main transformer
# ---------------------------------------------------------------------------

def transform_section(
    section: Dict[str, Any],
    parent_doc_uuid: str,
    aku_start_index: int,
) -> tuple:
    """Transform a single level_4 section into the structured output format.

    Returns (transformed_dict, next_aku_index).
    """
    raw_summary = section.get("summary", "")
    cleaned_text = clean_summary_text(raw_summary)
    raw_entities = list(dict.fromkeys(section.get("preserved_entities", [])))
    raw_akus = clean_akus(section.get("preserved_akus", []))

    # Generate entity IDs
    entity_ids = [_entity_to_id(e) for e in raw_entities]

    # Generate AKU IDs
    aku_ids = []
    for i, _ in enumerate(raw_akus):
        aku_ids.append(_aku_to_id(aku_start_index + i))
    next_aku_index = aku_start_index + len(raw_akus)

    # Extract source chunk IDs from the section's chunks
    chunk_ids = []
    for chunk in section.get("chunks", []):
        chunk_ids.append(chunk.get("chunk_id", ""))
    if not chunk_ids:
        # Derive from section_id if chunks not available
        sec_id = section.get("section_id", "unknown")
        sec_num = re.search(r'\d+', sec_id)
        if sec_num:
            chunk_ids = [f"chunk_{int(sec_num.group()):03d}"]

    # Compression ratio
    original_len = len(raw_summary)
    cleaned_len = len(cleaned_text)
    compression_ratio = round(cleaned_len / original_len, 3) if original_len > 0 else 0.0

    # Classify category
    category = _classify_category(cleaned_text)

    doc_id = section.get("doc_id", "unknown")
    doc_name = doc_id.replace("-", "-").replace("_", "-")
    if "S3" in doc_id or "s3" in doc_id:
        doc_name = "AWS-S3-Guide"

    result = {
        "summary_id": str(uuid.uuid4()),
        "level": 4,
        "level_name": "section",
        "text": cleaned_text,
        "token_count": len(cleaned_text.split()),
        "source_chunk_ids": chunk_ids,
        "source_document": doc_name,
        "heading_path": [],
        "category": category,
        "preserved_akus": aku_ids,
        "preserved_entities": entity_ids,
        "compression_ratio": compression_ratio,
        "parent_summary_id": parent_doc_uuid,
        "child_summary_ids": [],
    }

    return result, next_aku_index


def transform_output(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """Transform the full integration output into structured format."""
    sections = input_data.get("level_4_sections", [])

    # Generate a stable parent document UUID
    parent_doc_uuid = str(uuid.uuid4())

    transformed = []
    aku_index = 0
    for section in sections:
        result, aku_index = transform_section(section, parent_doc_uuid, aku_index)
        transformed.append(result)

    return {"level_4": transformed}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Transform Module 3 output into clean structured format"
    )
    parser.add_argument(
        "--input", "-i",
        default="integration_output.json",
        help="Path to integration_output.json",
    )
    parser.add_argument(
        "--output", "-o",
        default="structured_output.json",
        help="Path for the structured output file",
    )
    args = parser.parse_args()

    print(f"Reading: {os.path.abspath(args.input)}")
    with open(args.input, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    print(f"Transforming {len(input_data.get('level_4_sections', []))} sections...")
    result = transform_output(input_data)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    # Print summary
    print(f"\nTransformation Complete!")
    print(f"  Output: {os.path.abspath(args.output)}")
    print(f"  Sections: {len(result['level_4'])}")

    total_original = sum(s.get("token_count", 0) for s in input_data.get("level_4_sections", []))
    total_cleaned = sum(s["token_count"] for s in result["level_4"])
    avg_ratio = sum(s["compression_ratio"] for s in result["level_4"]) / len(result["level_4"])

    print(f"  Original tokens: {total_original}")
    print(f"  Cleaned tokens:  {total_cleaned}")
    print(f"  Avg compression: {avg_ratio:.2%}")


if __name__ == "__main__":
    main()
