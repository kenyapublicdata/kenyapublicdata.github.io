# Publication charts — KID-001

Canonical source: [`KID-001 Current Debt Baseline.md`](../../KID-001%20Current%20Debt%20Baseline.md).

These charts are derived from the source-checked publication CSV. Internal figure IDs remain in filenames for asset control but are not displayed in the visible chart header.

## Chart set

| Asset | Purpose | PNG | Vector files | Article use |
|---|---|---|---|:---:|
| 001 | May 2026 domestic/external composition | [PNG](FIG-KID001-001_current_debt_composition.png) | [SVG](FIG-KID001-001_current_debt_composition.svg) · [PDF](FIG-KID001-001_current_debt_composition.pdf) | Yes |
| 002 | Debt-service components as comparable amounts | [PNG](FIG-KID001-002_debt_service_components.png) | [SVG](FIG-KID001-002_debt_service_components.svg) · [PDF](FIG-KID001-002_debt_service_components.pdf) | Alternative |
| 003 | Domestic interest components as comparable amounts | [PNG](FIG-KID001-003_domestic_interest_by_instrument.png) | [SVG](FIG-KID001-003_domestic_interest_by_instrument.svg) · [PDF](FIG-KID001-003_domestic_interest_by_instrument.pdf) | Alternative |
| 004 | June 2025 debt stock by instrument and creditor | [PNG](FIG-KID001-004_june_2025_debt_components.png) | [SVG](FIG-KID001-004_june_2025_debt_components.svg) · [PDF](FIG-KID001-004_june_2025_debt_components.pdf) | Yes |
| 005 | Debt-service composition as an additive 100% bar | [PNG](FIG-KID001-005_debt_service_composition.png) | [SVG](FIG-KID001-005_debt_service_composition.svg) · [PDF](FIG-KID001-005_debt_service_composition.pdf) | Yes |
| 006 | Domestic interest composition as an additive 100% bar | [PNG](FIG-KID001-006_domestic_interest_composition.png) | [SVG](FIG-KID001-006_domestic_interest_composition.svg) · [PDF](FIG-KID001-006_domestic_interest_composition.pdf) | Yes |
| 007 | Domestic debt holders | [PNG](FIG-KID001-007_domestic_debt_holders.png) | [SVG](FIG-KID001-007_domestic_debt_holders.svg) · [PDF](FIG-KID001-007_domestic_debt_holders.pdf) | Yes |
| 008 | Weighted average interest rates | [PNG](FIG-KID001-008_weighted_average_interest_rates.png) | [SVG](FIG-KID001-008_weighted_average_interest_rates.svg) · [PDF](FIG-KID001-008_weighted_average_interest_rates.pdf) | Yes |

Every PNG is 3600 × 2025 px at 300 DPI. Every chart is also exported as SVG and PDF. Visible chart attribution follows this format:

- `Data: [primary source and exact location]`
- `Analysis and visualisation: Kenya in Data • kenyaindata.org`

## Alt text

### 001 — Current debt composition

A horizontal stacked bar shows Kenya's May 2026 public and publicly guaranteed debt of KSh 12.896 trillion. Domestic debt is KSh 7.239 trillion, or 56.1%, and external debt is KSh 5.657 trillion, or 43.9%.

### 002 — Debt-service amounts

Four horizontal bars compare FY 2024/25 debt service. Domestic interest is KSh 776.3 billion and external interest is KSh 211.2 billion. Domestic principal is KSh 366.8 billion and external principal is KSh 367.8 billion.

### 003 — Domestic interest amounts

Three horizontal bars show FY 2024/25 domestic interest and charges. Treasury bonds account for KSh 677.8 billion, Treasury bills KSh 87.6 billion and other charges KSh 10.9 billion.

### 004 — June 2025 debt components

A ranked horizontal bar chart shows the June 2025 public debt stock by component. Domestic Treasury bonds are 43.3% of the total, followed by external multilateral debt at 25.8%, external commercial debt at 11.2%, external bilateral debt at 9.4% and domestic Treasury bills at 8.8%. Other categories account for less than 2% each.

### 005 — Debt-service composition

A 100% stacked bar shows FY 2024/25 debt service. Domestic interest accounts for 45.1%, external interest 12.3%, domestic principal 21.3% and external principal 21.4%. Total debt service is KSh 1.722 trillion, equivalent to 71.2% of ordinary revenue.

### 006 — Domestic interest composition

A 100% stacked bar shows FY 2024/25 domestic interest and charges. Treasury bonds account for KSh 677.8 billion or 87.3%, Treasury bills KSh 87.6 billion or 11.3%, and other charges KSh 10.9 billion or 1.4%.

### 007 — Domestic debt holders

A ranked horizontal bar chart shows domestic debt holders at June 2025. Commercial banks hold 34.7%, pension funds 14.1%, government and parastatals 13.8%, insurance companies 12.6%, other investors 11.5%, households 6.0%, non-residents 4.4% and the Central Bank of Kenya 2.7%.

### 008 — Weighted average interest rates

Three horizontal bars show FY 2024/25 weighted average interest rates: domestic debt at 13.0%, total public debt at 8.7% and external debt at 3.9%.

## Source map

| Asset | Primary data source |
|---|---|
| 001 | CBK, *Monthly Economic Indicators: June 2026*, Table 7.1, p. 22 |
| 002 and 005 | National Treasury, *Annual Public Debt Management Report FY 2024/25*, Table 4, p. 30 |
| 003 and 006 | National Treasury, same report, Table 9, p. 44 |
| 004 | National Treasury, same report, Tables 5 and 10, pp. 34 and 45 |
| 007 | National Treasury, same report, Table 6, p. 36 |
| 008 | National Treasury, same report, Section 9.3 and Figure 17, p. 68 |

## Rebuild

[`build_article_charts.py`](build_article_charts.py) reads only the publication CSV and regenerates all 24 chart files. Use the project's Python environment with a non-interactive plotting backend.

## Scope boundary

The older historical figures in the project's main `Figures` folders are research artifacts and are excluded from this current-baseline article. Any new public claim must first be added to the canonical article and publication dataset.
