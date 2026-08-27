---
title: Kenya Public Debt Source Register
project_id: PRJ-001
status: active
created: 2026-08-27
last_updated: 2026-08-28
---

# Source Register

Record sources before extracting figures. Prefer the responsible Kenyan institution and the most granular official table available.

## Registered Source Portals

| Source ID | Publisher | Source | Intended use | URL | Checked | Status |
|---|---|---|---|---|---|---|
| SRC-DEBT-001 | National Treasury | Annual Debt Management Reports | Historical debt stock, composition, servicing, risks, and report vintages | [Official archive](https://www.treasury.go.ke/annual-debt-management-reports-0) | 2026-08-27 | available |
| SRC-DEBT-002 | National Treasury PDMO | PDMO Reports and Documents | Debt strategy, sustainability, guarantees, external register, monthly bulletins, and related reports | [Official portal](https://www.treasury.go.ke/pdmo-reports-and-documents) | 2026-08-27 | available |
| SRC-DEBT-003 | Central Bank of Kenya | Monthly Economic Indicators | Monthly debt stock and domestic/external composition cross-checks | [Official archive](https://www.centralbank.go.ke/monthly-economic-indicators/) | 2026-08-27 | available |
| SRC-MACRO-001 | Central Bank of Kenya | Annual GDP | Nominal and real GDP series sourced from KNBS | [Official table](https://www.centralbank.go.ke/annual-gdp/) | 2026-08-27 | available |
| SRC-MACRO-002 | Kenya National Bureau of Statistics | 2025 Economic Survey and Data Tables | GDP, inflation, public finance, and historical statistical tables | [Official release](https://www.knbs.or.ke/reports/2025-economic-survey/) | 2026-08-27 | available |
| SRC-FISCAL-001 | National Treasury | Budget Review and Outlook Papers | Fiscal outturns, debt ratios, revenue, macro assumptions, and projections | [Official archive](https://www.treasury.go.ke/budget-review-and-outlook-paper) | 2026-08-27 | available |
| SRC-LAW-001 | Kenya Law | Public Finance Management Act | Statutory borrowing, reporting, and debt-management framework | [Current consolidated act](https://new.kenyalaw.org/akn/ke/act/2012/18/eng@2024-04-26) | 2026-08-27 | available |
| SRC-LAW-002 | Kenya Law | PFM National Government Regulations | Fiscal rules, debt limits, debt management, and amendments | [Current regulations](https://new.kenyalaw.org/akn/ke/act/ln/2015/34/eng@2022-12-31) | 2026-08-27 | available |
| SRC-AUDIT-001 | Office of the Auditor-General | Public Debt Audit Reports | Debt management, servicing, commercial loans, Eurobond proceeds, and use-of-funds audits | [Official reports](https://www.oagkenya.go.ke/public-debt-audit-reports/) | 2026-08-27 | available |
| SRC-INTL-001 | International Monetary Fund | World Economic Outlook Database | Later macro and international-comparison cross-checks | [Official dataset](https://data.imf.org/Datasets/WEO) | 2026-08-27 | available |
| SRC-DEBT-004 | National Treasury PDMO | Monthly Public Debt Bulletins | Monthly debt stock, borrowing, debt service, cost and risk updates | [Official archive](https://www.treasury.go.ke/monthly-bulletins/) | 2026-08-28 | available |
| SRC-DEBT-005 | National Treasury | Debt Sustainability Analyses | Official debt-sustainability assessments, thresholds, assumptions and historical vintages | [Official archive](https://www.treasury.go.ke/debt-sustainability-analysis/) | 2026-08-28 | available |
| SRC-DEBT-006 | National Treasury | Medium-Term Debt Management Strategies | Borrowing strategy, portfolio risk indicators and forward financing plans | [Official archive](https://www.treasury.go.ke/medium-term-debt-management-strategy) | 2026-08-28 | available |
| SRC-FISCAL-002 | Office of the Controller of Budget | National Government Budget Implementation Review Reports | Actual expenditure, exchequer releases, budget absorption and implementation context | [Official archive](https://cob.go.ke/publications/national-government-budget-implementation-review-reports/) | 2026-08-28 | available |
| SRC-REVENUE-001 | Kenya Revenue Authority | Annual Revenue Performance | Tax and agency revenue collections by fiscal year; use only where the required denominator is specifically KRA revenue | [Official archive](https://www.kra.go.ke/184-kra-revenue-performance) | 2026-08-28 | available |
| SRC-INTL-002 | World Bank | International Debt Statistics — Kenya | Standardized external debt stock, creditor composition and debt-service cross-checks | [Official Kenya table](https://datatopics.worldbank.org/debt/ids/creditorcomposition/KEN) | 2026-08-28 | available |

## Public Data Acquisition and Publication Map

These portals may be linked publicly even before individual files are downloaded. A portal link records discovery; it does **not** make every number on that portal part of the verified project dataset. Any value used in a chart, post, article or PDF must still receive a document-level extraction row below.

| Publication need | Canonical source | Trust/use rule | Current readiness |
|---|---|---|---|
| Current fiscal-year debt stock, composition, debt service and official ratios | National Treasury Annual Debt Management Reports (`SRC-DEBT-001`) | Primary source for fiscal-year-end observations. Preserve the report vintage and provisional/revised status. | **Ready for the June 2025 baseline** |
| Latest monthly debt update | CBK Monthly Economic Indicators (`SRC-DEBT-003`) and Treasury monthly bulletins (`SRC-DEBT-004`) | Use only complete observations. Do not combine domestic and external components from different months. | **Ready through the complete May 2026 observation in the June 2026 CBK bulletin** |
| Historical annual debt series | Treasury annual reports (`SRC-DEBT-001`) | Extract each year from an identified table and retain revisions. Do not infer missing years or silently splice report vintages. | **Rebuild required before publication** |
| Nominal GDP and real growth | KNBS Economic Survey tables (`SRC-MACRO-002`); CBK annual GDP (`SRC-MACRO-001`) as a convenient official table | Match fiscal debt to a fiscal-year GDP denominator where the Treasury report supplies one. Treat changes in real-GDP base years as series breaks unless an official linked series is available. | **Current baseline ready; historical denominator mapping required** |
| Inflation adjustment | KNBS CPI tables (`SRC-MACRO-002`) | Store the original index, base period and rebasing formula. Label CPI-deflated amounts as CPI-adjusted, not GDP-deflated. | **Source extraction and methodology decision required** |
| Ordinary revenue and total expenditure | Treasury annual debt reports and BROP (`SRC-FISCAL-001`) | Use the exact denominator published with the debt-service ratio. Keep ordinary revenue distinct from KRA tax revenue. | **FY 2024/25 ready; historical series requires reconstruction** |
| Tax-revenue context | KRA annual revenue performance (`SRC-REVENUE-001`) | Use for tax-collection stories and tax-head composition. Do not substitute KRA collections for Treasury ordinary revenue. | **Available as a supporting series** |
| Budget execution | Controller of Budget reports (`SRC-FISCAL-002`) | Use for actual expenditure, absorption and exchequer releases; reconcile definitions with Treasury fiscal tables. | **Available as a supporting series** |
| Debt sustainability and forward projections | Treasury DSA, MTDS and BROP (`SRC-DEBT-005`, `SRC-DEBT-006`, `SRC-FISCAL-001`) | Projections must be visually and textually separated from actual observations and tagged by forecast vintage. | **Available for a clearly labelled outlook section** |
| International comparison | IMF WEO (`SRC-INTL-001`) and World Bank IDS (`SRC-INTL-002`) | Use standardized international data for comparison and cross-checking, not to overwrite a more granular Kenyan official fiscal observation without a reconciliation note. | **Available with coverage caveats** |
| Law and accountability | Kenya Law and Auditor-General (`SRC-LAW-001`, `SRC-LAW-002`, `SRC-AUDIT-001`) | Canonical for legal rules and audit findings; do not treat audit narrative as a substitute for the underlying statistical series. | **Ready for explanatory context** |

## Document-Level Extraction Register

Add one row for every specific document, spreadsheet, or table actually used.

| Extraction ID | Parent source ID | Document or dataset | Edition or period | Relevant table/page/sheet | Unit | Local file or direct URL | Retrieved | Use | Notes |
|---|---|---|---|---|---|---|---|---|---|
| EXT-DOC-001 | SRC-DEBT-001 | Annual Public Debt Report 2024-2025 | FY 2024/25 | Table 3 (p. 28), Table 4 (p. 30), Tables 5 and 10 (pp. 34 and 45), Ch. 8 and Tables 26–27 (pp. 63, 78–79) | KSh Million / % | `Sources/Documents/TNT_Annual_Public_Debt_Report_2024_2025.pdf` | 2026-08-27 | Baseline debt stock, composition, debt service, sustainability and projections | Official Treasury report; distinguish FY outturns from medium-term projections |
| EXT-DOC-002 | SRC-DEBT-001 | Annual Public Debt Report 2023-2024 | FY 2023/24 | Main Debt Stock & Composition Tables | KSh Million / % | `Sources/Documents/TNT_Annual_Public_Debt_Report_2023_2024.pdf` | 2026-08-27 | Ruto FY2023/24 public debt comparison | Official Treasury report |
| EXT-DOC-003 | SRC-DEBT-001 | Annual Public Debt Report 2022-2023 | FY 2022/23 | Handover transition debt stock & FX impact | KSh Million / % | `Sources/Documents/TNT_Annual_Public_Debt_Report_2022_2023.pdf` | 2026-08-27 | Uhuru to Ruto handover transition snapshot (June 2022 / June 2023) | Official Treasury report |
| EXT-DOC-004 | SRC-DEBT-001 | Annual Public Debt Report 2021-2022 | FY 2021/22 | Pre-transition debt stock | KSh Million / % | `Sources/Documents/TNT_Annual_Public_Debt_Report_2021_2022.pdf` | 2026-08-27 | End of Uhuru term baseline (June 2022) | Official Treasury report |
| EXT-DOC-005 | SRC-DEBT-001 | Annual Public Debt Report 2012-2013 | FY 2012/13 | Table 1.1 and Principal Secretary statement (p. 6) | KSh Million / % | `Sources/Documents/TNT_Annual_Public_Debt_Report_2012_2013.pdf` | 2026-08-27 | Kibaki to Uhuru handover snapshot (June 2013) | Reported total debt KSh 1,894,117 million and 51.7% of GDP |
| EXT-DOC-006 | SRC-DEBT-001 | Annual Public Debt Report 2005-2006 | FY 2005/06 | Early Kibaki era debt series | KSh Million / % | `Sources/Documents/TNT_Annual_Public_Debt_Report_2005_2006.pdf` | 2026-08-27 | Early Kibaki baseline & historical reference | Official Treasury report |
| EXT-DOC-007 | SRC-DEBT-003 | Monthly Economic Indicators June 2026 | June 2026 | Table 7.1 (p. 22), Table 7.2 (p. 23) | KSh Billion | `Sources/Documents/CBK_MEI_June_2026.pdf` | 2026-08-27 | Latest 2025/2026 monthly public debt & composition series | Official CBK release |
| EXT-DOC-008 | SRC-DEBT-003 | Monthly Economic Indicators June 2024 | June 2024 | Table 7.1, Table 7.2 | KSh Billion | `Sources/Documents/CBK_MEI_June_2024.pdf` | 2026-08-27 | 2023/2024 monthly debt reconciliation | Official CBK release |
| EXT-DATA-001 | SRC-MACRO-001 | CBK Annual GDP Time Series (2000–2025) | 2000–2025 | Annual GDP web table | KSh Million / % | `Data/Raw/CBK_Annual_GDP_2000_2026.csv` | 2026-08-27 | Nominal GDP and annual real growth | Sourced from KNBS via CBK; real-GDP levels use 2001 prices through 2008 and 2009 prices from 2009, so they are not one linked constant-price level series |

## Source Hierarchy

1. Original official machine-readable tables or datasets.
2. Official statistical bulletins, debt reports, budget documents, and annual reports.
3. Official legal texts, audit reports, and parliamentary research.
4. International official datasets used for reconciliation, standardized comparisons, or gaps.
5. Academic and policy analysis used for interpretation.
6. Media reporting used to discover claims or sources, not as the canonical numerical source where primary material exists.

## Recording Standard

For every used source, record:

- exact table, page, sheet, row, and column;
- debt definition and institutional coverage;
- observation date and reporting frequency;
- currency, unit, and scale;
- actual, estimate, projection, or revised status;
- edition, publication date, and retrieval date;
- local filename or direct link;
- transformation needed before comparison;
- discrepancies with other sources and how they were resolved.

## Source Cautions Already Identified

- Public-debt definitions and classification can change across report vintages.
- Fiscal-year debt stocks and calendar-year GDP values must not be combined without an explicit convention.
- Nominal and real GDP series may have different base years or historical revisions.
- The shilling value of external debt changes with exchange rates even without equivalent new borrowing.
- “Debt service” may refer to interest only, interest plus principal, or a budget accounting category; always define it.
- Projections and estimates must never be presented as final actual observations.
