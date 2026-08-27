---
title: Kenya Public Debt Figure Plan
project_id: PRJ-001
status: draft
created: 2026-08-27
last_updated: 2026-08-27
---

# Figure Plan

| Figure ID | Working title | Analytical purpose | Required indicators | Format & Output | Generator Script | Status |
|:---|:---|:---|:---|:---|:---|:---|
| **FIG-DEBT-001** | Nominal versus Real Public Debt (2002–2026) | Show inflation deflator impact on debt trajectory | `IND-PF-001` (Nominal & Constant 2024 KSh) | PNG + SVG (16:9)<br>[`FIG-DEBT-001.png`](Final/FIG-DEBT-001_nominal_vs_real_public_debt.png) | `Code/generate_debt_figures.py` | **Generated (Final)** |
| **FIG-DEBT-002** | Public Debt as % of GDP (2002–2026) | Scale debt to macroeconomic size against statutory anchor | `IND-PF-001` (% of GDP) | PNG + SVG (16:9)<br>[`FIG-DEBT-002.png`](Final/FIG-DEBT-002_public_debt_to_gdp.png) | `Code/generate_debt_figures.py` | **Generated (Final)** |
| **FIG-DEBT-003** | Domestic vs External Debt Mix (2002–2026) | Reveal shifting borrowing structure | Domestic vs External Shares | PNG + SVG (16:9)<br>[`FIG-DEBT-003.png`](Final/FIG-DEBT-003_domestic_vs_external_composition.png) | `Code/generate_debt_figures.py` | **Generated (Final)** |
| **FIG-DEBT-004** | The Debt Servicing Squeeze (2002–2026) | Contrast tax revenue against debt service & domestic interest | Debt Service / Revenue (%) | PNG + SVG (16:9)<br>[`FIG-DEBT-004.png`](Final/FIG-DEBT-004_debt_service_to_tax_revenue.png) | `Code/generate_debt_figures.py` | **Generated (Final)** |

## Manifest & Generation Protocol
All figures are programmatically generated using the standard `kid_theme` module (`Code/kid_theme.py`) which enforces:
- Brand colors (Navy `#0F172A`, Crimson `#DC2626`, Gold `#D97706`, Emerald `#059669`).
- Presidential administration shading bands (`add_administration_shading`).
- Direct end-line labeling (`add_end_line_label`).
- Standardized 3-part layout (Track ID, Title/Subtitle header, Source/Provenance footer).
- Dual output: 300 DPI PNG raster and Scalable Vector Graphics (SVG).


