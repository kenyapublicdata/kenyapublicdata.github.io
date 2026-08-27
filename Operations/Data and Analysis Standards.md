---
title: Kenya in Data Data and Analysis Standards
project: Kenya in Data
document_type: operations-standard
status: active
created: 2026-08-28
last_updated: 2026-08-28
tags: [operations, data-standards, analysis-methodology, reproducibility, provenance]
---

# Kenya in Data — Data & Analysis Standards

This document codifies the operational standards, analytical methodology, and data management lifecycle for all research projects and publications within **Kenya in Data**.

---

## 1. The Four-Tier Epistemic Separation Rule

To maintain trust and epistemic integrity, every publication and data analysis strictly separates four tiers of information:

```text
+-------------------------------------------------------------------------+
| TIER 1: FACT (Direct Official Observation)                              |
| "The National Treasury reports total PPG debt was KSh 11.814 Trillion." |
+-------------------------------------------------------------------------+
                                    ↓
+-------------------------------------------------------------------------+
| TIER 2: CALCULATION (Transparent Arithmetic)                            |
| "Dividing debt by nominal GDP of KSh 17.434 T yields a ratio of 67.8%." |
+-------------------------------------------------------------------------+
                                    ↓
+-------------------------------------------------------------------------+
| TIER 3: INTERPRETATION (Economic Mechanisms & Context)                  |
| "Domestic interest absorbs 32.1% of revenue due to high T-bill yields." |
+-------------------------------------------------------------------------+
                                    ↓
+-------------------------------------------------------------------------+
| TIER 4: JUDGMENT (Moral / Political Assertions)                         |
| "This borrowing is irresponsible."  --> [LEFT STRICTLY TO THE READER]   |
+-------------------------------------------------------------------------+
```

> **Core Mandate:** Kenya in Data produces content strictly in **Tiers 1, 2, and 3**. We provide transparent data, rigorous calculations, and clear explanations of economic mechanisms. Moral, electoral, and political judgments are left entirely to the reader.

---

## 2. The Four-Stage Data Directory Lifecycle

Every research project (`PRJ-001`, `PRJ-002`, etc.) must organize its data into four strictly defined directory stages:

```text
Project_Root/
└── Data/
    ├── Raw/         # 1. IMMUTABLE ORIGINAL EXTRACTS
    │   └── Official CSVs, TSVs, raw Excel extracts, and source PDFs. Never edited manually.
    │
    ├── Interim/     # 2. STAGING & RECONCILIATION
    │   └── Intermediate joins, calendar-to-fiscal year mappings, and preliminary extraction tables.
    │
    ├── Processed/   # 3. NORMALIZED & DERIVED ANALYSIS TABLES
    │   └── Tidy CSV datasets with standard snake_case columns, deflators, and computed ratios.
    │
    └── Published/   # 4. RELEASE-LOCKED PUBLIC ARTIFACTS
        └── Versioned release datasets (.csv + multi-tab .xlsx) with checksums and data dictionaries.
```

### Protocol & Checksum Maintenance
1. **Raw Immutability Rule:** Files in `Data/Raw/` and `Sources/Documents/` are immutable primary records.
2. **Deterministic Scripts:** Transformations from `Data/Raw/` to `Data/Processed/` must be 100% reproducible via a Python script located in `Code/` (e.g. `Code/compute_debt_series.py`).
3. **Catalog Synchronization:** Every time data files are added or updated, run the project synchronizer:
   ```bash
   python Code/sync_data_catalog.py
   ```
   This generates `Data/catalog.json` with SHA-256 cryptographic checksums for every data asset.

---

## 3. The Denominator & Deflator Mandate

Raw nominal figures in Kenyan public debate frequently distort historical reality due to inflation, population expansion, and macroeconomic growth.

### A. Inflation Deflator Standard
- **Consumer Purchasing Context (CPI):** Use the KNBS Consumer Price Index series rebased to the latest benchmark year (e.g. Base 2024 = 100.0) to compute constant-price series:
  $$\text{Real Value}_{\text{Base Year}} = \text{Nominal Value}_t \times \left( \frac{\text{CPI}_{\text{Base}}}{\text{CPI}_t} \right)$$
- **Macroeconomic & National Accounts Context (GDP Deflator):** For macroeconomic aggregates and capital stock, compute real figures using the official KNBS GDP deflator series.

### B. Denominators & Scaling
Whenever a multi-year trend is presented:
1. **Macroeconomic Scale:** Pair absolute amounts with **% of Nominal GDP**.
2. **Fiscal Burden Scale:** For debt service, expenditures, and deficits, pair nominal totals with **% of Ordinary Tax Revenue** to reflect true liquidity burden.
3. **Demographic Scale:** Where public expenditure or social metrics are evaluated, provide **Per Capita** amounts alongside national aggregates.

---

## 4. Multi-Sheet Published Excel Standard

Every published dataset released to the public (`Data/Published/`) must be provided in two formats:
1. **Tidy CSV (`.csv`):** Open, UTF-8 encoded, comma-separated table for data analysts, researchers, and code pipelines.
2. **Structured Excel Workbook (`.xlsx`):** A formatted, multi-tab workbook containing:
   - **Sheet 1: Master Time Series** (Full annual/quarterly historical data).
   - **Sheet 2: Key Benchmarks / Snapshots** (Handover points, baseline comparisons).
   - **Sheet 3: Data Dictionary** (Variable names, exact units, definitions, formulas).
   - **Sheet 4: Sources & Provenance** (Source document names, publishing institutions, tables, and access links).

---

## 5. Pre-Publication Verification Gate

Before any figure, analysis note, or data table is released:
- [ ] **Exact Provenance:** Every single plotted value is traceable to a specific official document, table, and page number in `Sources/Documents/`.
- [ ] **Dual Export Generated:** Both high-res raster (`.png` at 300 DPI) and scalable vector (`.svg`) files are saved in `Figures/Final/`.
- [ ] **Direct End-Labels:** Line and bar series have direct end-point labels rather than detached legends.
- [ ] **Administration Landmarks:** Presidential tenures are shaded neutrally using standard tokens without claiming direct political causality.
- [ ] **Arithmetic Verification:** All derived percentages and sums are verified against underlying source tables.
- [ ] **Checksum Registered:** `python Code/sync_data_catalog.py` has been executed and `Data/catalog.json` is up to date.
