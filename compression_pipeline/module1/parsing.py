import os
import re
import sys


NOISE_PATTERNS = [
    r"Table of Contents",
    r"Amazon Simple Storage Service API Reference",
    r"API Reference",
    r"Copyright © .*",
    r"Amazon's trademarks.*",
    r"All other trademarks.*",
    r"API Version \d{4}-\d{2}-\d{2}",
]

SECTION_DROP_PATTERNS = [
    r"^Table of Contents",
    r"^API Reference$",
]

REPEATED_LINE_THRESHOLD = 3

def fix_encoding(text):
    """Fix broken ligatures and encoding artifacts"""
    replacements = {
        "\ufb01": "fi",
        "\ufb02": "fl",
        "\u2013": "-",
        "\u2014": "-",
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def remove_noise_lines(lines):
    cleaned = []

    for line in lines:
        l = line.strip()

        if not l:
            continue

        if any(re.search(p, l, re.IGNORECASE) for p in NOISE_PATTERNS):
            continue

        cleaned.append(line)

    return cleaned


def remove_repeated_lines(lines):
    """Remove excessive repeated headers"""
    freq = {}
    for l in lines:
        key = l.strip()
        freq[key] = freq.get(key, 0) + 1

    cleaned = []
    for l in lines:
        if freq[l.strip()] > REPEATED_LINE_THRESHOLD:
            continue
        cleaned.append(l)

    return cleaned


def remove_toc_blocks(text):
    """Remove TOC-like dense dotted lines or bullet dumps"""
    text = re.sub(r".*\.{5,}.*\n", "", text)

    # remove large bullet-only regions (TOC style)
    text = re.sub(r"(\n[\-\*\•].*){10,}", "", text)

    return text


def normalize_spacing(text):
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()

# Main cleaning pipeline

def clean_markdown(text):
    text = fix_encoding(text)

    # remove TOC-like structures early
    text = remove_toc_blocks(text)

    lines = text.split("\n")

    lines = remove_noise_lines(lines)
    lines = remove_repeated_lines(lines)

    text = "\n".join(lines)

    text = normalize_spacing(text)

    return text

def process_file(input_path, out_dir="cleaned"):
    with open(input_path, "r", encoding="utf-8") as f:
        raw = f.read()

    cleaned = clean_markdown(raw)

    filename = os.path.basename(input_path)
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, filename)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(cleaned)

    print(f"Cleaned file written to: {out_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parsing.py <input_md_path> <optional_output_dir>")
        sys.exit(1)

    if len(sys.argv) > 2:
        process_file(sys.argv[1], sys.argv[2])
    else:
        process_file(sys.argv[1])