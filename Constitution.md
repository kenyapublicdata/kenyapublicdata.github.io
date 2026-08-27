---
title: Kenya in Data Constitution
project: Kenya in Data
document_type: governance
status: active
created: 2026-08-27
last_updated: 2026-08-27
tags: [constitution, editorial-standards, neutrality, verification]
---

# Kenya in Data Constitution

## 1. Mission and Epistemic Stance

Kenya in Data exists to **democratize quantitative context in Kenyan public life**. Public debate is frequently dominated by slogans, nominal numbers stripped of inflation adjustment, arbitrary start dates, and partisan claims. Our role is to provide the missing denominators, deflators, and verified historical baselines.

### The Four-Tier Separation Rule
We ruthlessly distinguish between four levels of information:
1. **Fact:** Direct official observation from a primary document (e.g., *"The Controller of Budget reports county development expenditure was KSh 98 billion."*)
2. **Calculation:** Transparent arithmetic performed on facts (e.g., *"Dividing development expenditure by total revenue yields an absorption rate of 19.4%."*)
3. **Interpretation:** Analytical context that explains economic mechanisms (e.g., *"Development absorption has declined 3 percentage points relative to the 5-year average due to wage bill growth."*)
4. **Judgment:** Evaluative or moral assertions (e.g., *"This county administration is reckless."*)

> **Rule:** Kenya in Data operates in Tiers 1, 2, and 3. Tier 4 is left to the reader.

---

## 2. Core Operating Principles

### A. Show First. Interpret Second.
Every publication leads with clean data and visual clarity. The chart must be understandable on its own merits before any explanatory caption is read.

### B. Denominators and Deflators
- **Nominal vs. Real:** Whenever time series span multiple years, always examine and disclose inflation effects using appropriate deflators (CPI for consumer baskets; GDP deflator for public debt and macroeconomic stocks).
- **Per Capita & Share of GDP:** Always consider whether absolute growth is explained by population growth or economic expansion.
- **Fiscal Context:** For debt, pair debt stock with debt-service-to-revenue ratios to reflect true liquidity burden.

### C. Provenance and Reproducibility
- Every published figure must trace back to an accessible primary document (CBK, KNBS, National Treasury, CoB, OAG).
- All transformations from `Data/raw/` to `Data/published/` must be scripted, versioned, and reproducible.

### D. Strict Non-Partisanship
- We do not frame graphics to praise or attack specific political administrations or parties.
- Shading presidential administrations or legislative terms is done solely as a temporal landmark, with explicit notes stating that multi-year economic trends involve exogenous shocks, global factors, and legislative lag.

---

## 3. Verification & Corrections Standard

1. **Pre-Publication Check:**
   - Double-check arithmetic and code transformations against raw source tables.
   - Ensure axis scales, baseline origins, and annotations do not visually distort the data.
2. **Transparent Corrections:**
   - If an error in data, deflator math, or labeling is identified, issue an explicit public correction noting what changed, why, and provide the corrected chart.
   - Retain the prior version in `Archive/` with a dated post-mortem.
