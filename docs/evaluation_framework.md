
# Evaluation Framework


## 1. Executive Overview

This evaluation framework defines the methodology for definitively
measuring whether the Hierarchical Prompt System outperforms a
traditional flat LLM approach on AWS domain queries. It establishes
rigorous, reproducible standards across four critical dimensions of
system quality:

- Accuracy — Correctness of generated responses against verified AWS
  technical facts.

- Consistency — Stability and reproducibility of responses across
  independent sessions.

- Efficiency — Optimization of token usage, computational cost, and
  response latency.

- Reliability — The system's ability to avoid hallucinations and
  out-of-domain errors.

This document will serve as the primary driver for all Phase 4
validation activities. Its hybrid evaluation approach — combining
statistical metrics, logical inference validation, and hard
fact-checking via Atomic Knowledge Units (AKUs) — is what distinguishes
this system as research-grade rather than benchmark-grade.

## 2. Test Dataset Design

The evaluation is anchored on a curated dataset of 150 questions,
carefully constructed to exercise all system components: all AWS
services in scope, all prompt hierarchy levels, and all cognitive
question types.

### 2.1 Dataset Specifications

| **Parameter**    | **Value**                                   | **Notes**                               |
|------------------|---------------------------------------------|-----------------------------------------|
| Total Questions  | 150 (range: 100–200)                        | Balanced for statistical validity       |
| AWS Services     | S3, EC2, Lambda, IAM, VPC , CloudFormation , CloudWatch ,RDC| Covers core compute, storage & security |
| Layers Triggered | Layer 0, Layer 1, Layer 2, Layer 3, Layer 4 | All hierarchy levels must be exercised  |

*Table 1: Dataset specification parameters.*

### 2.2 Question Type Distribution

| **Question Type** | **Weight** | **Count**    | **Purpose**                                     | **Example**                   |
|-------------------|------------|--------------|-------------------------------------------------|-------------------------------|
| **Factual**       | 30%        | 45 questions | Verify direct facts, limits, and specifications | "Max S3 object size?"         |
| **Procedural**    | 25%        | 37 questions | Evaluate step-by-step task execution accuracy   | "Upload to S3 via Lambda?"    |
| **Conceptual**    | 20%        | 30 questions | Test understanding of service relationships     | "How does S3 trigger Lambda?" |
| **Contextual**    | 25%        | 38 questions | Evaluate decision-making based on real-world scenarios and constraints|"Which AWS service should I use for low-latency file processing?"|

*Table 2: Question type distribution across the evaluation dataset.*

## 3. Ground Truth & Scoring Methodology

Ground truth represents the precise, unambiguous correct answer for each
evaluation question, extracted from official AWS documentation and
formally structured as Atomic Knowledge Units (AKUs). AKUs serve as the
atomic unit of factual verification throughout the framework.

### 3.1 Ground Truth Construction Process

1.  Extract relevant AKUs from official AWS documentation for each
    question in scope.

2.  Cross-validate extracted AKUs against the documentation source to
    confirm accuracy.

3.  Construct canonical reference answers from validated AKUs,
    specifying all required entities, relationships, and numerical
    parameters.

4.  Conduct optional human expert review for high-ambiguity questions.

5.  Store final ground truth entries in the evaluation database, tagged
    by service, question type, and source version.

#### 3.1.1 Ground Truth Data Storage Format (NEW)

To ensure consistency, reproducibility, and seamless integration with the evaluation pipeline, all ground truth entries will be stored in a structured JSON format.

Each entry captures the question, its classification, and a fully specified ground truth representation derived from validated AKUs.

```
{
  "question_id": "q_001",
  "question": "What is the maximum size of an S3 object?",
  "type": "factual",
  "service": "S3",
  "ground_truth": {
    "akus": [
      ["S3 Object", "has_max_size", "5 TB"]
    ],
    "canonical_answer": "The maximum size of a single S3 object is 5 TB.",
    "entities": ["S3", "Object"],
    "parameters": ["5 TB"],
    "source": "AWS S3 Documentation",
    "source_version": "v1.0"
  }
}
```

#### 3.1.2 Ground Truth Examples

- Example 1 — Factual Question
  - Question: What is the maximum size of an S3 object?
  - Ground Truth AKUs:
    - (S3 Object, has_max_size, 5 TB)
  - Canonical Answer:
    - The maximum size of a single S3 object is 5 TB.
  - Entities:
    - S3, Object
  - Parameters:
    - 5 TB

- Example 2 — Conceptual Question
  - Question: How does S3 trigger a Lambda function?
  - Ground Truth AKUs:
    - (S3 Event, triggers, Lambda Function)
    - (Lambda Function, requires, IAM Role)
  - Canonical Answer:
    - S3 can trigger a Lambda function through event notifications. When a specified event occurs in an S3 bucket, it invokes the Lambda function, which must have an appropriate IAM role for execution.
  - Entities:
    - S3, Lambda, IAM Role
  - Relationships:
    - TRIGGERS, REQUIRES

### 3.2 Scoring Rubric

Every generated response is evaluated against its corresponding ground
truth using a standardized three-point rubric:

| **Score**         | **Label** | **Meaning**                         | **Description**                                                                     |
|-------------------|-----------|-------------------------------------|-------------------------------------------------------------------------------------|
| **2 / Correct**   | Full Pass | Fully accurate and complete         | Response satisfies all AKU facts, entities, relationships, and parameters.          |
| **1 / Partial**   | Minor Gap | Mostly correct with minor omissions | Core answer is correct but one or more secondary parameters or details are missing. |
| **0 / Incorrect** | Failure   | Factually wrong or hallucinated     | Response contradicts AKU facts, fabricates information, or is wholly off-topic.     |

*Table 3: Three-point evaluation scoring rubric.*

## 4. Quality Validation Engine

The Quality Validation Engine is the most critical component of this
framework. It deliberately rejects simplistic text-similarity approaches
in favour of genuine factual correctness verification. The engine
operates across three integrated validation layers.

### 4.1 Automated Fact-Checking

Each response is checked against its ground truth AKUs along three
dimensions:

- Entity Preservation — Verifies that all required key entities (e.g.,
  IAM, S3, Lambda) are explicitly present in the generated response.

- Relationship Integrity — Confirms that logical relationships between
  entities are correctly represented (e.g., S3 triggers Lambda, not the
  reverse).

- Parameter and Numerical Accuracy — Validates exact technical
  specifications, API configurations, and numerical limits (e.g., Lambda
  timeout: 15 minutes; S3 maximum object size: 5 TB).

### 4.2 Hallucination & Reliability Detection

Two mechanisms are employed to detect fabricated content:

- Entailment Checking (NLI) — A Natural Language Inference model
  verifies that the generated response is logically entailed by the
  source context provided. Any claim not derivable from the source is
  flagged as a potential hallucination.

- Out-of-Domain Detection — A classifier identifies fabricated concepts
  that have no basis in the AWS documentation corpus (e.g., "S3
  Blockchain encryption" or non-existent API parameters).

### 4.3 Information Preservation Metrics

In addition to logical validation, quantitative metrics measure the
degree of information retention:

| **Metric**        | **Threshold** | **Description**                                                                      |
|-------------------|---------------|--------------------------------------------------------------------------------------|
| **ROUGE-L**       | \> 0.40       | Longest common subsequence overlap between generated response and ground truth.      |
| **BERTScore**     | \> 0.85       | Semantic similarity using contextual embeddings from a pre-trained BERT model.       |
| **Entity Recall** | \> 90%        | Percentage of key source entities retained and correctly referenced in the response. |

*Table 4: Information preservation metric thresholds.*

## 5. Consistency Testing

Consistency testing verifies that the system produces stable,
reproducible outputs across independent sessions for the same input
query — a critical quality requirement for a knowledge system.

### 5.1 Methodology

For each test query in the evaluation dataset, the following procedure
is followed:

1.  Execute the identical query across 5 fully independent sessions
    (cleared context, no shared state).

2.  Collect all 5 generated responses.

3.  Compute dense embedding vectors for each response using a
    sentence-level embedding model.

4.  Calculate pairwise cosine similarity scores across all response
    pairs.

5.  Report the mean cosine similarity as the consistency score for that
    query.

### 5.2 Interpretation Scale

| **Cosine Similarity** | **Classification**    | **Interpretation**                                                                         |
|-----------------------|-----------------------|--------------------------------------------------------------------------------------------|
| **\> 0.90**           | Highly Consistent     | System reliably produces equivalent responses. Meets production quality standard.          |
| **0.70 – 0.90**       | Moderately Consistent | Minor response variation acceptable. Recommend further prompt tuning.                      |
| **\< 0.70**           | Inconsistent          | Significant response variability. Indicates knowledge coverage gaps or prompt instability. |

*Table 5: Cosine similarity interpretation scale for consistency
testing.*

## 6. Token Cost & Efficiency Evaluation

Efficiency evaluation directly compares token consumption and response
latency between the hierarchical system and a traditional baseline LLM,
quantifying the performance advantage delivered by the multi-level
caching architecture.

### 6.1 Comparison Setup

| **System**                  | **Description**                                      | **Caching**                            |
|-----------------------------|------------------------------------------------------|----------------------------------------|
| **Baseline (Flat LLM)**     | Traditional single-layer LLM with no caching layer.  | None — full recomputation per query.   |
| **Proposed (Hierarchical)** | Hierarchical prompt system with multi-level caching. | L1 / L2 / L3 multi-level cache active. |

*Table 6: Evaluation system comparison setup.*

#### 6.1.1 Baseline Definition

The baseline system represents a traditional flat LLM setup without hierarchical structuring or caching.

To ensure a fair and reproducible comparison, the baseline is defined with the following constraints:

- Model: Same LLM as hierarchical system (e.g., GPT / Claude / LLaMA API)
- Prompt Structure: Single-layer prompt containing all relevant context
- Context Construction: Raw or lightly processed documentation chunks concatenated into a single prompt
- No Layering: No L0/L1/L2/L3/L4 hierarchy
- No Caching: Full recomputation for every query
- Temperature: Fixed (e.g., 0.2–0.3 for factual consistency)
- Token Budget: Same maximum context window as hierarchical system

Example Baseline Prompt:

```
[Full AWS documentation context]

Question: What is the maximum size of an S3 object?
```


### 6.2 Efficiency Metrics

The following metrics are captured for each query against both systems:

- Total tokens per query (prompt tokens + completion tokens).

- Percentage token reduction relative to the flat baseline.

- Cache tier contribution — which cache level (L1/L2/L3) served the
  response.

- Total response time (wall clock, end-to-end).

- Cache lookup latency vs. LLM generation latency (decomposed timing).

**Target: Achieve a 40 – 60% reduction in token usage per query
alongside measurably faster execution latency across the majority of
query types.**

## 7. Failure Taxonomy & Root Cause Analysis

All failed responses — those scoring 0 or 1 on the rubric — are
categorized into one of four failure modes. This taxonomy enables
systematic root cause analysis and targeted architectural improvement.

| **Failure Type**    | **Description**                                                   | **Remediation Action**                                                          |
|---------------------|-------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Coverage Gap**    | Required knowledge was absent from the loaded prompt layers.      | Expand AKU extraction scope; add missing topic nodes to L3 cache.               |
| **Budget Overflow** | Critical context was truncated due to token limit constraints.    | Optimize layer compression; prioritize high-value AKUs within budget.           |
| **Hallucination**   | Model generated fabricated technical facts not present in source. | Strengthen NLI entailment checks; tighten prompt grounding instructions.        |
| **Inconsistency**   | Different responses returned for semantically identical queries.  | Increase L1 cache hit scope; reduce generation temperature for factual queries. |

*Table 7: Failure taxonomy with root cause and remediation guidance.*

## 8. Evaluation Pipeline Workflow

The complete evaluation workflow follows a structured pipeline with six
discrete stages:

1.  Dataset Preparation — Finalize the 150-question dataset. Confirm AWS
    service coverage, layer coverage, and question type distribution
    against specification.

2.  Response Generation — Execute all queries against both the
    hierarchical system (with caching) and the flat LLM baseline. Log
    all responses, token counts, and timing data.

3.  Validation Engine Application — Apply automated fact-checking, NLI
    entailment checks, and information preservation metrics to all
    generated responses.

4.  Rubric Scoring — Score each response as Correct (2), Partial (1), or
    Incorrect (0) against ground truth AKUs.

5.  Failure Analysis — Categorize all sub-threshold responses into the
    failure taxonomy. Identify systemic patterns and high-impact gaps.
  
```
Results storage format

{
  "question_id": "q_001",
  "hierarchical_response": "...",
  "baseline_response": "...",
  "tokens_used": {
    "hierarchical": 1200,
    "baseline": 3500
  },
  "latency_ms": {
    "hierarchical": 800,
    "baseline": 2200
  },
  "cache_hit": "L2"
}
```

> Comparative Reporting — Aggregate all scores, metrics, and efficiency
> data. Produce a structured evaluation report comparing hierarchical
> vs. baseline performance.

## 9. Success Criteria & Target KPIs

For the Hierarchical AWS LLM System to be considered successful at Phase
4 completion, it must meet or exceed all of the following Key
Performance Indicators:

| **Metric**             | **Target Value**   | **Rationale**                                                                  |
|------------------------|--------------------|--------------------------------------------------------------------------------|
| **Overall Accuracy**   | ≥ 85%              | Ensures the system is reliable enough for production or research use.          |
| **Consistency Score**  | ≥ 0.85 (cosine)    | Confirms stable, reproducible outputs across independent sessions.             |
| **Token Reduction**    | ≥ 40% vs. baseline | Validates the economic and computational efficiency of the cache architecture. |
| **Hallucination Rate** | \< 5%              | Ensures factual trustworthiness as a domain knowledge system.                  |
| **Entity Recall**      | \> 90%             | Confirms that critical technical entities are preserved in all responses.      |
| **BERTScore**          | \> 0.85            | Ensures semantic fidelity between generated responses and ground truth.        |

*Table 8: Phase 4 success criteria and target KPI values.*

### 9.1 Bias Prevention & Ground Truth Integrity

To ensure the validity and credibility of evaluation results, strict measures are enforced to prevent evaluation bias and data leakage.

Ground Truth Isolation Principle
  - Ground truth answers must be created only from raw AWS documentation
  - Compressed outputs (summaries, AKUs generated by the system) must NOT be used to construct evaluation answers

Why This Matters
If ground truth is derived after compression:
  - The evaluation becomes biased toward system outputs
  - The model may appear artificially accurate
  - Results lose scientific validity

Enforcement Rules
  1. Ground truth dataset must be finalized before running the compression pipeline
  2. Separate storage:
    - /ground_truth/ → immutable dataset
    - /pipeline_outputs/ → generated data
  3. No reuse of:
    - summaries
    - extracted AKUs
    - cached responses

Optional Safeguards
  - Version-lock ground truth dataset
  - Manual audit for 10–15% of questions
  - Track source references for every answer


## 10. Key Insight & Framework Strength

The defining strength of this evaluation framework is its hybrid,
multi-layered validation approach. Unlike benchmark systems that rely
exclusively on n-gram overlap (ROUGE) or embedding similarity
(BERTScore), this framework combines three validation modalities:

- Statistical Evaluation — ROUGE-L and BERTScore provide quantitative
  bounds on textual fidelity.

- Logical Validation — NLI-based entailment checking provides a formal
  guarantee that generated claims are derivable from the source context.

- Hard Fact-Checking — AKU and knowledge graph validation provides
  ground-truth entity and relationship verification at the atomic level.

This combination means the framework does not merely ask whether an
answer looks similar — it mathematically proves whether the answer is
factually correct. This elevates the evaluation from a benchmark
exercise to a genuine research-grade validation methodology.

## 11. Conclusion

This evaluation framework provides a complete, rigorous, and
reproducible methodology for validating the Hierarchical AWS LLM System
at Phase 4. It is designed to generate findings that are both
technically defensible and practically meaningful — quantifying
improvements in accuracy, efficiency, consistency, and reliability
relative to a flat LLM baseline.

By grounding all validation in Atomic Knowledge Units and augmenting
statistical metrics with logical entailment checking, the framework
ensures that evaluation conclusions reflect genuine system capability
rather than surface-level text similarity.

The structured failure taxonomy and systematic pipeline workflow further
ensure that any performance gaps identified during evaluation can be
traced to specific architectural causes and addressed through targeted
improvements — making this framework an ongoing driver of system quality
beyond Phase 4.
