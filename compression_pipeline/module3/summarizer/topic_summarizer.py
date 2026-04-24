"""
Level 2 — Topic Summarizer (Abstractive)

Produces topic-level summaries (≤100 tokens) by:
1. Grouping document summaries by topic (via ``related_docs``).
2. Merging the grouped summaries into a single input.
3. Using BART to produce a concise abstractive summary guided by the topic label.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List

from summarizer.document_summarizer import _run_summarizer

logger = logging.getLogger(__name__)


def _count_tokens(text: str) -> int:
    return len(text.split())


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def summarize_topic(
    topic: Dict[str, Any],
    doc_summaries: List[Dict[str, Any]],
    max_tokens: int = 100,
) -> Dict[str, Any]:
    """Produce an abstractive summary for a single topic.

    Parameters
    ----------
    topic : dict
        Topic object with ``topic_id``, ``label``, ``related_docs``.
    doc_summaries : list[dict]
        Level-3 document summaries.
    max_tokens : int
        Maximum token budget.

    Returns
    -------
    dict
        ``{"topic_id": str, "label": str, "summary": str, "token_count": int}``
    """
    topic_id: str = topic.get("topic_id", "unknown")
    label: str = topic.get("label", "General")
    related_docs: List[str] = topic.get("related_docs", [])

    # Gather document summaries that belong to this topic
    relevant = [
        ds.get("summary", "")
        for ds in doc_summaries
        if ds.get("doc_id") in related_docs and ds.get("summary")
    ]

    if not relevant:
        return {
            "topic_id": topic_id,
            "label": label,
            "summary": "",
            "token_count": 0,
        }

    # Build input with topic label as context
    combined = f"Topic: {label}. " + " ".join(relevant)
    input_tokens = combined.split()
    if len(input_tokens) > 1024:
        combined = " ".join(input_tokens[:1024])

    try:
        summary = _run_summarizer(
            combined,
            max_length=max_tokens,
            min_length=max(10, max_tokens // 4),
        )
    except Exception as exc:
        logger.warning("Topic summarization failed for %s: %s — falling back", topic_id, exc)
        summary = " ".join(combined.split()[:max_tokens])

    return {
        "topic_id": topic_id,
        "label": label,
        "summary": summary,
        "token_count": _count_tokens(summary),
    }


def summarize_topics(
    topics: List[Dict[str, Any]],
    level_3_documents: List[Dict[str, Any]],
    max_tokens: int = 100,
) -> List[Dict[str, Any]]:
    """Summarize every topic (Level 2).

    Parameters
    ----------
    topics : list[dict]
        Topic objects from Module 2 output.
    level_3_documents : list[dict]
        Document summaries from Level 3.
    max_tokens : int
        Per-topic token budget.

    Returns
    -------
    list[dict]
        One summary dict per topic.
    """
    results: List[Dict[str, Any]] = []
    for topic in topics:
        summary = summarize_topic(topic, level_3_documents, max_tokens=max_tokens)
        results.append(summary)
        logger.info("Topic %s (%s): %d tokens", summary["topic_id"], summary["label"], summary["token_count"])
    return results