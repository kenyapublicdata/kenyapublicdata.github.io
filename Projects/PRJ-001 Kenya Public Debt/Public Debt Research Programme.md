---
title: Public Debt Research Programme
project_id: PRJ-001
document_type: research_programme
status: living
created: 2026-08-27
last_updated: 2026-08-27
time_horizon: multi-month
tags: [kenya-in-data, public-debt, research-programme]
---

# Public Debt Research Programme

## Purpose

This is the long-horizon map of work Kenya in Data could undertake on Kenyan public debt. It is a programme backlog, not a promise to study every question immediately.

The programme should grow in layers. Begin with definitions, sources, and a small number of reproducible indicators. Add composition, servicing, risks, institutions, and accountability only after the underlying data are reliable.

The first bounded release is defined separately in [[10-Hour Launch Sprint]].

## Central Public Question

> What does Kenya owe, to whom, on what terms, for what purpose, and what does servicing that debt mean for the economy and the public budget?

## Editorial Principles

- **Show first; interpret second.**
- Use several measures because no single debt number tells the whole story.
- Separate what happened during an administration from what an administration caused.
- Distinguish stocks, flows, ratios, costs, and risks.
- Prefer primary official sources and disclose conflicts between them.
- Make transformations reproducible and preserve the source vintage used.
- Use international comparisons only when definitions and reporting periods are comparable.
- State uncertainty and missing information rather than filling gaps with false precision.

## Research Architecture

### Track 0 — Definitions, Data Infrastructure, and Provenance

This track underpins everything else.

#### Questions

- What is included in Kenya's reported public debt?
- How do central-government debt, public and publicly guaranteed debt, general-government debt, and public-sector debt differ?
- Are figures gross or net of government deposits?
- Which contingent liabilities, county debts, state-corporation debts, arrears, guarantees, and public-private partnership obligations are excluded?
- Which series are calendar-year, fiscal-year, month-end, quarter-end, or end-period?
- Where do definitions or classification standards change?
- How should revised data vintages be handled?

#### Assets to build

- Debt glossary and definition crosswalk.
- Source hierarchy and source register.
- Document archive with retrieval dates and checksums.
- Canonical observation schema.
- Reproducible extraction and transformation pipeline.
- Data-quality and revision log.
- Administration-boundary decision rule.

### Track 1 — Size and Historical Trajectory

#### Core measures

- Total public debt in nominal KSh.
- Total public debt in constant KSh using a clearly identified price index.
- Debt as a percentage of GDP.
- Debt per capita in nominal and constant KSh.
- Debt relative to ordinary revenue, total revenue, exports, and government expenditure.
- Annual change in debt in KSh and percentage terms.
- Cumulative change over consistent comparison periods.

#### Questions

- How has debt changed over 10, 20, and eventually 50 years?
- How different is the story in nominal terms, real terms, and relative to GDP?
- Where are the genuine structural breaks in the series?
- Which shocks coincide with the fastest increases or declines?
- What debt stock was inherited and handed over at precisely defined dates?

#### Possible outputs

- Long-run public-debt timeline.
- Administration-annotated series.
- Nominal-versus-real explainer.
- Debt-to-GDP and debt-per-capita comparison.
- Interactive timeline with source documents.

### Track 2 — Debt Service and the Budget Burden

Debt stock is not the same as the annual repayment burden.

#### Measures

- Interest payments.
- Principal repayments or redemptions.
- Total debt service.
- Domestic versus external debt service.
- Interest as a share of ordinary revenue.
- Total debt service as a share of revenue and grants.
- Interest and debt service as shares of the national budget and expenditure.
- Debt service per resident and per taxpayer where defensible.
- Gross financing need and net new borrowing.

#### Questions

- For every KSh100 collected, how much goes to interest or total debt service?
- How much is principal repayment versus the cost of borrowing?
- How much new borrowing refinances maturing debt rather than financing new spending?
- Which years contain large repayment spikes?
- How much fiscal space remains after debt service and other mandatory expenditure?

#### Important distinction

Do not casually add principal repayments to ordinary programme spending and call the result a simple “share of the budget.” Define the denominator, budget accounting treatment, and whether refinancing is included.

### Track 3 — Domestic and External Composition

#### Domestic debt

- Treasury bills versus Treasury bonds.
- Central Bank overdraft and other instruments.
- Fixed versus floating-rate debt.
- Maturity profile and average time to maturity.
- Auction yields and effective interest cost.
- Holdings by commercial banks, pension funds, insurers, households, and other investors where available.

#### External debt

- Multilateral, bilateral, commercial-bank, export-credit, and international-bond debt.
- Creditor and creditor-country composition.
- Currency composition.
- Concessional versus non-concessional borrowing.
- Fixed versus variable interest rates.
- Maturity and grace periods.
- Exchange-rate revaluation of KSh debt values.

#### Questions

- How has the domestic-external mix changed?
- What portion is exposed to currency depreciation?
- What portion is exposed to refinancing or variable-rate risk?
- How does a change in the shilling affect the reported external-debt stock without new borrowing?

### Track 4 — Cost, Maturity, and Risk

#### Measures

- Effective interest rate on the debt stock.
- Weighted average interest rate.
- Average time to maturity and average time to refixing.
- Debt maturing within one, three, and five years.
- Share in foreign currency.
- Share on variable rates.
- Short-term debt and refinancing concentration.
- Interest-growth differential.

#### Analyses

- Maturity wall and refinancing calendar.
- Interest-rate sensitivity.
- Exchange-rate sensitivity.
- Primary-balance requirements under alternative assumptions.
- Scenario and stress testing.
- Comparison between concessional and commercial financing costs.
- Risks from domestic rollover dependence.

### Track 5 — Major Borrowing Episodes and Instruments

Each major episode can become its own case study.

#### Candidate topics

- Eurobond issuances, coupons, maturities, buybacks, and refinancing.
- Syndicated commercial loans.
- IMF programmes and disbursements.
- World Bank and African Development Bank financing.
- Bilateral lending and export-credit facilities.
- Infrastructure and supplier-credit arrangements.
- Domestic infrastructure bonds and tax-exempt bonds.
- Treasury-bill and Treasury-bond market development.
- Debt swaps, liability-management operations, and refinancing transactions.

#### Standard case-study questions

- How much was contracted, disbursed, and outstanding?
- In what currency and on what financial terms?
- What fees and transaction costs applied?
- What was the stated use of proceeds?
- Can proceeds be traced to expenditure or projects?
- What has been repaid, refinanced, or restructured?
- What risks remain?

### Track 6 — Creditors and Domestic Financial Institutions

#### Questions

- Who ultimately holds Kenya's domestic debt?
- How concentrated are government securities among banks, pension funds, insurers, and other institutions?
- How much interest income do commercial banks receive from government securities?
- What share of bank assets and earnings is linked to government lending?
- Does government borrowing crowd out private-sector credit?
- How are pension savers and insurance policyholders indirectly exposed to sovereign debt?
- Who receives the income generated by domestic public debt?

#### Guardrail

Bank profits or dividends cannot be attributed to government debt merely because banks hold government securities. The analysis must isolate securities holdings, interest income, funding cost, taxes, impairments, and other business lines.

### Track 7 — Use of Proceeds and Value for Money

#### Questions

- What expenditures or projects were specific loans intended to finance?
- Were proceeds disbursed and absorbed as planned?
- Did project costs, completion dates, and outputs match the financing documents?
- Are completed assets generating the expected economic or social benefits?
- Which loans paid for recurrent expenditure, budget support, or refinancing rather than identifiable capital projects?
- What do audit reports say about utilization, procurement, delays, and leakage?

#### Possible products

- Loan-to-project register.
- Project financing and repayment profiles.
- Audit finding tracker.
- “Promise → Loan → Disbursement → Asset → Outcome” case studies.

### Track 8 — Macroeconomic Effects

#### Questions

- How is debt related to economic growth over different periods?
- Does domestic borrowing influence interest rates or private credit?
- How do exchange-rate movements affect external-debt valuation and service?
- How do inflation and financial repression change the real domestic-debt burden?
- How does fiscal consolidation affect growth, investment, and service delivery?
- What is the interaction between sovereign credit ratings, spreads, and borrowing cost?
- When does borrowing stabilize an economy, and when does it amplify vulnerability?

#### Guardrail

These are causal questions. Descriptive correlation should not be presented as proof without an appropriate research design.

### Track 9 — Citizens, Distribution, and Opportunity Cost

#### Questions

- What does debt service mean for the resources available to health, education, infrastructure, counties, and social protection?
- Who bears adjustment through taxes, inflation, spending restraint, or reduced public investment?
- Who earns interest from domestic government debt?
- How is the burden distributed across current and future taxpayers?
- What does the debt burden look like per person, worker, or household?
- Which “per Kenyan” framings clarify the issue, and which mislead?

#### Possible outputs

- “Where KSh100 of revenue goes.”
- Debt service compared with selected service-delivery budgets.
- Opportunity-cost comparisons with explicit caveats.
- Intergenerational debt explainer.

### Track 10 — Law, Institutions, and Political Economy

#### Topics

- Constitutional borrowing and public-finance principles.
- Public Finance Management Act and regulations.
- Evolution from percentage-based limits to numerical ceilings and debt anchors.
- Parliamentary approvals, amendments, and oversight.
- National Treasury and Public Debt Management Office mandates.
- Auditor-General findings.
- Parliamentary Budget Office analysis.
- Transparency of loan terms and public participation.
- Changes in fiscal rules and compliance.
- Electoral incentives, supplementary budgets, and borrowing cycles.

#### Questions

- How has Kenya's formal debt ceiling changed, and why?
- Was the rule binding, breached, amended, or redefined?
- What institutions can authorize, scrutinize, or audit borrowing?
- Which documents are legally required, and are they published on time?

### Track 11 — Hidden, Contingent, and Wider Public-Sector Liabilities

#### Topics

- Publicly guaranteed debt.
- State-corporation obligations.
- County debt and pending bills.
- Public-private partnership commitments.
- Government arrears and unpaid bills.
- Pension liabilities.
- Legal claims and other fiscal risks.
- Central Bank overdrafts and on-lent funds.

#### Questions

- What is excluded from the headline stock?
- Which liabilities could migrate onto the national balance sheet?
- How consistently are fiscal risks valued and disclosed?

### Track 12 — International and Peer Comparison

#### Possible peers

- East African Community countries.
- Sub-Saharan African lower-middle-income economies.
- Countries with similar revenue capacity, market access, or commodity exposure.
- Countries with comparable domestic bond markets.

#### Comparison dimensions

- Debt to GDP.
- Debt service to revenue.
- Interest to revenue.
- Foreign-currency share.
- Concessional share.
- Maturity and refinancing profile.
- Revenue to GDP.
- Sovereign spreads and ratings.

#### Guardrail

Do not rank countries using one debt ratio. Compare definitions, institutional coverage, exchange rates, revenue capacity, maturity, and financing terms.

### Track 13 — Sustainability and Forward Scenarios

#### Questions

- Under what combinations of growth, interest rates, exchange rates, inflation, and primary balances does debt stabilize?
- What happens under plausible exchange-rate, growth, or refinancing shocks?
- How large is the gross financing need in coming years?
- Which maturities create concentration risk?
- How do official projections compare with realized outcomes?
- What assumptions drive IMF and Treasury debt-sustainability assessments?

#### Possible outputs

- Adjustable debt-dynamics calculator.
- Maturity and repayment calendar.
- Official forecast-versus-outturn tracker.
- Plain-language debt sustainability explainer.

### Track 14 — Public Information Products

- Canonical public-debt dataset with source-level provenance.
- Indicator registry and glossary.
- Public-debt timeline.
- Debt servicing dashboard.
- Domestic-debt holder map.
- External creditor and currency map.
- Eurobond and major-loan register.
- Loan-to-project and audit tracker.
- Debt ceiling and legal-history timeline.
- Claims ledger for public statements about debt.
- Downloadable chart data and methodology pages.
- “Ask Kenya in Data” interface over verified indicators in a later phase.

## Recommended Sequence

### Phase 1 — Foundations and First Release

- Freeze initial definitions and dates.
- Build a small source register.
- Produce nominal debt, real debt, and debt-to-GDP snapshots.
- Release figures, an essay, source links, and a downloadable dataset.

### Phase 2 — Annual Historical Series

- Extend from snapshots to a consistent annual series.
- Reconcile revisions and administration boundaries.
- Add debt per capita and sensitivity to alternative inflation adjustments.

### Phase 3 — Composition and Servicing

- Add domestic/external composition.
- Separate interest, principal, and total debt service.
- Relate servicing to revenue and the budget.

### Phase 4 — Cost and Risk

- Add creditor, currency, instrument, interest-rate, and maturity structure.
- Build maturity calendars and stress scenarios.

### Phase 5 — Institutions and Accountability

- Map debt ceilings, parliamentary oversight, audits, guarantees, and contingent liabilities.
- Begin major-loan and use-of-proceeds case studies.

### Phase 6 — Comparative and Living Observatory

- Add peer comparisons, forecast tracking, dashboards, and recurring updates.
- Maintain revision history and publish corrections transparently.

## Prioritization Test

Before starting a piece of work, score it against:

1. **Public relevance:** Does it answer a question Kenyans are already asking?
2. **Data readiness:** Can the required evidence be obtained and reconciled?
3. **Clarity:** Can the result be explained without misleading simplification?
4. **Original contribution:** Does it add missing context rather than repeat a headline?
5. **Reproducibility:** Can another person rebuild the result?
6. **Time-to-release:** Can it become a complete public artifact within the available time?
7. **Compounding value:** Will the data or method support later projects?

## Programme Definition of Done

The programme is not “finished” when every possible debt question is answered. It succeeds when Kenya in Data maintains a trustworthy, revisable evidence layer from which public questions can be answered quickly, transparently, and repeatedly.

