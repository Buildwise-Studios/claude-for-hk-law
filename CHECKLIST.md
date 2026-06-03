# ✅ Checklist — Claude for HK Law

**Subagents:** When you complete a task, append your results to the bottom of your `task` with `[DONE]` and update this file by editing it. Stick to the format below.

---

## Phase 1 — Foundation

- [x] **A1** — `CLAUDE.md` + `QUICKSTART.md` rewritten for HK
- [x] **A2** — `README.md` + `CONNECTORS.md` rewritten for HK
- [x] **A3** — `marketplace.json` updated, `CONTRIBUTING.md` tweaked

## Phase 1b — Reference Docs

- [x] **B1** — `references/hk-legal-system-overview.md` + `references/hk-citation-style.md`
- [x] **B2** — `references/key-hk-ordinances-index.md` + `references/hk-court-structure.md`
- [x] **B3** — `references/company-profile-template.md` (HK-adapted) + `references/dashboard-template.md`

## Phase 2 — Core Plugin Adaptation

### C1 — commercial-legal + privacy-legal
- [x] `commercial-legal/` — plugin.json, CLAUDE.md, skills, agents adapted for HK
- [x] `privacy-legal/` — plugin.json, CLAUDE.md, skills, agents adapted for HK

### C2 — product-legal + corporate-legal
- [x] `product-legal/` — adapted for HK
- [x] `corporate-legal/` — adapted for HK

### C3 — employment-legal + litigation-legal
- [x] `employment-legal/` — adapted for HK
- [x] `litigation-legal/` — adapted for HK

### C4 — regulatory-legal + ip-legal
- [x] `regulatory-legal/` — adapted for HK
- [x] `ip-legal/` — adapted for HK

### C5 — ai-governance-legal + law-student
- [x] `ai-governance-legal/` — adapted for HK
- [x] `law-student/` — adapted for HK

### C6 — legal-clinic + legal-builder-hub
- [x] `legal-clinic/` — adapted for HK
- [x] `legal-builder-hub/` — adapted for HK

## Phase 3 — HK-Native Plugins

- [x] **D1** — `hk-basic-law` + `hk-companies`
- [x] **D2** — `hk-employment` + `hk-litigation-procedure`
- [x] **D3** — `hk-property` + `hk-data-privacy`
- [x] **D4** — `hk-intellectual-property` + `hk-arbitration`
- [x] **D5** — `hk-commercial-law` + `hk-competition`
  - [x] Plugin files moved to `.claude-plugin/` (fix applied)
- [x] **D6** — `hk-immigration` + `hk-shipping-maritime`
- [x] **D7** — `hk-family-law` + `hk-trusts-estate`
- [x] **D8** — `hk-nsl-rules`

## Review Queue

- [ ] Alex review — Phase 1
- [ ] Alex review — Phase 2
- [ ] Alex review — Phase 3
- [ ] Alex fix round — any issues spun as new subagents

## Phase 4a — Managed Agent Cookbooks (E1 ✅)

- [x] **E1** — `managed-agent-cookbooks/` adapted for HK:
  - `renewal-watcher/` — HK contract notice periods (common law, no statutory defaults), HKD thresholds
  - `docket-watcher/` — HK Judiciary system, no public docket API, RHC/RDC/CFA Rules replacing FRCP/FRAP
  - `reg-monitor/` — HK Gazette, SFC/HKMA/IA/LegCo/CR feeds replacing US Federal Register
  - `launch-radar/` — HK licensing (SFC, HKMA, IA, Customs, PCPD, Competition) replacing US regulatory approvals
  - `diligence-grid/` — HK Cap 622, Cap 571, Cap 57, Cap 486, Cap 112, Cap 619 diligence
