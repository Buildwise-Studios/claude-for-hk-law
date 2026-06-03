# 🇭🇰 Claude for Hong Kong Law — Adaptation Plan

**Goal:** Adapt `anthropics/claude-for-legal` (via Buildwise-Studios fork) for Hong Kong legal practice. 
**Pattern:** Same as `Klotzkette/claude-fuer-deutsches-recht` — translate from US/UK focus → HK common law & ordinances.
**Install path stays identical** to original Anthropic README (`claude plugin add .claude-plugin/marketplace.json`).

---

## Phase 1 — Foundation (Root-Level Changes)

Rewrite root files to HK context:

| File | Action | Owner |
|------|--------|-------|
| `CLAUDE.md` | Rewrite for HK legal practice | Subagent A1 |
| `QUICKSTART.md` | Rewrite for HK lawyers | Subagent A1 |
| `README.md` | Rewrite for HK market | Subagent A2 |
| `CONNECTORS.md` | HK-specific integrations | Subagent A2 |
| `.claude-plugin/marketplace.json` | Rename + update descriptions | Subagent A3 |
| `CONTRIBUTING.md` | Minor updates | Subagent A3 |

## Phase 1b — Reference Docs (Root Level)

| File | Content | Owner |
|------|--------|-------|
| `references/hk-legal-system-overview.md` | One country, two systems, Basic Law, common law, sources of law | Subagent B1 |
| `references/hk-citation-style.md` | HK case citation (HKCFA, HKCU, JUDGMENTS.HK), ordinance citation (Cap) | Subagent B1 |
| `references/key-hk-ordinances-index.md` | 50 most important ordinances with Cap numbers and descriptions | Subagent B2 |
| `references/hk-court-structure.md` | CFA, CA (Civil/Criminal), CFI, DC, TC, tribunals | Subagent B2 |
| `references/company-profile-template.md` | Adapt for HK firm profiles | Subagent B3 |
| `references/dashboard-template.md` | Keep as-is or minor tweaks | Subagent B3 |

## Phase 2 — Core Plugin Adaptation (12 Plugins)

Each plugin needs:
- `plugin.json` → update description, author
- `CLAUDE.md` → rewrite practice profile for HK
- `skills/` → adapt skills for HK law (keep structure, change legal references)
- `agents/` → adapt agents for HK context
- `README.md` → HK-focused docs

| Plugin | Owner |
|--------|-------|
| `commercial-legal` | Subagent C1 |
| `privacy-legal` | Subagent C1 |
| `product-legal` | Subagent C2 |
| `corporate-legal` | Subagent C2 |
| `employment-legal` | Subagent C3 |
| `litigation-legal` | Subagent C3 |
| `regulatory-legal` | Subagent C4 |
| `ip-legal` | Subagent C4 |
| `ai-governance-legal` | Subagent C5 |
| `law-student` | Subagent C5 |
| `legal-clinic` | Subagent C6 |
| `legal-builder-hub` | Subagent C6 |

## Phase 3 — HK-Native Plugins

New plugins for HK-specific practice areas:

| Plugin | Key Legislation | Owner |
|--------|----------------|-------|
| `hk-basic-law` | Basic Law, NPCSC interpretations | Subagent D1 |
| `hk-companies` | Cap 622, Cap 32 | Subagent D1 |
| `hk-employment` | Cap 57, Cap 485, Cap 282 | Subagent D2 |
| `hk-litigation-procedure` | HCR, DCAC, Appeal rules | Subagent D2 |
| `hk-property` | Cap 219, conveyancing | Subagent D3 |
| `hk-data-privacy` | Cap 486, PDPO | Subagent D3 |
| `hk-intellectual-property` | Cap 559, 514, 528 | Subagent D4 |
| `hk-arbitration` | Cap 609, UNCITRAL | Subagent D4 |
| `hk-commercial-law` | Cap 26, Sale of Goods | Subagent D5 |
| `hk-competition` | Cap 619 | Subagent D5 |
| `hk-immigration` | Cap 115 | Subagent D6 |
| `hk-shipping-maritime` | Cap 440 | Subagent D6 |
| `hk-family-law` | Cap 179, Cap 192 | Subagent D7 |
| `hk-trusts-estate` | Cap 29, Probate | Subagent D7 |
| `hk-nsl-rules` | National Security Law | Subagent D8 |

## Key Resources for Subagents

- **HK e-Legislation:** https://www.elegislation.gov.hk
- **HKLII (case law):** https://www.hklii.org
- **DOJ Legal System:** https://www.doj.gov.hk/en/our_legal_system/
- **CLIC (community legal info):** https://www.clic.org.hk
- **Basic Law:** https://www.basiclaw.gov.hk
- **Judiciary:** https://www.judiciary.hk
- **Companies Registry:** https://www.cr.gov.hk
- **PCPD (privacy):** https://www.pcpd.org.hk

## Structure Rules (maintained from original)

Each plugin directory:
```
<plugin>/
  .claude-plugin/plugin.json   # manifest
  .mcp.json                    # MCP connectors (optional)
  CLAUDE.md                    # practice profile TEMPLATE
  README.md                    # docs
  skills/<name>/SKILL.md       # skills
  agents/<name>.md             # subagent definitions
  hooks/hooks.json             # hooks
  logs/                        # (keep as dir)
```

Frontmatter rules:
- Every `SKILL.md` needs `name` and `description` in YAML frontmatter
- `description` ≤ 1024 chars
- `name` ≤ 64 ASCII chars, must match `^[a-z0-9][a-z0-9-]{1,63}$`
- No `triggers`, `when_to_use`, `language`, `tools` in frontmatter

Validation:
```bash
claude plugin validate .claude-plugin/marketplace.json
claude plugin validate <plugin>/.claude-plugin/plugin.json
python3 scripts/lint-tool-scope.py
```
