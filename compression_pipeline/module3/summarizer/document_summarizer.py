"""
Level 3 — Document Summarizer (Hybrid: Extractive + Abstractive)

Produces document-level summaries (≤200 tokens) by:
1. Collecting section summaries from Level 4.
2. Extracting the most important sentences (extractive pass).
3. Refining with BART abstractive model, guided by top entities and relationships.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Lazy model singleton
# ---------------------------------------------------------------------------
_MODEL = None
_TOKENIZER = None


def _get_summarizer():
    """Return cached (tokenizer, model) for DistilBART summarization."""
    global _MODEL, _TOKENIZER
    if _MODEL is None:
        logger.info("Loading abstractive summarization model (DistilBART)...")
        model_name = "sshleifer/distilbart-cnn-12-6"
        _TOKENIZER = AutoTokenizer.from_pretrained(model_name)
        _MODEL = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        _MODEL.eval()
    return _TOKENIZER, _MODEL


def _run_summarizer(text: str, max_length: int = 200, min_length: int = 50) -> str:
    """Run abstractive summarization using the cached model."""
    tokenizer, model = _get_summarizer()
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=max_length,
        min_length=min_length,
        num_beams=4,
        length_penalty=2.0,
        early_stopping=True,
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _count_tokens(text: str) -> int:
    return len(text.split())


def _extract_top_entities(
    chunks: List[Dict[str, Any]],
    top_n: int = 10,
) -> List[str]:
    """Return the *top_n* most frequent entities across all chunks."""
    freq: Dict[str, int] = {}
    for chunk in chunks:
        for entity in chunk.get("entities", []):
            key = entity if isinstance(entity, str) else str(entity)
            freq[key] = freq.get(key, 0) + 1
    sorted_entities = sorted(freq, key=freq.get, reverse=True)  # type: ignore[arg-type]
    return sorted_entities[:top_n]


def _extract_important_relationships(
    chunks: List[Dict[str, Any]],
    top_n: int = 5,
) -> List[Dict[str, str]]:
    """Return top relationships ordered by source-chunk importance score."""
    scored: List[tuple] = []
    for chunk in chunks:
        imp = chunk.get("importance_score", 0.0)
        for rel in chunk.get("relationships", []):
            scored.append((imp, rel))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [r for _, r in scored[:top_n]]


def _build_entity_hint(entities: List[str]) -> str:
    """Create a natural-language hint listing must-include entities."""
    if not entities:
        return ""
    return "Key entities: " + ", ".join(entities) + ". "


def _build_relationship_hint(relationships: List[Dict[str, str]]) -> str:
    """Create a hint encoding important relationships."""
    if not relationships:
        return ""
    parts = []
    for rel in relationships:
        src = rel.get("source", rel.get("subject", ""))
        tgt = rel.get("target", rel.get("object", ""))
        label = rel.get("relation", rel.get("predicate", "related to"))
        if src and tgt:
            parts.append(f"{src} {label} {tgt}")
    if not parts:
        return ""
    return "Important relationships: " + "; ".join(parts) + ". "


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def summarize_document(
    doc: Dict[str, Any],
    section_summaries: List[Dict[str, Any]],
    max_tokens: int = 200,
) -> Dict[str, Any]:
    """Produce a hybrid summary for a single document.

    Parameters
    ----------
    doc : dict
        Original document object (with ``doc_id``, ``sections``).
    section_summaries : list[dict]
        Level-4 summaries whose ``doc_id`` matches this document.
    max_tokens : int
        Maximum token budget.

    Returns
    -------
    dict
        ``{"doc_id": str, "summary": str, "top_entities": list,
          "top_relationships": list, "token_count": int}``
    """
    doc_id: str = doc.get("doc_id", "unknown")

    # Gather all chunks from the document
    all_chunks: List[Dict[str, Any]] = []
    for section in doc.get("sections", []):
        all_chunks.extend(section.get("chunks", []))

    # Top entities & relationships
    top_entities = _extract_top_entities(all_chunks, top_n=10)
    top_relationships = _extract_important_relationships(all_chunks, top_n=5)

    # Combine section summaries as extractive base
    combined_text = " ".join(s.get("summary", "") for s in section_summaries if s.get("summary"))
    if not combined_text.strip():
        return {
            "doc_id": doc_id,
            "summary": "",
            "top_entities": top_entities,
            "top_relationships": top_relationships,
            "token_count": 0,
        }

    # Prepend entity / relationship hints so the model is nudged to preserve them
    entity_hint = _build_entity_hint(top_entities)
    rel_hint = _build_relationship_hint(top_relationships)
    input_text = entity_hint + rel_hint + combined_text

    # Truncate input to model max (BART accepts up to 1024 tokens)
    input_tokens = input_text.split()
    if len(input_tokens) > 1024:
        input_text = " ".join(input_tokens[:1024])

    # Abstractive refinement
    try:
        summary = _run_summarizer(
            input_text,
            max_length=max_tokens,
            min_length=max(10, max_tokens // 4),
        )
    except Exception as exc:
        logger.warning("Abstractive summarization failed for %s: %s — falling back to truncation", doc_id, exc)
        summary = " ".join(combined_text.split()[:max_tokens])

    return {
        "doc_id": doc_id,
        "summary": summary,
        "top_entities": top_entities,
        "top_relationships": top_relationships,
        "token_count": _count_tokens(summary),
    }


def summarize_documents(
    documents: List[Dict[str, Any]],
    level_4_sections: List[Dict[str, Any]],
    max_tokens: int = 200,
) -> List[Dict[str, Any]]:
    """Summarize every document (Level 3).

    Parameters
    ----------
    documents : list[dict]
        Original document objects.
    level_4_sections : list[dict]
        All section summaries from Level 4.
    max_tokens : int
        Per-document token budget.

    Returns
    -------
    list[dict]
        One summary dict per document.
    """
    # Index section summaries by doc_id
    sec_by_doc: Dict[str, List[Dict[str, Any]]] = {}
    for sec in level_4_sections:
        did = sec.get("doc_id", "unknown")
        sec_by_doc.setdefault(did, []).append(sec)

    results: List[Dict[str, Any]] = []
    for doc in documents:
        doc_id = doc.get("doc_id", "unknown")
        doc_sections = sec_by_doc.get(doc_id, [])
        summary = summarize_document(doc, doc_sections, max_tokens=max_tokens)
        results.append(summary)
        logger.info("Document %s: %d tokens", doc_id, summary["token_count"])
    return results