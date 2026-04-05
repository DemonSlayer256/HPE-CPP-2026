# Compression Pipeline Design

## 1. Overview
This document outlines the architecture for the AWS Knowledge Compression Pipeline. The pipeline is designed to ingest raw Markdown documentation and process it through a multi-stage funnel, ultimately producing highly compressed, structured representations of AWS knowledge.

The pipeline consists of four primary stages:
1.  **Chunking Module**
2.  **Atomic Knowledge Unit (AKU) Extraction**
3.  **Topic Extraction Module**
4.  **Hierarchical Summarisation**

---

## 2. Chunking Module
The first stage processes raw Markdown files and splits them into manageable semantic blocks suitable for Large Language Model (LLM) context windows.

* **Primary Boundaries (Semantic):** Documents are split at Markdown heading boundaries, specifically `##` (Level 2) and `###` (Level 3) headers. This ensures chunks naturally align with the author's intended topic breaks.
* **Secondary Boundaries (Length-Based):** If a specific section exceeds a soft limit of **~500 tokens**, the module falls back to splitting at paragraph double-newlines (`\n\n`) to prevent context overflow.
* **Overlap Strategy:** To prevent context loss across boundaries (e.g., a pronoun in the first sentence of a new chunk referring to an entity in the previous chunk), the system implements a **~50-token overlap**. The last 50 tokens of chunk $N$ are prepended to the start of chunk $N+1$.

---

## 3. Atomic Knowledge Unit (AKU) Extraction
*This is the core parsing innovation of the pipeline. It sits precisely between the Chunking module and the Structured Representation stage.*

### 3.1. Definition
An **Atomic Knowledge Unit (AKU)** is the smallest, self-contained piece of knowledge that independently answers a single question or asserts a single verifiable fact. Instead of summarising a chunk directly, the LLM decomposes the chunk into a discrete list of AKUs. This allows for granular, programmatic control over what data is retained or discarded during final compression.

### 3.2. The Quality Bar
For a statement to qualify as an AKU, it must strictly pass the following criteria:
1.  **Self-Contained:** It does not rely on preceding or following sentences to be understood (no dangling pronouns like "It also requires...").
2.  **Single-Fact/Action:** It contains only one primary assertion or workflow step.
3.  **Entity-Grounded:** It explicitly names at least one AWS service, component, or conceptual entity.
4.  **The Reverse-Question Test:** You must be able to instantly reconstruct the exact question this AKU is answering.

### 3.3. AKU Archetypes (Examples)
* **Factual:** "AWS Lambda maximum execution timeout is strictly 900 seconds (15 minutes)." *(Reverse Question: What is the maximum execution timeout for Lambda?)*
* **Procedural:** "Step 3: Attach an IAM execution role to the target AWS Lambda function prior to initiating deployment." *(Reverse Question: What must be attached to a Lambda function before deployment?)*
* **Conceptual:** "Principle of Least Privilege requires granting IAM users only the absolute minimum permissions necessary to execute a specific task." *(Reverse Question: What is the Principle of Least Privilege in IAM?)*

---

## 4. Topic Extraction Module
Once AKUs are extracted, this module enriches them with metadata to build a connected knowledge graph.

* **Entity Recognition:** Extracts and tags specific nouns.
    * *Services:* (e.g., `AWS Lambda`, `Amazon S3`)
    * *Components:* (e.g., `Execution Role`, `S3 Bucket Policy`)
    * *Configurations:* (e.g., `MemorySize`, `Timeout`)
* **Relationship Mapping:** Defines directed edges between entities based on the AKU.
    * *Example:* `AWS Lambda` → [DEPENDS_ON] → `IAM Execution Role`.
* **Importance Signals:** Assigns a weight to the topic based on structural position (e.g., was it derived from an H1 title or a deeply nested bullet point?) and frequency of occurrence across the service domain.

---

## 5. Hierarchical Summarisation
The final stage rolls up the atomic data into a four-level compression stack. Summaries at Level $N$ are used strictly as the input to generate Level $N+1$, ensuring extreme data reduction at the top level without hallucination.

| Level | Scope | Mechanism / Output |
| :--- | :--- | :--- |
| **Level 0** | **Chunk Level** | Direct synthesis of the highest-value AKUs extracted from a single Markdown chunk. |
| **Level 1** | **Document Level** | Synthesis of all Level 0 summaries within a single `.md` file (e.g., `ec2-ug.md`). |
| **Level 2** | **Domain Level** | Synthesis of all Level 1 summaries for an entire AWS Service (e.g., the complete "Amazon EC2" profile). |
| **Level 3** | **Org Overview** | A global snapshot of the AWS ecosystem, synthesizing all Level 2 domain summaries into a single executive artifact. |