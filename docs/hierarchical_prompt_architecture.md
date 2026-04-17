# Hierarchical Prompt Architecture

## 1. Overview

This document defines the static context loading strategy for the compressed AWS knowledge base.

Because the full AWS documentation cannot fit within a single prompt without degrading reasoning quality and exceeding context limits, the knowledge is structured into three layers.

This architecture ensures:

* Foundational context is always available
* Domain knowledge is selectively loaded
* Specific topics are injected only when required

This prevents context dilution and enables high-signal reasoning within strict token constraints.

---

## 2. Token Budget Summary

| Layer | Tokens               | Trigger          |
| ----- | -------------------- | ---------------- |
| L0    | 500–1000             | Always           |
| L1    | 2000–3000 per domain | Intent-based     |
| L2    | 500–2000 per topic   | Entity-triggered |

---

## 3. Layer 0: The Core Snapshot (Always Loaded)

**Token Budget:** ~500–1000 tokens
**Loading Trigger:** Always Active

### Specification

Layer 0 is a dense, cross-linked snapshot of foundational AWS primitives.

It defines system-wide invariants and service interactions.

### Structure

* Entities → Core services
* Relationships → Service interactions
* Constraints → Limits and defaults
* Scope → Global vs regional behavior

### Constraints

Layer 0 must not include:

* Procedural steps
* Configuration details
* Deep implementation logic

---

## 4. Layer 1: Domain-Specific Blocks

**Token Budget:** ~2000–3000 tokens
**Loading Trigger:** Intent Classification

### Supported Domains

* Database
* Infrastructure as Code
* Observability

### Specification

* Contains compressed domain-level knowledge
* Multiple domains may be loaded
* Maximum of 2–3 domains

### Mapping Priority

**Explicit Entity > Keyword Match > Semantic Intent**

---

## 5. Layer 2: On-Demand Topics

**Token Budget:** ~500–2000 tokens per topic
**Loading Trigger:** Entity Detection

### Specification

* Contains service-specific knowledge
* Loaded only when required

### Trigger Mechanism

* Exact match (e.g., API Gateway)
* Semantic match (e.g., API endpoints)

### Constraints

* Maximum 2–3 topics
* Skipped if no relevant entities

---

## 6. Fact Grounding (AKUs)

### Role

AKUs provide atomic, verifiable facts used to ground responses.

### Contents

* Service relationships
* Limits and configurations
* Critical constraints

### Behavior

AKUs are injected before all layers in the final prompt and act as the primary factual grounding mechanism. They are used for maintaining the following parameters strictly.

  * Limits
  * Configurations
  * Permissions

---

## 7. Routing Strategy

### Inputs

* Query text
* Detected entities
* Semantic intent

### Priority

**Explicit Entity > Keyword > Semantic Intent**

### Output

* Selected domains (Layer 1)
* Selected topics (Layer 2)

---

## 8. Prompt Ordering Strategy

Final prompt structure:

1. AKUs (facts)
2. Layer 1 (domain context)
3. Layer 2 (topic context, if needed)
4. Layer 0 (core snapshot)

This ordering ensures:

* Facts anchor reasoning
* Domain context guides interpretation
* Details refine outputs

---

## 9. Context Optimization

### Techniques

* Deduplication of repeated entities
* Removal of overlapping summaries
* Priority-based trimming

### Trimming Order

**Layer 2 → Layer 1 → Layer 0**

---

## 10. Layer Interaction Model

* Layer 0 → Provides system-wide constraints
* Layer 1 → Narrows reasoning to domain
* Layer 2 → Injects precise task-level details

This creates a progressive refinement pipeline:

**General → Specific → Precise**

---

## 11. Edge Case Handling

### No Match

Fallback to Layer 0 + closest semantic domain

### Too Many Matches

Limit to top 2–3 domains/topics

### Ambiguous Query

Prioritize broader domain over specific topics

---

## 12. Assembly Example

### Query

"Deploy RDS Postgres using CloudFormation and monitor CPU"

### Context Assembly

* Layer 0 → Core services and relationships
* Layer 1 → IaC, Database, Observability
* Layer 2 → Not required

This ensures high relevance with minimal redundancy.

---

## 13. Final Summary

This architecture transforms prompting from **Flat context loading** into **Structured, layered knowledge injection**

It functions as a context-aware reasoning system rather than a static prompt.