# Caching Strategy

## Multi-Level Cache Architecture for Latency, Cost & Computation Optimization

---

## 1. Executive Summary

The multi-level caching strategy is a core optimization component of the Hierarchical AWS LLM System.

Instead of recomputing responses for every query, the system stores and reuses previously computed artifacts at different abstraction levels:

- L1 → Final Answers  
- L2 → Contextual Building Blocks  
- L3 → Structured Knowledge  

This layered approach reduces latency, token usage, and computation while maintaining accuracy through version-controlled invalidation.

---

## 2. Objectives

The caching system is designed to:

- Reduce redundant computation  
- Minimize token usage  
- Improve response latency  
- Enhance scalability  
- Ensure factual consistency with AWS documentation  

---

## 3. Multi-Level Cache Architecture

| Level | Cache Name | Cached Data | Role |
|------|------------|------------|------|
| L1 | Answer Cache | Final responses | Instant retrieval |
| L2 | Context Cache | Reusable context blocks | Prompt construction |
| L3 | Knowledge Cache | Structured knowledge | Source of truth |

---

## 4. Cache Level Specifications

---

### 4.1 L1 Cache — Answer Cache

Stores final LLM-generated responses.

#### Mechanism

- Query normalization (lowercase, punctuation removal)
- Semantic matching using embeddings (cosine similarity)
- Similarity threshold for safe reuse
- Key-value lookup (e.g., Redis)

#### Example

Queries like:

- "How to upload file to S3?"
- "How can I store files in S3?"

→ Can reuse the same cached response.

#### Advantages

- Instant response (no LLM call)
- Maximum cost savings
- High performance

#### Limitations

- Works only for similar queries
- Requires versioning to avoid stale responses

---

### 4.2 L2 Cache — Context Cache

Stores reusable contextual building blocks used to construct prompts.

#### Definition

L2 consists of:

- **L0 (Global)** → System instructions  
- **L1 (Domain)** → AWS domain knowledge  
- **L2 (Topic)** → Specific task-level details  

#### Key Concept

> L2 does NOT store answers — it stores reusable explanation units.

#### Mechanism

- Context blocks are pre-built
- Relevant blocks are selected per query
- Blocks are dynamically assembled into prompts

#### Example

Queries:

- "Upload file to S3"
- "Store images in S3"

→ Reuse:

- S3 explanation  
- Storage context  

#### Advantages

- Reduces prompt construction cost
- Enables reuse across queries
- Modular design

#### Limitations

- Requires LLM generation
- Needs version validation

---

### 4.3 L3 Cache — Knowledge Cache

Stores structured knowledge extracted from raw documentation.

#### Components

- Atomic Knowledge Units (AKUs)
- Summaries
- Knowledge graph triples

#### Role

L3 acts as the **source of truth**.

#### Important Clarification

> L3 is NOT query-specific.  
> Queries are mapped to L3 via retrieval (keyword or embedding search).

#### Mechanism

- Raw documents are processed once
- Knowledge is extracted and stored
- Retrieved when needed to build context

#### Advantages

- Eliminates repeated document processing
- Ensures factual accuracy
- High reuse potential

#### Limitations

- Requires retrieval logic
- Needs transformation into L2

---

## 5. System Interaction & Flow

### Step 1: Query Understanding

- Identify topic (e.g., S3, EC2)
- Use keyword or embedding-based retrieval

---

### Step 2: L1 Cache Check

- Check exact or semantic match
- If found → return cached response

---

### Step 3: L2 Cache Check

- Retrieve context blocks
- Assemble prompt
- Send to LLM

---

### Step 4: L3 Cache Check

- Retrieve structured knowledge
- Build context dynamically
- Send to LLM

---

### Step 5: Full Pipeline

- Process raw documents
- Generate AKUs and knowledge graph
- Store across all cache layers

---

## 6. Cache Invalidation Strategy

---

### 6.1 Time-Based Expiry (TTL)

| Layer | TTL |
|------|-----|
| L1 | 1–6 hours |
| L2 | 1–3 days |
| L3 | 1–2 weeks |

---

### 6.2 Version-Based Invalidation (Git Commit Hash)

Each cache entry is tagged with a Git commit hash representing the documentation version.

#### Mechanism

- System always uses latest hash
- Cache keys include hash
- Old cache is automatically ignored

#### Key Insight

> Cache is not deleted — outdated entries are simply not used.

---

### 6.3 Dynamic Cache Key Construction

| Layer | Key |
|------|-----|
| L1 | query + context_hash + commit_hash |
| L2 | context_hash + commit_hash |
| L3 | topic + commit_hash |

#### Benefit

- Automatic invalidation
- No manual clearing
- Ensures consistency

---

### 6.4 Cache Analytics & Monitoring (CORE)

Tracks:

- Cache hit/miss ratio  
- Latency per cache layer  
- TTL expiry behavior  

#### Role

- Identifies bottlenecks  
- Helps tune TTL and thresholds  
- Enables performance optimization  

> Monitoring is essential for production systems.

---

## 7. Performance & Token Savings

| Layer | Hit Rate | Token Savings |
|------|---------|--------------|
| L1 | 20–30% | ~100% |
| L2 | 50–70% | 50–70% |
| L3 | 80–90% | 30–50% |

### Overall Impact

> 40–70% reduction in token usage

---

## 8. Additional Optimizations (Optional)

---

### 8.1 Adaptive TTL

Adjusts expiry based on usage frequency.

---

### 8.2 Cache Warm-Up

Preloads frequently used queries and context blocks.

---

### 8.3 Cache Safety Constraint

Ensures all cache entries match current Git hash.

---

## 9. Design Principles

- Reuse over recompute  
- Layered knowledge representation  
- Version-controlled accuracy  
- Latency optimization  
- Fact-grounded responses  

---

## 10. Conclusion

The multi-level caching architecture transforms the system into a scalable and efficient knowledge engine.

By combining:

- L1 → Answers  
- L2 → Context  
- L3 → Knowledge  

The system achieves improvements in:

- Speed  
- Cost  
- Accuracy  

---

### Final Insight

> Query understanding determines what to retrieve  
> Versioning ensures correctness