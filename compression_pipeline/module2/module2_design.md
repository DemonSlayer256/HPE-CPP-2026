# Module 2: Knowledge Graph Construction

## 1. Overview

Module 2 is the second stage of the **AWS Knowledge Compression Pipeline**. It transforms the raw structured output of Module 1 into a **knowledge graph** that captures the entities and relationships within the documentation.

The graph drives all downstream stages: nodes with high importance are preserved during summarisation; edges carry the relational context that keeps summaries factually grounded.

---

## 2. Inputs

| File | Produced by | Description |
|------|-------------|-------------|
| `chunks.json` | Module 1 | Array of document chunks with text, heading path, position, token count, and section ID |
| `akus.json` | Module 1 | Array of per-chunk AKU lists – each AKU is a `[subject, predicate, object]` triple |

### 2.1 Chunk schema (relevant fields)

```json
{
  "chunk_id": "c0",
  "text": "...",
  "tokens": 511,
  "heading_path": ["API Reference", "S3 API Reference"],
  "section_id": "cf29d78c-...",
  "source": "",
  "position": 0
}
```

### 2.2 AKU schema

```json
{
  "chunk_id": "c0",
  "akus": [
    ["Authenticated access", "require", "credentials that AWS can use to"],
    ["the SDK clients",      "authenticate", "your requests"]
  ]
}
```

---

## 3. Processing Pipeline

```
chunks.json ──┐
              ├──▶ Topic Extraction ──▶ topics[]
akus.json  ──┘
              └──▶ Graph Construction ──▶ G(nodes, edges)
                        │
                        ▼
                 Importance Scoring
                        │
                        ▼
               knowledge_graph.json
```

### 3.1 Topic Extraction

Chunks are grouped by their `heading_path` value. Each unique heading path becomes a **topic**, which maps to the set of chunk IDs that share it.

Topics are used by Module 3 to scope summarisation and ensure that section-level summaries cover all relevant chunks.

### 3.2 Entity Extraction

Entities are derived from two sources:

1. **AKU subjects and objects** — both ends of every triple are treated as entities. This is the primary source and covers named services, components, configurations, and API constructs.
2. **Section headings** — `heading_path` labels are seeded as entities to ensure structural document anchors are represented in the graph even if they appear only lightly in AKU triples.

All entity strings undergo **canonical normalisation**: stripped of leading/trailing whitespace, lower-cased, and collapsed to single internal spaces. This merges slight surface variations of the same entity.

### 3.3 Graph Construction

A **directed graph** (`networkx.DiGraph`) is built as follows:

| Element | Derivation |
|---------|-----------|
| **Node** | One per unique normalised entity |
| **Edge** | One per unique `(subject, predicate, object)` triple across all AKUs |
| Edge `weight` | Count of times the same triple appears across different chunks |
| Edge `source_chunks` | List of chunk IDs that contributed the triple |

### 3.4 Importance Scoring

Each node receives a composite **importance score ∈ [0, 1]** computed from three independent signals, each independently min-max normalised:

| Signal | Weight | Derivation |
|--------|--------|-----------|
| `frequency` | 40% | Number of AKU triples that reference the entity as subject or object |
| `structural_position` | 30% | Inverse of earliest chunk position — entities appearing near document start score higher |
| `degree_centrality` | 30% | Normalised sum of in-degree + out-degree in the graph |

**Formula:**

```
importance = 0.40 × freq_norm
           + 0.30 × structural_position_norm
           + 0.30 × degree_centrality_norm
```

This ensures that an entity must be both **frequently mentioned** and **well-connected** to score highly, rather than just occurring many times in isolated triples.

---

## 4. Output

### 4.1 File

`compression_pipeline/module2/knowledge_graph.json`

### 4.2 JSON Schema

```json
{
  "metadata": {
    "total_chunks":  <int>,
    "total_akus":    <int>,
    "total_nodes":   <int>,
    "total_edges":   <int>,
    "total_topics":  <int>,
    "generated_at":  "<ISO-8601 UTC timestamp>"
  },
  "topics": [
    {
      "topic_id":    "t0",
      "heading_path": ["API Reference", "S3 API Reference"],
      "chunk_ids":   ["c0", "c1", "c2", "..."]
    }
  ],
  "nodes": [
    {
      "id":                   "bucket owners",
      "label":                "Bucket owners",
      "frequency":            <int>,
      "structural_position":  <float 0–1>,
      "degree_centrality":    <float 0–1>,
      "importance":           <float 0–1>
    }
  ],
  "edges": [
    {
      "source":        "bucket owners",
      "target":        "this parameter",
      "predicate":     "specify",
      "weight":        <int>,
      "source_chunks": ["c2", "c26"]
    }
  ]
}
```

> **Ordering:** Nodes are sorted by `importance` descending; edges are sorted by `weight` descending.

---

## 5. Usage

```bash
cd compression_pipeline

# Default paths (chunks.json and akus.json in parent of module2/)
python module2/module2.py

# Explicit paths
python module2/module2.py \
  --chunks  chunks.json \
  --akus    akus.json \
  --output  module2/knowledge_graph.json
```

### CLI Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `--chunks` | `../chunks.json` | Path to Module 1 chunks output |
| `--akus` | `../akus.json` | Path to Module 1 AKUs output |
| `--output` | `knowledge_graph.json` | Destination for the knowledge graph JSON |

### Dependencies

```bash
pip install networkx
```

---

## 6. Downstream Usage (Module 3)

The knowledge graph is consumed by **Module 3: Hierarchical Summarisation** as follows:

- **High-importance nodes** → entities that *must* appear in every level of the summary hierarchy.
- **Edge predicates** → relational constraints that summaries must preserve (e.g. *"Bucket owners specify this parameter"*).
- **Topics** → scoping boundaries for section-level (Level 4) summaries.
- **AKU anchors** → factual correctness validators during compression.

---

## 7. Design Decisions

| Decision | Rationale |
|----------|-----------|
| Directed graph | AKU triples are inherently directional (`subject → object`). Undirected edges would lose predicate semantics. |
| Section headings as entity seeds | Ensures high-level structural anchors are graph nodes even if they appear only in chunk metadata and not explicitly in AKU triples. |
| Composite importance score | A single signal (e.g. frequency alone) could over-rank noisy entities. Combining frequency, position, and connectivity produces more stable rankings. |
| Edge deduplication with weight | Multiple occurrences of the same triple across chunks are collapsed into a single edge with a `weight` counter, keeping the graph compact while preserving co-occurrence information. |
| Min-max normalisation per signal | Makes each dimension comparable regardless of the raw value ranges. |
