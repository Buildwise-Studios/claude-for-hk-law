> [!IMPORTANT]
> **Built by [Buildwise Studios](https://github.com/Buildwise-Studios)** — we design and integrate AI agents for professional services: law firms, in-house legal, headhunters, eCommerce operators, and similar teams.
>
> **This repo** is a free Claude plugin marketplace for Hong Kong legal workflows. Install it in [Claude Code](https://claude.com/product/claude-code) ([QUICKSTART.md](QUICKSTART.md); walkthrough video below). Also works in [Claude Cowork](https://claude.com/product/cowork). Your documents stay in **your** Claude environment—data handling follows **your** Anthropic subscription, not Buildwise.
>
> **Want it tailored to your firm?**
>
>
>
> **Examples of what we build on engagement:**
>
> - Playbook-aware **NDA / vendor MSAs** wired to iManage or your CLM, with tracked changes in Word
> - **PDPO DSAR** workflows with repo scripts for HKLII / e-Legislation and firm escalation rules
> - **Conveyancing SPA** review skills + Land Registry / stamp-duty checklists for property teams
> - **Regulatory digest** managed agents (SFC, HKMA, PCPD, LegCo consultations) posted to Slack
> - **Headhunter / recruiting** agents: JD parsing, shortlist scoring, CRM sync (non-legal vertical)
> - **Custom MCP servers** and managed-agent cookbooks behind your orchestrator
>
> **New here?** → [QUICKSTART.md](QUICKSTART.md) — install in 60 seconds.

# Claude for Hong Kong Law

Reference agents, skills, and data connectors for the Hong Kong legal workflows we see most — in-house commercial, privacy, corporate, employment, litigation, regulatory, AI governance, IP, conveyancing, arbitration, competition, and the learning side of the practice (PCLL and law students).

> **Full reference below.** For a fast install path, use [QUICKSTART.md](QUICKSTART.md).

Everything here is available **two ways from one source**: install it as a [Claude Code](https://claude.com/product/claude-code) plugin (recommended; see video below), in [Claude Cowork](https://claude.com/product/cowork), or deploy it through the [Claude Managed Agents API](https://docs.claude.com/en/api/managed-agents) behind your own workflow engine. Same system prompt, same skills — you choose where it runs.

## Getting started in Claude Code

- [Install Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) (CLI in your terminal, or the IDE integration)
- Add the marketplace and a plugin — copy-paste commands in [QUICKSTART.md](QUICKSTART.md)
- Clone this repo if you want HK legislation / HKLII search scripts ([setup guide](references/hk-primary-sources-setup.md))
- Follow the walkthrough in the video below:

https://github.com/user-attachments/assets/2e4c1282-e6a7-4839-91a6-4b4847e7c251

> [!IMPORTANT]
> **Every output from these plugins is a draft for solicitor review — not legal advice, not a legal conclusion, not a substitute for a solicitor or barrister.** They are built with guardrails that reflect that: source attribution on every citation, conservative defaults on privilege and subjective legal calls, jurisdiction assumptions surfaced, and explicit gates before anything is filed, sent, or relied on. A solicitor reviews, verifies, and takes professional responsibility for anything that leaves the building. These plugins make that review faster; they do not replace it.
>
> **These plugins do not represent the legal positions of the developers.** They are tools that help lawyers analyse issues. Where a skill includes a checklist item, a suggested framework, a risk flag, or a characterisation of case law or regulatory guidance, that is an aid to the reviewing solicitor's own analysis, not a statement of the developer's view of the law. The law in many of these areas is unsettled and evolving. The solicitor using the plugin — not the plugin, and not the developer — is responsible for the legal positions taken in their work product.
>
> **Primary sources relied upon:** Hong Kong e-Legislation ([https://www.elegislation.gov.hk](https://www.elegislation.gov.hk)) and the Hong Kong Judiciary website ([https://www.judiciary.hk](https://www.judiciary.hk)) should be consulted for the authoritative version of any ordinance, regulation, or judgment cited by these plugins.

What's in the repo:

- **Practice-area plugins** covering in-house, firm, and academic legal work — each one built around a cold-start interview that learns your pHKLIIlaybook and a `CLAUDE.md` practice profile that every skill reads from.
- **Managed-agent cookbooks** for the scheduled, eyes-on-the-feed workflows (renewal watcher, docket watcher, regulatory feed monitor, diligence grid, launch radar).
- **Optional MCP connectors** (Slack, Google Drive, iManage, Ironclad, and others — see [MCP Connectors](#mcp-connectors); varies by plugin) plus **repo scripts** for HK legislation and company lookup.
- **[Named agents](#agents)** — end-to-end workflow agents (Vendor Agreement Reviewer, DSAR Responder, Termination Reviewer, Claim Chart Builder, …) with job-style names and a single command to run each one.

## Agents

Each agent is named for the workflow it runs. They're the most common surface — start with the ones that match your work, then tune the underlying skill, the practice profile, and the connectors to how your team does it.


| Agent                                   | What it does                                                                                                             | Plugin                | Command                                       |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------- | --------------------------------------------- |
| **Vendor Agreement Reviewer**           | Reviews a vendor MSA against your playbook and produces a redline memo                                                   | `commercial-legal`    | `/commercial-legal:review`                    |
| **NDA Triager**                         | GREEN/YELLOW/RED triage of inbound NDAs so only the hard ones hit a solicitor's desk                                     | `commercial-legal`    | `/commercial-legal:review`                    |
| **Amendment Tracer**                    | Traces how a contract has changed across its base agreement and every amendment                                          | `commercial-legal`    | `/commercial-legal:amendment-history`         |
| **Renewal Watcher**                     | Scans the contract register for cancel-by and renewal deadlines                                                          | `commercial-legal`    | scheduled agent                               |
| **Deal Debrief**                        | Weekly sweep of signed agreements with playbook deviations — prompts the solicitor to log context while memory is fresh  | `commercial-legal`    | scheduled agent                               |
| **Playbook Monitor**                    | Watches the deviation log and proposes playbook updates when a clause has drifted                                        | `commercial-legal`    | scheduled agent                               |
| **Escalation Router**                   | Routes contract issues to the right approver and drafts the ask                                                          | `commercial-legal`    | `/commercial-legal:escalation-flagger`        |
| **Tabular Diligence Review**            | Tabular review over a data room with one row per document and every cell cited                                           | `corporate-legal`     | `/corporate-legal:tabular-review`             |
| **Issue Extractor**                     | Reads VDR documents and extracts issues per house categories and materiality thresholds                                  | `corporate-legal`     | `/corporate-legal:diligence-issue-extraction` |
| **Board Consent Drafter**               | Drafts unanimous written consents in house format with precedent search under the Companies Ordinance                    | `corporate-legal`     | `/corporate-legal:written-consent`            |
| **Material Contracts Schedule Builder** | Builds the disclosure schedule from diligence findings against the purchase-agreement threshold                          | `corporate-legal`     | `/corporate-legal:material-contract-schedule` |
| **Entity Compliance Tracker**           | Computes filing deadlines across jurisdictions and entity types (HK, BVI, Cayman), runs health audits                    | `corporate-legal`     | `/corporate-legal:entity-compliance`          |
| **Closing Checklist Driver**            | Tracks every condition, consent, document, and filing blocking close                                                     | `corporate-legal`     | `/corporate-legal:closing-checklist`          |
| **Integration Runbook**                 | Phased post-closing integration plan with consent tracking and weekly status                                             | `corporate-legal`     | `/corporate-legal:integration-management`     |
| **Data Room Watcher**                   | Monitors the VDR for new uploads and posts closing checklist status on schedule                                          | `corporate-legal`     | scheduled agent                               |
| **Termination Reviewer**                | Runs a proposed termination against jurisdiction-specific risk flags (Cap 57)                                            | `employment-legal`    | `/employment-legal:termination-review`        |
| **Hire Reviewer**                       | Reviews offer letters and restrictive covenants with a jurisdiction check                                                | `employment-legal`    | `/employment-legal:hiring-review`             |
| **Worker Classification Screener**      | Tests a proposed engagement against the HK common law test and Inland Revenue criteria                                   | `employment-legal`    | `/employment-legal:worker-classification`     |
| **Leave Tracker**                       | Monitors open leave with Employment Ordinance (Cap 57) deadlines and decision-point alerts                               | `employment-legal`    | scheduled agent                               |
| **Investigation Lead**                  | Opens, tracks, adds to, and summarises internal investigation matters                                                    | `employment-legal`    | `/employment-legal:investigation-open`        |
| **Policy Drafter**                      | Drafts employment policies consistent with HK legislation and industry practice                                          | `employment-legal`    | `/employment-legal:policy-drafting`           |
| **International Expansion Planner**     | Kicks off EOR-vs-entity planning and outside-counsel briefing for a new jurisdiction                                     | `employment-legal`    | `/employment-legal:expansion-kickoff`         |
| **Wage & Hour Q&A**                     | Jurisdiction-aware employment Q&A for the "quick question" channel                                                       | `employment-legal`    | `/employment-legal:wage-hour-qa`              |
| **DSAR Responder**                      | Drafts DSAR acknowledgments and substantive responses within PDPO (Cap 486) statutory timelines                          | `privacy-legal`       | `/privacy-legal:dsar-response`                |
| **DPA Reviewer**                        | Reviews a DPA against your playbook as data user or data processor                                                       | `privacy-legal`       | `/privacy-legal:dpa-review`                   |
| **PIA Generator**                       | Generates a Privacy Impact Assessment in house format for a new feature or activity                                      | `privacy-legal`       | `/privacy-legal:pia-generation`               |
| **Privacy Triager**                     | Decides whether a processing activity needs a PIA or can proceed under the PDPO                                          | `privacy-legal`       | `/privacy-legal:use-case-triage`              |
| **Privacy Reg Gap Checker**             | Diffs a new or changed regulation against current privacy policy and practice                                            | `privacy-legal`       | `/privacy-legal:reg-gap-analysis`             |
| **Privacy Policy Monitor**              | Sweeps saved PIAs, DPA reviews, and triage results for policy drift                                                      | `privacy-legal`       | `/privacy-legal:policy-monitor`               |
| **Launch Reviewer**                     | Reviews a product launch against your risk calibration                                                                   | `product-legal`       | `/product-legal:launch-review`                |
| **Marketing Claims Checker**            | Flags copy that needs substantiation, reframing, or cutting                                                              | `product-legal`       | `/product-legal:marketing-claims-review`      |
| **"Is this a problem?" Triage**         | Fast answer for the quick Slack question — pattern-matches your calibration                                              | `product-legal`       | `/product-legal:is-this-a-problem`            |
| **Launch Watcher**                      | Watches the launch tracker for upcoming launches that need legal review                                                  | `product-legal`       | scheduled agent                               |
| **Reg Feed Watcher**                    | Polls regulatory feeds and writes the Monday-morning digest                                                              | `regulatory-legal`    | scheduled agent                               |
| **On-demand Reg Check**                 | Check regulatory feeds now and report what's new since last check                                                        | `regulatory-legal`    | `/regulatory-legal:reg-feed-watcher`          |
| **Policy Diff**                         | Diffs a specific regulatory change against the indexed policy library                                                    | `regulatory-legal`    | `/regulatory-legal:policy-diff`               |
| **Gap Tracker**                         | Open gaps tracker — what's flagged and not yet closed                                                                    | `regulatory-legal`    | `/regulatory-legal:gaps`                      |
| **Policy Redrafter**                    | Marked-up policy redraft closing a gap — a proposal for the policy owner's review, not a direct edit to source documents | `regulatory-legal`    | `/regulatory-legal:policy-redraft`            |
| **NPRM Comment Tracker**                | Review open consultation periods on proposed legislation, log decisions, track deadlines                                 | `regulatory-legal`    | `/regulatory-legal:comments`                  |
| **AI Use Case Triager**                 | Classifies proposed AI use cases against your registry                                                                   | `ai-governance-legal` | `/ai-governance-legal:use-case-triage`        |
| **AI Impact Assessor**                  | Runs an AIA across the regimes in scope                                                                                  | `ai-governance-legal` | `/ai-governance-legal:aia-generation`         |
| **Vendor AI Reviewer**                  | Reviews vendor AI terms for training-on-data, liability, model-change, and policy gaps                                   | `ai-governance-legal` | `/ai-governance-legal:vendor-ai-review`       |
| **AI Reg Gap Checker**                  | Diffs a new AI regulation against your current governance posture                                                        | `ai-governance-legal` | `/ai-governance-legal:reg-gap-analysis`       |
| **AI Policy Monitor**                   | Sweeps saved AIAs, triage results, and vendor reviews for AI-policy drift                                                | `ai-governance-legal` | `/ai-governance-legal:policy-monitor`         |
| **Trade Mark Clearance Screener**       | First-pass clearance with knockout check and confusion heuristics under Cap 559                                          | `ip-legal`            | `/ip-legal:clearance`                         |
| **Cease & Desist Drafter**              | Drafts or triages a C&D, calibrated to your enforcement posture                                                          | `ip-legal`            | `/ip-legal:cease-desist`                      |
| **Copyright Takedown**                  | Drafts a takedown notice or triages one received under Cap 528                                                           | `ip-legal`            | `/ip-legal:takedown`                          |
| **OSS Compliance Checker**              | Classifies open source licences against your deployment model                                                            | `ip-legal`            | `/ip-legal:oss-review`                        |
| **FTO Triager**                         | Structured first look at potentially blocking patents — triage, not an opinion                                           | `ip-legal`            | `/ip-legal:fto-triage`                        |
| **Infringement Triager**                | Triage across TM / copyright / patent / trade secrets — factors, not a finding                                           | `ip-legal`            | `/ip-legal:infringement-triage`               |
| **IP Clause Reviewer**                  | Reviews assignment, ownership, licence grants, warranties, and indemnities                                               | `ip-legal`            | `/ip-legal:ip-clause-review`                  |
| **IP Portfolio Tracker**                | Registrations, renewals, maintenance fees, use declarations                                                              | `ip-legal`            | `/ip-legal:portfolio`                         |
| **IP Renewal Watcher**                  | Scheduled deadline report from the IP portfolio register                                                                 | `ip-legal`            | scheduled agent                               |
| **Claim Chart Builder**                 | Element-by-element claim chart, patent or civil cause of action                                                          | `litigation-legal`    | `/litigation-legal:claim-chart`               |
| **Docket Watcher**                      | Weekly sweep of active matters by HK case ref (HCA, HCMP, DCCJ, etc.) — deadlines from your logs, OC correspondence, and RHC/RDC rules; not a live Judiciary docket API | `litigation-legal`    | scheduled agent                               |
| **Demand Letter Drafter**               | Drafts a demand with without-prejudice awareness and a send gate                                                         | `litigation-legal`    | `/litigation-legal:demand-draft`              |
| **Demand Intake**                       | Pre-drafting context gathering — parties, facts, basis, leverage, privilege                                              | `litigation-legal`    | `/litigation-legal:demand-intake`             |
| **Demand Received Triage**              | Triages an inbound demand — options, portfolio cross-check, handoff                                                      | `litigation-legal`    | `/litigation-legal:demand-received`           |
| **Subpoena Triage**                     | Classifies, scopes, and plans compliance with a new subpoena (Order 39, RHC)                                             | `litigation-legal`    | `/litigation-legal:subpoena-triage`           |
| **Chronology Builder**                  | Builds or updates a chronology from declared sources and uploads                                                         | `litigation-legal`    | `/litigation-legal:chronology`                |
| **Deposition Prep**                     | Builds a deposition outline tied to case theory with docs and impeachment                                                | `litigation-legal`    | `/litigation-legal:deposition-prep`           |
| **Brief Section Drafter**               | Drafts a brief section in house style, consistent with case theory                                                       | `litigation-legal`    | `/litigation-legal:brief-section-drafter`     |
| **Privilege Log Reviewer**              | First-pass privilege log review — obvious calls + flags for solicitor review                                             | `litigation-legal`    | `/litigation-legal:privilege-log-review`      |
| **Legal Hold**                          | Issue, refresh, release, or report on legal holds                                                                        | `litigation-legal`    | `/litigation-legal:legal-hold`                |
| **Matter Intake**                       | Uniform intake for a new matter — writes matter.md, history.md, appends to log                                           | `litigation-legal`    | `/litigation-legal:matter-intake`             |
| **Matter Briefing**                     | Deep briefing on one matter — ready for a GC or external counsel call                                                    | `litigation-legal`    | `/litigation-legal:matter-briefing`           |
| **Portfolio Status**                    | Risk distribution, upcoming deadlines, stale matters                                                                     | `litigation-legal`    | `/litigation-legal:portfolio-status`          |
| **Outside Counsel Status**              | Generates weekly status-request drafts across the active portfolio                                                       | `litigation-legal`    | `/litigation-legal:oc-status`                 |
| **Clinic Intake**                       | Structured client intake with cross-area issue spotting and conflict flags (PCLL clinics)                                | `legal-clinic`        | `/legal-clinic:client-intake`                 |
| **Case Memo Scaffold**                  | IRAC-scaffolded case analysis memo with research gaps flagged                                                            | `legal-clinic`        | `/legal-clinic:memo`                          |
| **Research Roadmap**                    | Ordinances to check, case law areas, HKLII search terms — leads, not cites                                               | `legal-clinic`        | `/legal-clinic:research-start`                |
| **Clinic Deadline Tracker**             | Add, report, update, and close case deadlines with professional-indemnity-aware warnings                                 | `legal-clinic`        | `/legal-clinic:deadlines`                     |
| **Case Status Summarizer**              | Case status by audience — client, professor, or court-ready                                                              | `legal-clinic`        | `/legal-clinic:status`                        |
| **Client Letter Drafter**               | Routine client correspondence — appointment confirms, doc requests, updates                                              | `legal-clinic`        | `/legal-clinic:client-letter`                 |
| **Student Ramp**                        | Semester onboarding — clinic procedures, tool walkthrough, practice exercises                                            | `legal-clinic`        | `/legal-clinic:ramp`                          |
| **Semester Handoff**                    | End-of-semester case handoff memos — the mirror of ramp                                                                  | `legal-clinic`        | `/legal-clinic:semester-handoff`              |
| **Supervisor Review Queue**             | Professor's review queue (when formal review supervision is configured)                                                  | `legal-clinic`        | `/legal-clinic:supervisor-review-queue`       |
| **PCLL Prep Coach**                     | Jurisdiction-aware PCLL and HK bar exam practice targeted at weak subjects                                               | `law-student`         | `/law-student:bar-prep-questions`             |
| **Socratic Drill Sergeant**             | It asks, you answer, it pushes back — does not give you the answer                                                       | `law-student`         | `/law-student:socratic-drill`                 |
| **IRAC Grader**                         | Grades your IRAC essay on structure, issue-spotting, rules, analysis                                                     | `law-student`         | `/law-student:irac-practice`                  |
| **Case Briefer**                        | Brief a case in your preferred format                                                                                    | `law-student`         | `/law-student:case-brief`                     |
| **Outline Builder**                     | Build or extend an outline in your format from class notes and casebook                                                  | `law-student`         | `/law-student:outline-builder`                |
| **Cold Call Prep**                      | Predicts professor's questions and drills them before class                                                              | `law-student`         | `/law-student:cold-call-prep`                 |
| **Exam Forecaster**                     | Analyse past exams from the same professor; forecast likely emphases                                                     | `law-student`         | `/law-student:exam-forecast`                  |
| **Legal Writing Critic**                | Structural feedback on a draft — never rewrites                                                                          | `law-student`         | `/law-student:legal-writing`                  |
| **Flashcard Drillmaster**               | Generate or drill flashcards — Leitner-style buckets                                                                     | `law-student`         | `/law-student:flashcards`                     |
| **Study Planner**                       | Long-term study plan with scheduled sessions, adaptive to session history                                                | `law-student`         | `/law-student:study-plan`                     |
| **Skill Registry Browser**              | Search watched registries for community legal skills                                                                     | `legal-builder-hub`   | `/legal-builder-hub:registry-browser`         |
| **Skill Installer**                     | Install a community skill with trust checks and skills-QA                                                                | `legal-builder-hub`   | `/legal-builder-hub:skill-installer`          |
| **Skill QA**                            | Evaluate a skill against the Legal Skill Design Framework                                                                | `legal-builder-hub`   | `/legal-builder-hub:skills-qa`                |
| **Community Skill Recommender**         | Suggest community skills based on recent activity in other plugins                                                       | `legal-builder-hub`   | `/legal-builder-hub:related-skills-surfacer`  |
| **Community Skill Updater**             | Check for updates to installed community skills                                                                          | `legal-builder-hub`   | `/legal-builder-hub:auto-updater`             |
| **Registry Sync**                       | Periodic check of watched registries for new and updated skills                                                          | `legal-builder-hub`   | scheduled agent                               |


For Managed Agent deployment — `agent.yaml`, leaf-worker subagents, steering-event examples, and per-agent security notes — see **[managed-agent-cookbooks/](./managed-agent-cookbooks)**.

## Repository Layout

```
commercial-legal/         # in-house commercial — vendor/NDA/SaaS review, renewals, escalations (Cap 26 context)
corporate-legal/          # M&A diligence, closing checklists, board consents, entity compliance (Cap 622)
employment-legal/         # hire/term review, worker classification, leave, investigations (Cap 57)
privacy-legal/            # DPA, DSAR, PIA, privacy triage, policy monitor (Cap 486)
product-legal/            # launch review, marketing claims, "is this a problem?" triage
regulatory-legal/         # reg feed watcher, policy diff, gap tracker, consultation comments
ai-governance-legal/      # AI use-case triage, AIAs, vendor AI review, AI reg gap-check
ip-legal/                 # trademark clearance, FTO, C&D, copyright takedown, OSS, IP clauses, portfolio (Cap 559/514/528)
litigation-legal/         # portfolio, matters, holds, demands, depo prep, claim charts (RHC/RDC)
legal-clinic/             # PCLL clinic setup, student ramp, intake, deadlines, memos, handoffs
law-student/              # Socratic drilling, outlining, IRAC, PCLL/bar prep, flashcards
legal-builder-hub/        # community skill discovery and install with a trust gate
external_plugins/         # partner-built plugins maintained by their vendors
managed-agent-cookbooks/  # Claude Managed Agent cookbooks — one dir per scheduled agent
  diligence-grid/
  docket-watcher/
  launch-radar/
  reg-monitor/
  renewal-watcher/
scripts/                  # deploy-managed-agent.sh · validate.py · orchestrate.py · lint-tool-scope.py · test-cookbooks.sh
.claude-plugin/
  marketplace.json        # plugin registry
```

Each plugin directory has the same shape:

```
<plugin>/
  .claude-plugin/plugin.json
  CLAUDE.md               # template practice profile — filled in by /<plugin>:cold-start-interview
  README.md
  skills/                 # skills — each is a /<plugin>:<skill> slash command
  agents/                 # scheduled agents (if any)
  hooks/                  # pre- and post-tool hooks (if any)
```

## Getting Started

### Claude Code

The video at the top of this README walks through this flow.

```bash
# Add the marketplace (GitHub — recommended)
/plugin marketplace add Buildwise-Studios/claude-for-hk-law

# Or local path while developing:
# /plugin marketplace add /path/to/claude-for-hk-law

# Install a plugin — pick the ones that match your practice
/plugin install commercial-legal@claude-for-hk-law
/plugin install privacy-legal@claude-for-hk-law
/plugin install corporate-legal@claude-for-hk-law

# Pick up skills, agents, and plugin MCP entries without restarting
/reload-plugins

# Run setup for each plugin you installed.
# This writes your practice profile to ~/.claude/plugins/config/claude-for-hk-law/<plugin>/CLAUDE.md
/commercial-legal:cold-start-interview
/privacy-legal:cold-start-interview
/corporate-legal:cold-start-interview
```

After install, slash commands are available via `/`, skills run when relevant, and scheduled agents use the cadence in their frontmatter.

### Claude Cowork (optional)

In Cowork:

1. Open the **Cowork** tab.
2. Click **Customize** in the left sidebar.
3. Click **Browse plugins** and install the ones you want, **or** upload a custom plugin file (any plugin directory zipped up).

HK primary-source scripts still run from a **clone of this repo** in a terminal session — see [references/hk-primary-sources-setup.md](references/hk-primary-sources-setup.md).

**Run the cold-start interview first.** Every other skill in a plugin reads from the practice profile it writes. Skipping setup is the single most common reason a skill produces generic output. The interview takes 10–20 minutes per plugin and will ask you to point at seed documents (a signed MSA, a playbook, a prior review memo — whatever fits the plugin). More seed material is better; a **quick start** option is available if you want to be productive in 2 minutes and refine later.

**Connect MCP servers that match your stack.** Most core plugins ship **Slack** and **Google Drive** by default; contract, litigation, and IP plugins may add vendor MCPs (see each plugin's `.mcp.json`). HK legislation and case **leads** use repo scripts ([setup guide](references/hk-primary-sources-setup.md)), not HKLII/CLIC MCP URLs. `**law-student`** ships Descrybe and CourtListener (US); `**cocounsel-legal**` is Thomson Reuters Westlaw Deep Research.

Updates: `/plugin update`.

### Claude Managed Agents

For the scheduled agents — regulatory feed monitor, renewal watcher, docket watcher, diligence grid, launch radar — deploy behind your own orchestrator:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
scripts/deploy-managed-agent.sh reg-monitor
scripts/deploy-managed-agent.sh renewal-watcher
scripts/deploy-managed-agent.sh docket-watcher
scripts/deploy-managed-agent.sh diligence-grid
scripts/deploy-managed-agent.sh launch-radar
```

Each template under `[managed-agent-cookbooks/](./managed-agent-cookbooks)` references the same system prompt and skills as its plugin counterpart. The deploy script resolves file references, uploads skills, creates leaf-worker subagents, and POSTs the orchestrator to `/v1/agents`. See `[scripts/orchestrate.py](./scripts/orchestrate.py)` for a reference event loop that routes `handoff_request` events between agents via your own orchestration layer.

> **Research Preview:** subagent delegation (`callable_agents`) is a preview capability and supports a single delegation level. See per-agent READMEs for security tier and handoff guidance.

## How It Fits Together


|                             | What it is                                                                                                                                                                                                                                   | Where it lives                                                  |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Plugins**                 | Self-contained practice-area bundles — skills, agents, hooks, and a template practice profile. Install the ones you need.                                                                                                                    | `<plugin>/`                                                     |
| **Skills**                  | Domain expertise, conventions, and step-by-step methods Claude draws on automatically when relevant — and slash actions you trigger explicitly: `/commercial-legal:review`, `/privacy-legal:dsar-response`, `/litigation-legal:claim-chart`. | `<plugin>/skills/<skill>/SKILL.md`                              |
| **Agents**                  | Scheduled or event-driven workflows (renewal watcher, docket watcher, reg-change monitor). Runs in the background, posts to a channel or writes a file.                                                                                      | `<plugin>/agents/`                                              |
| **Practice profile**        | Plain-English `CLAUDE.md` describing your playbook, escalation rules, and house style. Every skill reads from it.                                                                                                                            | `~/.claude/plugins/config/claude-for-hk-law/<plugin>/CLAUDE.md` |
| **Connectors**              | [MCP servers](https://modelcontextprotocol.io/) that wire Claude to your data — CLM, DMS, e-discovery, research platforms, productivity.                                                                                                     | `.mcp.json` (per plugin)                                        |
| **Managed-agent cookbooks** | `agent.yaml` + depth-1 subagents + steering examples for headless deployment.                                                                                                                                                                | `managed-agent-cookbooks/<slug>/`                               |


Everything is markdown and JSON. No build step.

## Vertical Plugins

Grouped by where the work sits. Each plugin's cold-start interview is what tailors it to your team — start there.

### Transactional & advisory


| Plugin                                           | What it adds                                                                                                                                                                                                                                                               |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[commercial-legal](./commercial-legal)**       | Playbook-aware review of vendor agreements, NDAs, and SaaS subscriptions under Hong Kong common law and Cap 26. Amendment tracing. Renewal register with cancel-by alerts. Escalation routing. Stakeholder summaries.                                                      |
| **[corporate-legal](./corporate-legal)**         | M&A diligence with tabular review and citation-per-cell. Disclosure schedules, closing checklists, written consents, board minutes under the Companies Ordinance (Cap 622). Entity compliance tracker across HK, BVI, Cayman. Post-close integration.                      |
| **[privacy-legal](./privacy-legal)**             | Privacy triage (PIA vs proceed under the PDPO), PIA generation, DPA review as data user or processor, DSAR response within Cap 486 timelines. Policy monitor watches drift between policy and practice.                                                                    |
| **[product-legal](./product-legal)**             | Launch review against house risk calibration. Marketing claims check. "Is this a problem?" triage for Slack questions. Feature risk assessment.                                                                                                                            |
| **[employment-legal](./employment-legal)**       | Hire and termination review with Hong Kong-specific flags (Cap 57, common law). Worker classification under Inland Revenue and common law tests. Leave tracker (Employment Ordinance, sickness allowance, maternity protection). Internal investigations. Policy drafting. |
| **[ai-governance-legal](./ai-governance-legal)** | AI use-case triage against your registry. Impact assessments across regimes in scope. Vendor AI review. Reg-to-policy gap analysis.                                                                                                                                        |
| **[regulatory-legal](./regulatory-legal)**       | Regulatory feed watcher, policy diff, gaps tracker, consultation-period comment tracker. The Monday-morning digest your team actually reads.                                                                                                                               |
| **[ip-legal](./ip-legal)**                       | Trade mark clearance (Cap 559), FTO triage, C&D drafting and triage, copyright takedown (Cap 528), OSS compliance, IP clause review, portfolio tracking. Registered designs (Cap 514) considered where relevant.                                                           |


### Litigation


| Plugin                                     | What it adds                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[litigation-legal](./litigation-legal)** | Works two surfaces. **In-house/portfolio:** matter intake, portfolio status, legal holds, outside counsel status, demands. **Firm/solo:** chronology building, claim charts (patent and civil), deposition prep, privilege log review, brief drafting. Operates within the Rules of the High Court (RHC) and Rules of the District Court (RDC). |


### Conveyancing & property


| Plugin                           | What it adds                                                                                                                                                                                                                                                 |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **[hk-property](./hk-property)** | Conveyancing workflows under the Conveyancing and Property Ordinance (Cap 219), land search, deeds registration, assignments, mortgages, and tenancy agreements (residential and commercial under the Landlord and Tenant (Consolidation) Ordinance, Cap 7). |


### Arbitration


| Plugin                                 | What it adds                                                                                                                                                           |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[hk-arbitration](./hk-arbitration)** | Arbitration workflow support under the Arbitration Ordinance (Cap 609) and HKIAC rules. Award drafting, procedural orders, and CIETAC/HKIAC case management practices. |


### Competition


| Plugin                                 | What it adds                                                                                                                                                                                        |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[hk-competition](./hk-competition)** | Competition law compliance under the Competition Ordinance (Cap 619). First-conduct agreements, abuse of substantial market power, merger control (especially telecoms), and leniency applications. |


### Learning & practice


| Plugin                             | What it adds                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **[law-student](./law-student)**   | Socratic drilling, case briefing, outline building, IRAC grading, cold-call prep, flashcards, PCLL and HK bar prep, exam forecasting, study planning. **Learning mode, not answer mode** — it never writes the answer for you.                                                                                                                               |
| **[legal-clinic](./legal-clinic)** | PCLL clinic professor setup and student semester ramp. Per-practice-area supervisor guide with pedagogy posture (assist / guide / teach). Structured intake with cross-area issue spotting. Deadline tracking with professional-indemnity-aware caution. Memo scaffolds, client letters, semester handoffs. Built within HK Solicitors' practice guidelines. |


### Ecosystem


| Plugin                                       | What it adds                                                                                                                                                                                                                    |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[legal-builder-hub](./legal-builder-hub)** | Community skill discovery and install with a real trust layer — watched registries, a QA framework (`/legal-builder-hub:skills-qa`), SHA-pinned updates, and a mandatory trust check before anything lands in your environment. |


### External / partner-built

Plugins under `[external_plugins/](./external_plugins)` are built and maintained by their vendors. They install from this marketplace like any other plugin, but the vendor owns the code, the connector, and the support channel.


| Plugin                                                    | Built by        | What it adds                                                                                                                                                                                                                                                       |
| --------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **[cocounsel-legal](./external_plugins/cocounsel-legal)** | Thomson Reuters | Westlaw Deep Research with fully cited reports — caselaw, statutes, regulations, Practical Law, and secondary sources. Requires a CoCounsel Legal subscription with the MCP connector enabled. Support: [cocounselsupport@tr.com](mailto:cocounselsupport@tr.com). |


## The trust layer for community legal skills

The community is building legal skills fast — registries like LegalOps Consulting's `lpm-skills` and Lawvable already list dozens. But nobody certifies community skills, and a solicitor installing a random skill from GitHub is installing code that runs with access to their matter files, their practice profile, and their research connectors.

`legal-builder-hub` gives the ecosystem the trust layer it's missing:

- **Security review** — hidden-content scan, injection detection, structural trust check on every install
- **Allowlist** — restrictive-by-default source gate (registries, publishers, connectors, licences)
- **Licence gate** — deployment-context-aware licence policy (personal / firm-internal / product-embedding)
- **Freshness gate** — tracks whether bundled reference content (regulations, ordinances, procedures) has passed its verification window, and warns at invocation
- **Re-scan at update** — a skill that was clean at v1.0 and poisoned at v1.1 gets caught
- **Install log** — an auditable record of what's installed, from where, under what licence, with what review verdict

The allowlist is restrictive by default. Permissive mode is an explicit choice. A non-lawyer gets routed to their solicitor contact, not an "install anyway" button.

Community skills go through the same design review (`/legal-builder-hub:skills-qa`) as the first-party plugins. If you build for lawyers, run the QA against your own skill before publishing. It's the review a lawyer would do if they could read code.

## MCP Connectors

> [!IMPORTANT]
> **What actually ships in this repo.** Each plugin's `.mcp.json` is the source of truth. Most **core practice plugins** default to **Slack** and **Google Drive** only. **HK legislation and case leads** use **repo Python scripts** (`hklii_search.py`, etc.) — not HKLII/CLIC MCP URLs. **HK specialty plugins** ship with **empty** MCP stubs until you add your own. Customer-subscription connectors need your account — configure via `claude mcp` or the plugin's `.mcp.json`. Citations from model knowledge alone are flagged `[verify]`; when a script or research MCP actually ran in the session, tags reflect that source.


| Connector                                                | What it gives Claude                            | Plugins (in `.mcp.json`)                                  | Notes                     |
| -------------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------------- | ------------------------- |
| **Slack**                                                | Read channels, search, post                     | 12 core practice plugins                                  | Your workspace            |
| **Google Drive**                                         | Read docs, sheets, slides                       | 12 core practice plugins                                  | Your account              |
| **Ironclad**                                             | Contract repository search                      | `commercial-legal`                                        | Customer subscription     |
| **DocuSign**                                             | Envelope status, agreements                     | `commercial-legal`                                        | Customer subscription     |
| **iManage**                                              | DMS read (permission-bound)                     | `commercial-legal`, `corporate-legal`                     | Customer subscription     |
| **Definely**                                             | Definitions, cross-references, structural diffs | `commercial-legal`, `corporate-legal`                     | Customer subscription     |
| **TopCounsel**                                           | Outside counsel recommendations                 | `commercial-legal`, `corporate-legal`, `litigation-legal` | Customer subscription     |
| **Box**                                                  | VDR / matter folders                            | `corporate-legal`                                         | Customer subscription     |
| **Solve Intelligence**                                   | Patent search and analysis                      | `corporate-legal`, `ip-legal`                             | Customer subscription     |
| **Everlaw**                                              | E-discovery productions                         | `litigation-legal`                                        | Customer subscription     |
| **Aurora (Consilio)**                                    | E-discovery / review platform                   | `litigation-legal`                                        | Customer subscription     |
| **Linear**                                               | Issue tracking                                  | `product-legal`                                           | Your workspace            |
| **Atlassian (Jira/Confluence)**                          | Issue tracking                                  | `product-legal`                                           | Your workspace            |
| **Asana**                                                | Project tracking                                | `product-legal`                                           | Your workspace            |
| **Lawve AI**                                             | Contract review assist                          | `legal-builder-hub`                                       | Customer subscription     |
| **Paid HK research** (Westlaw Asia, LexisNexis HK, etc.) | Judgments and commentary                        | Add yourself via `claude mcp`                             | URL from your vendor only |
| **Descrybe**                                             | Case law research                               | `law-student` only                                        | Customer subscription     |
| **CourtListener**                                        | US federal/state case law                       | `law-student` only                                        | US-focused                |
| **CoCounsel Legal (Thomson Reuters)**                    | Westlaw Deep Research                           | `cocounsel-legal` (vendor plugin)                         | Separate install; OAuth   |


### Repo scripts (not MCP)


| Tool                                           | What it does                                              | Used by                                                                                               |
| ---------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `**scripts/download_legislation_list.py`**     | HK ordinance index (DOJ open data)                        | All HK plugins — see [references/hk-primary-sources-setup.md](references/hk-primary-sources-setup.md) |
| `**scripts/download_legislation_text.py**`     | Ordinance XML text from DOJ ZIP packs                     | Same                                                                                                  |
| `**scripts/hklii_search.py**`                  | HKLII `simplesearch` API — cases/legislation leads + URLs | Same                                                                                                  |
| `**scripts/judiciary_search.py**`              | GovHK Judiciary site search (HTML parser)                 | Same                                                                                                  |
| `**corporate-legal/scripts/check_company.py**` | Companies Registry open data                              | `corporate-legal`                                                                                     |


**First-time setup:** [references/hk-primary-sources-setup.md](references/hk-primary-sources-setup.md) (Python 3, repo root, smoke tests).

**Not shipped:** `mcp.hklii.hk` and `mcp.clic.org.hk` do not resolve in DNS — use the scripts above and [hklii.hk](https://www.hklii.hk) / [clic.org.hk](https://www.clic.org.hk) in the browser. CLIC's on-site AI chat is not an MCP endpoint.

These scripts run from the **repo root** when a skill invokes them via Bash — they are not MCP servers and are not auto-installed with the plugin.

> **Microsoft 365:** Install the [Claude for Microsoft 365](https://marketplace.microsoft.com/en-us/product/office/wa200010453) add-in for Word/Excel — that is a separate product surface, not an entry in plugin `.mcp.json` files.

> **Building a connector?** See [CONNECTORS.md](./CONNECTORS.md) for submission guidelines and a wishlist of HK connectors we do not ship yet (Land Registry, SFC feeds, etc.).

## Claude for Microsoft 365

Lawyers live in Word and Excel. **Every contract-touching skill in this repo is authored to work in the Claude for Word sidebar, with tracked changes as the output mode.** That's `commercial-legal:review` (vendor agreements, NDAs, SaaS subscriptions), `commercial-legal:amendment-history`, `ip-legal:ip-clause-review`, `ai-governance-legal:vendor-ai-review`, `privacy-legal:dpa-review`, and the diligence extraction in `corporate-legal`. A reviewer accepts or rejects each change exactly as they would for a human markup — numbering, defined terms, cross-references, and styles are preserved.

The Excel-facing skills produce workbooks that open cleanly: `corporate-legal:tabular-review` writes a multi-sheet `.xlsx` with a sources sheet, `litigation-legal:claim-chart` writes an element-by-element claim chart with citation columns, `corporate-legal:entity-compliance` writes the compliance register with deadline columns, and `commercial-legal:renewal-tracker` exports the renewal register sorted by cancel-by date.

Install Claude for Microsoft 365 from **[Microsoft AppSource](https://marketplace.microsoft.com/en-us/product/office/wa200010453)**. Once installed, the skills from any plugin you've enabled are available from the sidebar via `/`, and connectors are reachable from the same surface. A single thread can span Word, Excel, PowerPoint, and Outlook.

For IT admins deploying the add-in against your own cloud (Azure OpenAI, or an internal gateway) rather than Anthropic's API, see the separate `[claude-for-msft-365-install](https://github.com/anthropics/financial-services/tree/main/claude-for-msft-365-install)` tooling.

## Making It Yours

These are reference templates. They get better when you tune them to how your team works — and the customisation mechanism is the plugin itself, not a config file buried in a repo.

- **Run the cold-start interview.** It **is** the customisation mechanism. It asks how your practice works, reads your seed documents, and writes your practice profile. Every other skill reads from that profile. A `/commercial-legal:cold-start-interview` with five signed MSAs, your playbook, and your escalation matrix will make the review skills noticeably sharper.
- **Edit the practice profile.** Your profile lives at `~/.claude/plugins/config/claude-for-hk-law/<plugin>/CLAUDE.md`. Edit it directly for small fixes — a wrong escalation threshold, a new integration, a policy update. It survives plugin updates.
- **Re-run setup.** `/<plugin>:cold-start-interview` again for a full re-interview when your practice shifts materially (new jurisdiction, new CLM, new policy).
- **Swap connectors.** Point `.mcp.json` at your CLM, DMS, e-discovery platform, launch tracker, HRIS. Skills fall back gracefully when a connector isn't configured — no silent no-ops.
- **Bring your playbook and templates.** Drop your terminology, house style, and branded templates into the plugin's `CLAUDE.md` and `references/`. The skills will pick them up.
- **Fork skills for house style.** Every skill is a markdown file under `skills/`. Edit the steps, the gates, the output format.
- **Add scheduled agents.** The agents under `<plugin>/agents/` are markdown with a cron-style schedule. Add your own for the watchers your team needs.

No build step. Everything is markdown and JSON.

## Skill & Command Reference

The full map across all plugins. The cold-start interview is the first thing to run in any plugin.

### ai-governance-legal


| Command                                     | Skill                | What it does                                                                                 |
| ------------------------------------------- | -------------------- | -------------------------------------------------------------------------------------------- |
| `/ai-governance-legal:cold-start-interview` | cold-start-interview | Cold-start — learns your AI governance practice                                              |
| `/ai-governance-legal:ai-inventory`         | ai-inventory         | HK AI system inventory — PCPD / SFC / HKMA sector and risk tier per system                   |
| `/ai-governance-legal:use-case-triage`      | use-case-triage      | Classify AI use case — approved, conditional, or no                                          |
| `/ai-governance-legal:aia-generation`       | aia-generation       | Run an AI impact assessment in house format                                                  |
| `/ai-governance-legal:vendor-ai-review`     | vendor-ai-review     | Review vendor AI terms against governance positions                                          |
| `/ai-governance-legal:reg-gap-analysis`     | reg-gap-analysis     | Diff a new AI regulation against your governance posture                                     |
| `/ai-governance-legal:policy-monitor`       | policy-monitor       | Keep the AI policy current with practice                                                     |
| `/ai-governance-legal:policy-starter`       | policy-starter       | Draft a firm AI usage policy from published model policies, adapted to your practice profile |
| `/ai-governance-legal:matter-workspace`     | matter-workspace     | Manage matter workspaces (practice-level)                                                    |


### legal-builder-hub


| Command                                      | Skill                   | What it does                                               |
| -------------------------------------------- | ----------------------- | ---------------------------------------------------------- |
| `/legal-builder-hub:cold-start-interview`    | cold-start-interview    | Practice profile interview and starter-pack recommendation |
| `/legal-builder-hub:registry-browser`        | registry-browser        | Search watched registries for community legal skills       |
| `/legal-builder-hub:skill-installer`         | skill-installer         | Install a community skill with trust checks                |
| `/legal-builder-hub:skills-qa`               | skills-qa               | Evaluate a skill against the Design Framework              |
| `/legal-builder-hub:related-skills-surfacer` | related-skills-surfacer | Suggest community skills from activity in other plugins    |
| `/legal-builder-hub:auto-updater`            | auto-updater            | Check for updates to installed community skills            |
| `/legal-builder-hub:disable`                 | skill-manager           | Disable a community skill without removing files           |
| `/legal-builder-hub:uninstall`               | skill-manager           | Uninstall a community skill installed via the hub          |
| scheduled                                    | registry-sync (agent)   | Periodic check of watched registries for updates           |


### legal-clinic


| Command                                 | Skill                                  | What it does                                                           |
| --------------------------------------- | -------------------------------------- | ---------------------------------------------------------------------- |
| `/legal-clinic:cold-start-interview`    | cold-start-interview                   | Professor setup — areas, jurisdiction, supervision style               |
| `/legal-clinic:build-guide`             | build-guide                            | Professor practice-area guide — intake, pedagogy posture, review gates |
| `/legal-clinic:ramp`                    | ramp                                   | Student semester onboarding with practice exercises                    |
| `/legal-clinic:client-intake`           | client-intake                          | Structured intake with cross-area issue spotting                       |
| `/legal-clinic:client-comms-log`        | client-comms-log                       | Log a client communication — append-only per-case record               |
| `/legal-clinic:research-start`          | research-start                         | Research roadmap — ordinances, case law, search terms                  |
| `/legal-clinic:memo`                    | memo                                   | IRAC-scaffolded analysis memo with research gaps flagged               |
| `/legal-clinic:draft`                   | draft                                  | First draft of a common clinic document                                |
| `/legal-clinic:client-letter`           | client-letter · plain-language-letters | Routine client correspondence from templates                           |
| `/legal-clinic:status`                  | status                                 | Case status by audience — client, professor, court-ready               |
| `/legal-clinic:deadlines`               | deadlines                              | Track case deadlines with professional-indemnity-aware warnings        |
| `/legal-clinic:supervisor-review-queue` | supervisor-review-queue                | Professor's review queue (if formal supervision)                       |
| `/legal-clinic:semester-handoff`        | semester-handoff                       | End-of-semester case handoff memos                                     |


### commercial-legal


| Command                                  | Skill                                                  | What it does                                            |
| ---------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------- |
| `/commercial-legal:cold-start-interview` | cold-start-interview                                   | Cold-start — learn your commercial contracts practice   |
| `/commercial-legal:review`               | vendor-agreement-review · nda-review · saas-msa-review | Review vendor agreement, NDA, or SaaS subscription      |
| `/commercial-legal:amendment-history`    | amendment-history                                      | Trace contract changes across base and amendments       |
| `/commercial-legal:renewal-tracker`      | renewal-tracker                                        | Show contracts with cancel-by deadlines within 90 days  |
| `/commercial-legal:escalation-flagger`   | escalation-flagger                                     | Route a contract issue and draft the ask                |
| `/commercial-legal:review-proposals`     | (internal)                                             | Review and approve pending playbook update proposals    |
| `/commercial-legal:matter-workspace`     | matter-workspace                                       | Manage matter workspaces (practice-level)               |
| —                                        | stakeholder-summary                                    | Translates a review into a business-stakeholder summary |
| scheduled                                | renewal-watcher (agent)                                | Weekly sweep of the renewal register                    |
| scheduled                                | deal-debrief (agent)                                   | Weekly surface of signed agreements with deviations     |
| scheduled                                | playbook-monitor (agent)                               | Proposes playbook updates when a clause has drifted     |


### corporate-legal


| Command                                       | Skill                      | What it does                                                      |
| --------------------------------------------- | -------------------------- | ----------------------------------------------------------------- |
| `/corporate-legal:cold-start-interview`       | cold-start-interview       | House cold-start, with optional `--new-deal` kickoff              |
| `/corporate-legal:tabular-review`             | tabular-review             | Tabular review — one row per document, every cell cited           |
| `/corporate-legal:diligence-issue-extraction` | diligence-issue-extraction | Extract issues from VDR documents per house thresholds            |
| `/corporate-legal:material-contract-schedule` | material-contract-schedule | Build material contracts disclosure schedule                      |
| `/corporate-legal:closing-checklist`          | closing-checklist          | What's blocking close with critical path                          |
| `/corporate-legal:written-consent`            | written-consent            | Draft board or committee consent in HK company format             |
| `/corporate-legal:entity-compliance`          | entity-compliance          | Entity compliance tracker across HK, BVI, and other jurisdictions |
| `/corporate-legal:integration-management`     | integration-management     | Post-closing integration tracker with consent tracking            |
| `/corporate-legal:matter-workspace`           | matter-workspace           | Manage matter workspaces (practice-level)                         |
| —                                             | board-minutes              | Drafts board or committee minutes in HK house format              |
| —                                             | deal-team-summary          | Aggregates diligence findings into a deal briefing                |
| —                                             | ai-tool-handoff            | Detects Luminance/Kira, QAs bulk-tool output                      |
| scheduled                                     | dataroom-watcher (agent)   | Monitors VDR uploads and posts checklist status                   |


### employment-legal


| Command                                   | Skill                   | What it does                                                    |
| ----------------------------------------- | ----------------------- | --------------------------------------------------------------- |
| `/employment-legal:cold-start-interview`  | cold-start-interview    | Cold-start — learns jurisdictions and escalation rules          |
| `/employment-legal:wage-hour-qa`          | wage-hour-qa            | Jurisdiction-aware wage/hour and employment Q&A                 |
| `/employment-legal:hiring-review`         | hiring-review           | Review offer letter and restrictive covenants under HK law      |
| `/employment-legal:termination-review`    | termination-review      | Termination review under Cap 57 with high-risk flag detection   |
| `/employment-legal:worker-classification` | worker-classification   | Classify a proposed engagement under HK common law and IR tests |
| `/employment-legal:policy-drafting`       | policy-drafting         | Draft employment policy with reference to HK legislation        |
| `/employment-legal:leave-tracker`         | leave-tracker           | Check open leaves for EO deadlines and alerts                   |
| `/employment-legal:log-leave`             | log-leave               | Add a new leave to the leave register                           |
| `/employment-legal:investigation-open`    | internal-investigation  | Open a new internal investigation matter                        |
| `/employment-legal:investigation-add`     | internal-investigation  | Add data to an open investigation — docs, notes                 |
| `/employment-legal:investigation-memo`    | internal-investigation  | Draft or update the privileged investigation memo               |
| `/employment-legal:investigation-query`   | internal-investigation  | Ask questions against an open investigation log                 |
| `/employment-legal:investigation-summary` | internal-investigation  | Draft audience-specific summary from investigation memo         |
| `/employment-legal:expansion-kickoff`     | international-expansion | Kick off expansion planning for a new jurisdiction              |
| `/employment-legal:expansion-update`      | international-expansion | Update status of an in-progress expansion project               |
| `/employment-legal:matter-workspace`      | matter-workspace        | Manage matter workspaces (practice-level)                       |
| —                                         | handbook-updates        | Diffs handbook changes and flags regulatory impacts             |
| scheduled                                 | leave-tracker (agent)   | Weekly monitor of open leaves with hard deadlines               |


### ip-legal


| Command                          | Skill                      | What it does                                                                |
| -------------------------------- | -------------------------- | --------------------------------------------------------------------------- |
| `/ip-legal:cold-start-interview` | cold-start-interview       | Cold-start — learn your IP practice and posture                             |
| `/ip-legal:clearance`            | clearance                  | Trade mark clearance first pass — knockout + similar marks under Cap 559    |
| `/ip-legal:fto-triage`           | fto-triage                 | Freedom-to-operate triage, not an FTO opinion                               |
| `/ip-legal:invention-intake`     | invention-intake           | Invention disclosure first-pass screen — novelty, obviousness, bar dates    |
| `/ip-legal:cease-desist`         | cease-desist               | Draft a C&D or triage one you received                                      |
| `/ip-legal:takedown`             | takedown                   | Copyright takedown notice under Cap 528, response triage, or counter-notice |
| `/ip-legal:infringement-triage`  | infringement-triage        | Infringement triage across all IP rights                                    |
| `/ip-legal:ip-clause-review`     | ip-clause-review           | Review IP clauses — assignment, licence, warranties                         |
| `/ip-legal:oss-review`           | oss-review                 | Open source licence compliance check                                        |
| `/ip-legal:portfolio`            | portfolio                  | Track IP portfolio deadlines and renewals                                   |
| `/ip-legal:matter-workspace`     | matter-workspace           | Manage matter workspaces (practice-level)                                   |
| scheduled                        | ip-renewal-watcher (agent) | Weekly report of IP portfolio deadlines                                     |


### litigation-legal


| Command                                   | Skill                  | What it does                                                            |
| ----------------------------------------- | ---------------------- | ----------------------------------------------------------------------- |
| `/litigation-legal:cold-start-interview`  | cold-start-interview   | Cold-start — risk, landscape, house brief style                         |
| `/litigation-legal:matter-intake`         | matter-intake          | Intake a new matter — writes matter.md and history                      |
| `/litigation-legal:matter-briefing`       | matter-briefing        | Deep briefing on one matter for a call                                  |
| `/litigation-legal:matter-update`         | matter-update          | Append a dated event to a matter's history                              |
| `/litigation-legal:portfolio-status`      | portfolio-status       | Portfolio rollup — risk, deadlines, stale matters                       |
| `/litigation-legal:matter-close`          | matter-close           | Close a matter — archive, retain record                                 |
| `/litigation-legal:matter-workspace`      | matter-workspace       | Manage matter workspaces (practice-level)                               |
| `/litigation-legal:demand-intake`         | demand-intake          | Pre-drafting context — parties, facts, leverage                         |
| `/litigation-legal:demand-draft`          | demand-draft           | Draft demand letter with without-prejudice gate and .docx output        |
| `/litigation-legal:demand-received`       | demand-received        | Triage inbound demand — options, portfolio cross-check                  |
| `/litigation-legal:subpoena-triage`       | subpoena-triage        | Triage subpoena — scope, burden, privilege, plan                        |
| `/litigation-legal:legal-hold`            | legal-hold             | Issue, refresh, release, or report on legal holds                       |
| `/litigation-legal:oc-status`             | oc-status              | Weekly status-request emails to outside counsel                         |
| `/litigation-legal:claim-chart`           | claim-chart            | Element chart — patent or civil cause of action                         |
| `/litigation-legal:chronology`            | chronology             | Build or update a chronology from sources and uploads                   |
| `/litigation-legal:deposition-prep`       | deposition-prep        | Deposition outline tied to case theory                                  |
| `/litigation-legal:privilege-log-review`  | privilege-log-review   | First-pass privilege log review with flags                              |
| `/litigation-legal:brief-section-drafter` | brief-section-drafter  | Draft a brief section in house style                                    |
| scheduled                                 | docket-watcher (agent) | HK matter deadline sweep (HCA, HCMP, DCCJ, etc.) from logs and correspondence — not a live court docket feed |


### privacy-legal


| Command                               | Skill                | What it does                                                          |
| ------------------------------------- | -------------------- | --------------------------------------------------------------------- |
| `/privacy-legal:cold-start-interview` | cold-start-interview | Cold-start — learns your privacy practice                             |
| `/privacy-legal:use-case-triage`      | use-case-triage      | Determine PIA vs proceed under the PDPO                               |
| `/privacy-legal:pia-generation`       | pia-generation       | Generate a Privacy Impact Assessment in house format                  |
| `/privacy-legal:dpa-review`           | dpa-review           | Review a DPA — auto-detects data user vs processor                    |
| `/privacy-legal:dsar-response`        | dsar-response        | Walk a DSAR and draft response under Cap 486 — verify, locate, assess |
| `/privacy-legal:reg-gap-analysis`     | reg-gap-analysis     | Diff a regulation against current policy and practice                 |
| `/privacy-legal:policy-monitor`       | policy-monitor       | Keep the privacy policy current with practice                         |
| `/privacy-legal:matter-workspace`     | matter-workspace     | Manage matter workspaces (practice-level)                             |


### product-legal


| Command                                  | Skill                   | What it does                                                |
| ---------------------------------------- | ----------------------- | ----------------------------------------------------------- |
| `/product-legal:cold-start-interview`    | cold-start-interview    | Cold-start — connects launch tracker, learns calibration    |
| `/product-legal:is-this-a-problem`       | is-this-a-problem       | Fast "is this a problem?" answer for quick questions        |
| `/product-legal:launch-review`           | launch-review           | Full launch review against framework and calibration        |
| `/product-legal:marketing-claims-review` | marketing-claims-review | Review marketing copy for claims that need work             |
| `/product-legal:matter-workspace`        | matter-workspace        | Manage matter workspaces (practice-level)                   |
| —                                        | feature-risk-assessment | Deep-dive risk on a single feature when launch review flags |
| scheduled                                | launch-watcher (agent)  | Monitors launch tracker for upcoming reviews                |


### regulatory-legal


| Command                                  | Skill                      | What it does                                                                    |
| ---------------------------------------- | -------------------------- | ------------------------------------------------------------------------------- |
| `/regulatory-legal:cold-start-interview` | cold-start-interview       | Cold-start — watchlist, policy index, materiality                               |
| `/regulatory-legal:reg-feed-watcher`     | reg-feed-watcher           | Check regulatory feeds now and report what's new                                |
| `/regulatory-legal:policy-diff`          | policy-diff                | Diff a regulatory change against the policy library                             |
| `/regulatory-legal:gaps`                 | gap-surfacer               | Open gaps tracker — what's flagged and not closed                               |
| `/regulatory-legal:policy-redraft`       | policy-redraft             | Marked-up policy redraft closing a gap — proposal for the policy owner's review |
| `/regulatory-legal:comments`             | (tracker)                  | Review open consultation periods and deadlines on proposed legislation          |
| `/regulatory-legal:matter-workspace`     | matter-workspace           | Manage matter workspaces (practice-level)                                       |
| scheduled                                | reg-change-monitor (agent) | Scheduled regulatory feed sweep with materiality filter                         |


### law-student


| Command                             | Skill                | What it does                                            |
| ----------------------------------- | -------------------- | ------------------------------------------------------- |
| `/law-student:cold-start-interview` | cold-start-interview | About-you interview — classes, bar, learning style      |
| `/law-student:socratic-drill`       | socratic-drill       | Socratic drill — it asks, you answer, it pushes back    |
| `/law-student:case-brief`           | case-brief           | Brief a case in your preferred format                   |
| `/law-student:outline-builder`      | outline-builder      | Build or extend an outline in your format               |
| `/law-student:irac-practice`        | irac-practice        | Grade IRAC essay — structure, issues, rules, analysis   |
| `/law-student:legal-writing`        | legal-writing        | Structural feedback on your writing — never rewrites    |
| `/law-student:cold-call-prep`       | cold-call-prep       | Predict professor's questions and drill them            |
| `/law-student:bar-prep-questions`   | bar-prep-questions   | PCLL or HK bar exam questions targeted at weak subjects |
| `/law-student:flashcards`           | flashcards           | Generate or drill flashcards — Leitner-style            |
| `/law-student:exam-forecast`        | exam-forecast        | Analyse past exams to forecast likely emphases          |
| `/law-student:study-plan`           | study-plan           | Build or update a long-term study plan                  |
| `/law-student:session`              | study-plan           | Run a focused N-question session; update the plan       |


### cocounsel-legal (Thomson Reuters)


| Command                          | Skill         | What it does                                                              |
| -------------------------------- | ------------- | ------------------------------------------------------------------------- |
| `/cocounsel-legal:deep-research` | deep-research | Run Westlaw Deep Research — start, poll, and present a fully cited report |


## Contributing

Everything here is markdown and JSON. Fork, edit, PR.

- **New skill** → add it under `<plugin>/skills/<skill-name>/SKILL.md` with the frontmatter the existing skills use (`name`, `description`, `argument-hint`). Keep the description under 1024 characters — it's the trigger signal. The skill is invokable as `/<plugin>:<skill-name>`. Mark pure-reference skills `user-invocable: false`.
- **New agent** → add `<plugin>/agents/<name>.md` with scheduling frontmatter and the system prompt. Add a matching `managed-agent-cookbooks/<name>/` if you want headless deployment.
- **Community skills** → use `/legal-builder-hub:skill-installer` to test a community skill in your environment. The hub runs `/legal-builder-hub:skills-qa` against every skill before installing — it scores the skill against the Legal Skill Design Framework (nine design parameters, three legal failure modes, a trust-surface check) and rejects anything that fails.
- **Validate cookbooks before pushing** → `bash scripts/test-cookbooks.sh` dry-runs every managed-agent cookbook and lints orchestrator tool scope.

## Licence

Licensed under the [Apache Licence, Version 2.0](LICENSE).

Copyright 2025.
