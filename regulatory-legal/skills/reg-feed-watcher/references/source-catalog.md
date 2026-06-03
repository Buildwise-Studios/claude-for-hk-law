# Hong Kong Regulatory Source Catalog

A starting catalog for the reg-feed-watcher. The cold-start interview configures
which sources to watch; this catalog provides the options. URLs verified as of
**June 2026** — feed URLs change; verify if a source stops returning results.

**How to read this catalog:**
- **Format** — what the feed returns: HTML page (needs browsing/scraping or change detection), Email (requires IMAP/Gmail/Outlook MCP), RSS (semi-structured, good).
- **Tier** — *Primary* means the regulator itself; *Secondary* means a commentator, aggregator, or law firm summarizing primary sources. Always trace a secondary source back to the primary before treating it as authoritative.
- **Auth** — None means open; Key means a free-but-registered API key; Paid means a subscription.
- **Notes** — any gotchas, discovery steps, or update cadence.

Sources flagged ⚠️ have been reported by users or regulators as unreliable or
discontinued — verify before configuring.

---

## Hong Kong — Primary Regulatory Sources

| Source | URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| SFC — Regulatory News | `https://www.sfc.hk/edistributionWeb/gateway/EN/news-and-announcements` | HTML | Circulars, guidelines, consultation papers, press releases, enforcement actions, policy statements | None | SFC publishes structured circulars by category. Check sub-pages for: intermediaries, asset management, corporate finance, investment products, enforcement. Email alert sign-up available. |
| SFC — Enforcement News | `https://www.sfc.hk/edistributionWeb/gateway/EN/news-and-announcements/news/enforcement-news` | HTML | Disciplinary actions, court actions, warnings, investigation outcomes | None | High-signal feed for sector-specific enforcement patterns. |
| SFC — Takeovers & Mergers Panel | `https://www.sfc.hk/edistributionWeb/gateway/EN/news-and-announcements/news/takeovers-and-mergers-panel` | HTML | M&A-related rulings and decisions | None | Important for corporate/regulatory practitioners. |
| HKMA — Press Releases | `https://www.hkma.gov.hk/eng/news-and-media/press-releases/` | HTML + email | Policy announcements, banking regulations, supervisory letters, statistical releases | None | Email newsletter sign-up available. Key sections: Banking policy, Deposit Protection, AML/CFT, Fintech. |
| HKMA — Guidelines & Circulars | `https://www.hkma.gov.hk/eng/key-functions/banking/banking-regulatory-and-supervisory-regime/banking-legislation/guidelines-and-circulars/` | HTML | All HKMA guidelines, supervisory policy manuals, and circulars to AIs | None | Structured by topic. Includes the Supervisory Policy Manual (SPM) — definitive source for HKMA expectations. |
| HKMA — AML/CFT Notices | `https://www.hkma.gov.hk/eng/key-functions/banking/aml-cft/` | HTML | AML/CFT guidelines, notices, and FATCA/CRS guidance | None | Key for AML compliance teams. Cross-reference with SFC AML notices. |
| IA — News & Notices | `https://www.ia.org.hk/en/infocenter/news_and_notices.html` | HTML | Guidelines, enforcement, industry notices, consultation papers | None | IA publishes guidelines for insurers, brokers, and agents. Important for insurance regulatory compliance. |
| IA — Guidelines & Legislation | `https://www.ia.org.hk/en/infocenter/guidelines_legislation.html` | HTML | Insurance Ordinance (Cap 41) guidelines, codes of conduct | None | |
| Competition Commission — News | `https://www.compcomm.hk/en/media/press_releases.html` | HTML + email | Press releases, merger decisions, enforcement actions, advisory bulletins | None | Email sign-up available. Key for Competition Ordinance (Cap 619) compliance. |
| Competition Commission — Resources | `https://www.compcomm.hk/en/legal_resources/decisions_and_guidance.html` | HTML | Merger decision summaries, leniency policy, prosecution guidance | None | Essential for anyone advising on HK competition law. |
| Hong Kong Government Gazette | `https://www.gld.gov.hk/egazette/` | RSS + HTML | Legal notices, subsidiary legislation enactment, bill gazettals, statutory orders | None | RSS feed available. The Gazette is the official legal publication for HK. Critical for tracking: new legislation, amendment commencement dates, subsidiary legislation. |
| LegCo — Bills Database | `https://www.legco.gov.hk/en/bills.html` or `https://www.legco.gov.hk/yr[YY]-[YY]/english/bills/brief/[bill]_brief.pdf` | HTML | Bills gazetted, committee stage amendments, enacted legislation | None | Browse by legislative year. Patterns: bills.gazetted → committee stage → passed → gazetted as law. Track committee papers and Bills Committee reports for policy nuance. |
| LegCo — Agenda & Minutes | `https://www.legco.gov.hk/en/meeting/` | HTML | Council meeting agendas, minutes, written questions | None | Useful for forecasting regulatory direction from member questions and government replies. |
| Department of Justice (DoJ) — Press Releases | `https://www.doj.gov.hk/en/community_engagement/press.html` | HTML | Prosecution decisions, law reform announcements, key legislative developments | None | Limited regulatory feed but useful for criminal enforcement (Customs, IP, corruption). |
| Privacy Commissioner for Personal Data (PCPD) | `https://www.pcpd.org.hk/english/news_events/` | HTML | Guidance, enforcement, consultation, Annual Reports | None | HK PDPO enforcement, data breach notifications, cross-border data transfer guidance. |
| Census & Statistics Department | `https://www.censtatd.gov.hk/en/eindex.html` | HTML | Economic indicators, trade statistics, price indices | None | Background data for materiality assessments on economic impact of regulatory changes. |

---

## Hong Kong — Court & Tribunal Decisions

| Source | URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| HKLII (HK Legal Information Institute) | `https://www.hklii.hk` | HTML | CFI, CA, CFA judgments; Competition Tribunal; Market Misconduct Tribunal | None | Free. Comprehensive. Search by court, date, topic. Essential for HK case law research. |
| Judiciary — Court Judgments | `https://www.judiciary.hk/en/judgments/index.html` | HTML | All HK court judgments from the official source | None | Official source. HKLII mirrors with added searchability. |
| Market Misconduct Tribunal | `https://www.mmt.gov.hk` | HTML | MMT decisions and reasons | None | Important for securities regulatory enforcement (insider dealing, market manipulation). Combined with SFC enforcement decisions. |

---

## EU / UK — Primary

| Source | URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| EDPB News | `https://www.edpb.europa.eu/news/news_en` | RSS (2 feeds offered) | Guidelines, opinions, enforcement summaries, binding decisions | None | Feeds advertised at edpb.europa.eu. |
| European Commission Press Corner | `https://ec.europa.eu/commission/presscorner/` | RSS + email | Press releases, speeches, Q&As | None | |
| ICO (UK) | `https://ico.org.uk/global/rss-feeds/` | RSS (multiple feeds) | Enforcement, guidance, news, consultations | None | |
| FCA (UK) | `https://www.fca.org.uk/news/rss.xml` (verify) | RSS + email | UK financial services rules, enforcement, warnings | None | |

---

## International

| Source | URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| OECD AI Policy Observatory | `https://oecd.ai/en/` | HTML + newsletter | National AI policies, OECD guidance | None | |
| EU AI Act Resources | `https://artificialintelligenceact.eu/` | HTML | EU AI Act timeline, delegated acts | None | |

---

## Secondary / Aggregators (HK-focused)

**Treat content from these sources as leads, not authority.** A secondary
source saying "the SFC issued X" means: find X on sfc.hk, then rely on it.
Tag items pulled from these feeds as `[secondary source]` in the digest.

| Source | URL | Format | Covers | Auth | Notes |
|---|---|---|---|---|---|
| Hong Kong Lawyer | `https://www.hk-lawyer.org/` | HTML | HK legal developments, regulatory analysis | None | |
| Norton Rose Fulbright — HK Regulatory | `https://www.nortonrosefulbright.com/en-hk/knowledge` | HTML | HK regulatory updates, SFC/HKMA/IA alerts | None | |
| Hogan Lovells — HK Regulatory | `https://www.hoganlovells.com/en/knowledge` | HTML | HK and cross-border regulatory, financial services | None | Per-practice blog alerts available. |
| Freshfields — HK | `https://www.freshfields.com/en-hk/` | HTML | HK regulatory, M&A, competition | None | |
| Allen & Overy — HK | `https://www.allenovery.com/en-gb/global/knowledge` | HTML | HK corporate, regulatory, dispute resolution | None | |
| Linklaters — HK | `https://www.linklaters.com/en/knowledge` | HTML | HK capital markets, regulatory, fintech | None | |
| Clifford Chance — HK | `https://www.cliffordchance.com/knowledge.html` | HTML | HK regulatory, banking, competition | None | |
| IAPP Daily Dashboard | `https://iapp.org/rss/daily-dashboard/` | RSS | Global privacy + AI governance news, curated | None (some items paywalled) | Highest signal-to-noise for privacy teams. |
| Law Society of Hong Kong | `https://www.hklawsoc.org.hk/en/news/` | HTML | Practice directions, regulatory updates for legal profession | None | Covers HK solicitor regulation updates. |

---

## Sources without feeds (need web monitoring or email)

| Source | URL | Notes |
|---|---|---|
| SFC circulars by email | `https://www.sfc.hk/en/News/Your-SFC-Email-Alerts` | Primary channel for SFC circulars — register for email alerts |
| HKMA e-newsletter | `https://www.hkma.gov.hk/eng/news-and-media/enews/` | Primary push channel for HKMA publications |
| IA email alerts | `https://www.ia.org.hk/en/forms/enquiry.html` | Register for IA circular email alerts |
| Competition Commission email | `https://www.compcomm.hk/en/media/email_alerts.html` | Register for competition enforcement alerts |
| LegCo webcast archive | `https://www.legco.gov.hk/en/webcast/` | Watch council and committee meetings |

---

## Suggested starter packs

**HK financial services / securities (in-house or firm):**
SFC Regulatory News, SFC Enforcement, SFC Takeovers, HKMA Press Releases, HKMA Guidelines, Gazette, LegCo Bills, HKLII, Competition Commission.

**HK banking and AML (in-house or firm):**
HKMA Press Releases, HKMA Guidelines & Circulars, HKMA AML Notices, SFC AML notices, PCPD, Gazette, LegCo Bills, HKLII.

**HK general corporate / regulatory:**
SFC Regulatory News, HKMA Press Releases, Competition Commission News, Gazette, LegCo Bills, PCPD, HKLII.

---

## Adding a source

To add a source that isn't in this catalog:
1. Check the HK regulator's website for a "News" or "Publications" section.
2. Look for RSS, email subscription, or a structured archive.
3. Add to the user's regulatory-legal CLAUDE.md under **Feed configuration → Direct regulator feeds**, with: source name, URL, format, what it covers.
4. If no feed exists, add it under **Sources without feeds** and decide: manual, email MCP subscription, or change detection.
