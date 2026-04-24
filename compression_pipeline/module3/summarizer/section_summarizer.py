"""
Level 4 — Section Summarizer (Extractive)

Produces extractive summaries for each section (≤500 tokens) by:
1. Scoring sentences using TextRank + entity/AKU/importance boosting.
2. Greedily selecting top sentences until the token budget is reached.
3. Preserving exact entity names, numerical values, and AKU facts.
"""

from __future__ import annotations

import re
import logging
from typing import Any, Dict, List

import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Ensure NLTK data is available
# ---------------------------------------------------------------------------
_NLTK_READY = False


def _ensure_nltk() -> None:
    """Download required NLTK data once per process."""
    global _NLTK_READY
    if _NLTK_READY:
        return
    for resource in ("punkt", "punkt_tab"):
        try:
            nltk.data.find(f"tokenizers/{resource}")
        except LookupError:
            nltk.download(resource, quiet=True)
    _NLTK_READY = True


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _count_tokens(text: str) -> int:
    """Approximate token count by whitespace splitting."""
    return len(text.split())


def _extract_numbers(text: str) -> List[str]:
    """Extract all numeric tokens (integers, floats, percentages)."""
    return re.findall(r"\b\d[\d,]*\.?\d*%?\b", text)


def _sentence_entity_overlap(sentence: str, entities: List[str]) -> float:
    """Fraction of entities mentioned in *sentence*."""
    if not entities:
        return 0.0
    lower = sentence.lower()
    hits = sum(1 for e in entities if e.lower() in lower)
    return hits / len(entities)


def _sentence_aku_coverage(sentence: str, akus: list) -> float:
    """Fraction of AKU triples whose subject OR object appears in *sentence*.

    Handles AKUs as either:
      - list of 3 elements: [subject, predicate, object]
      - dict with "subject" / "object" keys
    """
    if not akus:
        return 0.0
    lower = sentence.lower()
    hits = 0
    for aku in akus:
        if isinstance(aku, list) and len(aku) >= 2:
            subj = str(aku[0]).lower()
            obj_ = str(aku[-1]).lower()
        elif isinstance(aku, dict):
            subj = aku.get("subject", "").lower()
            obj_ = aku.get("object", "").lower()
        else:
            continue
        if (subj and subj in lower) or (obj_ and obj_ in lower):
            hits += 1
    return hits / len(akus)


def _score_sentence(
    sentence: str,
    textrank_score: float,
    entities: List[str],
    akus: List[Dict[str, str]],
    importance: float,
    *,
    w_textrank: float = 0.4,
    w_entity: float = 0.25,
    w_aku: float = 0.25,
    w_importance: float = 0.1,
) -> float:
    """Composite sentence score combining TextRank, entity overlap, AKU
    coverage, and chunk importance."""
    entity_score = _sentence_entity_overlap(sentence, entities)
    aku_score = _sentence_aku_coverage(sentence, akus)
    return (
        w_textrank * textrank_score
        + w_entity * entity_score
        + w_aku * aku_score
        + w_importance * importance
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def summarize_section(
    section: Dict[str, Any],
    max_tokens: int = 500,
) -> Dict[str, Any]:
    """Produce an extractive summary for a single section.

    Parameters
    ----------
    section : dict
        A section object with ``section_id`` and ``chunks`` list.
    max_tokens : int
        Maximum token budget for the summary.

    Returns
    -------
    dict
        ``{"section_id": str, "summary": str, "preserved_entities": list,
          "preserved_akus": list, "token_count": int}``
    """
    _ensure_nltk()

    section_id: str = section["section_id"]
    chunks: List[Dict[str, Any]] = section.get("chunks", [])

    if not chunks:
        return {
            "section_id": section_id,
            "summary": "",
            "preserved_entities": [],
            "preserved_akus": [],
            "token_count": 0,
        }

    # Gather all entities and AKUs across chunks
    all_entities: List[str] = []
    all_akus: List[Dict[str, str]] = []
    for chunk in chunks:
        all_entities.extend(chunk.get("entities", []))
        all_akus.extend(chunk.get("akus", []))
    unique_entities = list(dict.fromkeys(all_entities))  # preserves order

    # Concatenate chunk texts
    full_text = " ".join(c.get("text", "") for c in chunks)
    if not full_text.strip():
        return {
            "section_id": section_id,
            "summary": "",
            "preserved_entities": unique_entities,
            "preserved_akus": all_akus,
            "token_count": 0,
        }

    # --- TextRank sentence scoring ---
    parser = PlaintextParser.from_string(full_text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    # Ask for all sentences so we can re-rank
    ranked_sentences = summarizer(parser.document, sentences_count=len(parser.document.sentences))
    textrank_scores: Dict[str, float] = {}
    for idx, sent in enumerate(ranked_sentences):
        score = 1.0 / (idx + 1)  # inverse rank
        textrank_scores[str(sent)] = score

    # --- Composite scoring per sentence ---
    scored: List[tuple] = []
    for sent_obj in parser.document.sentences:
        sent_str = str(sent_obj)
        # Find which chunk this sentence most likely belongs to (by overlap)
        best_importance = 0.0
        best_akus = all_akus
        for chunk in chunks:
            if sent_str[:40] in chunk.get("text", ""):
                best_importance = chunk.get("importance_score", 0.0)
                best_akus = chunk.get("akus", [])
                break
        tr_score = textrank_scores.get(sent_str, 0.0)
        composite = _score_sentence(
            sent_str, tr_score, unique_entities, best_akus, best_importance
        )
        scored.append((composite, sent_str))

    scored.sort(key=lambda x: x[0], reverse=True)

    # --- Greedy sentence selection under token budget ---
    selected: List[str] = []
    token_budget = max_tokens
    for _, sent in scored:
        stokens = _count_tokens(sent)
        if stokens <= token_budget:
            selected.append(sent)
            token_budget -= stokens
        if token_budget <= 0:
            break

    # Re-order selected sentences to preserve original order
    original_order = [str(s) for s in parser.document.sentences]
    selected_ordered = sorted(selected, key=lambda s: original_order.index(s) if s in original_order else 0)

    summary = " ".join(selected_ordered)

    # Identify preserved entities & AKUs
    preserved_entities = [e for e in unique_entities if e.lower() in summary.lower()]
    preserved_akus = []
    for a in all_akus:
        if isinstance(a, list) and len(a) >= 2:
            subj = str(a[0]).lower()
            obj_ = str(a[-1]).lower()
        elif isinstance(a, dict):
            subj = a.get("subject", "").lower()
            obj_ = a.get("object", "").lower()
        else:
            continue
        if subj in summary.lower() or obj_ in summary.lower():
            preserved_akus.append(a)

    return {
        "section_id": section_id,
        "summary": summary,
        "preserved_entities": preserved_entities,
        "preserved_akus": preserved_akus,
        "token_count": _count_tokens(summary),
    }


def summarize_sections(
    documents: List[Dict[str, Any]],
    max_tokens: int = 500,
) -> List[Dict[str, Any]]:
    """Summarize every section across all documents (Level 4).

    Parameters
    ----------
    documents : list[dict]
        List of document objects each containing ``sections``.
    max_tokens : int
        Per-section token budget.

    Returns
    -------
    list[dict]
        One summary dict per section, keyed by ``section_id``.
    """
    results: List[Dict[str, Any]] = []
    for doc in documents:
        doc_id = doc.get("doc_id", "unknown")
        for section in doc.get("sections", []):
            summary = summarize_section(section, max_tokens=max_tokens)
            summary["doc_id"] = doc_id
            results.append(summary)
            logger.info(
                "Section %s (%s): %d tokens",
                summary["section_id"],
                doc_id,
                summary["token_count"],
            )
    return results