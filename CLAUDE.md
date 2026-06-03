# CLAUDE.md

Guidance for working on this repo. `claude-for-hk-law` is a Claude Code plugin
marketplace — twelve core practice-area plugins, one vendor plugin, five
managed-agent cookbooks, and eight Hong Kong-native plugins. Most work here is
editing prompt content (skills, agents, hooks), plugin metadata, or cookbook
config — not application code.

## Layout

```
.claude-plugin/marketplace.json   # the marketplace manifest — one entry per plugin
<plugin>/                         # core + HK-native plugins see below
  .claude-plugin/plugin.json      # plugin manifest (name, version, description, author)
  .mcp.json                       # MCP servers the plugin connects to
  CLAUDE.md                       # practice-profile TEMPLATE (see "Plugin CLAUDE.md" below)
  README.md                       # per-plugin docs
  skills/<name>/SKILL.md          # one skill per directory
  agents/<name>.md                # subagent definitions
  hooks/hooks.json                # hook config (most plugins ship an empty stub)
  .gitignore
external_plugins/<vendor>/        # vendor-maintained plugins (CoCounsel)
managed-agent-cookbooks/<name>/   # CMA agent.yaml + subagents/ + steering-examples.json
scripts/                          # validate.py, lint-tool-scope.py, orchestrate.py,
                                  # deploy-managed-agent.sh, test-cookbooks.sh
references/                       # shared templates (company-profile, dashboard)
```

## Legal System Context

This repository adapts Claude plugins for **Hong Kong legal practice**. Key
systemic facts:

- **Legal system:** Hong Kong operates a **common law** system under the
  principle of "one country, two systems." The **Basic Law** is the
  constitutional document. The Court of Final Appeal (HKCFA) is the highest
  appellate court, followed by the High Court (Court of Appeal and Court of
  First Instance), the District Court, and the Magistrates' Courts.
- **Statute law:** Ordinances enacted by the Legislative Council, cited by
  chapter number (e.g. Cap 622 for the Companies Ordinance). The authoritative
  source is the **Hong Kong e-Legislation** database
  (elegislation.gov.hk).
- **Case law:** HK follows **stare decisis**. Pre-1997 English common law
  applies under Article 8 of the Basic Law insofar as it is not inconsistent
  with Hong Kong legislation. HK cases are cited with neutral citations (e.g.
  *Re ABC* [2024] HKCFA 1) or with HKEC or HKCU references.
- **Legal reasoning:** The standard methodology is **IRAC** (Issue-Rule-
  Application-Conclusion), not Gutachtenstil. Skills and agents should generate
  analysis in IRAC structure.
- **Professional regulation:** The Law Society of Hong Kong administers the
  **Hong Kong Solicitors' Guide to Professional Conduct**. Barristers are
  regulated by the Hong Kong Bar Association. The **Legal Practitioners
  Ordinance (Cap 159)** governs admission and practice.
- **Language:** English is an official language of Hong Kong and the primary
  language of superior court proceedings. All plugin output is in English.

## Key Hong Kong Ordinances

Skills and agents should reference these core ordinances where relevant:

| Ordinance | Cap | Area |
|---|---|---|
| Basic Law | — | Constitutional document |
| Companies Ordinance | 622 | Corporate law |
| Employment Ordinance | 57 | Employment |
| Personal Data (Privacy) Ordinance | 486 | Data protection |
| Arbitration Ordinance | 609 | Arbitration |
| Control of Exemption Clauses Ordinance | 71 | Contract terms |
| Sale of Goods Ordinance | 26 | Commercial sales |
| Trade Marks Ordinance | 559 | IP / trade marks |
| Copyright Ordinance | 528 | IP / copyright |
| Patents Ordinance | 514 | IP / patents |
| Competition Ordinance | 619 | Competition |
| Securities and Futures Ordinance | 571 | Capital markets |
| Land Registration Ordinance | 128 | Property |
| Conveyancing and Property Ordinance | 219 | Property |
| Limitations Ordinance | 347 | Limitation periods |
| Evidence Ordinance | 8 | Evidence |
| Criminal Procedure Ordinances | 221 | Criminal procedure |
| District Court Ordinance | 336 | Court jurisdiction |
| High Court Ordinance | 4 | Court jurisdiction |
| Legal Practitioners Ordinance | 159 | Legal profession |

## Legal Research Sources

When skills or agents need legal research, they should reference these
authoritative sources:

- **Hong Kong e-Legislation** (elegislation.gov.hk) — official legislation
  database, maintained by the Department of Justice
- **Hong Kong Legal Information Institute — HKLII** (hklii.org) — free access
  to HK case law and legislation
- **Judiciary of Hong Kong** (judiciary.hk) — official judgments, practice
  directions, and court procedures
- **Law Society of Hong Kong** (hklawsoc.org.hk) — professional conduct rules,
  practice directions, CPD requirements
- **Department of Justice** (doj.gov.hk) — legal policy, treaties, and law
  reform materials
- **Hong Kong Court of Final Appeal** (hkefa.hk) — CFA judgments and practice
  directions

## HK Case Citation Format

Neutral citations follow this pattern: `[Year] HK<Court> <Number>`

| Court | Abbreviation | Example |
|---|---|---|
| Court of Final Appeal | HKCFA | *Re ABC* [2024] HKCFA 1 |
| High Court — Court of Appeal | HKCA | *XYZ Ltd v ABC* [2023] HKCA 456 |
| High Court — Court of First Instance | HKCFI | *Chan v Lee* [2024] HKCFI 789 |
| District Court | HKDC | *Wong v Hospital Authority* [2023] HKDC 123 |
| Magistrates' Court | HCMC | *HKSAR v Fung* [2024] HCMC 45 |

Non-neutral citations: HKCU (Hong Kong Current Unreported), HKEC (Hong Kong
Electronic Citation), HKC (Hong Kong Cases) — use these only when a neutral
citation is unavailable.

## Statute Citation Format

Cite Hong Kong Ordinances as: `Cap <number>`, e.g. Cap 622 (Companies
Ordinance). When referring to a specific section: s 123 of the Companies
Ordinance (Cap 622) or Companies Ordinance (Cap 622), s 123.

## Validation — run before opening a PR

This repo follows the same conventions `anthropics/claude-plugins-official`
enforces in CI. Run the equivalent checks locally:

```bash
# 1. Marketplace + per-plugin schema validation (source of truth)
claude plugin validate .claude-plugin/marketplace.json
for d in */; do [ -f "$d/.claude-plugin/plugin.json" ] && claude plugin validate "$d"; done
claude plugin validate external_plugins/cocounsel-legal

# 2. Cookbook tool-scope lint (orchestrators must not over-grant tools)
python3 scripts/lint-tool-scope.py

# 3. JSON/YAML sanity
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json', recursive=True)]"
```

### Marketplace invariants (I1–I11)

`claude-plugins-official` layers these on top of the schema check. They apply
here too — the ones most likely to trip a contributor:

- **I1** — `plugins[]` should be alpha-sorted by name (case-insensitive).
  *Currently a known warning: the array is in a curated display order. If you
  add a plugin, ask before re-sorting the whole array.*
- **I2** — no duplicate plugin names.
- **I3** — `description` 10–2000 chars, no leading/trailing whitespace.
- **I8** — every vendored `source` (`"./<dir>"`) must point at a directory that
  contains `.claude-plugin/plugin.json`.
- **I9** — `source` paths/URLs must contain no shell metacharacters or `..`.
- **I10** — no hidden Unicode (zero-width chars, bidi controls) in
  `name`/`description`.
- **I11** — `name` must match `^[a-z0-9][a-z0-9-]{1,63}$`.

### Frontmatter requirements

Every `agents/*.md` needs `name` and `description`. Every
`skills/<name>/SKILL.md` needs `description`. Every `commands/*.md` needs
`description`. Multi-line descriptions use `>` block scalars and that's fine —
`claude plugin validate` parses them correctly.

## Conventions

### Keep `marketplace.json` in sync with `plugin.json`

For first-party plugins, `marketplace.json`'s `name`, `description`, and
`author` should match the plugin's own `.claude-plugin/plugin.json` field for
field. If you change a plugin's description in one place, change it in the
other.

### Skill names in prose must be canonical

When a `SKILL.md` (especially `customize` or `cold-start-interview`) tells the
user "run `/foo`," `foo` must be the actual `skills/<foo>/` directory name.
Short forms like `/triage` for `/use-case-triage` look right in prose but are
dead commands — the user types them and nothing happens. Refs to Claude Code
built-ins (`/mcp`, `/plugin`) and to other plugins (`/<other-plugin>:<skill>`)
are fine.

### Plugin CLAUDE.md is a template, not project context

Each `<plugin>/CLAUDE.md` is a practice-profile template that the
`cold-start-interview` skill copies to
`~/.claude/plugins/config/claude-for-hk-law/<plugin>/CLAUDE.md`
on the user's machine. It is *not* loaded as project context when the plugin is
installed — `claude plugin validate` warns about this and the warning is
expected. Don't "fix" it by moving the content into a skill.

### `external_plugins/` is vendor-maintained

Plugins under `external_plugins/` are built and maintained by the vendor
(README.md has the policy). Don't change vendor-authored content without
checking with them first; whitespace normalization and formatting are usually
fine since the vendor lands changes via PR rather than mirroring a fork.

### Formatting

- 2-space indent in all JSON and `.mcp.json` files.
- Final newline at end of every text file.
- No trailing whitespace.
- Markdown tables: pipe-aligned columns are nice but not required; just keep
  the column count consistent.

## Cookbooks

Each `managed-agent-cookbooks/<name>/` has `agent.yaml` (the orchestrator),
`subagents/*.yaml` (the leaves), `steering-examples.json`, and `README.md`. Two
rules that `scripts/lint-tool-scope.py` enforces:

1. The orchestrator gets local-only tools (`read`, `grep`, `glob`,
   `agent_toolset`); MCP and write tools belong to specific subagent leaves.
2. The README's security table and the `agent.yaml` comments must match what
   the YAML actually grants. Don't claim a tool a subagent doesn't have.

## Things to leave alone

- Per-plugin `.gitignore` files differ slightly across plugins. Probably
  intentional; ask before unifying.
- `hooks/hooks.json` is missing in two plugins. Hooks are optional; the missing
  files are not a bug.
- `references/` lives only at repo root and is not shipped inside any plugin
  directory. Several plugin `CLAUDE.md` templates reference it as if it were —
  that's a known gap, not a thing to silently move.
