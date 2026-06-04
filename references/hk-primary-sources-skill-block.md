# HK primary sources — skill block (copy into SKILL.md)

Include this section in skills that cite Cap numbers, rules, or cases. Run commands from the **cloned marketplace repo root** (`claude-for-hk-law`). See [hk-primary-sources-setup.md](./hk-primary-sources-setup.md).

## HK primary sources (run before citing)

**Mandatory:** Before stating a Cap section, rule text, or case citation as current law, run the matching script **in this session** from the repo root. Tag every cite:

| Tag | Source |
|-----|--------|
| `[HK e-Legislation / DOJ open data]` | `download_legislation_*.py` output |
| `[HKLII search]` | `hklii_search.py` output (URL + neutral cite — open link for full judgment) |
| `[Judiciary site search]` | `judiciary_search.py` output |
| `[model knowledge — verify]` | No script ran this session |

**Not available:** HKLII MCP (`mcp.hklii.hk`) and CLIC MCP (`mcp.clic.org.hk`) are not shipped. CLIC is https://www.clic.org.hk only.

```bash
# Legislation (replace <cap>, keywords, queries)
python3 scripts/download_legislation_list.py --cap <cap>
python3 scripts/download_legislation_text.py <cap>

# Case leads (use for any skill mentioning judgments or case law)
python3 scripts/hklii_search.py "<query>" --cases --limit 10

# Judiciary website pages (Practice Directions, court info — not the judgments DB)
python3 scripts/judiciary_search.py "<query>" --limit 10
```

**Corporate only** (when the matter involves a HK company):

```bash
python3 corporate-legal/scripts/check_company.py <BRN_or_name>
```

Tag Companies Registry output `[Companies Registry open data]`.
