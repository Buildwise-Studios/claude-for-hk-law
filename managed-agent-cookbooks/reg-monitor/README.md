# Reg Monitor — managed-agent template (HK Law Edition)

## Overview

Checks Hong Kong regulatory feeds on a schedule, filters by the deploying
team's materiality threshold, runs a quick gap check against the policy
library for always-material items, and writes a digest.

**Hong Kong regulatory landscape (not US Federal Register).** The agent
monitors:

- **Hong Kong Gazette (憲報)** — official government publication; subsidiary
  legislation, ordinances, appointment notices
  
  Primary URL: `https://www.gld.gov.hk/egazette/`

- **Securities and Futures Commission (SFC)** — circulars, consultation
  papers, guidelines, codes and guidelines updates, enforcement news
  
  Primary URL: `https://www.sfc.hk/`

- **Hong Kong Monetary Authority (HKMA)** — banking supervision policy
  circulars, guideline updates, AML/CFT notices, payment systems
  
  Primary URL: `https://www.hkma.gov.hk/`

- **Insurance Authority (IA)** — guideline updates, rule amendments,
  authorization conditions, AML/CFT circulars
  
  Primary URL: `https://www.ia.org.hk/`

- **Legislative Council (LegCo)** — Bills, subsidiary legislation tabling,
  Panel discussions on regulatory proposals
  
  Primary URL: `https://www.legco.gov.hk/`

- **Companies Registry** — changes to the Companies Ordinance (Cap. 622)
  regulations, administrative guidelines
  
  Primary URL: `https://www.cr.gov.hk/`

- **Other HK regulators** — Competition Commission, Mandatory Provident Fund
  Schemes Authority (MPFA), Office of the Privacy Commissioner for Personal
  Data (PCPD), Customs & Excise Department, etc.

Same source as the [`reg-change-monitor`](../../regulatory-legal/agents/reg-change-monitor.md)
Claude Code agent and the [`reg-feed-watcher`](../../regulatory-legal/skills/reg-feed-watcher)
/ [`policy-diff`](../../regulatory-legal/skills/policy-diff) skills — this
directory is the Managed Agent cookbook for `POST /v1/agents`.

## ⚠️ Before you deploy

- **Digest items are screened leads, not legal conclusions.** The materiality
  filter applies a configurable threshold, not legal judgment. A regulatory
  change the agent classifies as "informational" may still be material to your
  business. A change it flags as "material" may turn out not to apply. Review
  every digest; a licensed attorney decides whether an item requires action,
  disclosure, policy change, or escalation.
- **The policy gap check is a first pass, not a legal assessment of
  applicability.** The gap surface compares new regulatory text against your
  policy library using heuristics. A "gap" is a lead for a lawyer to evaluate;
  an "aligned" result does not certify compliance.
- **The materiality threshold is your calibration, not law.** If your
  `## Materiality threshold` section is stale or was tuned for a different
  risk posture, the triage is stale. Recheck before enabling scheduled runs.
- **The watchlist is a coverage assertion you made.** A regulator not on the
  watchlist may still publish something material. Missing a regulator is a
  configuration bug, not a feed bug.
- **HK-specific note:** Unlike the US Federal Register, HK Gazette publications
  can be in English, Chinese, or both. The agent handles both language feeds
  where available. Some HK regulators (e.g., PCPD, Competition Commission)
  publish less frequently but their publications carry significant compliance
  implications.

## Deploy

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export GDRIVE_MCP_URL=...   # For policy library and materiality configuration
../../scripts/deploy-managed-agent.sh reg-monitor
```

## Steering events

See [`steering-examples.json`](./steering-examples.json). The default weekly
sweep uses the first example. The other two cover targeted deep checks on a
specific HK regulatory development and gap analysis on a flagged item.

## Security & handoffs

Regulatory feed content (Gazette entries, HK regulator RSS/API posts, paid
feed alerts) is **untrusted input.** Three-tier isolation:

| Tier | Touches untrusted docs? | Tools | Connectors |
|---|---|---|---|
| **`feed-reader`** | **Yes** | `Read`, `Grep`, `WebFetch` only | None |
| `materiality-filter` / Orchestrator | No | `Read`, `Grep`, `Glob`, `Agent` | gdrive (orchestrator only) |
| **`digest-writer`** (Write-holder) | No | `Read`, `Write`, `Edit` | None |

`feed-reader` returns length-capped, schema-validated JSON. `materiality-filter`
is pure computation over that JSON plus the regulatory-legal configuration on
disk — no MCP, no web. `digest-writer` produces `./out/reg-digest-<YYYY-MM-DD>.md`
and emits a `handoff_request` for Slack delivery.

**Handoffs:** the orchestrator routes the `handoff_request` from `digest-writer`
to a Slack send worker using the channel from the deploying team's House style
configuration. The agent never sends Slack messages itself.

**Not guaranteed:** this agent surfaces changes and flags potential policy gaps;
a lawyer decides whether a regulatory change requires action and who owns the
response.

## Adaptation notes (HK)

Before you trust the output on your workflow:

- **Point `feed-reader` at your HK sources.** The default target has been
  changed from the US Federal Register to the HK Gazette and primary HK
  regulators. The feed-reader's `allowed_hosts` configuration in
  `subagents/feed-reader.yaml` has been pre-configured for HK domains.
  If your firm subscribes to a paid regulatory feed (e.g., Westlaw Asia,
  Bloomberg Law with HK coverage), add those endpoints to the allowlist.
- **Configure the digest delivery channel.** The digest-writer emits a
  `handoff_request` that names a Slack channel. The orchestrator reads that
  channel from your regulatory-legal configuration's **House style → Reg
  digest** field. Set it before the first scheduled run or the handoff will
  dead-letter. Teams that want the digest by email or in a Confluence page
  instead should swap the handoff target in the orchestrator allowlist.
- **Tune the materiality threshold.** The materiality-filter reads your
  configuration's `## Materiality threshold` section — always material /
  review-worthy / FYI. Confirm the tiers reflect your current HK risk posture
  before enabling scheduled runs. HK securities and banking regulations
  typically have shorter implementation timelines than comparable US rules.
- **Update the watchlist.** The materiality-filter also reads the
  `## Regulators we watch` table. Add or remove HK regulators as your
  footprint changes. Key additions: SFC, HKMA, IA, PCPD, Competition
  Commission, MPFA, Companies Registry, Customs & Excise, Land Registry.
- **Confirm the work-product header.** The headless append in `agent.yaml`
  instructs the agent to prepend your configuration's work-product header.
  Verify the header language with your GC before turning this on.
  **HK note:** Legal professional privilege in HK is governed by common law.
- **Cadence.** Weekly is the default. Active regulatory environments
  (financial services rulemaking cycles in HK, SFC consultation paper
  response periods) may warrant daily. The cadence lives in your own workflow
  engine — the cookbook does not schedule itself.
- **Language considerations.** HK Gazette publishes in both English and
  Chinese. If your policy library is English-only, flagged items may need
  translation review. Consider adding a `language` field to the feed-reader
  output schema during deployment.
