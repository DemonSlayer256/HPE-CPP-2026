"""
Validation Module

Provides post-summarization validation to enforce:
1. Entity preservation — high-importance entities must appear in summaries.
2. Relationship consistency — important relationships must be reflected.
3. AKU fact checking — atomic knowledge units must not be altered.
4. Numerical accuracy — numbers, limits, configurations must be exact.
"""

from __future__ import annotations

import re
import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _normalize(text: str) -> str:
    """Lowercase and collapse whitespace for fuzzy matching."""
    return re.sub(r"\s+", " ", text.lower().strip())


def _extract_numbers(text: str) -> List[str]:
    """Extract all numeric tokens from *text*."""
    return re.findall(r"\b\d[\d,]*\.?\d*%?\b", text)


# ---------------------------------------------------------------------------
# Entity Coverage
# ---------------------------------------------------------------------------

def entity_coverage_check(
    summary: str,
    entities: List[str],
    threshold: float = 0.7,
) -> Dict[str, Any]:
    """Check what fraction of *entities* appear in *summary*.

    Parameters
    ----------
    summary : str
        The generated summary text.
    entities : list[str]
        Entity strings that should be preserved.
    threshold : float
        Minimum acceptable coverage ratio (0-1).

    Returns
    -------
    dict
        ``{"passed": bool, "coverage": float, "found": list, "missing": list}``
    """
    if not entities:
        return {"passed": True, "coverage": 1.0, "found": [], "missing": []}

    norm_summary = _normalize(summary)
    found: List[str] = []
    missing: List[str] = []

    for entity in entities:
        if _normalize(entity) in norm_summary:
            found.append(entity)
        else:
            missing.append(entity)

    coverage = len(found) / len(entities)
    passed = coverage >= threshold

    if not passed:
        logger.warning(
            "Entity coverage %.1f%% below threshold %.1f%%. Missing: %s",
            coverage * 100,
            threshold * 100,
            missing,
        )

    return {
        "passed": passed,
        "coverage": round(coverage, 4),
        "found": found,
        "missing": missing,
    }


# ---------------------------------------------------------------------------
# Relationship Consistency
# ---------------------------------------------------------------------------

def relationship_consistency_check(
    summary: str,
    relationships: List[Dict[str, str]],
    threshold: float = 0.5,
) -> Dict[str, Any]:
    """Check that important relationships are reflected in *summary*.

    A relationship is considered "reflected" if both the source and target
    entity names appear in the summary text.

    Parameters
    ----------
    summary : str
        The generated summary text.
    relationships : list[dict]
        Relationship dicts with ``source``/``subject`` and ``target``/``object`` keys.
    threshold : float
        Minimum acceptable consistency ratio (0-1).

    Returns
    -------
    dict
        ``{"passed": bool, "consistency": float,
          "reflected": list, "missing": list}``
    """
    if not relationships:
        return {"passed": True, "consistency": 1.0, "reflected": [], "missing": []}

    norm_summary = _normalize(summary)
    reflected: List[Dict[str, str]] = []
    missing: List[Dict[str, str]] = []

    for rel in relationships:
        src = rel.get("source", rel.get("subject", ""))
        tgt = rel.get("target", rel.get("object", ""))
        if not src or not tgt:
            continue
        src_present = _normalize(src) in norm_summary
        tgt_present = _normalize(tgt) in norm_summary
        if src_present and tgt_present:
            reflected.append(rel)
        else:
            missing.append(rel)

    total = len(reflected) + len(missing)
    consistency = len(reflected) / total if total > 0 else 1.0
    passed = consistency >= threshold

    if not passed:
        logger.warning(
            "Relationship consistency %.1f%% below threshold %.1f%%.",
            consistency * 100,
            threshold * 100,
        )

    return {
        "passed": passed,
        "consistency": round(consistency, 4),
        "reflected": reflected,
        "missing": missing,
    }


# ---------------------------------------------------------------------------
# AKU Fact Check
# ---------------------------------------------------------------------------

def aku_fact_check(
    summary: str,
    akus: List[Dict[str, str]],
    threshold: float = 0.6,
) -> Dict[str, Any]:
    """Check that AKU facts are not altered in *summary*.

    An AKU is considered "preserved" when its subject appears in the summary
    AND its object appears in the summary, ensuring the factual assertion is
    at least partially reflected.

    Parameters
    ----------
    summary : str
        The generated summary text.
    akus : list[dict]
        AKU dicts with ``subject``, ``predicate``, ``object`` keys.
    threshold : float
        Minimum acceptable preservation ratio (0-1).

    Returns
    -------
    dict
        ``{"passed": bool, "preservation": float,
          "preserved": list, "missing": list}``
    """
    if not akus:
        return {"passed": True, "preservation": 1.0, "preserved": [], "missing": []}

    norm_summary = _normalize(summary)
    preserved: List[Dict[str, str]] = []
    missing: List[Dict[str, str]] = []

    for aku in akus:
        if isinstance(aku, list) and len(aku) >= 2:
            subj = str(aku[0])
            obj_ = str(aku[-1])
        elif isinstance(aku, dict):
            subj = aku.get("subject", "")
            obj_ = aku.get("object", "")
        else:
            continue
        subj_ok = bool(subj) and _normalize(subj) in norm_summary
        obj_ok = bool(obj_) and _normalize(obj_) in norm_summary
        if subj_ok and obj_ok:
            preserved.append(aku)
        else:
            missing.append(aku)

    preservation = len(preserved) / len(akus)
    passed = preservation >= threshold

    if not passed:
        logger.warning(
            "AKU preservation %.1f%% below threshold %.1f%%.",
            preservation * 100,
            threshold * 100,
        )

    return {
        "passed": passed,
        "preservation": round(preservation, 4),
        "preserved": preserved,
        "missing": missing,
    }


# ---------------------------------------------------------------------------
# Numerical Accuracy
# ---------------------------------------------------------------------------

def numerical_accuracy_check(
    summary: str,
    source_text: str,
) -> Dict[str, Any]:
    """Verify that numbers appearing in *summary* also appear in *source_text*.

    Parameters
    ----------
    summary : str
        The generated summary text.
    source_text : str
        The original source text.

    Returns
    -------
    dict
        ``{"passed": bool, "accuracy": float,
          "verified": list, "suspect": list}``
    """
    summary_numbers = set(_extract_numbers(summary))
    source_numbers = set(_extract_numbers(source_text))

    if not summary_numbers:
        return {"passed": True, "accuracy": 1.0, "verified": [], "suspect": []}

    verified = sorted(summary_numbers & source_numbers)
    suspect = sorted(summary_numbers - source_numbers)
    accuracy = len(verified) / len(summary_numbers)
    passed = accuracy >= 0.9  # allow small tolerance

    if not passed:
        logger.warning("Suspect numbers in summary: %s", suspect)

    return {
        "passed": passed,
        "accuracy": round(accuracy, 4),
        "verified": verified,
        "suspect": suspect,
    }


# ---------------------------------------------------------------------------
# Aggregate Validation
# ---------------------------------------------------------------------------

def validate_summary(
    summary: str,
    entities: List[str] | None = None,
    relationships: List[Dict[str, str]] | None = None,
    akus: List[Dict[str, str]] | None = None,
    source_text: str | None = None,
) -> Dict[str, Any]:
    """Run all applicable validation checks on a single summary.

    Returns
    -------
    dict
        Keyed by check name, each value is the check result dict.
        Also includes an ``"overall_passed"`` boolean.
    """
    report: Dict[str, Any] = {}
    all_passed = True

    if entities is not None:
        r = entity_coverage_check(summary, entities)
        report["entity_coverage"] = r
        if not r["passed"]:
            all_passed = False

    if relationships is not None:
        r = relationship_consistency_check(summary, relationships)
        report["relationship_consistency"] = r
        if not r["passed"]:
            all_passed = False

    if akus is not None:
        r = aku_fact_check(summary, akus)
        report["aku_fact_check"] = r
        if not r["passed"]:
            all_passed = False

    if source_text is not None:
        r = numerical_accuracy_check(summary, source_text)
        report["numerical_accuracy"] = r
        if not r["passed"]:
            all_passed = False

    report["overall_passed"] = all_passed
    return report