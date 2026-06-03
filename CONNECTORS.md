# Adding a Connector

The plugins are at their best when connected to authoritative sources. If you build or operate a legal data source, research tool, CLM, DMS, eDiscovery platform, or practice management system, we want your MCP connector in the suite.

## What makes a good legal MCP connector

- **Remote MCP server over HTTPS** with OAuth or API-key auth (streamable HTTP or SSE transport)
- **Read-heavy tools** — search, fetch, list. Write tools (create, send, file) need an explicit confirmation prompt on the client side; say so in your tool descriptions.
- **Provenance in results** — return the source, date retrieved, and a citation-ready identifier. The plugins tag every cite by source; your connector should make that possible.
- **No instruction-like content in results** — the plugins treat retrieved content as data, not commands. If your tool results include metadata or system notes, mark them clearly so they don't look like embedded directives.
- **Rate limits and errors that degrade gracefully** — the plugins have a fallback for when a connector isn't responding; a clean error is better than a timeout.

## How to submit

1. Publish your MCP server and document its tools, auth flow, and data coverage.
2. Open a PR adding your server to the relevant plugin's `.mcp.json` with the URL, auth method, and a one-line description of what it gives Claude.
3. Include a note on which practice areas / plugins it's most useful for.
4. We'll test against the plugin workflows and merge. Connectors that pass the retrieval-quality and injection-resistance checks go in the default `.mcp.json`; others get documented in the plugin README for users to add themselves.

## Current connectors

Connectors shipped in the default `.mcp.json` of each plugin:

| Connector | Plugins | Notes |
|---|---|---|
| **Microsoft 365** | all 12 | Common in HK law firms |
| **Slack** | all 12 | |
| **Google Drive** (`gdrive`) | all 12 | |
| **HKLII** | all 12 | Hong Kong judgments and legislation — public, free |
| **e-Legislation API** | all 12 | Official Hong Kong e-Legislation — ordinances, regulations, commencement notices |
| **Companies Registry e-Search** | corporate-legal | HK company searches via CR cyberport.gov.hk |
| **Descrybe** | legal-clinic, ip-legal, law-student | |
| **Definely** | commercial-legal, corporate-legal | |
| **iManage** | commercial-legal, corporate-legal | Widely used in HK law firms |
| **Solve Intelligence** | corporate-legal, ip-legal | |
| **TopCounsel** | commercial-legal, corporate-legal, litigation-legal | |
| **Box** | corporate-legal | |
| **Ironclad** | commercial-legal | |
| **DocuSign / DocuSign CLM** | commercial-legal | |
| **Everlaw** | litigation-legal | |
| **Aurora** | litigation-legal | |
| **Lawve AI** | legal-builder-hub | |
| **Linear** | product-legal | |
| **Atlassian (Jira)** | product-legal | |
| **Asana** | product-legal | |

See the `.mcp.json` in each plugin directory for the authoritative list.

## Wanted connectors

These would make specific plugins significantly more useful. If you build or operate one, see "How to submit" above.

- **IP management systems** (Anaqua, Clarivate IPfolio, AppColl, FoundationIP) — full docket sync for `ip-legal` portfolio tracking, with Hong Kong trade mark and patent coverage
- **IPD (Intellectual Property Department) API** — Hong Kong patents, trade marks (Cap 559), registered designs (Cap 514), and copyright (Cap 528) status and deadlines for `ip-legal`
- **Land Registry** — Hong Kong land records search, property ownership history, deeds registration for `hk-property` conveyancing workflows
- **Judiciary e-Branch / ICCFS** — HK court case file system at judiciary.hk. No public API, but a custom MCP connector using Playwright can scrape case details, cause lists, hearing schedules, and filed documents from the public web portal. Ideal for the `docket-watcher` managed agent.
- **Judiciary iCMS (e-filing)** — HK e-filing via the Integrated Court Case Management System. Requires solicitor firm login. Can be wrapped via an authenticated MCP connector with Playwright/headless browser. Mandatory for High Court cases from June 2026.
- **Judiciary Judgments Database** — Published judgments searchable at judiciary.hk. Scrapable via HTTP (no login). Good supplementary feed for case research.
- **Land Tribunal** — Lands Tribunal (Cap 17) decisions and procedure support
- **Securities and Futures Commission (SFC)** — SFC regulatory feeds and codes for `regulatory-legal`
- **Hong Kong Monetary Authority (HKMA)** — HKMA banking rules, supervisory policy manuals, and enforcement actions
- **Competition Commission resources** — competition rules guidance, leniency tracker for `hk-competition`
- **Jira / Linear / Asana for OSS requests** — `ip-legal` OSS clearance can monitor and respond to incoming tickets
- **Thomson Reuters** (CoCounsel, Practical Law, Westlaw) — research and drafting for every plugin
- **SS&C Intralinks / Datasite** — VDR access for `corporate-legal` diligence
- **Relativity / Everlaw beyond read** — eDiscovery workflow for `litigation-legal`
- **Global AI Regulation Tracker** (techieray.com/GlobalAIRegulationTracker) — jurisdiction-tagged AI regulation tracking with structured API. Curated, verified, multi-jurisdiction. Would be a primary-source-adjacent feed for `ai-governance-legal` and `regulatory-legal`.
- **Regulatory primary sources** — a connector to official registers (e-Legislation, HKLII, Hong Kong e-Legislation, EUR-Lex, legislation.gov.uk, Singapore Statutes Online) that bypasses the agent-blockers many legislative sites use. A curated regulatory knowledge base would be a high-value addition.

## Questions

Open an issue on this repo. For partnership or integration questions, see the contact on each plugin's README.
