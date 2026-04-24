"""
Level 1 — Category Summarizer (Template-Based)

Produces category-level summaries (≤50 tokens) using a deterministic template:

    "Category X includes services such as A, B, C.
     Key functionalities include ..."

No neural model is needed—this is pure template interpolation from topic
summaries and entity lists.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


def _count_tokens(text: str) -> int:
    return len(text.split())


def _extract_service_names(
    topic_summaries: List[Dict[str, Any]],
) -> List[str]:
    """Derive service / feature names from topic labels."""
    names: List[str] = []
    for ts in topic_summaries:
        label = ts.get("label", "")
        if label:
            names.append(label)
    return list(dict.fromkeys(names))  # unique, order-preserving


def _extract_key_functionalities(
    topic_summaries: List[Dict[str, Any]],
    max_items: int = 3,
) -> List[str]:
    """Pull short capability phrases from topic-level summaries."""
    functionalities: List[str] = []
    for ts in topic_summaries:
        summary = ts.get("summary", "")
        if summary:
            # Use the first sentence of each topic summary as a functionality
            first_sentence = summary.split(".")[0].strip()
            if first_sentence:
                functionalities.append(first_sentence)
    return functionalities[:max_items]


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def summarize_category(
    category_name: str,
    topic_ids: List[str],
    level_2_topics: List[Dict[str, Any]],
    max_tokens: int = 50,
) -> Dict[str, Any]:
    """Produce a template-based summary for a single category.

    Parameters
    ----------
    category_name : str
        Category label (e.g. "Storage", "Compute").
    topic_ids : list[str]
        Topic IDs belonging to this category.
    level_2_topics : list[dict]
        All topic summaries from Level 2.
    max_tokens : int
        Maximum token budget.

    Returns
    -------
    dict
        ``{"category": str, "summary": str, "token_count": int}``
    """
    # Filter topic summaries belonging to this category
    relevant = [t for t in level_2_topics if t.get("topic_id") in topic_ids]

    services = _extract_service_names(relevant)
    functionalities = _extract_key_functionalities(relevant)

    if not services:
        summary = f"{category_name} category has no documented services."
    else:
        service_list = ", ".join(services[:5])  # cap at 5 to stay under budget
        if functionalities:
            func_list = "; ".join(functionalities)
            summary = (
                f"{category_name} includes services such as {service_list}. "
                f"Key functionalities include {func_list}."
            )
        else:
            summary = f"{category_name} includes services such as {service_list}."

    # Hard-truncate to token budget
    tokens = summary.split()
    if len(tokens) > max_tokens:
        summary = " ".join(tokens[:max_tokens])
        # Try to end on a full sentence / add ellipsis
        if not summary.endswith("."):
            summary = summary.rstrip(",;: ") + "."

    return {
        "category": category_name,
        "summary": summary,
        "token_count": _count_tokens(summary),
    }


def summarize_categories(
    categories: Dict[str, List[str]],
    level_2_topics: List[Dict[str, Any]],
    max_tokens: int = 50,
) -> List[Dict[str, Any]]:
    """Summarize every category (Level 1).

    Parameters
    ----------
    categories : dict[str, list[str]]
        Mapping of category name → list of topic IDs.
    level_2_topics : list[dict]
        Topic summaries from Level 2.
    max_tokens : int
        Per-category token budget.

    Returns
    -------
    list[dict]
        One summary dict per category.
    """
    results: List[Dict[str, Any]] = []
    for cat_name, topic_ids in categories.items():
        summary = summarize_category(cat_name, topic_ids, level_2_topics, max_tokens=max_tokens)
        results.append(summary)
        logger.info("Category %s: %d tokens", cat_name, summary["token_count"])
    return results