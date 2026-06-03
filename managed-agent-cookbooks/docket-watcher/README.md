# Docket Watcher — managed-agent template (HK Law Edition)

## Overview

Monitors active litigation matters in the Hong Kong Judiciary. Unlike the US
(which has PACER, CourtListener, Trellis), Hong Kong has no **public REST API**
for case data. However, there are web portals that can be accessed either
manually or via a custom MCP connector with a headless browser. The agent
works from multiple sources:

### Available HK Court Portals

| Portal | What it provides | Access | Auto-scrapable? |
|---|---|---|---|
| **e-Branch / ICCFS** (judiciary.hk) | Case details, cause lists, daily hearings, documents filed | Public web UI (no API key) | ✅ Via Playwright MCP connector — login on-demand, search cases via HTML forms |
| **iCMS** (judiciary.hk) | E-filing: issue writs, file documents, track submissions | Solicitor firm login only | ✅ Via Playwright MCP connector — requires firm credentials stored securely; iCMS is mandatory for High Court cases from June 2026 |
| **Judgments database** (judiciary.hk) | Published judgments only | Public web UI | ✅ Via HTTP scraper — no login needed for published judgments |
| **HKLII** (hklii.org) | Free judgments, legislation | Public | ✅ Via HTTP GET — returns structured pages, easiest to scrape |

**Recommended approach:** Build a custom MCP server (`hk-case-feed`) that wraps
one or more of these portals and exposes a clean read-only API to the agent:

```bash
# The MCP server would expose two tools:
hk_case_search(case_ref: str, court: str) → CaseStatus
hk_case_recent_updates(case_ref: str, since: str) → Filing[]
```

Under the hood, the MCP server uses Playwright to navigate e-Branch/iCMS,
extract filing dates and hearing schedules, and return structured JSON. See
[`CONNECTORS.md`](../../CONNECTORS.md) for the connector pattern.

### Manual / Correspondence Feed

Even with a portal scraper, some data must come from your team:

- **OC (Other Side's) correspondence** — cover letters, draft orders, and
  filings served by the opposing firm
- **Manual log entries** — paralegal/secretary notes when a filing is received
- **The firm's case management system** — intake records, deadline calendars
- **The e-Branch Integrated Court Case File System (ICCFS)** — when accessible
  via the firm's subscription or a manual feed. ICCFS provides electronic
  access to case files but is not a push-based docket feed.

For each active matter the agent pulls new filings/log entries since the last
check, maps filing types to candidate deadlines under the Rules of the High
Court (RHC) / Rules of the District Court (RDC) / Court of Final Appeal Rules,
cross-references against the matter's history and open deliverables, and
produces a docket status report plus a structured deadline feed.

Same source as the [`docket-watcher`](../../litigation-legal/agents/docket-watcher.md)
agent in the litigation-legal Claude Code plugin — this directory is the
Managed Agent cookbook for `POST /v1/agents`.

## ⚠️ Before you deploy (HK-specific)

- **No public docket = no automatic filing detection.** The agent depends on
  what your team logs. If a filing is served but not entered into the case
  management system, the agent will not detect it. Treat a "no new filings"
  result as a statement about your logs, not about the case.
- **Computed deadlines are leads, not calendar entries.** Court deadline rules
  vary by court, level, and judge, and can be modified by practice directions,
  case management orders, and the RHC/RDC. Missing a court deadline has
  malpractice consequences. A licensed attorney verifies every computed
  deadline against the controlling rules and any case-specific orders before
  it is docketed.
- **HK court levels matter for deadline computation:**
  - **Court of Final Appeal** — appeals from the High Court; leave required
  - **High Court (Court of Appeal)** — appeals from CFI and District Court
  - **High Court (Court of First Instance)** — civil claims > HK$3M, serious
    criminal matters; RHC Order and rules apply
  - **District Court** — civil claims HK$75K–HK$3M; RDC Order and rules apply
  - **Magistrates' Courts** — summary criminal matters
  - **Tribunals** — Labour Tribunal, Small Claims Tribunal, Lands Tribunal,
    etc. — each with its own procedural rules
- **Filing classifications are heuristic.** A filing the agent misclassifies
  — an OC letter read as a summons, a consent summons read as a contested
  application — can produce a wrong deadline rule. Read the filing; do not
  trust the label.
- **An unknown court level is not a default.** If the jurisdiction-rule table
  does not cover a court, the mapper must produce `confidence: low` +
  `needs_verification: true`, never a silent default.
- **A quiet log is not a clean docket.** Clerks file late. OC correspondence
  can be delayed. "No new entries" is a statement about the feed, not about
  the case. **HK note:** Unlike US federal courts with next-day electronic
  docketing, HK requires manual service of documents through solicitors,
  which introduces delays.

## Deploy

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export HK_CASE_FEED_URL=...   # Point at your firm's case management MCP or ICCFS feed
export GDRIVE_MCP_URL=...      # For jurisdiction-rule tables and practice directions
../../scripts/deploy-managed-agent.sh docket-watcher
```

## Steering events

See [`steering-examples.json`](./steering-examples.json).

## Security & handoffs

Case filings (served documents, OC cover letters, logged entries) are
UNTRUSTED INPUT. The serving party controls the text and can embed prompts,
URLs, and instructions aimed at the agent. Three-tier isolation:

| Tier | Touches filings? | Tools | Connectors |
|---|---|---|---|
| **`docket-reader`** | **Yes** | `Read`, `Grep` only | hk-case-feed (read-only) |
| `deadline-mapper` / Orchestrator | No — sees structured JSON only | `Read`, `Grep`, `Glob`, `Agent` | gdrive (jurisdiction config, read-only) |
| **`tracker-writer`** (Write-holder) | No | `Read`, `Write`, `Edit` | None |

`docket-reader` returns length-capped, schema-validated JSON. `deadline-mapper`
has no MCP and no web — it applies rules the deploying team has configured.
`tracker-writer` produces `./out/docket-report-<date>.md` and
`./out/deadlines.yaml` and never sees raw filings.

## Adaptation notes (HK)

This cookbook is a starting point. It will not work in production until you
have done the following:

- **Set the case feed MCP URL.** `HK_CASE_FEED_URL` must point at either
  (a) your firm's case management system with an MCP wrapper, (b) an ICCFS
  feed, or (c) a simple file-based feed where paralegals drop structured
  log entries. There is no free public docket API in Hong Kong.
- **Load the portfolio.** The agent reads `matters/_log.yaml` plus the
  per-matter `docket_id` and `court` from the deploying team's litigation-
  legal configuration. If your case management system is the source of truth,
  front it with an MCP or a scheduled sync into the config path.
- **Configure jurisdiction rules.** Ship the deadline-mapper a local-rule
  table for every court level in your portfolio:
  - **RHC Orders** — Order 12 (appearance), Order 14 (summary judgment),
    Order 18 (pleadings), Order 20 (amendment), Order 22 (payment into court),
    Order 24 (discovery), Order 38 (evidence), Order 41 (affidavits),
    Order 58 (appeals to CA), Order 59 (appeals from CFI on costs), etc.
  - **RDC Orders** — generally mirror RHC with lower-value adjustments
  - **CFA Rules** — entirely separate from RHC/RDC; practice directions apply
  - **Tribunal rules** — each tribunal has its own procedural regime
  - **Practice Directions** — over 30+ PDs from the Chief Justice; critically,
    PD 5.1 (Civil Listing), PD 14.1 (Case Management), PD SL1 (Skeleton
    Arguments), PD 21.1 (Costs), PD 25.2 (Mediation).
  - An unknown court level should produce `confidence: low` +
    `needs_verification: true`, never a silent default.
- **Wire delivery.** Decide where the output goes: your case management system
  ingests `./out/deadlines.yaml`; the narrative report goes to Slack, email,
  or your firm's matter management workspace; critical flags route to whoever
  you want woken up.
- **Set the schedule.** Weekly for most matters; daily for anything with a
  hearing inside 14 days, any trial or late-discovery posture, or any
  `risk: critical` matter.

## Computed deadlines are leads, not calendar entries

**The computed deadlines this agent produces require human verification against
the controlling rule (RHC/RDC/RFA), practice direction, and case management
order before they are calendared. Missing a court deadline has malpractice
consequences. This agent surfaces deadlines; a human verifies and dockets
them.**

Every deadline carries `confidence` and `needs_verification` fields. The report
segregates low-confidence entries and stamps a verification callout on anything
not derived from a clear RHC/RDC rule. Treat that as the minimum — not the
ceiling — of human review. Judges override defaults by individual order, local
rules (Practice Directions) change, and the date the document was actually
served may differ from the date logged.

**Not guaranteed:** this agent recommends a deadline; the docketing attorney
confirms against the controlling rule and books the date.
