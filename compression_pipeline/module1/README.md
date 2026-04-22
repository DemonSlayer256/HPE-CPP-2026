# Module 1: Document Chunking & AKU Extraction

## Overview

Module 1 is the first stage of the AWS Knowledge Compression Pipeline. It processes raw markdown documentation and produces:
- **chunks.json**: Semantic chunks of 200-500+ tokens with metadata and hierarchical context
- **akus.json**: Atomic Knowledge Units (AKUs) extracted from each chunk in Subject-Verb-Object form

The module preprocesses documents to remove noise (TOC, page numbers, copyright), parses markdown structure, creates overlapping chunks for context preservation, and extracts domain-relevant factual statements using NLP.

## Prerequisites

- Python 3.8+
- pip package manager

## Installation

### 1. Install Dependencies

```bash
pip install markdown-it-py spacy
python -m spacy download en_core_web_sm
```

### 2. Verify Installation

```bash
python -c "import markdown_it; import spacy; print('Dependencies OK')"
```

## Usage

### Basic Run

```bash
python parser.py
```

By default, this processes `../../data/prototype/S3/L0/s3-api.md` and outputs to `s3/intermediate/`.

### Custom Input and Output

Modify the `__main__` block in `parser.py`:

```python
if __name__ == "__main__":
    run("path/to/input.md", "path/to/output/dir")
```

Then run:

```bash
python parser.py
```

## Output Files

### chunks.json

Contains structured chunks with:
- `chunk_id`: Unique identifier (e.g., "c0")
- `text`: Chunk content with 100-token overlap with next chunk
- `tokens`: Word count
- `heading_path`: Document hierarchy
- `section_id`: Source section identifier
- `source`: Source reference
- `position`: Sequential position

### akus.json

Contains extracted AKUs per chunk:
- `chunk_id`: Reference to chunk
- `akus`: Array of [Subject, Verb, Object] tuples

Example AKU:
```
["S3 bucket", "store", "objects"]
```

## How It Works

1. **Load & Preprocess**: Removes TOC lines, API versions, headers, copyright, trademarks
2. **Parse**: Converts markdown to hierarchical sections with content
3. **Chunk**: Splits sections into semantic chunks (200-500+ tokens)
4. **Overlap**: Adds last 100 tokens from previous chunk for context
5. **Extract AKUs**: Uses spaCy NLP to identify Subject-Verb-Object triples from domain text

## Configuration

Edit constants in `parser.py` to customize:

- `BAD_SUBJECTS`, `BAD_OBJECTS`, `BAD_VERBS`: Filter low-quality AKUs
- `DOMAIN_TERMS`: AWS-specific vocabulary for relevance filtering
- Chunk size thresholds in `build_chunks()` function

## Troubleshooting

**Issue**: spaCy model not found
```bash
python -m spacy download en_core_web_sm
```

**Issue**: No chunks generated
- Check that input file contains meaningful content sections
- Verify chunk size constraints match your document

**Issue**: Few or no AKUs extracted
- Content may lack domain terminology
- Review `DOMAIN_TERMS` and `BAD_*` filters for your domain
