# Diligence Grid — managed-agent template (HK Law Edition)

## Overview

Batch document review over a virtual data room, adapted for Hong Kong M&A
due diligence. Two modes:

- **watch** — monitors the VDR for new uploads since a cutoff, classifies each
  against the deploying team's diligence request-list categories (HK-adapted),
  and flags uploads in high-priority categories (Material Contracts, Litigation,
  IP, Cap. 622 statutory records, Cap. 571 regulated activities).
- **grid** — runs a tabular review against a column schema over a folder of
  documents. One row per document, one column per data point, every cell cited
  back to a verbatim source quote. The M&A diligence workhorse.

**Hong Kong diligence framework (not US).** HK M&A due diligence is governed by:

- **Companies Ordinance (Cap. 622)** — the primary corporate statute. Key
  diligence areas: statutory registers, directors' service contracts, charges
  (registerable at the Companies Registry), financial assistance prohibition
  (s. 274), share capital structure, distributions, annual returns, disclosures
  of interests, substantial shareholder registers, auditors' reports.
- **Securities and Futures Ordinance (Cap. 571)** — for listed targets: inside
  information disclosures, discloseable transactions, connected transactions,
  notifiable transactions, the Takeovers Code (administered by the SFC),
  market misconduct provisions, Part XV disclosure regime.
- **Competition Ordinance (Cap. 619)** — the First Conduct Rule (anti-competitive
  agreements), Second Conduct Rule (abuse of substantial market power), and
  merger control (telecom/broadcasting only). Distribution agreements and
  pricing arrangements require specific attention.
- **Employment Ordinance (Cap. 57)** — MPF compliance, ORSO schemes, long
  service payments, severance, termination notice, restrictive covenants
  enforceability under HK common law.
- **Personal Data (Privacy) Ordinance (Cap. 486)** — PICS, cross-border data
  transfer provisions, direct marketing opt-in requirements, data breach
  notification.
- **Inland Revenue Ordinance (Cap. 112)** — stamp duty on share transfers
  (0.2% of consideration), profits tax exposure, property tax, tax clearance.
- **Other key ordinances:** Trade Marks Ordinance (Cap. 559), Patents
  Ordinance (Cap. 514), Copyright Ordinance (Cap. 528), Mandatory Provident
  Fund Schemes Ordinance (Cap. 485), Occupational Retirement Schemes
  Ordinance (Cap. 426).

Same source as the [`corporate-legal`](../../corporate-legal) plugin — this
directory is the Managed Agent cookbook for `POST /v1/agents`. Grid mode is
the `tabular-review` skill, running headless across a fleet of extractor
workers.

## ⚠️ Before you deploy

- **Every cell is a lead, not a finding.** A diligence grid is not a
  representation, a disclosure schedule, or a diligence memo until a lawyer
  has read the underlying documents. The verbatim quote in every cell is
  there so the reviewer can verify fast — use it.
- **The materiality filter and column classifications apply heuristics, not
  legal judgment.** A contract the schema calls immaterial may be the one
  that kills the deal. An "answered" cell is still wrong if the extractor
  misread the clause. Reviewer time scales with `unclear` + `needs_review` +
  `answered` — not just the flagged ones.
- **Watch mode classifies metadata and previews, not full documents.** A new
  upload the classifier tags "low priority" can still be the side letter that
  changes the deal. Treat the watch report as a queue, not a filter.
- **HK-specific:** The Companies Registry maintains public records (charges
  register, register of directors, annual returns) that can verify certain
  diligence items but are not uploaded to the VDR. The grid may need a
  separate CR search MCP to cross-reference.
- **Counterparty-uploaded documents are untrusted input for the toolchain
  too.** The grid-writer's CSV formula-injection defense is mandatory, not
  optional — see the security section below.

## Deploy (HK)

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export BOX_MCP_URL=...         # VDR connection
export GDRIVE_MCP_URL=...      # For playbook and schema configuration
export IMANAGE_MCP_URL=...     # Optional
export DEFINELY_MCP_URL=...    # Optional; for clause-structure QA
# HK-specific: enable CR search MCP for Companies Registry cross-reference
export CR_MCP_URL=...          # Optional; for public record verification
../../scripts/deploy-managed-agent.sh diligence-grid
```

## Steering events

See [`steering-examples.json`](./steering-examples.json).

## Security and handoffs

VDR documents — contracts, board minutes, side letters, counterparty uploads —
are **untrusted input**. A counterparty-uploaded contract can contain strings
meant to manipulate the reviewer or the downstream toolchain. Four-tier
isolation keeps the Write hand and the MCP hand away from the documents:

| Tier | Touches untrusted docs? | Tools | Connectors |
|---|---|---|---|
| **`doc-reader`** | **Yes** (read-only) | `Read`, `Grep` | Box, Google Drive, iManage (read); optional CR MCP |
| **`extractor`** | **Yes** (read-only) | `Read`, `Grep` | None |
| `normalizer` / Orchestrator | No | `Read`, `Grep`, `Glob`, `Agent` | None (definely optional, read-only) |
| **`grid-writer`** (Write-holder) | No | `Read`, `Write` | None |

**CSV formula injection.** Every cell written by `grid-writer` — values,
verbatim quotes, locations, document names, column labels — is
first-character-checked against `=`, `+`, `-`, `@`, tab, and carriage return.
Cells that match are prefixed with a single apostrophe before they land in
the CSV.

**Not guaranteed:** every cell this agent produces is a **lead that needs
verification**, not a finding. The reviewer reads the source, checks the quote,
marks the `Verified` column. A lawyer decides what goes into a rep, a schedule,
or a memo.

## Adaptation notes (HK)

- **VDR URL.** Set `BOX_MCP_URL` / `GDRIVE_MCP_URL` / `IMANAGE_MCP_URL` to
  match your data room. Most HK M&A deals use Box, Datasite, or Intralinks.
  If your VDR is Intralinks or Datasite, add an entry to `mcp_servers` and
  `tools` with the matching MCP URL.
- **Column schema (HK-specific).** The default M&A diligence standard column
  set has been adapted for HK corporate practice. Key additions include:
  - Cap. 622: Register of members (s. 632–638), directors' service contracts
    (s. 290–294), charges register (s. 338–341), financial assistance
    (s. 274–282), substantial shareholder register (s. 308–317), annual
    return compliance (s. 662–671)
  - Cap. 571: Inside information disclosure (Part XIVA), discloseable
    transactions (Listing Rules), connected transactions (LR), Part XV
    interests
  - Cap. 57: MPF compliance, restrictive covenants, termination entitlements
  - Cap. 486: Data user registration, cross-border transfer compliance,
    direct marketing consents
  - Cap. 112: Stamp duty computation, tax clearance status
  - Cap. 619: Competition compliance, exclusivity, resale price maintenance
- **CR search MCP (optional).** If available, enable `cr-mcp` in the
  doc-reader's toolset to cross-reference Companies Registry public records
  (charges register, director register, register of members) against VDR
  documents. This is an HK-specific addition not available in the US version.
- **Output destination.** Outputs land in `./out/`. Wire them to your deal
  folder, Google Drive, iManage workspace, or Box folder through your deploy
  pipeline.
- **Default mode.** Watch vs grid is selected per steering event. For HK due
  diligence, start with watch mode to understand the VDR structure, then
  run grid mode on high-priority folders.
- **Work-product header.** `grid-writer` prepends the header from the deploying
  team's `## Outputs` configuration. Confirm the header with your HK legal
  team before deploying. **HK note:** Legal professional privilege in Hong
  Kong is governed by common law.
- **Slack routing.** This agent never posts directly. Reports are files; a
  `handoff_request` tells your orchestrator which channel to route to.
  Configure the deal channel in the deploying team's `CLAUDE.md` House style
  section.
