#!/usr/bin/env python3
"""
HKLII search via the public simplesearch API (discovered on hklii.hk).

Returns structured JSON: titles, neutral citations, paths, court/database labels.
Does not download full judgment text (HKLII case pages require JavaScript).

Usage:
    python3 scripts/hklii_search.py "employment termination"
    python3 scripts/hklii_search.py "negligence" --cases --limit 10
    python3 scripts/hklii_search.py "Cap 57" --legislation --limit 5
    python3 scripts/hklii_search.py "Wills" --json
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request

API_URL = "https://www.hklii.hk/api/simplesearch"
USER_AGENT = "Mozilla/5.0 (compatible; claude-for-hk-law/1.0)"


def search(query: str, disable_fuzzy: bool = False) -> dict:
    params = urllib.parse.urlencode(
        {
            "searchstring": query,
            "disablefuzzy": "1" if disable_fuzzy else "0",
        }
    )
    url = f"{API_URL}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read())


def filter_results(data: dict, cases_only: bool, legislation_only: bool) -> list[dict]:
    results = data.get("results") or []
    if cases_only:
        results = [r for r in results if "/cases/" in (r.get("path") or "")]
    if legislation_only:
        results = [r for r in results if "/legis/" in (r.get("path") or "")]
    return results


def format_hit(r: dict) -> str:
    lines = []
    title = r.get("title") or r.get("subtitle") or "(no title)"
    lines.append(title)
    if r.get("neutral"):
        lines.append(f"  Citation: {r['neutral']}")
    if r.get("subtitle") and r.get("subtitle") != title:
        lines.append(f"  Label: {r['subtitle']}")
    if r.get("db"):
        lines.append(f"  Source: {r['db']}")
    if r.get("pub_date"):
        lines.append(f"  Date: {r['pub_date']}")
    path = r.get("path") or ""
    if path:
        lines.append(f"  URL: https://www.hklii.hk{path}")
    if r.get("act"):
        lines.append(f"  Case no.: {r['act']}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Search HKLII (hklii.hk public API)")
    parser.add_argument("query", help="Search string")
    parser.add_argument("--limit", type=int, default=15, help="Max results to print")
    parser.add_argument("--cases", action="store_true", help="Only /cases/ hits")
    parser.add_argument("--legislation", action="store_true", help="Only /legis/ hits")
    parser.add_argument("--exact", action="store_true", help="disablefuzzy=1")
    parser.add_argument("--json", action="store_true", help="Print raw JSON hits")
    args = parser.parse_args()

    try:
        data = search(args.query, disable_fuzzy=args.exact)
    except Exception as e:
        print(f"HKLII search failed: {e}", file=sys.stderr)
        sys.exit(1)

    hits = filter_results(data, args.cases, args.legislation)[: args.limit]
    total = data.get("count", len(data.get("results") or []))

    if args.json:
        print(json.dumps({"count": total, "results": hits}, indent=2, ensure_ascii=False))
        return

    print(f"Query: {args.query!r}  (API reports {total} matches; showing {len(hits)})", file=sys.stderr)
    if not hits:
        print("No results.")
        return

    for i, r in enumerate(hits, 1):
        print(f"\n--- {i} ---")
        print(format_hit(r))

    print(
        "\nNote: open the URL in a browser for full text. "
        "For ordinance text use scripts/download_legislation_text.py.",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
