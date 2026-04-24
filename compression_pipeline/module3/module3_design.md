# Module 3: Hierarchical Summarisation

## 1. Overview

Module 3 is the third stage of the **AWS Knowledge Compression Pipeline**. It transforms the knowledge graph and chunked documentation produced by Modules 1 and 2 into a **five-level hierarchical summary** that progressively compresses information from fine-grained section extracts down to a single global sentence.

Each level uses a different summarisation strategy — extractive, hybrid, abstractive, or template-based — chosen to match the compression ratio and fidelity requirements at that granularity. A post-summarisation **validation layer** enforces entity preservation, relationship consistency, AKU fact-checking, and numerical accuracy across all levels.

---

## 2. Inputs

| File / Data | Produced by | Description |
|-------------|-------------|-------------|
| `chunks.json` | Module 1 | Array of document chunks with text, heading path, position, token count, and section ID |
| `akus.json` | Module 1 | Array of per-chunk AKU lists — each AKU is a `[subject, predicate, object]` triple |
| `knowledge_graph.json` | Module 2 | Knowledge graph with nodes (entities + importance scores), edges (relationships), and topics |

### 2.1 Combined input schema (expected by pipeline)

The pipeline expects a single JSON object combining Module 1 and Module 2 outputs into the following structure:

```json
{
  "documents": [
    {
      "doc_id": "AWS-S3-Module1-Test",
      "sections": [
        {
          "section_id": "sec_001",
          "chunks": [
            {
              "chunk_id": "chunk_000",
              "text": "...",
              "akus": [["subject", "predicate", "object"]],
              "entities": ["AWS", "Amazon S3"],
              "relationships": [],
              "importance_score": 0.8
            }
          ]
        }
      ]
    }
  ],
  "topics": [
    {
      "topic_id": "topic_mock_01",
      "label": "Storage Operations",
      "related_docs": ["AWS-S3-Module1-Test"]
    }
  ],
  "categories": {
    "Storage": ["topic_mock_01"],
    "Security": ["topic_mock_02"]
  }
}
```

---

## 3. Processing Pipeline

```
                        Input Data (M1 + M2)
                              │
                              ▼
                 ┌────────────────────────┐
          L4     │   Section Summarizer   │  Extractive (TextRank + boosting)
                 │      ≤500 tokens       │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
          L3     │  Document Summarizer   │  Hybrid (Extractive + BART abstractive)
                 │      ≤200 tokens       │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
          L2     │   Topic Summarizer     │  Abstractive (BART)
                 │      ≤100 tokens       │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
          L1     │  Category Summarizer   │  Template-based (no neural model)
                 │       ≤50 tokens       │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
          L0     │   Global Summarizer    │  Abstractive (BART, single sentence)
                 │       ≤25 tokens       │
                 └───────────┴────────────┘
                             │
                             ▼
                    Validation Layer
                   (per-level checks)
                             │
                             ▼
                      Output JSON
```

### 3.1 Level 4 — Section Summaries (Extractive)

**Strategy:** TextRank + entity/AKU/importance boosting → greedy sentence selection.

For each section across all documents:

1. **Concatenate** all chunk texts within the section into a single passage.
2. **TextRank scoring** — use `sumy.TextRankSummarizer` to rank every sentence by graph-based centrality.
3. **Composite scoring** — re-rank each sentence using a weighted combination of four signals:

| Signal | Weight | Derivation |
|--------|--------|------------|
| `textrank_score` | 40% | Inverse rank from TextRank (1/rank) |
| `entity_overlap` | 25% | Fraction of known entities mentioned in the sentence |
| `aku_coverage` | 25% | Fraction of AKU triples whose subject or object appears in the sentence |
| `importance` | 10% | Chunk-level importance score from Module 2 |

**Formula:**

```
score = 0.40 × textrank_score
      + 0.25 × entity_overlap
      + 0.25 × aku_coverage
      + 0.10 × importance
```

4. **Greedy selection** — sort sentences by composite score descending, then greedily add sentences until the token budget (≤500) is exhausted.
5. **Re-ordering** — selected sentences are re-sorted into their original document order to preserve narrative flow.
6. **Preservation tracking** — identify which entities and AKU triples survived into the summary by substring matching.

**Output per section:**

```json
{
  "section_id": "sec_001",
  "doc_id": "AWS-S3-Module1-Test",
  "summary": "...",
  "preserved_entities": ["AWS", "Amazon S3"],
  "preserved_akus": [["subject", "predicate", "object"]],
  "token_count": 487
}
```

### 3.2 Level 3 — Document Summaries (Hybrid)

**Strategy:** Extractive base from L4 → abstractive refinement via DistilBART.

For each document:

1. **Collect** all Level 4 section summaries belonging to the document.
2. **Extract top entities** — rank entities by frequency across all chunks; keep top 10.
3. **Extract top relationships** — rank relationships by source-chunk importance; keep top 5.
4. **Build input** — prepend entity/relationship hints to the combined section summaries:
   ```
   Key entities: AWS, Amazon S3, IAM Role, ...
   Important relationships: X relates-to Y; ...
   [combined section summaries]
   ```
5. **Abstractive refinement** — pass the combined text through `sshleifer/distilbart-cnn-12-6` with beam search (num_beams=4, length_penalty=2.0).
6. **Fallback** — if the model fails, truncate the extractive input to the token budget.

**Output per document:**

```json
{
  "doc_id": "AWS-S3-Module1-Test",
  "summary": "...",
  "top_entities": ["AWS", "Amazon S3", "IAM Role"],
  "top_relationships": [],
  "token_count": 178
}
```

### 3.3 Level 2 — Topic Summaries (Abstractive)

**Strategy:** Pure abstractive compression via DistilBART.

For each topic:

1. **Group** Level 3 document summaries by `related_docs` membership.
2. **Build input** — prefix the topic label as context:
   ```
   Topic: Storage Operations. [combined document summaries]
   ```
3. **Abstractive summarisation** — pass through DistilBART with the same beam-search configuration as Level 3.
4. **Fallback** — truncate on model failure.

**Output per topic:**

```json
{
  "topic_id": "topic_mock_01",
  "label": "Storage Operations",
  "summary": "...",
  "token_count": 89
}
```

### 3.4 Level 1 — Category Summaries (Template-Based)

**Strategy:** Deterministic template interpolation — no neural model required.

For each category:

1. **Filter** Level 2 topic summaries belonging to the category (via `categories` mapping).
2. **Extract service names** from topic labels.
3. **Extract key functionalities** — take the first sentence of each topic summary (up to 3).
4. **Interpolate template:**
   ```
   {Category} includes services such as {service_list}.
   Key functionalities include {func_list}.
   ```
5. **Hard-truncate** to the token budget (≤50 tokens), ending on a full sentence where possible.

**Output per category:**

```json
{
  "category": "Storage",
  "summary": "Storage includes services such as Storage Operations. Key functionalities include ...",
  "token_count": 42
}
```

### 3.5 Level 0 — Global Summary (Abstractive)

**Strategy:** Single-sentence abstractive compression via DistilBART.

1. **Combine** all Level 1 category summaries into a single input.
2. **Abstractive summarisation** — generate a single sentence (≤25 tokens, min_length=5).
3. **Post-processing** — ensure the output ends with a period.
4. **Fallback** — truncate on model failure.

**Output:** A single string.

```json
"Amazon S3 provides scalable storage with security, API operations, and SDK integration."
```

---

## 4. Validation Layer

Every generated summary is validated by `validator.py`, which runs four independent checks. Each check produces a `passed` boolean and a quantitative score.

### 4.1 Entity Coverage

| Parameter | Value |
|-----------|-------|
| Threshold | 70% |
| Method | Normalised substring matching (lowercase, collapsed whitespace) |

Checks what fraction of expected entities appear in the summary.

```json
{"passed": true, "coverage": 0.85, "found": ["AWS", "Amazon S3"], "missing": ["CloudFront"]}
```

### 4.2 Relationship Consistency

| Parameter | Value |
|-----------|-------|
| Threshold | 50% |
| Method | Both source and target entity names must appear in the summary |

A relationship is "reflected" if both its endpoints are mentioned.

```json
{"passed": true, "consistency": 0.75, "reflected": [...], "missing": [...]}
```

### 4.3 AKU Fact Check

| Parameter | Value |
|-----------|-------|
| Threshold | 60% |
| Method | Both subject and object of each AKU triple must appear in the summary |

Ensures factual assertions from AKU triples are not silently dropped.

```json
{"passed": true, "preservation": 0.80, "preserved": [...], "missing": [...]}
```

### 4.4 Numerical Accuracy

| Parameter | Value |
|-----------|-------|
| Threshold | 90% |
| Method | All numbers in the summary must also appear in the source text |

Guards against hallucinated or distorted numerical values.

```json
{"passed": true, "accuracy": 1.0, "verified": ["1024", "5GB"], "suspect": []}
```

### 4.5 Aggregate Report

All checks are combined into an aggregate report per summary with an `overall_passed` flag:

```json
{
  "entity_coverage": { "passed": true, "coverage": 0.85, ... },
  "relationship_consistency": { "passed": true, "consistency": 0.75, ... },
  "aku_fact_check": { "passed": true, "preservation": 0.80, ... },
  "numerical_accuracy": { "passed": true, "accuracy": 1.0, ... },
  "overall_passed": true
}
```

---

## 5. Output

### 5.1 Raw Pipeline Output

`compression_pipeline/integration_output.json`

```json
{
  "level_4_sections": [ ... ],
  "level_3_documents": [ ... ],
  "level_2_topics": [ ... ],
  "level_1_categories": [ ... ],
  "level_0_global": "...",
  "validation_reports": { ... },
  "timing": {
    "level_4": 12.345,
    "level_3": 3.210,
    "level_2": 1.456,
    "level_1": 0.002,
    "level_0": 0.891
  }
}
```

### 5.2 Structured Output (Post-Transform)

`compression_pipeline/structured_output.json`

The raw output is cleaned by `transform_output.py`, which applies:

1. **Boilerplate stripping** — removes known boilerplate patterns (e.g. "Amazon Simple Storage Service API Reference", "Request Syntax …", "See Also …").
2. **Sentence deduplication** — exact-match removal after normalisation.
3. **Near-duplicate merging** — word-overlap-based redundancy removal (threshold: 75%).
4. **Noise filtering** — strips short fragments, single-word headers, and non-informative sentences.
5. **UUID assignment** — each summary receives a unique `summary_id`.
6. **AKU/Entity ID generation** — entities mapped to stable IDs like `ent_aws_s3`; AKUs receive sequential IDs like `aku_0`.
7. **Category classification** — keyword-based classification into: `security`, `storage`, `networking`, `api`, `configuration`, `operational`, `contextual`.
8. **Compression ratio** — `cleaned_length / original_length`.

#### Structured section schema

```json
{
  "summary_id": "dd639c7c-9986-432b-a426-5df6bc8885e4",
  "level": 4,
  "level_name": "section",
  "text": "...",
  "token_count": 240,
  "source_chunk_ids": ["chunk_001"],
  "source_document": "AWS-S3-Guide",
  "heading_path": [],
  "category": "api",
  "preserved_akus": ["aku_0", "aku_1", "aku_2"],
  "preserved_entities": ["ent_aws", "ent_amazon_s3"],
  "compression_ratio": 0.474,
  "parent_summary_id": "08d6964a-...",
  "child_summary_ids": []
}
```

---

## 6. Usage

### 6.1 Full Pipeline (Integration Runner)

```bash
cd compression_pipeline
python module3/integration_runner.py
```

This automatically:
1. Loads Module 1 output from `module1/s3/intermediate/`
2. Mocks Module 2 entity/relationship data
3. Runs the full L4 → L3 → L2 → L1 → L0 pipeline
4. Saves output to `final_pipeline_output.json`


---

## 7. Design Decisions

| Decision | Rationale |
|----------|-----------|
| Five-level hierarchy | Matches the natural granularity of technical documentation: sections → documents → topics → categories → corpus. Each level halves (or more) the token budget, producing a smooth compression curve. |
| Extractive L4, hybrid L3, abstractive L2/L0, template L1 | Extractive at L4 preserves exact wording and prevents hallucination at the most detailed level. Hybrid at L3 balances fidelity with coherence. Abstractive at L2/L0 achieves aggressive compression. Template at L1 avoids model overhead for a structurally predictable output. |
| TextRank + composite boosting (L4) | Pure TextRank ignores domain knowledge. Boosting with entity overlap, AKU coverage, and importance scores from Module 2 ensures that graph-important sentences are preferred. |
| Entity / relationship hints prepended to BART input (L3) | Nudges the abstractive model to mention critical entities without hard constraints, acting as a soft prompt. |
| DistilBART over full BART | 2× faster inference with minimal quality loss for summarisation tasks. Fits within the pipeline's latency budget. |
| Lazy model singleton | Avoids reloading the 1.2 GB model for every document; pays the cost once per process. |
| Section batching (`CHUNKS_PER_SECTION = 20`) | TextRank builds a fully-connected sentence similarity graph — O(n²). Batching keeps n small, reducing L4 runtime from minutes to seconds for large documents. |
| Validation as a separate pass (not inline) | Decouples summarisation from quality enforcement. Allows thresholds to be tuned independently and validation reports to be inspected without re-running the pipeline. |
| Post-transform output cleaner | Raw pipeline output contains boilerplate, duplicates, and noise inherited from the source documentation. A dedicated cleaning pass produces a polished, deduplicated structured output suitable for downstream consumption. |
| Keyword-based category classification | Lightweight and deterministic. Avoids adding another model dependency for a task that can be solved with simple keyword matching on well-structured AWS documentation. |
| Compression ratio tracking | Provides a quantitative measure of how aggressively each section was compressed, useful for identifying sections that may need re-processing or manual review. |
