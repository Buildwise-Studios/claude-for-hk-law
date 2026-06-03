---
name: trial-procedure
description: >
  Guide legal practitioners through the trial procedure for NSL offences in Hong Kong courts, covering the designated judge system (Art 44), judge-only trials (Art 46), evidence and disclosure, and appeals.
---
# Trial Procedure — Skill

## Purpose

Guide legal practitioners through the trial procedure for NSL offences in Hong Kong courts, covering the designated judge system (Art 44), judge-only trials (Art 46), evidence and disclosure, and appeals.

## Scope

- Designated judge appointment and panel composition (Art 44)
- Judge-only trial procedure (Art 46) — no jury, reasoned judgments
- The Art 47 certificate procedure (SJ certificate binding on the court)
- Evidence and disclosure in NSL trials (closed hearings, PII)
- Trial management and case progression
- Sentencing procedure
- Appeal routes

## Workflow

### 1. Pre-Trial

**Jurisdictional assessment**:
- Confirm the case falls under Art 41 (HK court jurisdiction)
- Identify if there is any Art 55 risk (Central Government assumption of jurisdiction)
- Monitor SJ announcements or indications

**Designated judge assignment**:
- The case is assigned to a panel of designated judges (one or three) under Art 44
- Designated judges are appointed by the CE from the existing judiciary
- No jury will sit for the trial (Art 46)
- Counsel should consider whether to challenge the composition of the panel (rare; grounds limited)

**Case management**:
- Pre-trial review hearings (disclosure, timelines, preliminary issues)
- Applications for case management directions
- Consider applications for closed hearings or special measures for sensitive evidence
- Bail applications (Art 42 — see bail-assessment skill)

**Art 47 certificate**:
- If a question arises about whether an act involves national security, the SJ issues a certificate
- The certificate is conclusive and binding on the court (Tam Sze Leung v SJ)
- Counsel should anticipate whether the SJ may certify a national security question
- The certificate cannot be challenged on its merits, but its scope can be argued

### 2. Trial (Judge-Only)

**Trial structure**:
- The panel of designated judges (single judge or three-judge panel) presides
- No jury empanelment or jury selection
- Opening statements
- Prosecution case (witness examination, documentary evidence)
- Defence case (including right to silence)
- Closing submissions
- Judgment (written, with reasons)

**Key procedural features**:
- No jury — counsel address the bench directly
- Judges deliver a reasoned verdict (guilty/not guilty) in writing
- The panel must provide reasons for its decision
- The judgment addresses findings of fact and law
- No need for jury directions

**Evidence and disclosure**:
- Standard HK rules of evidence apply (but modified by NSL provisions)
- Closed hearings may be ordered where national security is prejudiced (Art 48)
- Public interest immunity (PII) applications for sensitive evidence
- Restrictions on disclosure to the defence where national security engaged
- The court may receive evidence in camera
- Special advocates may be appointed for national security evidence

**Art 47 certificate at trial**:
- If the SJ issues a certificate during trial, it is binding on the panel
- The panel cannot independently determine the national security character of the act
- The certificate does not determine guilt or innocence — only the national security character

### 3. Judgment and Sentencing

**Judgment**:
- Written reasons must be provided for the verdict
- The judgment should address:
  - Findings of fact
  - Application of the law
  - Evaluation of evidence
  - The Art 47 certificate (if issued)
  - The basis for the verdict

**Sentencing**:
- Range by offence: life imprisonment (principals), 10+ years, 3–10 years, up to 3 years
- Factors (per HKSAR v Ma Chun Wai 2023):
  - Aggravating: leadership role, planning, cross-border elements, foreign collusion
  - Mitigating: cooperation, early guilty plea, limited role, voluntary disclosure
- Disqualification from office (up to 5 years post-sentence, Art 49)
- Forfeiture of property connected to NSL offences

### 4. Appeals

**Routes**:
- CA: Appeal from CFI as of right or with leave
- CFA: Appeal from CA with leave (or certificate from CA)
- SJ appeal against sentence as of right
- No HK appellate jurisdiction where Art 55 jurisdiction is invoked

**Grounds for appeal**:
- Error of law
- Verdict unsafe or unsatisfactory
- Material irregularity in proceedings
- Sentence manifestly excessive or wrong in principle

### 5. Post-Trial

- Enforcement of sentence (prison, disqualification, forfeiture)
- Periodic review of sentence (where available)
- Post-conviction bail pending appeal (Art 42 test applies)

## Key Precedents

- **HKSAR v Lai Chee Ying (2021)** — Art 46 constitutionality, judge-only trial, no jury
- **Tam Sze Leung v Secretary for Justice (2022)** — Art 47 certificate procedure, procedural fairness
- **HKSAR v Ma Chun Wai (2023)** — Sentencing guidelines for NSL offences

## Practical Checklist

- [ ] Confirm jurisdiction (Art 41 v Art 55)
- [ ] Identify designated judge panel
- [ ] Assess Art 47 certificate risk
- [ ] Prepare for no-jury trial — adjust advocacy for bench trial
- [ ] Plan for closed hearings / PII applications
- [ ] Prepare written submissions tailored to reasoned judgment
- [ ] Anticipate sentencing factors
- [ ] Preserve appeal grounds


## Scripts

Use these scripts to fetch live data:

```bash
# Search legislation index by keyword
python3 scripts/download_legislation_list.py --search "keyword"

# Download full ordinance text
python3 scripts/download_legislation_text.py <cap_no>
```
