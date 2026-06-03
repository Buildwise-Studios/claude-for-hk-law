#!/usr/bin/env python3
"""
Hong Kong Legislation List — Download & Search

Downloads the official list of all HK legislation from the DOJ open data portal.
No authentication required.

Usage:
    python3 scripts/download_legislation_list.py              # full list
    python3 scripts/download_legislation_list.py --search "employment"  # search by keyword
    python3 scripts/download_legislation_list.py --cap 622              # specific ordinance
    python3 scripts/download_legislation_list.py --refresh             # force re-download
"""

import sys
import os
import json
import urllib.request
import argparse


CACHE_FILE = os.path.join(os.path.dirname(__file__), "..", "references", "hk-legislation-cache.json")
DATA_URL = "https://resource.data.one.gov.hk/doj/data/hkel_list_c_all_en.json"


def download(refresh: bool = False) -> list:
    """Download or load cached legislation list."""
    if not refresh and os.path.exists(CACHE_FILE):
        with open(CACHE_FILE) as f:
            data = json.load(f)
            return data.get("Chapter", [])

    print(f"Downloading legislation list from data.gov.hk...", file=sys.stderr)
    req = urllib.request.Request(DATA_URL, headers={"User-Agent": "Mozilla/5.0 (compatible; HK-Legal-Agent)"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())

    # Cache it
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=2)

    chapters = data.get("Chapter", [])
    print(f"  {len(chapters)} entries cached", file=sys.stderr)
    return chapters


def search(chapters: list, keyword: str = None, cap_no: str = None):
    """Search legislation by keyword or Cap number."""
    results = []
    for ch in chapters:
        if not ch:
            continue
        title = ch.get("ChapterTitleEnglish", "")
        cap = ch.get("CapNo", "")

        if cap_no and cap == cap_no:
            results.append(ch)
        elif keyword and keyword.lower() in title.lower():
            results.append(ch)

    return results


DISPLAY_FIELDS = [
    ("Cap", "CapNo"),
    ("Title", "ChapterTitleEnglish"),
    ("Type", "LegislationType"),
]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search HK legislation")
    parser.add_argument("--search", help="Keyword search in legislation titles")
    parser.add_argument("--cap", help="Filter by Cap number")
    parser.add_argument("--refresh", action="store_true", help="Force re-download")
    parser.add_argument("--all", action="store_true", help="List all legislation")
    args = parser.parse_args()

    chapters = download(refresh=args.refresh)

    if args.cap:
        results = search(chapters, cap_no=args.cap)
    elif args.search:
        results = search(chapters, keyword=args.search)
    elif args.all:
        results = chapters
    else:
        # Default: search for keyword if provided, otherwise show count
        print(f"Total entries: {len(chapters)}")
        print("Use --search <keyword>, --cap <no>, or --all to list")
        sys.exit(0)

    for ch in results:
        cap = ch.get("CapNo", "")
        title = ch.get("ChapterTitleEnglish", "")
        leg_type = ch.get("LegislationType", "")
        status = "In effect"
        versions = ch.get("Version", [])
        if versions:
            status = versions[0].get("VersionDate", {}).get("statusCategory", "Unknown")
        print(f"Cap {cap} — {title}")
        print(f"  Type: {'Ordinance' if leg_type == 'O' else 'Subsidiary' if leg_type == 'S' else leg_type}")
        print(f"  Status: {status}")
        # Show download URL if available
        if versions:
            url = versions[0].get("DataResourceUrl", "")
            if url:
                print(f"  Download: {url}")
        print()
