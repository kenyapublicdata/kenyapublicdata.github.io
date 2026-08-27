---
title: Kenya in Data Source Registry
project: Kenya in Data
document_type: source-registry
status: active
created: 2026-08-27
last_updated: 2026-08-27
tags: [sources, provenance, official-data, data-registry]
---

# Official Source Registry

This registry tracks the official Kenyan primary data providers, canonical URLs, publication schedules, and reliability notes.

| Institution | Abbr | Canonical Data Topics | Publication URL / Portal | Release Cadence |
| :--- | :--- | :--- | :--- | :--- |
| **Central Bank of Kenya** | CBK | Exchange Rates, Inflation, Public Debt Bulletins, Diaspora Remittances, Interest Rates | [centralbank.go.ke/statistics](https://www.centralbank.go.ke/statistics/) | Weekly / Monthly / Annual |
| **Kenya National Bureau of Statistics** | KNBS | CPI & Inflation Reports, GDP quarterly reports, Economic Survey, Census, Labor Force | [knbs.or.ke](https://www.knbs.or.ke/) | Monthly (CPI) / Quarterly (GDP) / Annual (Survey) |
| **The National Treasury** | TNT | Budget Policy Statements, Budget Estimates, Public Debt Reports, Medium Term Debt Strategy | [treasury.go.ke](https://www.treasury.go.ke/) | Annual Budget Cycle (Feb, Apr, Jun) & Quarterly |
| **Office of the Controller of Budget** | OCOB | National & County Government Budget Implementation Review Reports (BIRRs) | [cob.go.ke](https://cob.go.ke/) | Quarterly / Annual |
| **Office of the Auditor-General** | OAG | National, County, and State Corporation Financial & Performance Audit Reports | [oagkenya.go.ke](https://www.oagkenya.go.ke/) | Annual (tabled in Parliament) |
| **Commission on Revenue Allocation** | CRA | County Revenue Sharing Recommendations, Marginalisation Policy | [cra.go.ke](https://cra.go.ke/) | Annual / Periodic |

---

## Ingestion & Provenance Guidelines
1. **Never use secondary news reports for quantitative claims** when the underlying primary bulletin or gazette notice is available.
2. Store raw downloaded PDFs/CSVs under `Data/raw/` with a standard naming convention:
   `[YEAR]_[INSTITUTION]_[TOPIC]_[PERIOD].[ext]`  
   *Example:* `2026_CBK_ExchangeRates_Historical.csv` or `2026_OCOB_CountyBIRR_Q3.pdf`.
