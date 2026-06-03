#!/usr/bin/env python3
"""
Hong Kong Companies Registry Lookup

Uses the public open data API at data.cr.gov.hk (no authentication required).

Usage:
    python3 scripts/check_company.py C1572528          # by BRN (quick)
    python3 scripts/check_company.py "Company Name"    # by name (may return fewer results)
"""

import sys
import json
import urllib.request


API_BASE = "https://data.cr.gov.hk/cr/api/api/v1/api_builder/json/local/search"


def search(brn_or_name: str) -> list:
    """Search by BRN or company name. BRN searches are most reliable."""
    # Decide if it's a BRN or name
    is_brn = brn_or_name.startswith("C") and brn_or_name[1:].isdigit()

    if is_brn:
        field, op = "Brn", "equal"
    else:
        field, op = "Eng_Comp_Name", "contains"
    
    # Build URL with literal brackets (API doesn't accept %5B/%5D encoding)
    qs = f"query[0][key1]={field}&query[0][key2]={op}&query[0][key3]={urllib.parse.quote(brn_or_name)}"
    url = f"{API_BASE}?{qs}"
    
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def fmt_company(co: dict) -> str:
    """Format company record for display."""
    return (
        f"{co.get('English_Company_Name', 'N/A')} (BRN: {co.get('Brn', 'N/A')})\n"
        f"  Type: {co.get('Company_Type', 'N/A')}\n"
        f"  Status: {co.get('Company_Status', 'N/A')}\n"
        f"  Incorporated: {co.get('Date_of_Incorporation', 'N/A')}\n"
        f"  Office: {co.get('Address_of_Registered_Office', 'N/A')}"
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 check_company.py <BRN_or_name>")
        sys.exit(1)

    results = search(sys.argv[1])

    if not results:
        print("No results found.")
        sys.exit(0)

    for i, co in enumerate(results):
        if i > 0:
            print()
        print(fmt_company(co))
