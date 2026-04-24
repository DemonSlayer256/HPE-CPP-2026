# Module 1: LLM-Based Document Chunking & AKU Extraction

## Overview

Module 1 is the first stage of the AWS Knowledge Compression Pipeline. It consists of two scripts that work together:

1. **parsing.py**: Cleans raw markdown documentation by removing noise (TOC, copyright, repeated headers, etc.) and reduces token count for efficient processing
2. **llm_pipeline.py**: Processes the cleaned markdown using Google's Gemini AI model to extract structured knowledge artifacts

The pipeline produces:
- **chunks_{i}.json**: Semantic chunks of knowledge with metadata (one file per API request)
- **akus_{i}.json**: Atomic Knowledge Units (AKUs) extracted from each chunk in Subject-Relation-Object form (one file per API request)

The module splits large documents into chunks of up to 100,000 characters, sends each chunk to the Gemini AI for processing, and handles multiple requests with error handling and raw response dumps.

## Prerequisites

- Python 3.8+
- Google AI API key (Gemini)
- pip package manager

## Installation

### 1. Install Dependencies

```bash
pip install google-genai
```

### 2. Set Up API Key

The script uses a hardcoded API key. For production use, consider using environment variables:

```python
import os
api_key = os.getenv('GOOGLE_AI_API_KEY')
```

## Scripts

### parsing.py

**Purpose**: Preprocesses raw markdown files to remove noise and reduce token count before sending to the LLM.

**Functions**:
- Fixes encoding artifacts (ligatures, special characters)
- Removes noise lines (copyright, trademarks, TOC headers)
- Eliminates repeated headers and TOC blocks
- Normalizes spacing and formatting

**Usage**:
```bash
python parsing.py <input_md_file> <optional_output_dir>
```

Example:
```bash
python parsing.py ../../data/prototype/S3/L0/s3-api.md cleaned/
```

**Output**: Cleaned markdown file in the specified output directory (default: `cleaned/`)

### llm_pipeline.py

**Purpose**: Processes cleaned markdown using Gemini AI to extract chunks and AKUs.

**Functions**:
- Splits large documents into API-sized chunks
- Sends structured prompts to Gemini with chunking rules
- Parses JSON responses into chunks and AKUs
- Handles multiple requests for large documents
- Provides error handling with raw response dumps

**Usage**:
```bash
python llm_pipeline.py <cleaned_md_file> <output_directory>
```

Example:
```bash
python llm_pipeline.py cleaned/s3-api.md output/
```

**Output**:
- `chunks_{request_number}.json`: Chunks from each API request
- `akus_{request_number}.json`: AKUs from each API request
- `raw_request_{request_number}.json`: Raw API response (only on parsing errors)

## Full Pipeline Usage

To process a document end-to-end:

```bash
# Step 1: Clean the raw markdown
python parsing.py ../../data/prototype/S3/L0/s3-api.md cleaned/

# Step 2: Extract knowledge artifacts
python llm_pipeline.py cleaned/s3-api.md output/
```

## Configuration

Edit constants in `llm_pipeline.py`:

- `MODEL`: Gemini model to use (default: "gemini-2.0-flash-exp")
- `MAX_INPUT_CHARS`: Maximum characters per request (default: 100000)

## How It Works

1. **Preprocessing (parsing.py)**: Cleans the raw markdown by removing noise, fixing encoding, eliminating repeated content, and normalizing formatting to reduce token count
2. **Load Cleaned Document (llm_pipeline.py)**: Reads the preprocessed markdown file
3. **Calculate Requests**: Determines how many API requests are needed based on document size and `MAX_INPUT_CHARS`
4. **Split & Process**: For each chunk:
   - Extracts a portion of the document
   - Builds a prompt with chunking and AKU extraction rules
   - Sends to Gemini AI with request metadata (number, total, character range)
   - Parses the JSON response
   - Saves chunks and AKUs to numbered files
5. **Error Handling**: If JSON parsing fails, dumps raw response and stops, showing last successful character position

### Prompt Structure

The AI is instructed to:
- Remove any remaining noise (TOC, headers, code blocks, etc.)
- Create semantic chunks of 150-500 words
- Extract meaningful AKUs as [subject, relation, object] triples
- Focus on domain knowledge from descriptive text

## Output Files

### chunks_{i}.json

Contains structured chunks with:
- `chunk_id`: Unique identifier (e.g., "c0")
- `text`: Chunk content
- `token_count`: Estimated token count
- `heading_path`: Document hierarchy
- `section_type`: "concept", "api", "reference", or "procedure"
- `position`: Sequential position
- `overlap_start`: Words overlapping with previous chunk
- `overlap_end`: Words overlapping with next chunk

### akus_{i}.json

Contains extracted AKUs per chunk:
- `chunk_id`: Reference to chunk
- `akus`: Array of [Subject, Relation, Object] triples

Example AKU:
```
["S3 bucket", "stores", "objects"]
```

## Error Handling

- **Parsing Errors**: If the AI response cannot be parsed as JSON, the raw response is saved to `raw_request_{i}.json`
- **API Errors**: The script stops on the first failed request and reports the last successful character position
- **Progress Tracking**: Shows request progress and success/failure status

## Troubleshooting

**Issue**: API key invalid
- Verify your Google AI API key
- Check API quotas and billing

**Issue**: Model not found
- Update `MODEL` to a valid Gemini model name

**Issue**: Large documents
- The script automatically splits large documents
- Monitor the number of requests needed

**Issue**: Parsing failures
- Check `raw_request_{i}.json` for the raw AI response
- The response may contain markdown formatting around JSON
```

**Issue**: No chunks generated
- Check that input file contains meaningful content sections
- Verify chunk size constraints match your document

**Issue**: Few or no AKUs extracted
- Content may lack domain terminology
- Review `DOMAIN_TERMS` and `BAD_*` filters for your domain
