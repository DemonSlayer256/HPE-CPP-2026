"""
CLI Entry Point for Module 3: Hierarchical Summarization

Usage:
    python -m summarizer.main input.json
    python -m summarizer.main input.json --output results.json

Loads the input JSON (combined output of Module 1 + Module 2), runs the
hierarchical summarization pipeline, and writes the output to a JSON file.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

from summarizer.pipeline import run_pipeline


def _setup_logging(verbose: bool = False) -> None:
    """Configure root logger."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="summarizer",
        description="Module 3 — Hierarchical Summarization Pipeline",
    )
    parser.add_argument(
        "input",
        type=str,
        help="Path to the input JSON file (Module 1 + Module 2 output).",
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default="output.json",
        help="Path for the output JSON file (default: output.json).",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose / debug logging.",
    )
    args = parser.parse_args(argv)

    _setup_logging(args.verbose)
    logger = logging.getLogger("summarizer.main")

    # ---- Load input ----
    input_path = Path(args.input)
    if not input_path.is_file():
        logger.error("Input file not found: %s", input_path)
        sys.exit(1)

    logger.info("Loading input from %s ...", input_path)
    with open(input_path, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    # ---- Run pipeline ----
    logger.info("Starting hierarchical summarization pipeline...")
    output = run_pipeline(input_data)

    # ---- Write output ----
    output_path = Path(args.output)
    logger.info("Writing output to %s ...", output_path)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    logger.info("Done. Output saved to %s", output_path)


if __name__ == "__main__":
    main()