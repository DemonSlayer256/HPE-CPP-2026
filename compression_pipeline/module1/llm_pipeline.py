import os
import json
import sys
import google.genai as genai

# Configuration

MODEL = "gemini-2.5-flash"
MAX_INPUT_CHARS = 10000

def build_prompt(md_text_chunk, request_num, total_requests, start_char, end_char):
    return f"""
You are an expert system for extracting structured knowledge from technical API documentation.

Your task is to process the given markdown document and output TWO structured artifacts:

1. CHUNKS (semantic units of knowledge)
2. AKUs (Atomic Knowledge Units: subject-relation-object triples)

Return ONLY valid JSON in this exact format:

{{
  "chunks": [
    {{
      "chunk_id": "c0",
      "text": "...",
      "token_count": 123,
      "heading_path": ["..."],
      "section_type": "concept | api | reference | procedure",
      "position": 0,
      overlap_start: 0,  # number of words overlapping with previous chunk
      overlap_end: 0     # number of words overlapping with next chunk
    }}
  ],
  "akus": [
    {{
      "chunk_id": "c0",
      "akus": [
        ["subject", "relation", "object"]
      ]
    }}
  ]
}}

DO NOT include any explanation. ONLY JSON.
CHUNKING RULES

- Remove noise:
  - table of contents
  - repeated headers
  - copyright / trademarks
  - navigation text

- Preserve:
  - headings
  - paragraphs
  - meaningful lists
  - API descriptions

- DO NOT include:
  - raw HTTP request examples
  - code blocks
  - authorization headers
  - sample requests/responses

- Chunk constraints:
  - Each chunk = ONE coherent topic
  - 150-500 words per chunk
  - Do NOT mix unrelated topics
  - Split large sections (like "Actions")

- Special handling:
  - Large API lists → split into multiple chunks
  - Keep heading hierarchy in "heading_path"

Assign each chunk:

- "concept" → definitions, explanations
- "procedure" → how-to / steps
- "api" → API operation descriptions
- "reference" → lists, parameters, enums

AKU EXTRACTION RULES
Extract ONLY meaningful domain knowledge.

Each AKU = (subject, relation, object)

GOOD examples:
- ("UploadId", "identifies", "multipart upload")
- ("CreateSession API", "returns", "session token")
- ("Bucket name", "must follow", "naming rules")

BAD examples:
- vague pronouns (it, this, they)
- generic verbs (is, has, does)
- broken phrases
- anything from code or HTTP examples

AKU CONSTRAINTS

- subject and object:
  - 2-6 words
  - domain-specific
  - no noise text

- relations:
  - use meaningful verbs:
    - "requires"
    - "returns"
    - "identifies"
    - "specifies"
    - "supports"
    - "fails_if"
    - "must_include"
    - "must_follow"

- Extract as many AKUs per chunk as possible, but only if they meet the quality criteria.

- Only extract AKUs from:
  - descriptive text
  - constraints
  - permissions
  - API definitions

This is request {request_num} of {total_requests}. Processing characters {start_char} to {end_char}.

INPUT DOCUMENT
{md_text_chunk[:MAX_INPUT_CHARS]}
"""

# Gemini call
def call_gemini(prompt):
    client = genai.Client(api_key='YOUR_API_KEY')

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text


def parse_output(text):
    try:
        # Handle markdown-wrapped JSON
        if "```" in text:
            parts = text.split("```")
            for p in parts:
                if p.strip().startswith("{") or p.strip().startswith("json"):
                    text = p.strip()
                    if text.startswith("json"):
                        text = text[4:].strip()
                    break

        return json.loads(text)

    except Exception as e:
        raise e

def run(input_path, output_dir):
    with open(input_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    total_chars = len(md_text)
    num_requests = (total_chars + MAX_INPUT_CHARS - 1) // MAX_INPUT_CHARS  # ceil division

    print(f"Total characters: {total_chars}")
    print(f"Max input chars per request: {MAX_INPUT_CHARS}")
    print(f"Number of requests needed: {num_requests}")

    os.makedirs(output_dir, exist_ok=True)

    last_successful_end = 0

    for i in range(1, num_requests + 1):
        start = (i - 1) * MAX_INPUT_CHARS
        end = min(i * MAX_INPUT_CHARS, total_chars)
        chunk_text = md_text[start:end]

        prompt = build_prompt(chunk_text, i, num_requests, start, end)

        print(f"[LLM] Sending request {i} of {num_requests}...")
        raw_output = call_gemini(prompt)

        print(f"[LLM] Parsing response for request {i}...")
        try:
            data = parse_output(raw_output)

            chunks = data.get("chunks", [])
            akus = data.get("akus", [])

            with open(os.path.join(output_dir, f"chunks_{i}.json"), "w") as f:
                json.dump(chunks, f, indent=2)

            with open(os.path.join(output_dir, f"akus_{i}.json"), "w") as f:
                json.dump(akus, f, indent=2)

            print(f"Request {i} successful | Chunks: {len(chunks)} | AKUs: {sum(len(a['akus']) for a in akus)}")

            last_successful_end = end

        except Exception as e:
            print(f"Failed to parse JSON output for request {i}")
            # dump raw response
            with open(os.path.join(output_dir, f"raw_request_{i}.json"), "w", encoding="utf-8") as f:
                f.write(raw_output)
            print(f"Raw response dumped to raw_request_{i}.json")
            print(f"Last successful end character: {last_successful_end}")
            sys.exit(1)

    print("All requests completed successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python llm_pipeline.py <input_md> <output_dir>")
        sys.exit(1)

    run(sys.argv[1], sys.argv[2])