"""
Module 2 – Knowledge Graph Construction
========================================
AWS Knowledge Compression Pipeline

Consumes the output of Module 1:
  - chunks.json  : chunked document segments with metadata
  - akus.json    : Atomic Knowledge Units (subject, predicate, object) per chunk

Produces:
  - knowledge_graph.json : a structured knowledge graph with scored nodes and edges

Uses only Python standard library (no external dependencies required).

Usage
-----
    python module2.py \\
        --chunks  ../chunks.json \\
        --akus    ../akus.json \\
        --output  knowledge_graph.json
"""

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def normalize_entity(text: str) -> str:
    """Return a canonical key for an entity string."""
    return " ".join(text.strip().lower().split())


def minmax_normalize(values: list) -> list:
    """Min-max scale a list of floats to [0, 1]."""
    if not values:
        return values
    lo, hi = min(values), max(values)
    if hi == lo:
        return [1.0 if hi > 0 else 0.0] * len(values)
    return [(v - lo) / (hi - lo) for v in values]


# ──────────────────────────────────────────────────────────────────────────────
# Loading
# ──────────────────────────────────────────────────────────────────────────────

def load_json(path: str):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ──────────────────────────────────────────────────────────────────────────────
# Topic extraction
# ──────────────────────────────────────────────────────────────────────────────

def extract_topics(chunks: list) -> list:
    """
    Group chunks by unique heading_path into topics.
    Returns a sorted list of topic dicts.
    """
    path_to_chunks = defaultdict(list)
    for chunk in chunks:
        path = tuple(chunk.get("heading_path") or [])
        path_to_chunks[path].append(chunk["chunk_id"])

    topics = []
    for idx, (path, chunk_ids) in enumerate(sorted(path_to_chunks.items())):
        topics.append({
            "topic_id": f"t{idx}",
            "heading_path": list(path),
            "chunk_ids": chunk_ids,
        })
    return topics


# ──────────────────────────────────────────────────────────────────────────────
# Graph construction (stdlib-only, no networkx)
# ──────────────────────────────────────────────────────────────────────────────

def build_graph(chunks: list, akus: list) -> tuple:
    """
    Build a knowledge graph from AKU triples using plain dicts.

    Returns:
        nodes  : dict  { entity_key -> {label, frequency, min_position, heading_depth} }
        edges  : dict  { (src, pred, tgt) -> {weight, source_chunks} }
        adj    : dict  { entity_key -> set of neighbour keys } (undirected view for degree)
    """
    chunk_meta = {c["chunk_id"]: c for c in chunks}

    nodes = {}   # key -> attrs
    edges = {}   # (src, pred, tgt) -> {weight, source_chunks}
    adj = defaultdict(set)   # adjacency for degree computation

    def ensure_entity(key: str, raw: str, chunk_id: str) -> None:
        chunk = chunk_meta.get(chunk_id, {})
        pos   = chunk.get("position", 0)
        depth = len(chunk.get("heading_path") or [])
        if key not in nodes:
            nodes[key] = {
                "label":         raw.strip(),
                "frequency":     0,
                "min_position":  pos,
                "heading_depth": depth,
            }
        else:
            if pos < nodes[key]["min_position"]:
                nodes[key]["min_position"] = pos
            if depth > nodes[key]["heading_depth"]:
                nodes[key]["heading_depth"] = depth
        nodes[key]["frequency"] += 1

    for aku_entry in akus:
        chunk_id = aku_entry["chunk_id"]
        for triple in aku_entry.get("akus", []):
            if len(triple) != 3:
                continue
            subj_raw, pred_raw, obj_raw = triple
            subj_key = normalize_entity(subj_raw)
            obj_key  = normalize_entity(obj_raw)
            pred     = pred_raw.strip()

            if not subj_key or not obj_key:
                continue

            ensure_entity(subj_key, subj_raw, chunk_id)
            ensure_entity(obj_key,  obj_raw,  chunk_id)

            edge_key = (subj_key, pred, obj_key)
            if edge_key not in edges:
                edges[edge_key] = {"weight": 0, "source_chunks": []}
            edges[edge_key]["weight"] += 1
            if chunk_id not in edges[edge_key]["source_chunks"]:
                edges[edge_key]["source_chunks"].append(chunk_id)

            adj[subj_key].add(obj_key)
            adj[obj_key].add(subj_key)

    # Seed heading labels as entities
    for chunk in chunks:
        chunk_id = chunk["chunk_id"]
        for heading in (chunk.get("heading_path") or []):
            key = normalize_entity(heading)
            if key:
                ensure_entity(key, heading, chunk_id)

    return nodes, edges, adj


# ──────────────────────────────────────────────────────────────────────────────
# Importance scoring
# ──────────────────────────────────────────────────────────────────────────────

FREQ_WEIGHT       = 0.40
STRUCT_WEIGHT     = 0.30
CENTRALITY_WEIGHT = 0.30


def compute_importance(nodes: dict, adj: dict) -> None:
    """
    Add normalised importance scores to every node (in-place).

    importance = 0.40 * freq_norm
               + 0.30 * structural_norm   (earlier position = higher score)
               + 0.30 * centrality_norm   (higher degree = higher score)
    """
    keys = list(nodes.keys())
    if not keys:
        return

    n = len(keys)

    # -- frequency
    freqs = [nodes[k]["frequency"] for k in keys]
    freq_norm = minmax_normalize(freqs)

    # -- structural position (invert: lower position index → more important)
    positions  = [nodes[k]["min_position"] for k in keys]
    max_pos    = max(positions) if positions else 1
    inv_pos    = [max_pos - p for p in positions]
    struct_norm = minmax_normalize(inv_pos)

    # -- degree centrality (normalised adjacency size)
    max_degree = max((len(adj.get(k, set())) for k in keys), default=1)
    max_degree = max(max_degree, 1)
    raw_cent   = [len(adj.get(k, set())) / max_degree for k in keys]
    cent_norm  = minmax_normalize(raw_cent)

    for i, key in enumerate(keys):
        score = (FREQ_WEIGHT       * freq_norm[i]
                 + STRUCT_WEIGHT     * struct_norm[i]
                 + CENTRALITY_WEIGHT * cent_norm[i])
        nodes[key]["structural_position"] = round(struct_norm[i], 6)
        nodes[key]["degree_centrality"]   = round(cent_norm[i],   6)
        nodes[key]["importance"]          = round(score,           6)


# ──────────────────────────────────────────────────────────────────────────────
# Serialisation
# ──────────────────────────────────────────────────────────────────────────────

def build_output(nodes: dict, edges: dict, topics: list,
                 total_chunks: int, total_akus: int) -> dict:
    """Assemble the final JSON-serialisable output dict."""

    nodes_out = []
    for node_id, data in nodes.items():
        nodes_out.append({
            "id":                   node_id,
            "label":                data.get("label", node_id),
            "frequency":            data.get("frequency", 0),
            "structural_position":  data.get("structural_position", 0.0),
            "degree_centrality":    data.get("degree_centrality", 0.0),
            "importance":           data.get("importance", 0.0),
        })
    nodes_out.sort(key=lambda x: x["importance"], reverse=True)

    edges_out = []
    for (src, pred, tgt), edata in edges.items():
        edges_out.append({
            "source":        src,
            "target":        tgt,
            "predicate":     pred,
            "weight":        edata["weight"],
            "source_chunks": edata["source_chunks"],
        })
    edges_out.sort(key=lambda x: x["weight"], reverse=True)

    return {
        "metadata": {
            "total_chunks":  total_chunks,
            "total_akus":    total_akus,
            "total_nodes":   len(nodes_out),
            "total_edges":   len(edges_out),
            "total_topics":  len(topics),
            "generated_at":  datetime.now(timezone.utc).isoformat(),
        },
        "topics": topics,
        "nodes":  nodes_out,
        "edges":  edges_out,
    }


# ──────────────────────────────────────────────────────────────────────────────
# Validation
# ──────────────────────────────────────────────────────────────────────────────

def validate_output(output: dict) -> list:
    """Return a list of error strings (empty = valid)."""
    errors = []
    node_ids = {n["id"] for n in output["nodes"]}

    for edge in output["edges"]:
        if edge["source"] not in node_ids:
            errors.append(f"Edge source not in nodes: {edge['source']!r}")
        if edge["target"] not in node_ids:
            errors.append(f"Edge target not in nodes: {edge['target']!r}")

    for node in output["nodes"]:
        imp = node["importance"]
        if not (0.0 <= imp <= 1.001):
            errors.append(f"Node {node['id']!r} has out-of-range importance: {imp}")

    return errors


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Module 2 – Knowledge Graph Construction (stdlib-only).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--chunks", default="../chunks.json",
                        help="Path to chunks.json  (default: %(default)s)")
    parser.add_argument("--akus",   default="../akus.json",
                        help="Path to akus.json    (default: %(default)s)")
    parser.add_argument("--output", default="knowledge_graph.json",
                        help="Output file path     (default: %(default)s)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # ── load inputs ───────────────────────────────────────────────────────────
    print(f"[Module 2] Loading chunks from:  {args.chunks}")
    chunks = load_json(args.chunks)
    print(f"           Loaded {len(chunks)} chunks")

    print(f"[Module 2] Loading AKUs from:    {args.akus}")
    akus = load_json(args.akus)
    total_akus = sum(len(e.get("akus", [])) for e in akus)
    print(f"           Loaded {len(akus)} AKU entries / {total_akus} triples")

    # ── extract topics ────────────────────────────────────────────────────────
    topics = extract_topics(chunks)
    print(f"\n[Module 2] Topics identified:    {len(topics)}")

    # ── build graph ───────────────────────────────────────────────────────────
    print("[Module 2] Building knowledge graph …")
    nodes, edges, adj = build_graph(chunks, akus)
    print(f"           Nodes: {len(nodes)}   Edges: {len(edges)}")

    # ── compute importance ────────────────────────────────────────────────────
    print("[Module 2] Computing importance scores …")
    compute_importance(nodes, adj)

    # ── assemble output ───────────────────────────────────────────────────────
    output = build_output(nodes, edges, topics, len(chunks), total_akus)

    # ── validate ──────────────────────────────────────────────────────────────
    errors = validate_output(output)
    if errors:
        print("\n[Module 2] VALIDATION ERRORS:", file=sys.stderr)
        for e in errors:
            print(f"  • {e}", file=sys.stderr)
        sys.exit(1)
    else:
        print("[Module 2] Validation passed ✓")

    # ── write output ──────────────────────────────────────────────────────────
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    m = output["metadata"]
    print(f"\n[Module 2] Output written to: {out_path}")
    print(f"           {m['total_nodes']} nodes | "
          f"{m['total_edges']} edges | "
          f"{m['total_topics']} topics")

    # ── top-10 most important entities ────────────────────────────────────────
    top10 = output["nodes"][:10]
    print("\n  Top-10 most important entities:")
    print(f"  {'Rank':<5} {'Importance':>10}  {'Entity'}")
    print("  " + "-" * 60)
    for i, node in enumerate(top10, 1):
        label = node["label"][:45]
        print(f"  {i:<5} {node['importance']:>10.4f}  {label}")


if __name__ == "__main__":
    main()
