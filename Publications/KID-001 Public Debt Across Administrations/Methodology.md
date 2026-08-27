---
post_id: KID-001
document_type: methodology
status: drafting
primary_indicator: IND-PF-001
created: 2026-08-27
last_updated: 2026-08-27
---

# Methodology & Data Provenance: KID-001 Public Debt

## 1. Data Sources
1. **Gross Public Debt (2002–2026):**
   - *Primary Source:* The National Treasury, Annual Public Debt Reports & Public Debt Statistical Bulletins; Central Bank of Kenya Monthly Economic Indicators.
   - *Definitions:* Total Public and Publicly Guaranteed Debt (Domestic Debt + External Debt).
2. **GDP and Deflator Series:**
   - *Primary Source:* Kenya National Bureau of Statistics (KNBS), Statistical Abstracts & Economic Surveys.
   - *GDP Deflator:* Applied to convert current nominal KSh to constant 2024 KSh.

## 2. Mathematical Transformations
$$\text{Real Debt}_{t} = \frac{\text{Nominal Debt}_{t}}{\text{GDP Deflator}_{t}} \times \text{GDP Deflator}_{2024}$$

$$\text{Debt-to-GDP Ratio}_{t} = \frac{\text{Nominal Public Debt}_{t}}{\text{Nominal GDP}_{t}} \times 100\%$$

## 3. Disclosures and Limitations
- **External Debt FX Effect:** The sharp jump in external debt during 2022–2023 was partially driven by currency depreciation (KES falling against USD from ~115 to ~160) rather than net new dollar borrowings.
- **GDP Rebasing:** Historical GDP series prior to 2014 are spliced using KNBS rebased series to ensure denominator consistency.
