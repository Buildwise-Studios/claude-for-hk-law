# Hong Kong primary sources — first-time setup

Use this when you clone **claude-for-hk-law** and want Claude (or your students) to pull **real** HK legislation and research leads — not training-data cites.

## What you need once

| Requirement | Why |
|---|---|
| **Python 3.9+** | All repo scripts are stdlib-only (`urllib`, `json`, `zipfile`). |
| **This repo on disk** | Scripts live under `scripts/` at the repo root. |
| **Network** | Downloads from `resource.data.one.gov.hk`, `www.hklii.hk`, `www.search.gov.hk`. |
| **Run from repo root** | `cd /path/to/claude-for-hk-law` before every command below. |

Optional: add the repo path to your shell profile so skills can find it:

```bash
export CLAUDE_FOR_HK_LAW_ROOT="$HOME/Dev/claude-for-hk-law"   # your path
```

Tell Claude in your practice profile (`~/.claude/plugins/config/claude-for-hk-law/<plugin>/CLAUDE.md`) where the repo lives if you use a non-default path.

## Official sites vs what this repo ships

| Source | Human URL | In this repo |
|---|---|---|
| **HK e-Legislation** | https://www.elegislation.gov.hk | `scripts/download_legislation_*.py` (DOJ open data — same corpus, bulk ZIP/JSON) |
| **HKLII** | https://www.hklii.hk | `scripts/hklii_search.py` (public `simplesearch` API — search + URLs, not full judgment HTML) |
| **Judiciary** | https://www.judiciary.hk | `scripts/judiciary_search.py` (GovHK Site Search HTML parser — site pages, not judgment database API) |
| **CLIC** | https://www.clic.org.hk | **Website only** — plain-language guides and an on-site AI chat widget. **No MCP server** is shipped or verified in this repo. |
| **Companies Registry** | https://www.icris.cr.gov.hk | `corporate-legal/scripts/check_company.py` (open data API) |

There are **no** working `mcp.hklii.hk` or `mcp.clic.org.hk` endpoints in our testing (DNS does not resolve). Do not rely on those URLs in `.mcp.json` until the operator publishes a real MCP server and documents auth.

Paid research (Westlaw Asia, LexisNexis HK) is **your** subscription — add only the MCP URL your vendor gives you.

## Quick smoke test (copy-paste)

```bash
cd /path/to/claude-for-hk-law

# 1) Legislation index
python3 scripts/download_legislation_list.py --cap 57

# 2) Ordinance text (first run downloads ~5–15 MB ZIP into references/legislation/zips/)
python3 scripts/download_legislation_text.py 57 --full | head -80

# 3) HKLII case/legislation search
python3 scripts/hklii_search.py "employment termination" --cases --limit 5

# 4) Judiciary website search (not the judgments DB)
python3 scripts/judiciary_search.py "possession order" --limit 5

# 5) Companies Registry (example BRN — use a real BRN you are allowed to look up)
python3 corporate-legal/scripts/check_company.py C0000001
```

If step 2 fails, run `python3 scripts/download_legislation_text.py 57 --refresh`.

## How Claude should use these in a session

1. **User installs a plugin** from this marketplace (user scope — see [QUICKSTART.md](../QUICKSTART.md)).
2. **User clones the repo** (or already has it from marketplace add path).
3. When a skill needs a Cap or a case lead, Claude runs the matching script via **Bash**, reads stdout/stderr, and tags cites:
   - `[HK e-Legislation / DOJ open data]` — text from `download_legislation_text.py`
   - `[HKLII search]` — hit from `hklii_search.py` (student must open URL for full text)
   - `[Judiciary site search]` — hit from `judiciary_search.py` (verify on judiciary.hk)
   - `[model knowledge — verify]` — anything not from a tool run this session

Skills must **not** claim `HKLII ✓ verified` unless a script or a **working** research MCP returned the cite in that conversation.

## Caching

| Path | Contents |
|---|---|
| `references/hk-legislation-cache.json` | Legislation list (`download_legislation_list.py`) |
| `references/legislation/zips/*.zip` | DOJ ZIP packs (`download_legislation_text.py`) |

Add `references/legislation/` to `.gitignore` if you do not want large ZIPs in git (optional local cache).

## Limitations (be explicit with clients)

- **Legislation text** comes from DOJ XML packs; always confirm currency on e-Legislation for filing/submission.
- **HKLII** search API returns metadata and links; judgment pages are JavaScript-heavy — open in browser or use paid databases for full-text workflow.
- **Judiciary search** indexes the **website**, not necessarily every published judgment; use HKLII for case law leads.
- **CLIC** is for public legal information, not a substitute for solicitor advice or live MCP tooling in Claude.
