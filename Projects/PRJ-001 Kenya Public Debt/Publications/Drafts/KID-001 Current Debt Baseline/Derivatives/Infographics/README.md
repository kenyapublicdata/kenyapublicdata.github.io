# Infographic production specification — KID-001

Canonical source: [`KID-001 Current Debt Baseline.md`](../../KID-001%20Current%20Debt%20Baseline.md).

This folder is for designed explanatory graphics derived from the canonical article. Data encodings must originate from the source-checked publication CSV.

## Built assets

| Asset | Use | PNG | Vector and print |
|---|---|---|---|
| ASSET-010 — Article/Open Graph hero | Website previews and link sharing; 1200 × 628 | [PNG](ASSET-KID001-010_article_og_hero.png) | [SVG](ASSET-KID001-010_article_og_hero.svg) · [PDF](ASSET-KID001-010_article_og_hero.pdf) |
| ASSET-012 — Why domestic interest was higher | Portrait social explainer; 1080 × 1350 | [PNG](ASSET-KID001-012_domestic_interest_explainer.png) | [SVG](ASSET-KID001-012_domestic_interest_explainer.svg) · [PDF](ASSET-KID001-012_domestic_interest_explainer.pdf) |
| ASSET-014 — Present value and the statutory anchor | Square social and article card; 1080 × 1080 | [PNG](ASSET-KID001-014_statutory_anchor.png) | [SVG](ASSET-KID001-014_statutory_anchor.svg) · [PDF](ASSET-KID001-014_statutory_anchor.pdf) |

### Alt text

- **ASSET-010:** Branded Kenya in Data card stating that Kenya's public debt reached KSh 12.896 trillion in May 2026. A stacked bar divides the provisional total into domestic debt at 56.1%, or KSh 7.239 trillion, and external debt at 43.9%, or KSh 5.657 trillion.
- **ASSET-012:** Portrait infographic comparing FY 2024/25 domestic interest of KSh 776.3 billion with external interest of KSh 211.2 billion. It identifies the larger domestic debt stock, the 13.0% domestic weighted average rate compared with 3.9% externally, and the 55.5% multilateral share of external debt as relevant portfolio facts. A caveat says principal is not interest and domestic principal excludes routine Treasury-bill redemptions.
- **ASSET-014:** Square bullet chart showing present-value debt at 63.7% of GDP in June 2025 against Kenya's 55% statutory anchor, a gap of 8.7 percentage points. A note says this legal-benchmark comparison is not by itself a forecast of default.

Rebuild all three formats with [`build_infographics.py`](build_infographics.py) using the canonical publication CSV.

## Required visual identity

- **Wordmark:** `KENYA IN DATA • PUBLIC DEBT`. Use this until a formal logo asset is approved.
- **Primary typeface:** Inter or Plus Jakarta Sans.
- **Fallbacks:** Helvetica Neue, Arial, DejaVu Sans or Liberation Sans.
- **Headline colour:** navy `#0F172A`.
- **Canvas:** ivory `#F8FAFC`; plot or content card `#FFFFFF`.
- **Domestic debt:** royal blue `#2563EB`.
- **External debt:** ochre `#D97706`.
- **Interest costs:** violet `#7C3AED`.
- **Total debt or fiscal pressure:** crimson `#DC2626`.
- **Neutral text and notes:** slate `#64748B`; rules and gridlines `#E2E8F0`.

Do not introduce a new typeface or decorative colour without updating the project-wide visual style guide.

## Standard canvas sizes

| Use | Ratio | Export size |
|---|---:|---:|
| Article, PDF or presentation | 16:9 | 1920 × 1080 px |
| LinkedIn, Instagram or WhatsApp card | 1:1 | 1080 × 1080 px |
| Mobile carousel | 4:5 | 1080 × 1350 px |
| Link preview or Open Graph image | 1.91:1 | 1200 × 628 px |

Retain at least 64 px of safe space on 1080 px canvases. No essential text may sit against an edge.

## Layout hierarchy

1. **Brand line:** Kenya in Data wordmark and topic.
2. **Finding-led headline:** one complete statement, normally no more than two lines.
3. **Reporting label:** date, unit and provisional status where relevant.
4. **Primary visual:** chart, number or explanatory diagram.
5. **Interpretive note:** one sentence only when the graphic needs it.
6. **Provenance:** exact data source and Kenya in Data attribution.

## Attribution format

Every infographic must include both lines:

`Data: [institution, report, table or figure, page]`

`Analysis and visualisation: Kenya in Data • kenyaindata.org`

Do not label an official source chart as if Kenya in Data created the underlying data. Do not omit Kenya in Data's analytical and visual role when the graphic is original.

## Approved KID-001 infographic concepts

1. **Headline debt card:** KSh 12.896 trillion at May 2026, with domestic and external shares.
2. **Debt-service composition:** a 100% stacked bar showing four service components and their percentages.
3. **Domestic interest composition:** a 100% stacked bar showing bonds, bills and other charges.
4. **Interest-rate comparison:** domestic 13.0%, total 8.7% and external 3.9%.
5. **Domestic holder profile:** ranked bars for the eight holder categories, clearly labelled as stock holdings rather than interest recipients.
6. **Glossary card:** a simple illustrated explanation of principal, interest and maturity using one hypothetical bond.

The source charts in [`../Charts/`](../Charts/) provide the approved data encodings. Social or infographic remixes may change layout and aspect ratio, but not values, reporting periods, labels or caveats.

## Illustration and image-generation rules

AI-generated material may be used only as clearly labelled illustration. It must never imitate an official document, portray a fabricated public event, or encode numerical data. Record the model, prompt, generation date, edits and usage status alongside each generated image.

Use illustration sparingly. The data remains the primary visual element.

## Export and QA

- Export PNG at the specified pixel dimensions.
- Export SVG or PDF when the design contains vector elements.
- Provide alt text for every released asset.
- Check legibility at actual mobile size.
- Confirm that all bars start at zero and that part-to-whole graphics sum to 100% within rounding.
- Confirm the source line remains readable after platform compression.
- Store editable source files or generation specifications with the output.
