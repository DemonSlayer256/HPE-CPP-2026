import json
import os
import sys
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')
# Ensure the local summarizer package can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from summarizer.pipeline import run_pipeline

# ---------------------------------------------------------------------------
# Configuration — tune these to control performance vs. quality
# ---------------------------------------------------------------------------
CHUNKS_PER_SECTION = 20   # Smaller = faster TextRank (O(n²) on sentences)


def build_bridge_input():
    """Reads Module 1 output and mocks Module 2 data for testing.

    Key optimisation: splits chunks into multiple sections of
    CHUNKS_PER_SECTION size so that TextRank doesn't have to process
    thousands of sentences at once.
    """
    m1_dir = os.path.abspath("./module1/s3/intermediate/")
    chunks_path = os.path.join(m1_dir, "chunks.json")
    akus_path = os.path.join(m1_dir, "akus.json")

    print(f"Loading Module 1 data from: {m1_dir}")

    with open(chunks_path, 'r') as f:
        m1_chunks = json.load(f)
    with open(akus_path, 'r') as f:
        m1_akus = json.load(f)

    # Handle both dict and list structures from Module 1 output
    chunk_list = m1_chunks if isinstance(m1_chunks, list) else list(m1_chunks.values())
    aku_list = m1_akus if isinstance(m1_akus, list) else list(m1_akus.values())

    print(f"  Total chunks loaded: {len(chunk_list)}")
    print(f"  Total AKUs loaded:   {len(aku_list)}")

    # Format the flat M1 chunks into the nested schema expected by M3
    formatted_chunks = []
    for i, chunk_text in enumerate(chunk_list):
        # Extract text safely
        text = chunk_text.get("text", str(chunk_text)) if isinstance(chunk_text, dict) else str(chunk_text)

        # Match AKUs
        chunk_aku = aku_list[i].get("akus", []) if i < len(aku_list) and isinstance(aku_list[i], dict) else []

        # Mock Module 2 entities based on content keywords
        entities = ["AWS"]
        lower = text.lower()
        if "s3" in lower:
            entities.extend(["AWS S3", "Amazon S3"])
        if "iam" in lower:
            entities.append("IAM Role")
        if "ec2" in lower:
            entities.append("Amazon EC2")
        if "lambda" in lower:
            entities.append("AWS Lambda")
        if "cloudfront" in lower:
            entities.append("CloudFront")

        formatted_chunks.append({
            "chunk_id": f"chunk_{i:03d}",
            "text": text,
            "akus": chunk_aku,
            # --- MOCKING MODULE 2 DATA BELOW ---
            "entities": list(dict.fromkeys(entities)),  # deduplicate
            "relationships": [],
            "importance_score": 0.8,
        })

    # ---- Split chunks into multiple sections ----
    sections = []
    for start in range(0, len(formatted_chunks), CHUNKS_PER_SECTION):
        batch = formatted_chunks[start : start + CHUNKS_PER_SECTION]
        sec_idx = start // CHUNKS_PER_SECTION + 1
        sections.append({
            "section_id": f"sec_{sec_idx:03d}",
            "chunks": batch,
        })

    print(f"  Sections created:    {len(sections)} (≤{CHUNKS_PER_SECTION} chunks each)")

    # Wrap in the final master schema
    input_data = {
        "documents": [
            {
                "doc_id": "AWS-S3-Module1-Test",
                "sections": sections,
            }
        ],
        "topics": [
            {
                "topic_id": "topic_mock_01",
                "label": "Storage Operations",
                "related_docs": ["AWS-S3-Module1-Test"],
            },
            {
                "topic_id": "topic_mock_02",
                "label": "Security & Access Control",
                "related_docs": ["AWS-S3-Module1-Test"],
            },
        ],
        "categories": {
            "Storage": ["topic_mock_01"],
            "Security": ["topic_mock_02"],
        },
    }

    return input_data


def main():
    t_start = time.time()

    print("=" * 60)
    print("  Module 3 — Hierarchical Summarization (Integration Test)")
    print("=" * 60)

    print("\nStep 1: Building bridged input data...")
    input_data = build_bridge_input()

    print("\nStep 2: Triggering Hierarchical Summarization Pipeline...")
    print("  Pipeline: L4 (Sections) → L3 (Documents) → L2 (Topics) → L1 (Categories) → L0 (Global)\n")

    # This will run L4 -> L3 -> L2 -> L1 -> L0 automatically
    final_output = run_pipeline(
        input_data,
        level_4_max_tokens=500,
        level_3_max_tokens=200,
        level_2_max_tokens=100,
        level_1_max_tokens=50,
        level_0_max_tokens=25,
    )

    # Save raw pipeline output (for comparison)
    raw_output_path = "integration_output.json"
    with open(raw_output_path, 'w', encoding='utf-8') as f:
        json.dump(final_output, f, indent=2, ensure_ascii=False)

    # Step 3: Transform into clean structured format
    print(f"\nStep 3: Transforming into structured output format...")
    # transform_output.py is in the same directory as this script (module3/)
    # sys.path already has this directory appended at the top of the file
    from transform_output import transform_output
    structured = transform_output(final_output)

    structured_output_path = "structured_output.json"
    with open(structured_output_path, 'w', encoding='utf-8') as f:
        json.dump(structured, f, indent=2, ensure_ascii=False)

    # Summary stats
    total_orig = sum(s.get("token_count", 0) for s in final_output.get("level_4_sections", []))
    total_clean = sum(s["token_count"] for s in structured["level_4"])
    avg_ratio = sum(s["compression_ratio"] for s in structured["level_4"]) / len(structured["level_4"])

    elapsed = round(time.time() - t_start, 1)
    print(f"\n{'=' * 60}")
    print(f"  Integration Test Complete!")
    print(f"  Raw output:        {os.path.abspath(raw_output_path)}")
    print(f"  Structured output: {os.path.abspath(structured_output_path)}")
    print(f"  Sections: {len(structured['level_4'])}")
    print(f"  Tokens: {total_orig} → {total_clean} (compression: {avg_ratio:.1%})")
    print(f"  Total time: {elapsed}s")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()