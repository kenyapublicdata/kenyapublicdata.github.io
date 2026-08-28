# QA and release checklist — KID-001 current debt baseline

**Review date:** 2026-08-28  
**Current status:** **Published — mobile revision prepared for deployment**

**Canonical document:** [`KID-001 Current Debt Baseline.md`](../KID-001%20Current%20Debt%20Baseline.md). All derivative QA is performed against this document.

## 1. Data and source checks

| Check | Result | Evidence |
|---|:---:|---|
| CSV schema | PASS | 43 data rows; every row has 19 fields |
| Unique indicator codes | PASS | No duplicate codes |
| June 2025 stock | PASS | EXT-DOC-001, Table 3, p. 28 |
| May 2026 complete total | PASS | EXT-DOC-007, Table 7.1, p. 22 |
| No June/May hybrid total | PASS | June 2026 domestic-only observation excluded from release CSV |
| May 2026 GDP ratio | PASS | No ratio calculated without a matched GDP denominator |
| Currency consistency | PASS | USD/KSh cross-unit GDP ratio removed |
| Debt-service arithmetic | PASS | Interest plus principal equals total service within source precision |
| Revenue ratios | PASS | Same-period Treasury numerator and denominator used |
| Total-expenditure claim | PASS | Unsupported expenditure denominator and 39% derived claim removed from this release |
| Source identifiers | PASS | Document-level IDs match the project Source Register |

## 2. Editorial checks

| Check | Result | Notes |
|---|:---:|---|
| Provisional status disclosed | PASS | Article labels Treasury and CBK figures as provisional |
| Current-snapshot scope | PASS | Administration and long historical comparisons excluded |
| Article/data agreement | PASS | Retained headline figures reconcile to corrected CSV |
| Social/data agreement | PASS | Retained social figures reconcile to corrected CSV |
| X post length | PASS | Four posts checked at 204, 213, 163 and 219 characters |
| Allocation overclaim | PASS | Mechanical “28.8% left” interpretation removed |
| Domestic-debt generalization | PASS | “Domestic debt is short-term” claim removed |
| Debt-distress freshness | PASS | October 2024 assessment removed from current post |
| Formal citations | PASS | Author–date citations and a reference list added to canonical article |
| Interest-recipient boundary | PASS | Holder shares distinguished from interest receipts and bank profit |
| Figure/article agreement | PASS | Eight charts regenerate from the canonical publication CSV; six are embedded in the report |
| Plain-language report style | PASS | Finding-led structure, neutral institutional voice and glossary applied |
| Internal commentary removed | PASS | No working questions or production notes remain in the visible report body |
| Focused asset list | PASS | Reduced from 90 concepts to 15 assets; additional production parked |
| Quick-post package | PASS | Primary caption, 247-character X version, image, alt text and sources ready |
| GitHub resource hub | PASS | Public README, six table extracts, selected chart formats and resource manifest prepared |
| Follow-up infographic batch | PASS | ASSET-010, ASSET-012 and ASSET-014 built in PNG, SVG and PDF with alt text |
| Mobile chart variants | PASS | Eight 1080 × 1350 charts built in PNG, SVG and PDF from the canonical dataset |
| Responsive figure markup | PASS | Article uses mobile SVG below 700 px and reserves the correct aspect ratio before lazy loading |

## 3. Open release gates

| Requirement | Status |
|---|:---:|
| Eight current-snapshot charts | PASS |
| Landscape SVG, PDF and 300-DPI PNG exports | PASS — 24 files |
| Mobile SVG, PDF and 1080 × 1350 PNG exports | PASS — 24 files |
| Alt text and source line for every visual | PASS |
| Quick-post social asset | PASS |
| Broader social asset production | PARTIAL — three follow-up graphics built; carousel and glossary card parked |
| Magazine PDF production | PARKED — Typst selected |
| GitHub table and figure links | PASS — local package paths |
| Live publication URL | PASS |
| Mobile revision deployment | PENDING |
| Public-link test after mobile deployment | PENDING |
| Visual QA at intended sizes | PASS — mobile and landscape source files |
| Release manifest and checksums | PENDING |

## Release decision

The article is published. The mobile revision is ready locally and should be deployed before the next distribution push. After deployment, repeat the 360, 390, 430 and 1280 px browser checks against the public URL.

## Editorial notes addressed — 2026-08-28

| Note added to the canonical article | Resolution |
|---|---|
| Clarify whether 53.5% domestic / 46.5% external is the May 2026 or June 2025 split | Identified it as the June 2025 Treasury split; added the distinct May 2026 CBK split of 56.1% / 43.9% and the 2.6 percentage-point comparison. |
| Determine how much domestic interest relates to bonds | Added Treasury Table 9 breakdown: bonds KSh 677.762B (87.3%), bills KSh 87.560B (11.3%), and other charges KSh 10.935B (1.4%). |
| Determine whether domestic interest can be assigned to Kenyan recipients or bank profits | Added Treasury Table 6 holder shares, while explicitly stating that year-end holdings cannot be treated as annual interest receipts and bank interest revenue is not net profit. |
| Explain why domestic interest is much higher although domestic and external principal look similar | Added a dedicated explanation covering maturities, the Treasury-bill redemption exclusion, debt-stock size, instrument pricing and the 55.5% multilateral share of external debt. Marked the flow/end-stock ratios as illustrative rather than yields. |
| Consider a separate article on domestic interest | Recorded the required follow-up evidence in the canonical article: average stocks, security-level coupons/maturities, external-loan terms, exchange-rate effects, fees and holder-by-instrument data. |
| Make citations formal and academic | Added granular author–date citations, table/page references and a formal reference list. |
| Add figures and plots to the article | Added three source-labelled figures directly to the canonical Markdown article. |
| Cite data sources on each figure | Added exact source/table/page footers in every PNG, SVG and PDF, plus captions and an alt-text registry. |
| Define public and publicly guaranteed debt for non-economists | Added a plain-language definition at first use and a glossary entry. |
| Separate the article page from the project page | Added a two-page publication model: the article carries the report; the project page carries data, methods, sources and reusable assets. |
| Remove internal figure IDs from visible graphics | Retained IDs in filenames only; visible headers now read “KENYA IN DATA • PUBLIC DEBT”. |
| Make Kenya in Data's analytical role clear | Every visual now distinguishes the primary data source from “Analysis and visualisation: Kenya in Data”. |
| Associate every analytical table with a visual | Added charts for June 2025 debt composition and domestic holders; converted debt-service and domestic-interest tables into additive 100% bars. |
| Produce multiple chart forms from the same data | Retained comparison-bar versions and added additive composition versions for article and social reuse. |
| Replace dialogue-style report sections | Rewrote question headings and process commentary as finding-led analytical sections. |
| Use think-tank and high-value report models | Added a reusable editorial guide drawing on IFS, Our World in Data, ONS/Government Analysis Function and the World Bank Kenya Economic Update. |
| Explain maturity and concessional financing | Added plain-language glossary definitions, including an illustrative bond-maturity example. |
| Identify specific domestic and external interest rates | Added the Treasury's FY 2024/25 weighted average rates: 13.0% domestic, 3.9% external and 8.7% total, with a dedicated figure. |
| Standardise infographic production | Expanded the infographic specification with fonts, colour tokens, layouts, attribution, export sizes, concepts and QA rules. |
