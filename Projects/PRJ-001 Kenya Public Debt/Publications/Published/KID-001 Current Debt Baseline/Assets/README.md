---
title: KID-001 Focused Asset List
publication_id: KID-001
project_id: PRJ-001
document_type: asset-catalogue
status: partial_follow_up_production
created: 2026-08-28
last_updated: 2026-08-28
---

# KID-001 — Focused Asset List

Canonical article: [`KID-001 Current Debt Baseline.md`](../KID-001%20Current%20Debt%20Baseline.md).

Canonical dataset: [`KID001_current_debt_baseline.csv`](../Data/KID001_current_debt_baseline.csv).

This publication is limited to **15 assets**: eight completed charts and seven selected distribution or explanatory assets. The broader 90-concept backlog was intentionally removed because it was disproportionate to a short current-baseline release.

## Current production decision

- **Ready now:** the quick post using ASSET-001.
- **Newly built:** the article/Open Graph hero, domestic-interest explainer and statutory-anchor card.
- **Still parked:** the carousel, glossary card and magazine PDF until there is a clear publication channel or editorial need.

`Assets/` remains the planning registry. Completed files stay in the existing `Derivatives` folders so outputs are not duplicated.

## The 15 assets

| ID | Asset | Form and channel | Status | Role |
|---|---|---|:---:|---|
| ASSET-001 | Current debt composition | 100% stacked bar; article and quick post | **Built** | Headline May 2026 total and domestic/external shares |
| ASSET-002 | Debt-service component amounts | Ranked horizontal bars; project page | **Built** | Compare domestic/external interest and principal amounts |
| ASSET-003 | Domestic interest by instrument | Ranked horizontal bars; project page | **Built** | Compare bond, bill and other interest amounts |
| ASSET-004 | June 2025 debt components | Ranked horizontal bars; article | **Built** | Show detailed instrument and creditor composition |
| ASSET-005 | Debt-service composition | 100% stacked bar; article and social | **Built** | Show the four components as parts of KSh 1.722 trillion |
| ASSET-006 | Domestic interest composition | 100% stacked bar; article and social | **Built** | Show bonds at 87.3%, bills at 11.3% and other charges at 1.4% |
| ASSET-007 | Domestic debt holders | Ranked horizontal bars; article | **Built** | Show holder shares without implying interest receipts |
| ASSET-008 | Weighted average interest rates | Horizontal bars; article | **Built** | Compare domestic 13.0%, total 8.7% and external 3.9% |
| ASSET-009 | Quick-post package | One caption, short variant, image, alt text and sources | **Ready** | Immediate publication using ASSET-001 |
| ASSET-010 | Article/Open Graph hero | 1200 × 628 branded preview | **Built** | Link sharing and article discovery |
| ASSET-011 | Five-slide findings carousel | 4:5 mobile carousel | **Parked** | Stock, composition, service, rates and methodology |
| ASSET-012 | Why domestic interest was higher | 1080 × 1350 explanatory infographic | **Built** | Explain stock size, rates, portfolio mix and the principal caveat |
| ASSET-013 | Principal, interest and maturity | Illustrated glossary card | **Parked** | Explain debt mechanics using one hypothetical bond |
| ASSET-014 | Present value and the statutory anchor | 1080 × 1080 bullet chart and annotated card | **Built** | Explain 63.7%, the 55% anchor and the 8.7-point gap |
| ASSET-015 | Magazine-quality PDF brief | Typst template and A4 report | **Parked** | Downloadable, reusable report derived from the article |

## Quick-post selection

Use [ASSET-001](../Derivatives/Charts/FIG-KID001-001_current_debt_composition.png) with the copy in [`Quick Post.md`](../Derivatives/Social/Quick%20Post.md).

This is the strongest first post because it communicates one current headline, uses a single reporting date, is immediately legible and does not require a reader to understand fiscal denominators before engaging with the work.

## Newly built follow-up assets

- [ASSET-010 — article/Open Graph hero](../Derivatives/Infographics/ASSET-KID001-010_article_og_hero.png)
- [ASSET-012 — domestic-interest explainer](../Derivatives/Infographics/ASSET-KID001-012_domestic_interest_explainer.png)
- [ASSET-014 — statutory-anchor card](../Derivatives/Infographics/ASSET-KID001-014_statutory_anchor.png)

Editable vector and PDF versions are registered in the [infographic documentation](../Derivatives/Infographics/README.md).

## PDF decision

Use **Typst** as the primary engine for ASSET-015. The magazine brief should use:

- A custom Kenya in Data template rather than a generic academic template
- A4 portrait pages with occasional full-width landscape-style chart spreads
- Inter or Plus Jakarta Sans with a restrained typographic hierarchy
- SVG charts for sharp vector output
- The Kenya in Data colour tokens and two-line data attribution
- A cover, key-findings spread, report body, glossary, methods, sources and project-page link
- PDF/UA accessibility checks where practical
- Page-by-page rendered-image QA before release

Use LaTeX only when an external journal, publisher or collaborator requires it, or when the document becomes mathematics-heavy enough to benefit from the mature TeX ecosystem.

## Rules retained for every asset

1. All numerical claims must originate in the canonical article and CSV.
2. Every visual displays its reporting date.
3. Visible headers use `KENYA IN DATA • PUBLIC DEBT`; internal IDs remain in filenames.
4. Every visual distinguishes the primary data source from `Analysis and visualisation: Kenya in Data`.
5. No asset may calculate a May 2026 debt-to-GDP ratio, assign interest receipts to holder categories, describe bank interest as profit or present 28.8% of revenue as money left for other spending.
