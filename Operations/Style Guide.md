---
title: Kenya in Data Visual Style Guide & Design System
project: Kenya in Data
document_type: style-guide
status: active
created: 2026-08-27
last_updated: 2026-08-28
tags: [style-guide, design-system, visualization, branding, typography, color-palette]
---

# Kenya in Data — Visual Style Guide & Design System

Mobile article graphics must also follow the dedicated [Mobile Visualization Standard](Mobile%20Visualization%20Standard.md). Mobile is the primary reading canvas; article figures require deliberate responsive variants rather than mechanically scaled landscape exports.

## 1. Visual Philosophy & Core Epistemic Identity

A reader scrolling through X (Twitter), LinkedIn, WhatsApp, or a policy brief should instantly recognize a **Kenya in Data** graphic before reading the account name or title.

### The Four Pillars of Our Visual Identity
1. **Evidence-Led & High-Contrast:** Bold conclusions backed by direct data citations; zero visual clutter or decorative chart junk.
2. **Denominators First:** Never present nominal sums in isolation over time; pair them with inflation deflators and GDP/revenue denominators.
3. **Direct Labelling over Distant Legends:** Series are labelled directly at their terminal points so the eye never has to decipher disconnected legend keys.
4. **Epistemic Neutrality:** Clear visual separation between historical facts, arithmetic calculations, and institutional policy mechanisms. Shading administrations serves solely as a temporal landmark, not a partisan ranking.

---

## 2. Typography & Text Hierarchy

We use a clean, modern sans-serif typography stack optimized for legibility on high-DPI mobile screens and sharp vector SVG print/PDF outputs.

### Typography Stack
- **Primary Sans-Serif:** `Inter`, `Plus Jakarta Sans`, or `Helvetica Neue`.
- **System / Vector Fallbacks:** `Arial`, `DejaVu Sans`, `Liberation Sans`, `sans-serif`.
- **Data Tables & Code:** `JetBrains Mono`, `Fira Code`, `SF Mono`, or `Courier New`.

### Standard Type Hierarchy

| Element | Size (pt) | Weight | Color Token | Purpose & Example |
|:---|:---:|:---:|:---|:---|
| **Publication Tracker** | 10.0 pt | Bold (Uppercase) | `PALETTE["red"]` / `navy` | `KENYA IN DATA • FIG-DEBT-001` |
| **Headline / Finding** | 16.0–18.0 pt | Heavy / Bold | `PALETTE["navy"]` (`#0F172A`) | Primary conclusion or theme of the graphic |
| **Subtitle / Question** | 10.5–11.5 pt | Regular | `PALETTE["slate"]` (`#64748B`) | Research question framing the metric context |
| **Axis Titles** | 11.0 pt | Bold | `PALETTE["navy"]` (`#0F172A`) | Explicit unit (e.g. `Gross Debt (% of GDP)`) |
| **Tick Labels** | 9.5–10.0 pt | Regular | `PALETTE["slate"]` (`#64748B`) | Formatted numbers (`KSh 1.2 T`, `55.0%`) |
| **Direct Series Labels**| 9.5–10.5 pt | Bold | Series Accent Color | Terminal line/bar annotations |
| **Callout Annotations** | 9.0–9.5 pt | Semibold | `PALETTE["navy"]` | Landmark explanations (e.g. `2014 Eurobond`) |
| **Provenance Footer** | 8.5 pt | Italic | `PALETTE["slate"]` (`#64748B`) | Granular source report, table, and page number |
| **Brand Stamp** | 8.5 pt | Bold | `PALETTE["navy"]` (`#0F172A`) | `kenyaindata.org • @KenyaInData` |

---

## 3. Comprehensive Semantic Color System

Our palette balances high-contrast accessibility (WCAG AA compliance) with clear semantic associations for economic and fiscal concepts.

```text
+-----------------------------------------------------------------------------------+
| CORE CANVAS & NEUTRALS                                                            |
| #0F172A (Obsidian Navy) | #F8FAFC (Ivory Canvas) | #FFFFFF (White Card Background) |
| #64748B (Slate Grey)    | #CBD5E1 (Light Border) | #E2E8F0 (Subtle Gridlines)      |
+-----------------------------------------------------------------------------------+
| PRIMARY SEMANTIC PALETTE                                                          |
| #DC2626 (Alert Crimson)  --> Public Debt, Deficits, Inflation, Distress Ratios   |
| #059669 (Emerald Green)  --> Revenue, Real Growth, Primary Baselines             |
| #D97706 (Amber Ochre)    --> External Debt, FX, Targets, Projections             |
| #2563EB (Royal Blue)     --> Domestic Debt, Commercial Banking, Core Series      |
| #7C3AED (Violet Purple)  --> Interest Burden, Taxes, Special Interventions       |
| #0D9488 (Teal Green)     --> Per Capita Metrics, Demographics, Deflators         |
+-----------------------------------------------------------------------------------+
```

### Color Token Reference Table

| Token Name | Hex Code | Semantic Role in Economic Visualizations |
|:---|:---:|:---|
| `navy` | `#0F172A` | Primary text, titles, dark backgrounds, high-emphasis benchmarks |
| `canvas_light` | `#F8FAFC` | Default figure background canvas (crisp ivory tone) |
| `white` | `#FFFFFF` | Plot axes background card |
| `slate` | `#64748B` | Subtitles, gridlines, axis ticks, source provenance footnotes |
| `slate_light` | `#E2E8F0` | Soft borders and subtle horizontal gridlines (`--` style) |
| `red` | `#DC2626` | Public debt stock, fiscal deficit, inflation spikes, debt distress thresholds |
| `green` | `#059669` | Ordinary revenue, tax collection, real GDP growth, positive reserves |
| `gold` | `#D97706` | External debt, foreign exchange rates, statutory debt ceiling anchors |
| `blue` | `#2563EB` | Domestic debt stock (Treasury bonds/bills), banking credit metrics |
| `purple` | `#7C3AED` | Domestic interest expense, fiscal squeeze indicators, tax brackets |
| `teal` | `#0D9488` | Real deflated series (GDP deflator), per capita figures, population |

### Administration Timeline Shading Tokens

To provide historical landmark context without asserting political causality:

| Administration | Historical Period | Fill Color | Alpha (Opacity) |
|:---|:---:|:---:|:---:|
| **Mwai Kibaki** | Dec 2002 – Apr 2013 | `#CBD5E1` | `0.22` |
| **Uhuru Kenyatta** | Apr 2013 – Sep 2022 | `#94A3B8` | `0.15` |
| **William Ruto** | Sep 2022 – Ongoing | `#CBD5E1` | `0.22` |

---

## 4. Standard 3-Tier Layout Architecture

Every figure exported by Kenya in Data must follow a standardized 3-tier bounding layout:

```text
+-----------------------------------------------------------------------------------+
| TIER 1: BRANDED HEADER                                                            |
| KENYA IN DATA • [FIG-ID-001]                                                      |
| Headline: Bold Statement Summarizing the Core Observation (16pt Bold)             |
| Subtitle: Clarifying research question, unit description, or time horizon (11pt)  |
+-----------------------------------------------------------------------------------+
| TIER 2: PLOT CANVAS & DATA AREA                                                   |
|                                                                                   |
|  14 T +----------------------------------------------+ [Nominal: KSh 11.81 T]     |
|       | [KIBAKI]       | [UHURU]       | [RUTO]      |                            |
|  10 T |                |               |             |                            |
|       |                |               |   /---------+ [Real (2024): KSh 11.31 T] |
|   6 T |                |          /----+--/          |                            |
|       |                |     /---+                   |                            |
|   2 T | /--------------+----+                        |                            |
|       +----------------------------------------------+                            |
|       2002    2006    2010    2014    2018    2022   2026                         |
|                                                                                   |
+-----------------------------------------------------------------------------------+
| TIER 3: PROVENANCE FOOTER                                                         |
| Source: National Treasury ADMR FY24/25 (Table 26) & CBK MEI  | Deflator: KNBS 2024 |
|                                                kenyaindata.org • @KenyaInData     |
+-----------------------------------------------------------------------------------+
```

---

## 5. Aspect Ratios & Export Presets

All figures are generated in two simultaneous formats:
1. **High-Resolution Raster (`.png`):** 300 DPI with anti-aliasing for web, social media, and slide presentations.
2. **Scalable Vector (`.svg`):** Lossless vector curves for print reports, Figma infographic remixing, and high-DPI web embedding.

### Standard Dimensions

| Preset | Aspect Ratio | Dimensions (px) | Primary Target |
|:---|:---:|:---:|:---|
| **Landscape / Presentation** | `16:9` | `1920 x 1080` (or `1200 x 675`) | Web articles, reports, slide decks, wide screens |
| **Square Card** | `1:1` | `1080 x 1080` | LinkedIn posts, Instagram feed, WhatsApp updates |
| **Mobile Portrait** | `4:5` | `1080 x 1350` | Mobile feeds, Instagram/LinkedIn portrait carousel |
| **Wide Social Card** | `1.91:1` | `1200 x 628` | Twitter / X link cards and OpenGraph previews |

---

## 6. Chart Rules & Epistemic Standards

1. **Always State Denominators:** Never show nominal debt or revenue in isolation over time; pair with inflation adjustments and share of GDP.
2. **Zero-Based Baselines for Bars and Areas:** Bar charts and area plots must always start at zero to avoid exaggerating relative proportions.
3. **Explicit Units on Every Axis:** Format all values clearly (`KSh 1.2 Trillion`, `KSh 450.0 Billion`, `67.8% of GDP`).
4. **Annotate Structural Shocks, Not Politicians:** Call out external macroeconomic events (e.g. *2008 Global Financial Crisis*, *2014 Initial Eurobond*, *2020 COVID-19 Shock*, *2023 Shilling Depreciation*) rather than making unsupported partisan claims.
5. **Granular Citations in Footers:** Never state vague sources like "Government Data". State the exact institution, report title, table number, and page number (e.g. `Source: National Treasury ADMR FY 2024/25, Table 4, p. 30`).
