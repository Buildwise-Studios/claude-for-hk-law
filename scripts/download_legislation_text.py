#!/usr/bin/env python3
"""
Hong Kong Legislation Text — Download & Read

Downloads and extracts the actual legislative text for a given Ordinance.
Uses the DOJ open data portal ZIP files.

Usage:
    python3 scripts/download_legislation_text.py 622          # Companies Ordinance
    python3 scripts/download_legislation_text.py 57           # Employment Ordinance
    python3 scripts/download_legislation_text.py 622 --html   # Show as HTML instead
    python3 scripts/download_legislation_text.py --list       # See all available
"""

import sys
import os
import json
import zipfile
import io
import urllib.request
import re
import argparse


CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", "references", "legislation")
LIST_URL = "https://resource.data.one.gov.hk/doj/data/hkel_list_c_all_en.json"


# Known ZIP ranges for English legislation
ZIP_RANGES = [
    ("1-300", "hkel_c_leg_cap_1_cap_300_en.zip"),
    ("301-600", "hkel_c_leg_cap_301_cap_600_en.zip"),
    ("601-end", "hkel_c_leg_cap_601_cap_end_en.zip"),
]

BASE_ZIP_URL = "https://resource.data.one.gov.hk/doj/data/"


def get_legislation_index() -> dict:
    """Download and return the legislation index (Cap -> metadata)."""
    req = urllib.request.Request(LIST_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
    
    index = {}
    for ch in data.get("Chapter", []):
        if not ch:
            continue
        cap = ch.get("CapNo", "")
        index[cap] = ch
    return index


def download_zip(url: str) -> zipfile.ZipFile:
    """Download a ZIP file and return as in-memory ZipFile."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    return zipfile.ZipFile(io.BytesIO(data))


def find_cap_in_zip(cap: str, zips: dict) -> tuple:
    """Find a Cap in the downloaded ZIP archives. Returns (zip_name, filename)."""
    cap_padded = cap.zfill(4)  # e.g., "1" -> "0001"
    
    for range_name, zf in zips.items():
        for name in zf.namelist():
            # Filenames look like: cap_0001_en.xml or CAP_0001_EN.XML
            if cap_padded in name and name.endswith((".xml", ".XML")):
                return zf, name
    return None, None


def main():
    parser = argparse.ArgumentParser(description="Download HK legislation text")
    parser.add_argument("cap", nargs="?", help="Cap number (e.g., 622)")
    parser.add_argument("--html", action="store_true", help="Show HTML instead of plain text")
    parser.add_argument("--list", action="store_true", help="List available caps")
    args = parser.parse_args()

    if args.list:
        index = get_legislation_index()
        print(f"Available legislation: {len(index)} entries")
        print("Use: python3 download_legislation_text.py <cap_no>")
        # Show some examples
        for cap in ["1", "57", "155",  "219", "486", "571", "609", "619", "622", "528"]:
            info = index.get(str(cap), {})
            if info:
                print(f"  Cap {cap}: {info.get('ChapterTitleEnglish', '?')}")
        return

    if not args.cap:
        print("Usage: python3 download_legislation_text.py <cap_no>")
        sys.exit(1)

    cap = str(args.cap)
    index = get_legislation_index()
    info = index.get(cap)
    if not info:
        print(f"Cap {cap} not found in legislation index.")
        sys.exit(1)

    title = info.get("ChapterTitleEnglish", "Unknown")
    print(f"Looking up: Cap {cap} — {title}", file=sys.stderr)

    # Determine which ZIP file contains this Cap
    cap_num = 0
    try:
        cap_num = int(cap)
    except ValueError:
        pass  # might be like "1A"

    # Download all ZIPs (small ones, ~1-5MB each)
    zips = {}
    for range_name, zip_file in ZIP_RANGES:
        url = BASE_ZIP_URL + zip_file
        print(f"  Downloading {zip_file}...", file=sys.stderr)
        zips[range_name] = download_zip(url)

    # Find the Cap in the ZIPs
    zf, filename = find_cap_in_zip(cap, zips)
    if not zf:
        print(f"Cap {cap} not found in ZIP archives.")
        sys.exit(1)

    print(f"  Found: {filename}", file=sys.stderr)
    content = zf.read(filename)

    if args.html:
        # Show HTML directly (legislation text is HTML inside XML)
        text = content.decode("utf-8")
        # Strip XML wrapper, show readable content
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
    else:
        # Show as plain text extracted from HTML
        text = content.decode("utf-8")
        # Simple HTML-to-text extraction
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
        text = re.sub(r'<br\s*/?>', '\n', text)
        text = re.sub(r'</p>', '\n\n', text, flags=re.IGNORECASE)
        text = re.sub(r'</div>', '\n', text, flags=re.IGNORECASE)
        text = re.sub(r'<[^>]+>', '', text)
        text = re.sub(r'&nbsp;', ' ', text)
        text = re.sub(r'&amp;', '&', text)
        text = re.sub(r'&lt;', '<', text)
        text = re.sub(r'&gt;', '>', text)

    # Print first 2000 chars as preview
    print(f"\n=== Cap {cap} — {title} (preview) ===\n")
    print(text[:3000])
    if len(text) > 3000:
        print(f"\n... ({len(text) - 3000} more characters)")


if __name__ == "__main__":
    main()
