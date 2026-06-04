#!/usr/bin/env python3
"""
Hong Kong Legislation Text — Download & Read

Downloads and extracts legislative text from DOJ open-data ZIP packs
(same corpus as https://www.elegislation.gov.hk). No authentication required.

Run from the repository root (or pass paths via env — see references/hk-primary-sources-setup.md).

Usage:
    python3 scripts/download_legislation_text.py 57
    python3 scripts/download_legislation_text.py 622 --full
    python3 scripts/download_legislation_text.py 622 --save references/legislation/cap_622.txt
    python3 scripts/download_legislation_text.py --list
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import sys
import urllib.request
import zipfile


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
CACHE_DIR = os.path.join(REPO_ROOT, "references", "legislation")
ZIP_CACHE_DIR = os.path.join(CACHE_DIR, "zips")
LIST_URL = "https://resource.data.one.gov.hk/doj/data/hkel_list_c_all_en.json"
BASE_ZIP_URL = "https://resource.data.one.gov.hk/doj/data/"

ZIP_BY_RANGE = [
    (1, 300, "hkel_c_leg_cap_1_cap_300_en.zip"),
    (301, 600, "hkel_c_leg_cap_301_cap_600_en.zip"),
    (601, 10_000, "hkel_c_leg_cap_601_cap_end_en.zip"),
]

USER_AGENT = "Mozilla/5.0 (compatible; claude-for-hk-law/1.0)"


def get_legislation_index() -> dict:
    req = urllib.request.Request(LIST_URL, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
    index: dict[str, dict] = {}
    for ch in data.get("Chapter", []):
        if not ch:
            continue
        cap = str(ch.get("CapNo", "")).strip()
        if cap:
            index[cap] = ch
    return index


def zip_filename_for_cap(cap: str) -> str | None:
    """Pick the DOJ ZIP pack that should contain this Cap."""
    m = re.match(r"^(\d+)", cap)
    if not m:
        return None
    n = int(m.group(1))
    for lo, hi, fname in ZIP_BY_RANGE:
        if lo <= n <= hi:
            return fname
    return ZIP_BY_RANGE[-1][2]


def cap_path_regex(cap: str) -> re.Pattern:
    """Match cap_57_ / cap_622_ / cap_101A_ path segments (not cap_457_ for cap 57)."""
    esc = re.escape(cap)
    return re.compile(rf"(?:^|[/\\])cap_{esc}(?:_|/|\\)", re.IGNORECASE)


def cap_main_xml_regex(cap: str) -> re.Pattern:
    """Match main chapter XML files like cap_57_20260514000000_en_c.xml."""
    esc = re.escape(cap)
    return re.compile(rf"^cap_{esc}_\d{{8,}}.*\.xml$", re.IGNORECASE)


def find_cap_xml(cap: str, zf: zipfile.ZipFile) -> str | None:
    path_re = cap_path_regex(cap)
    main_re = cap_main_xml_regex(cap)

    in_cap_folder: list[str] = []
    main_files: list[str] = []

    for name in zf.namelist():
        if not name.lower().endswith(".xml"):
            continue
        norm = name.replace("\\", "/")
        if not path_re.search(norm):
            continue
        in_cap_folder.append(name)
        base = os.path.basename(norm)
        if main_re.match(base):
            main_files.append(name)

    if main_files:
        return sorted(main_files)[-1]
    if in_cap_folder:
        return sorted(in_cap_folder)[-1]
    return None


def load_zip(zip_name: str, refresh: bool = False) -> zipfile.ZipFile:
    os.makedirs(ZIP_CACHE_DIR, exist_ok=True)
    cache_path = os.path.join(ZIP_CACHE_DIR, zip_name)
    if not refresh and os.path.isfile(cache_path):
        return zipfile.ZipFile(cache_path, "r")

    url = BASE_ZIP_URL + zip_name
    print(f"  Downloading {zip_name}...", file=sys.stderr)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=300) as resp:
        data = resp.read()
    with open(cache_path, "wb") as f:
        f.write(data)
    return zipfile.ZipFile(io.BytesIO(data))


def xml_to_text(content: bytes) -> str:
    text = content.decode("utf-8", errors="replace")
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</p>", "\n\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</div>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    for ent, ch in (("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">")):
        text = text.replace(ent, ch)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def fetch_cap_text(cap: str, refresh_zip: bool = False) -> tuple[str, str, str]:
    """Returns (title, zip_member_path, plain_text)."""
    index = get_legislation_index()
    info = index.get(cap)
    if not info:
        raise SystemExit(f"Cap {cap} not found in legislation index ({LIST_URL}).")

    title = info.get("ChapterTitleEnglish", "Unknown")
    zip_name = zip_filename_for_cap(cap)
    if not zip_name:
        raise SystemExit(f"Could not determine ZIP pack for Cap {cap}.")

    zf = load_zip(zip_name, refresh=refresh_zip)
    member = find_cap_xml(cap, zf)
    if not member:
        raise SystemExit(
            f"Cap {cap} not found in {zip_name}. "
            f"Try --refresh or confirm the cap exists on https://www.elegislation.gov.hk"
        )

    text = xml_to_text(zf.read(member))
    return title, member, text


def main() -> None:
    parser = argparse.ArgumentParser(description="Download HK legislation text (DOJ open data)")
    parser.add_argument("cap", nargs="?", help="Cap number (e.g. 57, 622, 101A)")
    parser.add_argument("--list", action="store_true", help="Show example caps from the index")
    parser.add_argument("--full", action="store_true", help="Print full text (default: 3000 char preview)")
    parser.add_argument("--save", metavar="PATH", help="Write plain text to this file")
    parser.add_argument("--refresh", action="store_true", help="Re-download ZIP cache")
    args = parser.parse_args()

    if args.list:
        index = get_legislation_index()
        print(f"Indexed legislation: {len(index)} chapters")
        print("Examples:")
        for cap in ("1", "57", "155", "219", "486", "571", "609", "619", "622", "528"):
            info = index.get(cap, {})
            if info:
                print(f"  Cap {cap}: {info.get('ChapterTitleEnglish', '?')}")
        print("\nRun: python3 scripts/download_legislation_text.py <cap>")
        return

    if not args.cap:
        parser.print_help()
        sys.exit(1)

    cap = str(args.cap).strip()
    print(f"Looking up: Cap {cap}", file=sys.stderr)
    title, member, text = fetch_cap_text(cap, refresh_zip=args.refresh)
    print(f"  Found: {member}", file=sys.stderr)
    print(f"  Title: {title}", file=sys.stderr)

    if args.save:
        out_path = args.save if os.path.isabs(args.save) else os.path.join(REPO_ROOT, args.save)
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Wrote {len(text)} characters to {out_path}", file=sys.stderr)

    print(f"\n=== Cap {cap} — {title} ===\n")
    if args.full:
        print(text)
    else:
        print(text[:3000])
        if len(text) > 3000:
            print(f"\n... ({len(text) - 3000} more characters; use --full or --save)")


if __name__ == "__main__":
    main()
