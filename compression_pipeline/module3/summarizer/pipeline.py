"""
Pipeline Orchestrator

Runs the full hierarchical summarization pipeline:
    Level 4 (sections) → Level 3 (documents) → Level 2 (topics) →
    Level 1 (categories) → Level 0 (global)

Validates each level after generation and returns the complete output
together with validation reports.
"""

from __future__ import annotations

import logging
import time
from typing import Any, Dict, List

from summarizer.section_summarizer import summarize_sections
from summarizer.document_summarizer import summarize_documents
from summarizer.topic_summarizer import summarize_topics
from summarizer.category_summarizer import summarize_categories
from summarizer.global_summarizer import generate_global_summary
from summarizer.validator import validate_summary

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _collect_all_entities(documents: List[Dict[str, Any]]) -> List[str]:
    """Flatten all entities from all chunks in all documents."""
    entities: List[str] = []
    for doc in documents:
        for section in doc.get("sections", []):
            for chunk in section.get("chunks", []):
                entities.extend(chunk.get("entities", []))
    return list(dict.fromkeys(entities))


def _collect_all_relationships(documents: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """Flatten all relationships from all chunks."""
    rels: List[Dict[str, str]] = []
    for doc in documents:
        for section in doc.get("sections", []):
            for chunk in section.get("chunks", []):
                rels.extend(chunk.get("relationships", []))
    return rels


def _collect_all_akus(documents: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """Flatten all AKUs from all chunks."""
    akus: List[Dict[str, str]] = []
    for doc in documents:
        for section in doc.get("sections", []):
            for chunk in section.get("chunks", []):
                akus.extend(chunk.get("akus", []))
    return akus


def _collect_source_text(documents: List[Dict[str, Any]]) -> str:
    """Concatenate all chunk texts for numerical accuracy checking."""
    parts: List[str] = []
    for doc in documents:
        for section in doc.get("sections", []):
            for chunk in section.get("chunks", []):
                parts.append(chunk.get("text", ""))
    return " ".join(parts)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def run_pipeline(
    input_data: Dict[str, Any],
    *,
    level_4_max_tokens: int = 500,
    level_3_max_tokens: int = 200,
    level_2_max_tokens: int = 100,
    level_1_max_tokens: int = 50,
    level_0_max_tokens: int = 25,
) -> Dict[str, Any]:
    """Execute the full hierarchical summarization pipeline.

    Parameters
    ----------
    input_data : dict
        The combined output of Module 1 (chunking) and Module 2 (topics),
        containing ``documents``, ``topics``, and ``categories``.

    Returns
    -------
    dict
        Keys: ``level_4_sections``, ``level_3_documents``, ``level_2_topics``,
        ``level_1_categories``, ``level_0_global``, ``validation_reports``,
        ``timing``.
    """
    documents: List[Dict[str, Any]] = input_data.get("documents", [])
    topics_input: List[Dict[str, Any]] = input_data.get("topics", [])
    categories_input: Dict[str, List[str]] = input_data.get("categories", {})

    all_entities = _collect_all_entities(documents)
    all_relationships = _collect_all_relationships(documents)
    all_akus = _collect_all_akus(documents)
    source_text = _collect_source_text(documents)

    validation_reports: Dict[str, Any] = {}
    timing: Dict[str, float] = {}

    # ---- Level 4: Section summaries ----
    logger.info("=" * 60)
    logger.info("LEVEL 4 — Section Summaries (extractive, ≤%d tokens)", level_4_max_tokens)
    logger.info("=" * 60)
    t0 = time.time()
    level_4 = summarize_sections(documents, max_tokens=level_4_max_tokens)
    timing["level_4"] = round(time.time() - t0, 3)

    # Validate each section summary
    for sec in level_4:
        vr = validate_summary(
            sec.get("summary", ""),
            entities=sec.get("preserved_entities"),
            akus=sec.get("preserved_akus"),
            source_text=source_text,
        )
        validation_reports[f"L4_{sec.get('section_id', '')}"] = vr

    # ---- Level 3: Document summaries ----
    logger.info("=" * 60)
    logger.info("LEVEL 3 — Document Summaries (hybrid, ≤%d tokens)", level_3_max_tokens)
    logger.info("=" * 60)
    t0 = time.time()
    level_3 = summarize_documents(documents, level_4, max_tokens=level_3_max_tokens)
    timing["level_3"] = round(time.time() - t0, 3)

    for doc_sum in level_3:
        vr = validate_summary(
            doc_sum.get("summary", ""),
            entities=doc_sum.get("top_entities"),
            relationships=doc_sum.get("top_relationships"),
            source_text=source_text,
        )
        validation_reports[f"L3_{doc_sum.get('doc_id', '')}"] = vr

    # ---- Level 2: Topic summaries ----
    logger.info("=" * 60)
    logger.info("LEVEL 2 — Topic Summaries (abstractive, ≤%d tokens)", level_2_max_tokens)
    logger.info("=" * 60)
    t0 = time.time()
    level_2 = summarize_topics(topics_input, level_3, max_tokens=level_2_max_tokens)
    timing["level_2"] = round(time.time() - t0, 3)

    for topic_sum in level_2:
        vr = validate_summary(
            topic_sum.get("summary", ""),
            entities=all_entities,
        )
        validation_reports[f"L2_{topic_sum.get('topic_id', '')}"] = vr

    # ---- Level 1: Category summaries ----
    logger.info("=" * 60)
    logger.info("LEVEL 1 — Category Summaries (template, ≤%d tokens)", level_1_max_tokens)
    logger.info("=" * 60)
    t0 = time.time()
    level_1 = summarize_categories(categories_input, level_2, max_tokens=level_1_max_tokens)
    timing["level_1"] = round(time.time() - t0, 3)

    for cat_sum in level_1:
        vr = validate_summary(
            cat_sum.get("summary", ""),
            entities=all_entities,
        )
        validation_reports[f"L1_{cat_sum.get('category', '')}"] = vr

    # ---- Level 0: Global summary ----
    logger.info("=" * 60)
    logger.info("LEVEL 0 — Global Summary (single sentence, ≤%d tokens)", level_0_max_tokens)
    logger.info("=" * 60)
    t0 = time.time()
    level_0 = generate_global_summary(level_1, max_tokens=level_0_max_tokens)
    timing["level_0"] = round(time.time() - t0, 3)

    vr = validate_summary(
        level_0,
        entities=all_entities,
        source_text=source_text,
    )
    validation_reports["L0_global"] = vr

    # ---- Assemble output ----
    output = {
        "level_4_sections": level_4,
        "level_3_documents": level_3,
        "level_2_topics": level_2,
        "level_1_categories": level_1,
        "level_0_global": level_0,
        "validation_reports": validation_reports,
        "timing": timing,
    }

    # Print summary statistics
    logger.info("=" * 60)
    logger.info("PIPELINE COMPLETE")
    logger.info("  Sections  : %d", len(level_4))
    logger.info("  Documents : %d", len(level_3))
    logger.info("  Topics    : %d", len(level_2))
    logger.info("  Categories: %d", len(level_1))
    logger.info("  Timing    : %s", timing)
    logger.info("=" * 60)

    return output