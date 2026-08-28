# Source-checked publication data — Current Debt Baseline

This directory contains the source-checked draft dataset and metadata for publication **KID-001**. Public release remains subject to final editorial and visual QA.

The canonical editorial interpretation is maintained in [`KID-001 Current Debt Baseline.md`](../KID-001%20Current%20Debt%20Baseline.md). Data files do not independently define publication claims.

## Data Files

| File | Description | Format | Status |
|:---|:---|:---:|:---:|
| [`KID001_current_debt_baseline.csv`](KID001_current_debt_baseline.csv) | Current baseline observations: June 2025 FY outturn, May 2026 CBK snapshot, composition, debt service, domestic-interest detail and domestic holder stocks | CSV (UTF-8) | **Source checked** |
| [`data_dictionary.csv`](data_dictionary.csv) | Definitions for all 19 columns, including denominator and transformation fields | CSV (UTF-8) | **Updated** |
| [`dataset_metadata.yml`](dataset_metadata.yml) | Machine-readable coverage, license, provenance and validation summary | YAML | **Draft** |

## Key Baseline Parameters

- **Fiscal Baseline Stock (End-June 2025):** KSh 11,814.474 billion (Domestic: 53.54% / External: 46.46%)
- **Latest Complete Monthly Stock (End-May 2026):** KSh 12,896.40 billion (Domestic: 56.13% / External: 43.87%)
- **Nominal Debt-to-GDP (June 2025):** 67.8% (Nominal GDP: KSh 17,434.5B)
- **Present Value Debt-to-GDP (June 2025):** 63.7% (Statutory anchor: 55.0%)
- **FY 2024/25 Total Debt Service:** KSh 1,722.10 billion (71.16% of Ordinary Revenue)
- **FY 2024/25 Domestic Interest:** KSh 776.257 billion (32.07% of Ordinary Revenue)
- **FY 2024/25 Weighted Average Interest Rates:** Domestic 13.0%; External 3.9%; Total Public Debt 8.7%

## Important limitations

- May 2026 debt values do not have a matched May 2026 GDP denominator in this release; no May 2026 debt-to-GDP ratio is calculated.
- The June 2026 domestic-debt figure is a partial observation and is excluded from this release dataset because the corresponding external-debt total was unavailable in the same bulletin.
- Treasury June 2025 and CBK May 2026 observations come from different official releases. The change between them is descriptive and may include classification or revision effects.
- The Treasury's holder categories sum to KSh 1 million more than the reported domestic-debt total because the source table is rounded. Holder stocks are not interpreted as annual interest receipts.
