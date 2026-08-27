---
title: 10-Hour Launch Sprint — Four Views of Kenya's Public Debt
project_id: PRJ-001
publication_id: KID-001
document_type: sprint_plan
status: ready_to_start
created: 2026-08-27
last_updated: 2026-08-27
time_budget_hours: 10
tags: [kenya-in-data, public-debt, launch-sprint, kid-001]
---

# 10-Hour Launch Sprint

## Release Concept

### Working title

**Kenya's Public Debt Across Administrations: What Changes When We Add Inflation and GDP?**

### Core question

How different does Kenya's debt story look when selected administration-era snapshots are compared using nominal shillings, inflation-adjusted shillings, and debt relative to GDP?

### Editorial claim

Nominal debt, real debt, and debt-to-GDP answer different questions. A fair comparison shows all three and labels the dates precisely.

This first release is descriptive. It does not rank presidents or claim that each administration caused every change observed during its tenure.

## Minimum Scope

Use four verified snapshots as close as the official data allow to:

1. the beginning of the Kibaki administration;
2. the transition from Kibaki to Uhuru;
3. the transition from Uhuru to Ruto;
4. the latest complete and comparable reporting period.

Every snapshot must display its exact observation date. If official reporting dates do not align with inauguration dates, say so. Do not silently relabel a June fiscal-year value as a December or September handover value.

## Measures

### Required

- Total public debt in nominal KSh.
- Total public debt in constant KSh using CPI and a stated base year.
- Total public debt as a percentage of GDP.

### Optional stretch measure

- Domestic and external debt shares.

CPI is the practical first-release adjustment because it answers the intuitive question, “What would those shillings be worth in today's consumer prices?” Debt-to-GDP separately supplies the macroeconomic scale. A GDP-deflator version can be added later as a robustness exercise, particularly because historical national-accounts rebasing requires careful treatment.

## Deliverables

By the end of ten hours, release one complete package:

1. **Figure 1:** Nominal public debt at the four dated snapshots.
2. **Figure 2:** The same snapshots in constant-price KSh.
3. **Figure 3:** Public debt as a percentage of GDP.
4. **Essay:** Approximately 900–1,300 words explaining the three measures, results, caveats, and what remains unanswered.
5. **Public data file:** One tidy CSV containing the exact values underlying the figures.
6. **Methodology note:** Definitions, dates, formulas, inflation base year, and limitations.
7. **Source sheet:** Direct links plus exact documents, tables, pages, retrieval dates, and data vintages.
8. **Sharing pack:** Three accessible image exports, one short thread or post, one concise LinkedIn-style caption, and one stable link to the essay or repository page.

## Ten-Hour Budget

| Work block                      |       Time | Output                                                |
| ------------------------------- | ---------: | ----------------------------------------------------- |
| Freeze scope and definitions    |      0.5 h | Exact debt definition, dates, measures, and cut rules |
| Acquire and register sources    |      2.0 h | Source files and completed source-register entries    |
| Extract and reconcile snapshots |      1.5 h | Four-row raw/interim table with discrepancy notes     |
| Calculate real debt and ratios  |      1.0 h | Reproducible processed dataset                        |
| Design and export three figures |      2.0 h | Drafts, review, and final image exports               |
| Write the essay and captions    |      1.5 h | Complete draft, not merely notes                      |
| Verify and package              |      1.0 h | Checked figures, CSV, methods, alt text, and links    |
| Publish and record the release  |      0.5 h | Public link and archived release package              |
| **Total**                       | **10.0 h** | **Complete KID-001 release**                          |

## Suggested Week

### Day 1 — 1 hour

- Freeze the debt definition, four target dates, price adjustment, and publication title.
- Open the source register and make a precise acquisition list.

### Day 2 — 2 hours

- Retrieve debt figures and composition from Treasury or CBK.
- Retrieve GDP and CPI inputs.
- Record exact tables, units, dates, and source vintages.

### Day 3 — 2 hours

- Reconcile conflicting figures.
- Build the tidy dataset.
- Calculate constant-price debt and debt-to-GDP.
- Write down every formula and assumption.

### Day 4 — 2 hours

- Create and refine the three figures.
- Add exact dates, units, administration annotations, source footers, and caveats.

### Day 5 — 2 hours

- Write the essay and social captions.
- Export the CSV and methodology note.
- Complete the verification checklist.

### Release block — 1 hour

- Check figure-caption-data agreement.
- Add alt text and stable source links.
- Publish, share, and record the release in `Updates/`.

## Primary Source Plan

### Debt stock and composition

- [National Treasury — Annual Debt Management Reports](https://www.treasury.go.ke/annual-debt-management-reports-0)
- [National Treasury — PDMO Reports and Documents](https://www.treasury.go.ke/pdmo-reports-and-documents)
- [Central Bank of Kenya — Monthly Economic Indicators](https://www.centralbank.go.ke/monthly-economic-indicators/)

Use Treasury as the primary reporting source and CBK as a cross-check where definitions and dates align.

### GDP and inflation inputs

- [Central Bank of Kenya — Annual GDP](https://www.centralbank.go.ke/annual-gdp/)
- [KNBS — 2025 Economic Survey and Data Tables](https://www.knbs.or.ke/reports/2025-economic-survey/)

Prefer KNBS data tables for the price series. Record base years and revisions. Use CBK's KNBS-sourced GDP table as a convenient cross-check, not as permission to splice differently based real-GDP series without adjustment.

### Fiscal context

- [National Treasury — Budget Review and Outlook Papers](https://www.treasury.go.ke/budget-review-and-outlook-paper)

Use published Treasury ratios only as cross-checks unless the numerator and denominator periods exactly match the project's calculations.

## Data Table Design

The processed and published CSV should contain at least:

| Field | Meaning |
|---|---|
| `observation_date` | Exact source date |
| `administration_context` | Descriptive administration label |
| `debt_definition` | Exact coverage of the debt measure |
| `nominal_debt_ksh_bn` | Nominal debt stock |
| `cpi_index` | CPI value used in conversion |
| `cpi_base_period` | Constant-price base |
| `real_debt_ksh_bn` | Inflation-adjusted debt |
| `nominal_gdp_ksh_bn` | Matching GDP denominator |
| `debt_to_gdp_pct` | Debt as percentage of GDP |
| `domestic_debt_ksh_bn` | Optional domestic component |
| `external_debt_ksh_bn` | Optional external component |
| `source_id` | Source-register reference |
| `notes` | Breaks, estimates, or caveats |

## Core Formulas

### Constant-price debt

`real debt in base-period KSh = nominal debt × (CPI in base period ÷ CPI in observation period)`

### Debt to GDP

`debt-to-GDP (%) = debt stock ÷ matching nominal GDP × 100`

The stock date and GDP period must be compatible and the convention must be disclosed.

## Essay Outline

1. **The familiar argument:** administrations are compared using large nominal totals.
2. **Why that is incomplete:** old and current shillings have different purchasing value, and Kenya's economy has changed size.
3. **What the three measures mean:** nominal debt, real debt, and debt-to-GDP.
4. **What the four snapshots show:** report observations only after verification.
5. **Why the lines moved:** identify plausible context without claiming unsupported causation.
6. **What this analysis does not answer:** debt service, loan quality, creditor terms, hidden liabilities, and value for money.
7. **What comes next:** annual series, composition, servicing burden, and exchange-rate effects.

## Cut Rules

If time runs short:

1. Keep the four snapshots; cut the full annual series.
2. Keep nominal, real, and debt-to-GDP; cut domestic/external composition.
3. Keep the essay concise; do not cut the methodology or source sheet.
4. Use static charts; do not build an interactive website.
5. Release one polished platform package; adapt to additional platforms later.
6. If one snapshot cannot be sourced consistently, use the nearest defensible date and label it exactly.
7. If inflation series continuity cannot be verified, do not improvise. Publish nominal and debt-to-GDP as a clearly labelled partial release or delay the real-debt figure.

## Explicitly Out of Scope This Week

- A 50-year annual series.
- International rankings.
- Bank profits or dividends from government securities.
- Full debt-service reconstruction.
- Eurobond-by-Eurobond investigation.
- Debt-ceiling legal history.
- Use-of-proceeds or value-for-money conclusions.
- Causal ranking of presidents.
- A dashboard, API, or AI agent.

## Verification Gate

Do not publish until:

- every plotted value maps to a source and exact table or page;
- observation dates and administration labels are honest;
- the debt definition is consistent or breaks are disclosed;
- CPI base and conversion are independently checked;
- GDP numerator and denominator periods are compatible;
- figures, essay, captions, and CSV contain the same values;
- every chart includes units, dates, sources, and accessible alt text;
- limitations are visible without requiring a reader to inspect the code.

## Sprint Definition of Done

The sprint is complete only when a reader can open a stable link, understand the three comparisons, inspect the source and methodology, download the plotted data, and share the figures independently.

