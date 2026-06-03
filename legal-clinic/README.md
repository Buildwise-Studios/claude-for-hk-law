# Claude for Hong Kong Law School Clinics

*Supercharging access to justice through AI-enabled clinical legal education in Hong Kong.*

A plugin for Hong Kong law school clinics — the institutions where law students, supervised by clinical professors and qualified solicitors, provide free legal services to people who can't afford representation. Immigration, housing, family law, consumer protection, criminal defence, civil rights.

Hong Kong's free legal services ecosystem includes the **Duty Lawyer Service** (providing legal representation in Magistrates' Courts), the **Free Legal Advice Scheme** (administered by the Law Society and Bar Association), **CLIC** (Community Legal Information Centre — online legal information), and the law school clinics at **HKU**, **CUHK**, and **CityU**.

**Every output is a draft for student analysis and attorney review — marked, gated, and logged. The plugin scaffolds the work; a student reasons through it; a supervising solicitor or professor reviews. Nothing leaves the clinic without going through the supervision model set at setup.**

## The problem this solves

Clinics are structurally capacity-constrained. A supervising professor manages 5–10 students. Each student carries a handful of cases while juggling classes. Students turn over every semester. Administrative tasks — intake write-up, first drafts, research starting points, status updates — consume hours that could go to advising clients. The result: long waitlists, limited caseloads, people who give up waiting.

Hong Kong's legal aid system is already under strain — the Duty Lawyer Service handles over 90,000 cases annually, and the Free Legal Advice Scheme operates through volunteer lawyers at evening centres. Law school clinics provide critical supplementary capacity.

This plugin cuts the time cost of everything *around* the lawyering, so the same students and professor serve meaningfully more clients — and students spend more time on the analysis and strategy that make clinical education worthwhile.

**It accelerates the non-educational parts. It preserves the analytical work.** That's the design principle.

## Who uses it

| Role | Runs | Gets |
|---|---|---|
| **Supervising professor / solicitor** | `/cold-start-interview` (once), `/supervisor-review-queue` (if formal review enabled) | Clinic context configured, student work reviewed |
| **Students** | `/ramp` (start of semester), then `/client-intake`, `/draft`, `/memo`, `/research-start`, `/status`, `/client-letter` | Starting points — never final work product |

## Commands

| Command | What it does | What it doesn't do |
|---|---|---|
| `/cold-start-interview` | **Professor.** One-time clinic config: practice areas, jurisdiction (Hong Kong), supervision style, handbook/rules upload | — |
| `/build-guide` | **Professor.** Author a per-practice-area guide: intake questions, pedagogy posture (assist / guide / teach), review gates, cross-plugin checks | Doesn't replace `/cold-start-interview` — this tunes skills for one practice area |
| `/ramp` | **Students.** Semester onboarding: clinic procedures, tool walkthrough, practice exercises | Doesn't replace the professor's orientation |
| `/client-intake` | Structured intake: practice-area templates, cross-area issue spotting, conflict flags, triage | Doesn't decide whether to take the case |
| `/draft [doc]` | First draft: submissions, statutory declarations, demand letters, protection orders — court-aware | Doesn't produce final work product |
| `/memo` | IRAC-scaffolded case analysis with research gaps flagged | Doesn't write the analysis — scaffolds it |
| `/research-start [issue]` | Research roadmap: ordinances to check, case law areas, HK legislation search terms | **Leads, not authoritative citations** — students verify everything |
| `/status [audience]` | Case status summary: client-facing, internal, or court-ready | Doesn't file anything |
| `/client-letter [type]` | Routine correspondence: appointment confirms, doc requests, brief updates | Doesn't do substantive advice — that's `/status client` or a conversation |
| `/deadlines` | Track case deadlines — add, cross-case rollup with warnings at 14/7/3/1 days, overdue flags | Doesn't calculate deadlines from triggering events; student does the math per HK Practice Directions |
| `/client-comms-log [case]` | Append-only per-case communication log — calls, emails, letters, in-person | Doesn't store substantive legal analysis; comm record only |
| `/semester-handoff` | End-of-semester offboarding — per-case handoff memos for the next cohort | Doesn't close cases; cases closing at semester end get a final `/status internal` memo and are marked closed in the handoff document |
| `/supervisor-review-queue` | **Professor, if formal review enabled.** What's waiting, approve/edit/return | Optional — one of three supervision models |

## Ethical and confidentiality preconditions

Before using this plugin with real client matters, confirm with your clinic's supervising solicitor and your university's ethics / IT office:

1. **Your Claude account tier and its data retention and training policies.** Team, Enterprise, Work, Education, and individual accounts have different guarantees about retention, training use, and subprocessor handling. Confirm what applies to the clinic's account.
2. **Your client consent and disclosure practices for AI-assisted work** per the Law Society of Hong Kong's "Guidelines on Practice of Law Using Generative Artificial Intelligence" (September 2024), the Hong Kong Bar Association's AI guidance, and the Solicitors' Practice Rules, the Barristers' Code of Conduct, and applicable professional conduct rules. Decide whether and how the clinic discloses AI use to clients; document it.
3. **How privileged and confidential material will be handled** under Hong Kong legal professional privilege — what gets pasted into sessions, where outputs are stored, who has access, how long material is retained, how student turnover affects access. Hong Kong's Personal Data (Privacy) Ordinance (Cap 486) imposes additional obligations on handling personal data.
4. **Whether any of your clinic's practice areas involve heightened confidentiality** (immigration, criminal defence, domestic violence, some family and civil rights matters) that require additional safeguards — and decide whether the plugin is appropriate for those case types at all.

Do not skip this step. The cold-start interview (`/legal-clinic:cold-start-interview`) captures these decisions as Part 0 before any other configuration.

## Confidence markers

Skills across this plugin flag confidence inline so students and supervising attorneys can see where the scaffold is uncertain vs. where it's asserting. Every marker is a prompt to verify — nothing marked is trusted.

- `[AI-ASSISTED DRAFT — requires student analysis and attorney review]` — baseline label applied to every output. Review label, not part of client-facing content; strip before anything goes out.
- `[UNCERTAIN: specific reason]` — the skill is genuinely unsure on this call (minority rule, debatable issue, jurisdiction the skill doesn't know well). Used in memo, intake, status, draft.
- `[VERIFY: claim — check source]` — a claim stated as likely but unverified. Student must confirm before relying — ordinances, Practice Directions, rule statements. Used heavily in research-start, draft, status, memo.
- `[RESEARCH NEEDED: ...]` — memo scaffold marker where a rule statement is a research gap, not a conclusion. The student runs `/research-start` and fills it in.
- `[STUDENT ANALYSIS: ...]` — memo scaffold marker where the application is blank by design. The student's reasoning fills it.
- `[STUDENT CONCLUSION: ...]` — memo scaffold marker where the conclusion is blank by design.
- `[FACT NEEDED: ...]` — draft scaffold marker where a required fact is missing from case notes. Student gets the fact; no guessing.
- `CHECK WITH [PROFESSOR] BEFORE SENDING` / `BEFORE FILING` — supervision-flag label applied in "configurable flags" supervision mode to outputs on flagged topics.

Trust the flags more than the absence of flags. An unflagged statement means the skill is confident — it does not mean the student or attorney skips verification.

## Built-in safeguards

Every output from every skill includes:

- **AI-assisted label** — requires student analysis and attorney review
- **Confidence indicators** — `[UNCERTAIN: ...]` where genuinely unsure, rather than guessing
- **Verification prompts** — specific things to fact-check before relying on output
- **Ethical reminders** calibrated to the task

These are designed to reinforce the clinical education model: the student does the thinking, the plugin does the heavy lifting around it.

**Research outputs specifically:** `/research-start` gives leads and frameworks for the student to verify and develop. It explicitly does **not** provide legal citations as authoritative. This is both an ethical safeguard and a pedagogical feature — students still learn to research and use judgment; they just start from a better place.

## Supervision workflow (configurable)

Whether the plugin includes a formal review workflow — student draft → professor review → approved — is a genuine open question. Some clinics want a hard gate; others find it overly prescriptive for their supervision structure.

The cold-start interview asks the professor to choose:

1. **Formal review queue** — client/court-bound output queues, professor approves, all logged
2. **Configurable flags, informal review** — certain triggers label output "CHECK WITH PROFESSOR," no queue mechanism
3. **Lighter-touch** — standard safeguard labels on everything, professor supervises through existing clinic structure (case rounds, one-on-ones)

Changeable later by editing `~/.claude/plugins/config/claude-for-hk-law/legal-clinic/CLAUDE.md`. Your configuration is stored at that version-independent path and survives plugin updates.

## Semester turnover: the `/ramp` solution

Every semester, clinics rebuild from scratch. New students need weeks to learn procedures, tools, practice-area basics. `/ramp` is the interactive onboarding — it reads the clinic handbook the professor uploaded at setup and teaches it, with low-stakes practice exercises (fake intake, practice draft, research roadmap) before the student touches a real case.

`/ramp --card` generates the one-page student reference card: commands, what Claude can and can't help with, verification habits. Hand it out on day one.

## Ethical framework: Law Society of Hong Kong Guidelines on AI (2024)

The ethical framework this plugin operates within. The Law Society of Hong Kong's "Guidelines on Practice of Law Using Generative Artificial Intelligence" (September 2024) and the Hong Kong Bar Association's related guidance establish that lawyers using generative AI must ensure: (1) competence in the technology (including understanding its limitations), (2) confidentiality of client information, (3) supervision and verification of AI outputs, (4) compliance with professional conduct rules (Solicitors' Practice Rules, Barristers' Code of Conduct), and (5) appropriate client communication about AI use where relevant.

The safeguards above — labels, confidence indicators, verification prompts, the explicit non-authority of research outputs — are built for this model.

## Skills

| Skill | Purpose |
|---|---|
| **cold-start-interview** | Professor's one-time setup — practice areas, jurisdiction (Hong Kong), supervision style, seed docs |
| **build-guide** | Professor's per-practice-area guide — intake, pedagogy posture (assist/guide/teach), review gates, cross-plugin checks |
| **ramp** | Student semester onboarding — procedures, tools, practice exercises |
| **client-intake** | Practice-area-specific intake with cross-area issue spotting, conflict flags, triage |
| **draft** | First-draft generation — practice-area templates, court-aware, explicitly starting point |
| **memo** | IRAC scaffolding with research gaps flagged — the analysis is the student's |
| **research-start** | Research roadmap — leads not authorities, students verify and develop |
| **status** | Audience-aware case summaries — client / internal / court |
| **client-letter** | Routine correspondence from templates |
| **supervisor-review-queue** | Optional formal review workflow — only active if professor chose it |
| **deadlines** | Per-case deadline tracking, cross-case rollup, warning cadence, overdue flags |
| **client-comms-log** | Append-only per-case communication record — calls, emails, letters, in-person |
| **semester-handoff** | End-of-semester offboarding memos; mirror of `/ramp` |

*(Two deprecated skills — `form-generation`, `plain-language-letters` — redirect to `/draft` and `/client-letter` + `/status client` respectively.)*

## Connectors and citation verification

**Connect a research tool first — the citation guardrails depend on it.** Without one, every cite is tagged `[verify]` and the reviewer note above each deliverable records that sources weren't verified. The plugin works either way; it just does more of the verification for you when a research tool is connected.

The legal research connectors in this plugin aren't just data sources — they're the difference between a verified citation and a citation you have to check. A citation retrieved through **HKLII** (Hong Kong Legal Information Institute — free access to HK judgments and legislation) or **Westlaw Asia** / **LexisNexis HK** is tagged with its source and can be traced back. A citation from the model's knowledge or from web search is tagged `[verify]` and should be checked against a primary source (HK e-Legislation, the Judiciary's website) before anyone relies on it. The plugin tiers its citations so your verification time goes where it matters.

**Hong Kong-specific research tools:**
- **HK e-Legislation** (https://www.elegislation.gov.hk) — official legislation database
- **HKLII** (https://www.hklii.hk) — free judgments and legislation
- **Judiciary website** (https://www.judiciary.hk) — Practice Directions, court lists
- **CLIC** (https://www.clic.org.hk) — Community Legal Information Centre
- **Law Reform Commission** (https://www.hkreform.gov.hk) — reports and recommendations

## Integrations (open questions)

Ships with the general bucket of connectors in `.mcp.json`:

- **Slack** — search messages, read channels, find discussions
- **Google Drive** — search, read, and fetch documents

Case management integration (Clio, PracticePanther, or HK-specific systems) is noted as an optional future integration. Starting with file upload.

Account tier (Team vs. Enterprise) for client confidentiality is an open question for each clinic's IT and ethics review.

## How it learns

Your practice profile at `~/.claude/plugins/config/claude-for-hk-law/legal-clinic/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. You can re-run setup, edit the file directly, or tell a skill to record a new position.

## File structure

```
legal-clinic/
├── .claude-plugin/plugin.json
├── .mcp.json
├── CLAUDE.md                          # Professor's clinic config — written by cold-start
├── README.md
├── deadlines.yaml                     # operational deadline ledger
├── skills/                            # each skill is also the slash command /legal-clinic:<skill>
│   ├── cold-start-interview/          # Professor — one-time setup
│   ├── build-guide/                   # Professor — per-practice-area guide
│   ├── ramp/                          # Students — semester onboarding
│   ├── client-intake/
│   │   └── references/intake-templates/
│   ├── draft/
│   ├── memo/
│   ├── research-start/
│   ├── status/
│   ├── client-letter/
│   ├── supervisor-review-queue/       # Professor, if formal review enabled
│   │   └── references/review-queue.yaml
│   ├── deadlines/
│   ├── client-comms-log/
│   ├── semester-handoff/
│   ├── form-generation/               # deprecated → /draft (reference-only)
│   └── plain-language-letters/        # deprecated → /client-letter, /status client (reference-only)
├── handoffs/                          # per-semester handoff memos
│   └── [YYYY-term]/
│       ├── _summary.md
│       └── [case-id].md
├── client-comms/                      # per-case communication logs
│   └── [case-id]/
│       └── log.md
└── hooks/hooks.json
```

## Prerequisites

Some features reference external integrations (document management, legal research tools, case management). These are not bundled — if you have an MCP server for one of these in your environment, the relevant features will use it. Without one, the plugin falls back to file upload and manual workflows. Run `/legal-clinic:cold-start-interview --check-integrations` to see what's available in your environment.
