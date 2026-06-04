#!/usr/bin/env python3
"""
Search the Judiciary section of GovHK Site Search (search.gov.hk).

There is no documented public JSON API. This script fetches the HTML results page
and parses titles, URLs, and snippets — same data a browser shows.

For published judgments, prefer scripts/hklii_search.py --cases (better metadata).

Usage:
    python3 scripts/judiciary_search.py "possession order"
    python3 scripts/judiciary_search.py "negligence" --limit 5 --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request

SEARCH_BASE = "https://www.search.gov.hk/result"
USER_AGENT = "Mozilla/5.0 (compatible; claude-for-hk-law/1.0)"


def build_url(query: str, page: int = 1, lang: str = "en") -> str:
    params = {
        "tpl_id": "judiciary_r3",
        "gp0": "judiciary_r3_home",
        "gp1": "judiciary_r3_home",
        "ui_charset": "utf-8",
        "web": "this",
        "ui_lang": lang,
        "query": query,
        "proxystylesheet": "depts",
        "output": "xml_no_dtd",
        "site": "judiciary_r3_home",
        "p_size": "10",
        "num": "10",
    }
    if page > 1:
        params["page"] = str(page)
    return SEARCH_BASE + "?" + urllib.parse.urlencode(params)


def fetch_results_html(query: str, page: int = 1) -> str:
    url = build_url(query, page=page)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse_results(html: str) -> list[dict]:
    """Parse GovHK search result blocks (waSearchResultTitleN / AbstrN)."""
    results: list[dict] = []
    title_re = re.compile(
        r'id="waSearchResultTitle(\d+)"[^>]*href="([^"]+)"[^>]*>\s*([^<]+?)\s*</a>',
        re.IGNORECASE | re.DOTALL,
    )
    abstr_re = re.compile(
        r'id="waSearchResultAbstr(\d+)"[^>]*>(.*?)</div>',
        re.IGNORECASE | re.DOTALL,
    )
    abstracts = {m.group(1): strip_html(m.group(2)) for m in abstr_re.finditer(html)}

    for m in title_re.finditer(html):
        pos, href, title = m.group(1), m.group(2), strip_html(m.group(3))
        results.append(
            {
                "position": int(pos),
                "title": title,
                "url": href,
                "snippet": abstracts.get(pos, ""),
            }
        )
    return results


def strip_html(fragment: str) -> str:
    text = re.sub(r"<[^>]+>", " ", fragment)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def main() -> None:
    parser = argparse.ArgumentParser(description="Judiciary site search via search.gov.hk")
    parser.add_argument("query", help="Search terms")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--page", type=int, default=1)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    try:
        html = fetch_results_html(args.query, page=args.page)
    except Exception as e:
        print(f"Judiciary search failed: {e}", file=sys.stderr)
        sys.exit(1)

    hits = parse_results(html)[: args.limit]
    if not hits:
        print("No results parsed (page layout may have changed).", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps(hits, indent=2, ensure_ascii=False))
        return

    print(f"Judiciary site search: {args.query!r} ({len(hits)} results)\n", file=sys.stderr)
    for h in hits:
        print(f"{h['position']}. {h['title']}")
        print(f"   {h['url']}")
        if h.get("snippet"):
            snip = h["snippet"]
            if len(snip) > 220:
                snip = snip[:217] + "..."
            print(f"   {snip}")
        print()


if __name__ == "__main__":
    main()
