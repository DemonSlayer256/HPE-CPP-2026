# AWS Knowledge Taxonomy & Categorization

## 1. Knowledge Types
To ensure the Context-Aware Hybrid RAG system applies the correct retrieval strategy (Dense vs. Sparse), all documents are classified into four types:
* **Factual:** API References, Instance Types, Limits, Quotas. (Heavy reliance on exact match/BM25).
* **Procedural:** User Guides (UG), Developer Guides (DG), step-by-step tutorials.
* **Conceptual:** Well-Architected Framework, Overviews, Architecture whitepapers. (Heavy reliance on Dense Vector search).
* **Contextual:** Historical rationale, blog announcements, deprecation notices.

## 2. Target Layers (Data Funneling)
Documents are layered to allow the pipeline to prioritize core knowledge during compression and optionally exclude peripheral data.
* **Layer 0 (L0) - The Core:** The absolute minimum context required to understand a service (e.g., `ec2-ug.md`, `aws-overview.md`).
* **Layer 1 (L1) - The Details:** Deep-dive technical specifications and API definitions (e.g., `ec2-api.md`, `iam-managed-policies.md`).
* **Layer 2 (L2) - The Periphery:** Niche use-cases, legacy support, or highly specific tool integrations (e.g., `s3-outposts.md`, `windows-ami-reference.md`).
* **Excluded:** Files that are raw boilerplate, purely index HTML, or irrelevant to the compression goals.