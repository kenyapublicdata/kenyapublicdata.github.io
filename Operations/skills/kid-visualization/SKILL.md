---
name: kid-visualization
description: Canonical instructions, visual design standards, color tokens, and Python engine for creating publication-grade graphics, figures, and infographics for Kenya in Data projects.
---

# Kenya in Data — Visualization & Graphics Standard (kid-visualization)

This skill documents the design rules, typography hierarchy, semantic color tokens, and reproducible Python engine (`Code/kid_theme.py`) for generating charts, figures, and infographics across all Kenya in Data projects (`PRJ-001`, `PRJ-002`, etc.).

---

## 1. Visual Standards & Semantic Tokens

Every graphic must strictly follow the **Kenya in Data Visual Style Guide**:

### Brand Palette Tokens
| Token Name | Hex Code | Semantic Role |
|:---|:---:|:---|
| **Navy** | `#0F172A` | Primary text, titles, dark backgrounds, high-emphasis benchmarks |
| **Canvas Light** | `#F8FAFC` | Figure background canvas (crisp ivory tone) |
| **Pure White** | `#FFFFFF` | Plot axes background card |
| **Alert Crimson** | `#DC2626` | Public debt stock, fiscal deficit, inflation spikes, debt distress thresholds |
| **Emerald Green** | `#059669` | Ordinary revenue, tax collection, real GDP growth, positive reserves |
| **Amber Gold** | `#D97706` | External debt, foreign exchange rates, statutory debt ceiling anchors |
| **Royal Blue** | `#2563EB` | Domestic debt stock (Treasury bonds/bills), banking credit metrics |
| **Violet Purple** | `#7C3AED` | Domestic interest expense, fiscal squeeze indicators, tax brackets |
| **Neutral Slate** | `#64748B` | Subtitles, gridlines, axis ticks, source provenance footnotes |

### Administration Shading Tokens (Timeline Landmarks)
- **Mwai Kibaki (2002–2013):** `#CBD5E1` (`alpha=0.22`)
- **Uhuru Kenyatta (2013–2022):** `#94A3B8` (`alpha=0.15`)
- **William Ruto (2022–Present):** `#CBD5E1` (`alpha=0.22`)

---

## 2. Standard 3-Tier Layout Frame & Aspect Ratios

Every figure must follow a standardized 3-tier bounding box:
1. **Top Header:** Tracker tag (`KENYA IN DATA • ID`) + 16pt Heavy Title + 11pt Subtitle Question.
2. **Center Canvas Area:** Direct end-line labels (zero floating separate legends), zero-origin baselines where proportional changes are shown, and subtle background vertical administration shading bands.
3. **Bottom Footer:** Granular source citation (Institution, Report Name, Table, Page) + Deflator note + Website/Handle branding (`kenyaindata.org • @KenyaInData`).

### Aspect Ratio Presets
- `16:9` (`12.0 x 6.75 in`): Landscape / Presentation / Widescreen
- `1:1` (`8.5 x 8.5 in`): Square Social Card (LinkedIn, Instagram)
- `4:5` (`8.0 x 10.0 in`): Mobile Portrait / Feed Carousel
- `1.91:1` (`12.0 x 6.28 in`): X (Twitter) Summary Card

---

## 3. Python Plotting Engine API Reference (`Code/kid_theme.py`)

All projects use the shared module `Code/kid_theme.py`.

### Available Functions
```python
from Code.kid_theme import (
    PALETTE,                      # Color token dictionary
    ASPECT_RATIOS,                # Dimension preset dictionary
    apply_kid_theme,              # Applies matplotlib runtime parameters
    create_kid_figure,            # Factory: fig, ax = create_kid_figure("16:9")
    add_kid_header,               # Renders 3-line top header
    add_kid_footer,               # Renders bottom provenance & brand footer
    add_administration_shading,   # Adds Kibaki / Uhuru / Ruto background bands
    add_end_line_label,           # Annotates line series at terminal coordinate
    save_kid_figure               # Exports dual .png (300 DPI) and .svg files
)
```

---

## 4. Reusable Plotting Recipes

### Recipe A: Standard Multi-Line Time Series with Administration Shading

```python
import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from Code.kid_theme import (
    PALETTE, create_kid_figure, add_kid_header, add_kid_footer,
    add_administration_shading, add_end_line_label, save_kid_figure
)

# 1. Initialize 16:9 Canvas
fig, ax = create_kid_figure(aspect_ratio="16:9")

# 2. Add Presidential Shading Bands
add_administration_shading(ax, y_pos_pct=0.92)

# 3. Plot Series
ax.plot(df["year"], df["nominal_val"], color=PALETTE["red"], linewidth=3.2, marker="o")
ax.plot(df["year"], df["real_val"], color=PALETTE["navy"], linewidth=2.8, linestyle="--")

# 4. Direct End Labels (No detached legends)
last_yr = df["year"].iloc[-1]
add_end_line_label(ax, last_yr, df["nominal_val"].iloc[-1], "Nominal: KSh 11.8T", PALETTE["red"], offset_x=0.3)
add_end_line_label(ax, last_yr, df["real_val"].iloc[-1], "Real (2024): KSh 11.3T", PALETTE["navy"], offset_x=0.3)

# 5. Format Axes
ax.set_ylabel("KSh Trillions", fontsize=11, fontweight="bold")
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))

# 6. Add Branded Header & Footer
add_kid_header(fig, "FIG-DEBT-001", "Nominal vs Real Debt (2002–2026)", "Purchasing power comparison")
add_kid_footer(fig, "National Treasury ADMR FY24/25", "KNBS CPI Deflator Base 2024=100")

# 7. Export SVG + PNG
save_kid_figure(fig, "Figures/Final/FIG-DEBT-001_nominal_vs_real")
plt.close(fig)
```

### Recipe B: Stacked Area Composition Plot

```python
fig, ax = create_kid_figure(aspect_ratio="16:9")
add_administration_shading(ax, y_pos_pct=0.92)

ax.stackplot(
    df["year"],
    df["domestic_debt"],
    df["external_debt"],
    colors=[PALETTE["blue"], PALETTE["gold"]],
    alpha=0.75
)

# Label directly inside area slices
ax.text(2020.5, 1.8, "Domestic Debt\n(53.5%)", fontsize=10, fontweight="bold", color=PALETTE["white"], ha="center")
ax.text(2020.5, 5.2, "External Debt\n(46.5%)", fontsize=10, fontweight="bold", color=PALETTE["white"], ha="center")

add_kid_header(fig, "FIG-DEBT-003", "Domestic vs External Debt Mix (2002–2026)", "Evolution of Treasury debt vs foreign loans")
add_kid_footer(fig, "National Treasury PDMO Reports & CBK", "KES conversions at CBK closing fiscal rates")
save_kid_figure(fig, "Figures/Final/FIG-DEBT-003_composition")
plt.close(fig)
```

---

## 5. Cross-Project Checklist

When working on any future project (`PRJ-002`, `PRJ-003`, etc.):
- [ ] Read data from `Data/Processed/` or `Data/Raw/` via deterministic Python script.
- [ ] Never use standard floating box legends; always use `add_end_line_label`.
- [ ] Always export both `.png` (300 DPI) and `.svg` vector files using `save_kid_figure`.
- [ ] State exact source reports, table numbers, and page numbers in the footer.
- [ ] Run `python Code/sync_data_catalog.py` to register output files and SHA-256 hashes.
