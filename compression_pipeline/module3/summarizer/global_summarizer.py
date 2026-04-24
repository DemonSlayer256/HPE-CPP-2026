"""
Level 0 — Global Summarizer

Produces a single high-level sentence (≤25 tokens) summarising all
categories using BART abstractive summarization.
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

def generate_global_summary(
    level_1_categories: List[Dict[str, Any]],
    max_tokens: int = 25,
) -> str:
    """Produce a single-sentence global overview (Level 0).

    Parameters
    ----------
    level_1_categories : list[dict]
        Category summaries from Level 1.
    max_tokens : int
        Maximum token budget.

    Returns
    -------
    str
        A single sentence summarising all categories.
    """
    # Combine all category summaries
    combined = " ".join(c.get("summary", "") for c in level_1_categories if c.get("summary"))
    if not combined.strip():
        return "No content available for summarization."

    # Truncate input to stay within model limits
    input_tokens = combined.split()
    if len(input_tokens) > 1024:
        combined = " ".join(input_tokens[:1024])

    try:
        summary = _run_summarizer(
            combined,
            max_length=max_tokens,
            min_length=5,
        )
    except Exception as exc:
        logger.warning("Global summarization failed: %s — falling back", exc)
        summary = " ".join(combined.split()[:max_tokens])

    # Ensure it ends with a period
    summary = summary.strip()
    if not summary.endswith("."):
        summary += "."

    logger.info("Global summary: %d tokens", _count_tokens(summary))
    return summary