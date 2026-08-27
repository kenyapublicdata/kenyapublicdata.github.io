---
title: Kenya in Data Code & Visualization Engine
project: Kenya in Data
document_type: code-overview
status: active
created: 2026-08-27
last_updated: 2026-08-28
tags: [code, python, visualization, pipeline, data-architecture]
---

# Kenya in Data — Code & Visualization Architecture

This directory houses reproducible data pipelines, transformation scripts, the shared in-house visualization engine (`kid_theme`), and automated catalog synchronizers.

---

## 1. Directory Structure

```text
Kenya in Data/
├── Code/
│   ├── kid_theme.py           # Shared visual theme, brand tokens, admin shading & canvas factory
│   └── README.md              # Architecture and execution documentation
│
├── Projects/
│   ├── PRJ-001 Kenya Public Debt/
│   │   ├── Code/
│   │   │   ├── compute_debt_series.py    # Master data merge & multi-tab Excel generator
│   │   │   ├── generate_debt_figures.py  # Production SVG/PNG chart renderer
│   │   │   └── sync_data_catalog.py      # Checksum verifier & catalog.json builder
│   │   ├── Data/
│   │   │   ├── Raw/                      # Immutable official source CSVs
│   │   │   ├── Interim/                  # Staging joins
│   │   │   ├── Processed/                # Analysis-ready normalized series
│   │   │   └── Published/                # Release-locked CSV & multi-tab Excel
│   │   └── Figures/
│   │       ├── Drafts/                   # Working figures
│   │       └── Final/                    # Production 300 DPI PNG & SVG exports
│   │
│   └── PRJ-002 [Future Project]/         # Follows identical layout and tools
```

---

## 2. Environment Setup

The pipeline runs on Python 3.9+ with standard data and graphics dependencies:

```bash
# Create local virtual environment
python3 -m venv .venv

# Install dependencies
.venv/bin/pip install pandas matplotlib seaborn openpyxl
```

---

## 3. Plotting Library Architecture & In-House Engine

### A. Library Comparison & Role Matrix

| Framework | Role in Kenya in Data | Format Output | Why We Use It |
|:---|:---|:---|:---|
| **In-House Python (`kid_theme` + Matplotlib)** | **Primary Production Engine** | `SVG` + `PNG` (300 DPI) | 100% reproducible scripts, pixel-perfect layout control, automated 3-tier headers/footers, and presidential administration shading. |
| **Plotly / Altair (Python)** | **Exploratory & Interactive** | `HTML` / `JSON` | Dynamic zoom/hover widgets for internal research. |
| **D3.js / Observable Plot (Node/Web)** | **Web Publishing (`kenyaindata.org`)** | `DOM` / `Vector Web` | Client-side reactive charts for web portal releases. |
| **Typst / Quarto** | **Policy Reports** | `PDF` | Academic and policy brief layout. |

### B. In-House Plotting Boilerplate

Every publication figure uses the shared `kid_theme` module:

```python
import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Import shared theme
from Code.kid_theme import (
    PALETTE, apply_kid_theme, create_kid_figure,
    add_kid_header, add_kid_footer, add_administration_shading,
    add_end_line_label, save_kid_figure
)

# 1. Initialize canvas (presets: "16:9", "1:1", "4:5", "1.91:1")
fig, ax = create_kid_figure(aspect_ratio="16:9")

# 2. Add historical presidential administration shading
add_administration_shading(ax, y_pos_pct=0.92)

# 3. Plot data series
ax.plot(df["year"], df["debt_to_gdp"], color=PALETTE["red"], linewidth=3.0)

# 4. Add direct end-line labels (no floating legends)
add_end_line_label(ax, df["year"].iloc[-1], df["debt_to_gdp"].iloc[-1], "67.8% of GDP", PALETTE["red"])

# 5. Add standard 3-tier header and provenance footer
add_kid_header(
    fig,
    figure_id="FIG-DEBT-002",
    title="Public Debt as a Share of Kenya's GDP (2002–2026)",
    subtitle="Gross public debt scaled to Nominal GDP at current market prices"
)

add_kid_footer(
    fig,
    source_text="National Treasury Annual Public Debt Reports & KNBS",
    notes_text="Target reflects PFM Act 55% Present Value statutory anchor"
)

# 6. Save dual vector SVG and high-res PNG
save_kid_figure(fig, "Figures/Final/FIG-DEBT-002_public_debt_to_gdp")
plt.close(fig)
```

---

## 4. Pipeline Execution Commands

To execute the data transformations and generate all production assets from the workspace root:

```bash
# 1. Merge raw datasets and build multi-tab Excel workbooks
.venv/bin/python3 "Projects/PRJ-001 Kenya Public Debt/Code/compute_debt_series.py"

# 2. Render all publication figures (SVG and PNG)
.venv/bin/python3 "Projects/PRJ-001 Kenya Public Debt/Code/generate_debt_figures.py"

# 3. Synchronize catalog checksums (SHA-256)
.venv/bin/python3 "Projects/PRJ-001 Kenya Public Debt/Code/sync_data_catalog.py"
```
