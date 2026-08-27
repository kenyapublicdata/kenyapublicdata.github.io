---
title: Kenya Public Debt — Data Catalog & Inventory
project_id: PRJ-001
document_type: data_catalog
status: active
created: 2026-08-27
last_updated: 2026-08-27
tags: [data-catalog, data-inventory, raw-data, processed-data, provenance, schema]
---

# PRJ-001 Data Catalog & Inventory

> **Directory Lifecycle Standard:** `Raw Data (Immutable)` $\rightarrow$ `Interim Staging` $\rightarrow$ `Processed / Normalized` $\rightarrow$ `Published (Locked Release)`

---

## 1. Raw Machine-Readable Datasets (`Data/Raw/`)

| File Name | Topic / Measure | Temporal Coverage | Frequency | Format | Size | Rows | Primary Source | Checksum (SHA-256) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [`CBK_Annual_GDP_2000_2026.csv`](Data/Raw/CBK_Annual_GDP_2000_2026.csv) | Nominal GDP, Real GDP, Annual Growth (%) | 2000 – 2025 | Annual | CSV | 780 B | 26 | KNBS via Central Bank of Kenya | *See catalog.json* |
| [`TNT_Public_Debt_Stock_2002_2026_raw.csv`](Data/Raw/TNT_Public_Debt_Stock_2002_2026_raw.csv) | Gross Debt, Domestic vs External Stock, USD Total, FX rate | 2002 – 2026 | Annual / Handover | CSV | 2.1 KB | 25 | National Treasury ADMRs & CBK MEI | *See catalog.json* |
| [`TNT_Debt_Service_Fiscal_2002_2026_raw.csv`](Data/Raw/TNT_Debt_Service_Fiscal_2002_2026_raw.csv) | Total Debt Service, Domestic/External Interest & Principal, Ordinary Revenue | 2002 – 2026 | Annual Fiscal | CSV | 1.8 KB | 25 | National Treasury ADMRs & BROP | *See catalog.json* |
| [`KNBS_CPI_Deflators_2002_2026_raw.csv`](Data/Raw/KNBS_CPI_Deflators_2002_2026_raw.csv) | KNBS Consumer Price Index (Base 2024=100) & GDP Deflators | 2002 – 2026 | Annual | CSV | 1.1 KB | 25 | KNBS Economic Surveys | *See catalog.json* |

### Schema: `CBK_Annual_GDP_2000_2026.csv`
- `year` *(integer)*: Calendar year (2000–2025).
- `nominal_gdp_million_ksh` *(float)*: Gross Domestic Product at current market prices (KSh Millions).
- `annual_growth_pct` *(float)*: Year-on-year real GDP expansion rate (%).
- `real_gdp_million_ksh` *(float)*: Gross Domestic Product at constant base prices (KSh Millions).

---

## 2. Primary Source Documents (`Sources/Documents/`)

| File Name | Institutional Publisher | Period / Edition | Pages | Format | File Size | Primary Use in Project |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [`TNT_Annual_Public_Debt_Report_2024_2025.pdf`](Sources/Documents/TNT_Annual_Public_Debt_Report_2024_2025.pdf) | National Treasury (PDMO) | FY 2024/25 | 89 | PDF | 1.61 MB | Baseline debt stock (KSh 11.81T), debt-service ratios (71.2%), DSA assessment |
| [`TNT_Annual_Public_Debt_Report_2023_2024.pdf`](Sources/Documents/TNT_Annual_Public_Debt_Report_2023_2024.pdf) | National Treasury (PDMO) | FY 2023/24 | 79 | PDF | 1.21 MB | Ruto administration FY2023/24 debt reconciliation & Eurobond buyback data |
| [`TNT_Annual_Public_Debt_Report_2022_2023.pdf`](Sources/Documents/TNT_Annual_Public_Debt_Report_2022_2023.pdf) | National Treasury (PDMO) | FY 2022/23 | 111 | PDF | 2.10 MB | Uhuru to Ruto transition handover year & FX depreciation impact |
| [`TNT_Annual_Public_Debt_Report_2021_2022.pdf`](Sources/Documents/TNT_Annual_Public_Debt_Report_2021_2022.pdf) | National Treasury (PDMO) | FY 2021/22 | 83 | PDF | 2.12 MB | End of Uhuru Kenyatta presidency benchmark (June 2022) |
| [`TNT_Annual_Public_Debt_Report_2012_2013.pdf`](Sources/Documents/TNT_Annual_Public_Debt_Report_2012_2013.pdf) | National Treasury (PDMO) | FY 2012/13 | 68 | PDF | 2.08 MB | Kibaki to Uhuru transition handover benchmark (June 2013) |
| [`TNT_Annual_Public_Debt_Report_2005_2006.pdf`](Sources/Documents/TNT_Annual_Public_Debt_Report_2005_2006.pdf) | National Treasury (PDMO) | FY 2005/06 | 63 | PDF | 319 KB | Early Kibaki administration baseline reference |
| [`CBK_MEI_June_2026.pdf`](Sources/Documents/CBK_MEI_June_2026.pdf) | Central Bank of Kenya | June 2026 | 28 | PDF | 1.72 MB | Latest monthly public debt breakdown (Bilateral, Multilateral, Commercial, T-bills, T-bonds) |
| [`CBK_MEI_June_2024.pdf`](Sources/Documents/CBK_MEI_June_2024.pdf) | Central Bank of Kenya | June 2024 | 27 | PDF | 1.80 MB | 2023/2024 monthly debt reconciliation cross-check |

---

## 3. Interim & Staging Datasets (`Data/Interim/`)

*Staging area for parsed PDF tables, merged fiscal-calendar series, and unverified extraction tables prior to finalization.*

| File Name | Purpose | Generated From | Status |
| :--- | :--- | :--- | :--- |
| `PRJ001_debt_reconciled_staging.csv` | Reconciled 4-snapshot staging table | Treasury ADMRs + CBK MEI | Verified |

---

## 4. Processed & Normalized Datasets (`Data/Processed/`)

*Clean, reproducible datasets with standardized columns, deflator math, and explicit administration tagging.*

| File Name | Primary Indicator | Time Span | Key Derived Fields | Associated Script |
| :--- | :--- | :--- | :--- | :--- |
| [`PRJ001_public_debt_timeseries_2002_2026.csv`](Data/Processed/PRJ001_public_debt_timeseries_2002_2026.csv) | `IND-PF-001` | 2002–2026 (25 rows) | `debt_to_gdp_pct`, `real_debt_2024_ksh_bn`, `debt_service_to_revenue_pct`, `domestic_interest_to_revenue_pct` | `Code/compute_debt_series.py` |
| [`PRJ001_presidential_snapshots_2002_2026.csv`](Data/Processed/PRJ001_presidential_snapshots_2002_2026.csv) | `IND-PF-001` | 4 Handover Benchmarks | `snapshot_label`, `nominal_debt_ksh_bn`, `real_debt_2024_ksh_bn`, `debt_to_gdp_pct` | `Code/compute_debt_series.py` |

---

## 5. Published Release Data (`Data/Published/`)

*Immutable versioned datasets released with public figures and essays.*

| Release ID | Publication Title | Release Date | Included Files | Format | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `KID-001-DATA` | Kenya's Public Debt: Baseline, Historical Series & Servicing (2002–2026) | 2026-08-27 | [`KID001_Kenya_Public_Debt_2002_2026.csv`](Data/Published/KID001_Kenya_Public_Debt_2002_2026.csv)<br>[`KID001_Kenya_Public_Debt_2002_2026.xlsx`](Data/Published/KID001_Kenya_Public_Debt_2002_2026.xlsx) | CSV + Multi-sheet Excel | Published |

---

## 6. Directory Maintenance Protocol

1. **Raw Immutability Rule:** Files in `Data/Raw/` and `Sources/Documents/` are never overwritten or edited manually.
2. **Catalog Updates:** Whenever a new file is added to `Data/` or `Sources/Documents/`, run:
   ```bash
   python Code/sync_data_catalog.py
   ```
3. **No Unversioned Outputs:** Every analytical script must write to `Data/Processed/` or `Data/Published/` with explicit timestamps and source identifiers.
