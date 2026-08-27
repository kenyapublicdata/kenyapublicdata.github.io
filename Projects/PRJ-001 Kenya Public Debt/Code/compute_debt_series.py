#!/usr/bin/env python3
"""
PRJ-001 Kenya Public Debt — Master Data Transformation & Harmonization Script
=============================================================================
Merges raw debt stock, debt service, GDP, and CPI deflator series from 2002 to 2026.
Produces:
1. Data/Processed/PRJ001_public_debt_timeseries_2002_2026.csv
2. Data/Processed/PRJ001_presidential_snapshots_2002_2026.csv
3. Data/Published/KID001_Kenya_Public_Debt_2002_2026.csv
4. Data/Published/KID001_Kenya_Public_Debt_2002_2026.xlsx (Formatted Multi-tab Excel)
"""

import sys
from pathlib import Path
import pandas as pd

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR
DATA_DIR = BASE_DIR / "Data"
RAW_DIR = DATA_DIR / "Raw"
PROCESSED_DIR = DATA_DIR / "Processed"
PUBLISHED_DIR = DATA_DIR / "Published"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)

def run_pipeline():
    print("[1/5] Loading Raw Source Files...")
    df_debt = pd.read_csv(RAW_DIR / "TNT_Public_Debt_Stock_2002_2026_raw.csv")
    df_service = pd.read_csv(RAW_DIR / "TNT_Debt_Service_Fiscal_2002_2026_raw.csv")
    df_cpi = pd.read_csv(RAW_DIR / "KNBS_CPI_Deflators_2002_2026_raw.csv")
    df_gdp = pd.read_csv(RAW_DIR / "CBK_Annual_GDP_2000_2026.csv")

    print("[2/5] Merging Datasets...")
    # Harmonize column types
    df_debt["calendar_year"] = df_debt["calendar_year"].astype(int)
    df_service["calendar_year"] = df_service["calendar_year"].astype(int)
    df_cpi["year"] = df_cpi["year"].astype(int)
    df_gdp["year"] = df_gdp["year"].astype(int)

    # Merge debt stock with debt service
    merged = pd.merge(
        df_debt,
        df_service.drop(columns=["source_document"]),
        on=["fiscal_year", "calendar_year"],
        how="inner"
    )

    # Merge with CPI deflators
    merged = pd.merge(
        merged,
        df_cpi[["year", "cpi_index_2024_base", "annual_inflation_pct", "gdp_deflator_index"]],
        left_on="calendar_year",
        right_on="year",
        how="left"
    ).drop(columns=["year"])

    # Merge with GDP
    merged = pd.merge(
        merged,
        df_gdp[["year", "nominal_gdp_million_ksh", "real_gdp_million_ksh", "annual_growth_pct"]],
        left_on="calendar_year",
        right_on="year",
        how="left"
    ).drop(columns=["year"])

    print("[3/5] Computing Derived Metrics & Deflators...")
    # Convert nominal GDP to Billions KSh
    merged["nominal_gdp_ksh_bn"] = merged["nominal_gdp_million_ksh"] / 1000.0
    merged["real_gdp_ksh_bn"] = merged["real_gdp_million_ksh"] / 1000.0

    # Debt-to-GDP (%)
    merged["debt_to_gdp_pct"] = (merged["total_public_debt_ksh_bn"] / merged["nominal_gdp_ksh_bn"]) * 100.0

    # Real Debt Stock (Constant 2024 Prices in KSh Billions)
    merged["real_debt_2024_ksh_bn"] = merged["total_public_debt_ksh_bn"] * (100.0 / merged["cpi_index_2024_base"])

    # Shares of Debt Composition (%)
    merged["domestic_debt_share_pct"] = (merged["domestic_debt_ksh_bn"] / merged["total_public_debt_ksh_bn"]) * 100.0
    merged["external_debt_share_pct"] = (merged["external_debt_ksh_bn"] / merged["total_public_debt_ksh_bn"]) * 100.0

    # Fiscal Servicing Ratios (%)
    merged["debt_service_to_revenue_pct"] = (merged["total_debt_service_ksh_bn"] / merged["ordinary_revenue_ksh_bn"]) * 100.0
    merged["domestic_interest_to_revenue_pct"] = (merged["domestic_interest_ksh_bn"] / merged["ordinary_revenue_ksh_bn"]) * 100.0
    merged["external_interest_to_revenue_pct"] = (merged["external_interest_ksh_bn"] / merged["ordinary_revenue_ksh_bn"]) * 100.0
    merged["debt_service_to_expenditure_pct"] = (merged["total_debt_service_ksh_bn"] / merged["total_expenditure_ksh_bn"]) * 100.0

    # Round floats for cleanliness
    float_cols = [c for c in merged.columns if merged[c].dtype == "float64"]
    merged[float_cols] = merged[float_cols].round(2)

    # Save Processed Master Timeseries
    processed_csv = PROCESSED_DIR / "PRJ001_public_debt_timeseries_2002_2026.csv"
    merged.to_csv(processed_csv, index=False)
    print(f" -> Saved processed master series ({len(merged)} rows): {processed_csv.name}")

    # Build Key Handover Snapshots Table (The 4 verified landmarks)
    # 1. 2002/03 (Kibaki Inauguration Baseline)
    # 2. 2012/13 (Kibaki to Uhuru Handover)
    # 3. 2021/22 (Uhuru to Ruto Handover)
    # 4. 2024/25 - 2025/26 (Latest Verified Baseline / Current)
    target_years = [2003, 2013, 2022, 2025]
    snapshots = merged[merged["calendar_year"].isin(target_years)].copy()
    snapshots["snapshot_label"] = [
        "1. Kibaki Inauguration Baseline (June 2003)",
        "2. Kibaki to Uhuru Handover (June 2013)",
        "3. Uhuru to Ruto Handover (June 2022)",
        "4. Current Verified Baseline (June 2025)"
    ]
    snapshots_csv = PROCESSED_DIR / "PRJ001_presidential_snapshots_2002_2026.csv"
    snapshots.to_csv(snapshots_csv, index=False)
    print(f" -> Saved presidential snapshots ({len(snapshots)} rows): {snapshots_csv.name}")

    # Save Published CSV
    published_csv = PUBLISHED_DIR / "KID001_Kenya_Public_Debt_2002_2026.csv"
    merged.to_csv(published_csv, index=False)
    print(f" -> Saved published release CSV: {published_csv.name}")

    print("[4/5] Generating Multi-Tab Formatted Excel Workbook...")
    excel_path = PUBLISHED_DIR / "KID001_Kenya_Public_Debt_2002_2026.xlsx"
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        # Sheet 1: Master Time Series
        merged.to_excel(writer, sheet_name="Debt Time Series 2002-2026", index=False)
        
        # Sheet 2: Presidential Snapshots
        snapshots.to_excel(writer, sheet_name="Key Snapshots", index=False)
        
        # Sheet 3: Data Dictionary
        dict_data = {
            "Variable Name": [
                "fiscal_year", "calendar_year", "observation_date", "administration",
                "domestic_debt_ksh_bn", "external_debt_ksh_bn", "total_public_debt_ksh_bn",
                "real_debt_2024_ksh_bn", "nominal_gdp_ksh_bn", "debt_to_gdp_pct",
                "ordinary_revenue_ksh_bn", "total_debt_service_ksh_bn", "domestic_interest_ksh_bn",
                "external_interest_ksh_bn", "debt_service_to_revenue_pct", "domestic_interest_to_revenue_pct"
            ],
            "Unit": [
                "Fiscal Year (Jul-Jun)", "Calendar Year", "YYYY-MM-DD", "Presidential Administration",
                "KSh Billion", "KSh Billion", "KSh Billion",
                "Constant 2024 KSh Billion", "KSh Billion", "% of GDP",
                "KSh Billion", "KSh Billion", "KSh Billion",
                "KSh Billion", "% of Ordinary Revenue", "% of Ordinary Revenue"
            ],
            "Description": [
                "Government of Kenya Fiscal Year", "Year of observation at end-June", "Exact reporting date", "Governing regime context",
                "Gross Domestic Public Debt (Treasury Bills, Bonds, Advances)", "Gross External Public Debt (Multilateral, Bilateral, Eurobonds)", "Total Gross Public Debt Stock",
                "Nominal Debt deflated using KNBS Consumer Price Index (Base 2024=100)", "Nominal GDP at current market prices", "Total Public Debt divided by Nominal GDP",
                "Ordinary tax revenues collected by KRA", "Total debt servicing outflow (Principal + Interest)", "Interest paid on domestic debt instruments",
                "Interest paid on external loans & Eurobonds", "Total Debt Service as percentage of Ordinary Revenue", "Domestic interest expense as percentage of Ordinary Revenue"
            ]
        }
        df_dict = pd.DataFrame(dict_data)
        df_dict.to_excel(writer, sheet_name="Data Dictionary", index=False)

        # Sheet 4: Sources & Provenance
        sources_data = {
            "Source ID": ["TNT-ADMR", "CBK-MEI", "KNBS-ES", "CBK-GDP"],
            "Institutional Publisher": [
                "National Treasury of Kenya (Public Debt Management Office)",
                "Central Bank of Kenya (CBK)",
                "Kenya National Bureau of Statistics (KNBS)",
                "Central Bank of Kenya / KNBS"
            ],
            "Reports Used": [
                "Annual Public Debt Reports (FY 2005/06 to FY 2024/25)",
                "Monthly Economic Indicators (June 2024, June 2026)",
                "Annual Economic Surveys (2007 to 2026 editions)",
                "Annual GDP Historical Series (2000 to 2026)"
            ],
            "Citation Standard": [
                "National Treasury, Annual Debt Report, Chapter 5 & Table 26",
                "CBK MEI, Table 7.1 (Gross Public Debt)",
                "KNBS Consumer Price Indices & Deflators",
                "CBK National Accounts Data Portal"
            ]
        }
        df_sources = pd.DataFrame(sources_data)
        df_sources.to_excel(writer, sheet_name="Sources & Provenance", index=False)

    print(f" -> Saved formatted Excel Workbook: {excel_path.name}")
    print("[5/5] Pipeline successfully completed!")

if __name__ == "__main__":
    run_pipeline()
