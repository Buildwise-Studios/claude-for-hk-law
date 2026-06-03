---
name: offence-classifier
description: >
  Classify conduct under the four Hong Kong National Security Law (NSL) offences: secession (Art 20), subversion (Art 22), terrorism (Art 24), and collusion with foreign or external forces (Art 29).
---
# Offence Classifier — Skill

## Purpose

Classify conduct under the four Hong Kong National Security Law (NSL) offences: secession (Art 20), subversion (Art 22), terrorism (Art 24), and collusion with foreign or external forces (Art 29).

## Scope

- Distinguishing between the four NSL offence categories
- Actus reus and mens rea requirements for each offence
- Sentencing exposure by offence and role (principal, active participant, other participant)
- Overlapping HK offences and charging alternatives
- Conspiracy, attempt, and incitement under Art 31

## Workflow

### 1. Gather Facts

Identify:
- Who: The person(s) involved (HK permanent resident? Organisation? Public officer?)
- What: The specific acts, statements, or conduct
- When: Timing — pre/post 30 June 2020 (NSL commencement)
- Where: Location — within HK, outside HK (extraterritorial under Art 65)
- Why: Purpose, intention, or knowledge of the conduct
- Foreign connections: Any link to foreign governments, organisations, or individuals

### 2. Assess Secession (Art 20)

**Check for**:
- Organising, planning, or committing acts to secede from the PRC
- Causing the severance of any part of the PRC
- Participating in an unlawful assembly or organisation with secessionist intent
- Using force or threat of force to challenge PRC sovereignty in HK

**Mens rea**: Intention to commit secession

**Penalty**:
- Principal: Life imprisonment or 10+ years
- Active participant: 3–10 years
- Other participant: Up to 3 years / detention

### 3. Assess Subversion (Art 22)

**Check for**:
- Overthrowing or undermining the state's political system
- Attacking or destroying state organs
- Serious interference with lawful state organ functions
- Inciting military/Police mutiny or refusal of orders
- Serious disruption of LegCo, courts, or state organ operations

**Mens rea**: Intention to subvert state power

**Penalty**: Same structure as secession

### 4. Assess Terrorism (Arts 24–28)

**Check for**:
- Assassination, explosions, arson, chemical/biological attacks
- Destruction of transportation, infrastructure, public places
- Hijacking aircraft, ships, or vehicles
- Serious violence against persons or property
- Threats to commit any of the above
- Organising/participating in terrorist organisations (Art 27)
- Provision of financial/material support to terrorist groups (Art 28)

**Mens rea**: Intention to seriously endanger national security

### 5. Assess Collusion with Foreign Forces (Art 29)

**Check for**:
- Engaging in acts endangering national security at the request of foreign forces
- Trespassing/damaging property at the direction of foreign forces
- Intimidating/coercing HK officials with foreign force support
- Inciting military/Police mutiny with foreign instigation
- Requesting foreign interference in HK affairs (sanctions, investigations)
- Requesting any foreign review of HK affairs

**"Foreign or external forces"** (Art 30): Foreign governments, organisations, institutions, individuals, or their agencies

**Mens rea**: Intention to endanger national security through collusion

### 6. Consider Overlapping HK Offences

- Treason (Cap 200) — overlaps with secession and collusion
- Sedition (Cap 200) — overlaps with secession
- Offences Against the Person Ordinance (Cap 212) — overlaps with terrorism
- Dangerous Goods Ordinance (Cap 295) — overlaps with terrorism

**Practice note**: The SJ may choose to charge under either NSL or the equivalent HK offence; the choice has significant procedural implications for the accused.

### 7. Assess Inchoate Liability (Art 31)

- Conspiracy to commit an NSL offence
- Attempt to commit an NSL offence
- Incitement to commit an NSL offence

### 8. Report

Provide a structured classification including:
- Most likely NSL offence(s)
- Level of participation (principal / active / other)
- Sentencing exposure range
- Overlapping HK offences (if any)
- Key evidence considerations
- Recommendation for further investigation or disclosure


## Scripts

Use these scripts to fetch live data:

```bash
# Search legislation index by keyword
python3 scripts/download_legislation_list.py --search "keyword"

# Download full ordinance text
python3 scripts/download_legislation_text.py <cap_no>
```
