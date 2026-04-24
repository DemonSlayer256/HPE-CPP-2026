"""
Module 3: Hierarchical Summarization Package

Provides five-level hierarchical summarization for a document compression pipeline:
    Level 4 → Section summaries (extractive, ≤500 tokens)
    Level 3 → Document summaries (hybrid, ≤200 tokens)
    Level 2 → Topic summaries (abstractive, ≤100 tokens)
    Level 1 → Category summaries (template-based, ≤50 tokens)
    Level 0 → Global summary (single sentence, ≤25 tokens)
"""

from summarizer.section_summarizer import summarize_sections
from summarizer.document_summarizer import summarize_documents
from summarizer.topic_summarizer import summarize_topics
from summarizer.category_summarizer import summarize_categories
from summarizer.global_summarizer import generate_global_summary
from summarizer.pipeline import run_pipeline
from summarizer.validator import (
    entity_coverage_check,
    relationship_consistency_check,
    aku_fact_check,
)

__all__ = [
    "summarize_sections",
    "summarize_documents",
    "summarize_topics",
    "summarize_categories",
    "generate_global_summary",
    "run_pipeline",
    "entity_coverage_check",
    "relationship_consistency_check",
    "aku_fact_check",
]