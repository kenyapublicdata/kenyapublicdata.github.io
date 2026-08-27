#!/usr/bin/env python3
"""
PRJ-001 Kenya Public Debt — Figure Generation Engine
=====================================================
Generates publication-ready figures conforming to Kenya in Data Style Guide:
- FIG-DEBT-001: Nominal vs Real Public Debt (2002–2026)
- FIG-DEBT-002: Public Debt as % of GDP (2002–2026)
- FIG-DEBT-003: Domestic vs External Debt Composition (2002–2026)
- FIG-DEBT-004: Debt Servicing as % of Tax Revenue & Domestic Interest Squeeze (2002–2026)

Exports to:
- Figures/Drafts/ (Working SVG and PNG)
- Figures/Final/ (Production SVG and PNG)
"""

import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Add workspace root to Python path to import kid_theme
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(WORKSPACE_ROOT / "Code"))

try:
    from kid_theme import (
        PALETTE, apply_kid_theme, add_kid_header, add_kid_footer,
        add_administration_shading, add_end_line_label, save_kid_figure
    )
except ImportError:
    # Fallback path if run from different cwd
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
    from Code.kid_theme import (
        PALETTE, apply_kid_theme, add_kid_header, add_kid_footer,
        add_administration_shading, add_end_line_label, save_kid_figure
    )

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "Data" / "Processed" / "PRJ001_public_debt_timeseries_2002_2026.csv"
FIGURES_FINAL = PROJECT_DIR / "Figures" / "Final"
FIGURES_DRAFTS = PROJECT_DIR / "Figures" / "Drafts"

FIGURES_FINAL.mkdir(parents=True, exist_ok=True)
FIGURES_DRAFTS.mkdir(parents=True, exist_ok=True)

def generate_all_figures():
    apply_kid_theme()
    print("[1/5] Loading processed dataset...")
    df = pd.read_csv(DATA_PATH)

    # -------------------------------------------------------------------------
    # FIG-DEBT-001: Nominal vs Real Public Debt (2002–2026)
    # -------------------------------------------------------------------------
    print("[2/5] Generating FIG-DEBT-001: Nominal vs Real Public Debt...")
    fig, ax = plt.subplots(figsize=(12, 6.75)) # 16:9 aspect ratio
    
    # Background admin shading
    add_administration_shading(ax, y_pos_pct=0.92)
    
    # Plot Lines
    line_nominal, = ax.plot(
        df["calendar_year"], df["total_public_debt_ksh_bn"] / 1000.0,
        color=PALETTE["red"], linewidth=3.2, marker="o", markersize=5,
        label="Nominal Debt (Current KSh Trillion)"
    )
    line_real, = ax.plot(
        df["calendar_year"], df["real_debt_2024_ksh_bn"] / 1000.0,
        color=PALETTE["navy"], linewidth=2.8, linestyle="--", marker="s", markersize=4.5,
        label="Real Debt (Constant 2024 KSh Trillion)"
    )
    
    # Axes styling
    ax.set_xlim(2001.5, 2027.8)
    ax.set_ylim(0, 14.0)
    ax.set_ylabel("KSh Trillions", fontsize=11, fontweight="bold", labelpad=10)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("KSh %.1f T"))
    
    # Direct end-line labels
    last_year = df["calendar_year"].iloc[-1]
    last_nom = df["total_public_debt_ksh_bn"].iloc[-1] / 1000.0
    last_real = df["real_debt_2024_ksh_bn"].iloc[-1] / 1000.0
    
    add_end_line_label(ax, last_year, last_nom, f"Nominal: KSh {last_nom:.2f}T", PALETTE["red"], offset_x=0.4, offset_y=0.1)
    add_end_line_label(ax, last_year, last_real, f"Real (2024): KSh {last_real:.2f}T", PALETTE["navy"], offset_x=0.4, offset_y=-0.3)
    
    # Callout annotation for 2013 handover
    val_2013 = df.loc[df["calendar_year"] == 2013, "total_public_debt_ksh_bn"].values[0] / 1000.0
    ax.annotate(
        f"2013 Handover\nKSh {val_2013:.2f}T",
        xy=(2013, val_2013),
        xytext=(2010.5, 3.8),
        arrowprops=dict(arrowstyle="->", color=PALETTE["slate"], lw=1.2),
        fontsize=9,
        fontweight="semibold",
        color=PALETTE["navy"],
        ha="center"
    )

    # Headers & Footers
    add_kid_header(
        fig,
        figure_id="FIG-DEBT-001",
        title="Nominal vs. Inflation-Adjusted Public Debt (2002–2026)",
        subtitle="Gross public debt in current prices vs constant 2024 shillings (KNBS CPI Deflator)"
    )
    add_kid_footer(
        fig,
        source_text="National Treasury Annual Public Debt Reports & CBK Monthly Economic Indicators",
        notes_text="CPI base 2024=100 | Deflator series sourced from KNBS Economic Surveys"
    )
    
    save_kid_figure(fig, FIGURES_FINAL / "FIG-DEBT-001_nominal_vs_real_public_debt")
    save_kid_figure(fig, FIGURES_DRAFTS / "FIG-DEBT-001_nominal_vs_real_public_debt")
    plt.close(fig)

    # -------------------------------------------------------------------------
    # FIG-DEBT-002: Public Debt as % of GDP (2002–2026)
    # -------------------------------------------------------------------------
    print("[3/5] Generating FIG-DEBT-002: Public Debt as % of GDP...")
    fig, ax = plt.subplots(figsize=(12, 6.75))
    add_administration_shading(ax, y_pos_pct=0.92)
    
    # Statutory & IMF reference lines
    ax.axhline(55.0, color=PALETTE["gold"], linestyle=":", linewidth=1.8, label="Statutory Debt Anchor (55% PV Target)")
    ax.text(2002.5, 56.0, "Statutory Debt Anchor Target (55% of GDP)", fontsize=8.5, color=PALETTE["gold"], fontweight="bold")
    
    # Plot line
    ax.plot(
        df["calendar_year"], df["debt_to_gdp_pct"],
        color=PALETTE["red"], linewidth=3.2, marker="o", markersize=5.5
    )
    
    ax.set_xlim(2001.5, 2027.8)
    ax.set_ylim(0, 85.0)
    ax.set_ylabel("Public Debt (% of Nominal GDP)", fontsize=11, fontweight="bold", labelpad=10)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
    ax.yaxis.set_major_formatter(ticker.PercentFormatter())
    
    # End label
    last_ratio = df["debt_to_gdp_pct"].iloc[-1]
    add_end_line_label(ax, last_year, last_ratio, f"{last_ratio:.1f}% of GDP", PALETTE["red"], offset_x=0.4)
    
    # Handover annotations
    gdp_2003 = df.loc[df["calendar_year"] == 2003, "debt_to_gdp_pct"].values[0]
    gdp_2013 = df.loc[df["calendar_year"] == 2013, "debt_to_gdp_pct"].values[0]
    gdp_2022 = df.loc[df["calendar_year"] == 2022, "debt_to_gdp_pct"].values[0]
    
    ax.scatter([2003, 2013, 2022], [gdp_2003, gdp_2013, gdp_2022], color=PALETTE["navy"], s=50, zorder=5)
    ax.annotate(f"2003: {gdp_2003:.1f}%", xy=(2003, gdp_2003), xytext=(2003.5, 71.0),
                arrowprops=dict(arrowstyle="->", color=PALETTE["slate"]), fontsize=8.5, fontweight="semibold")
    ax.annotate(f"2013: {gdp_2013:.1f}%", xy=(2013, gdp_2013), xytext=(2013, 23.0),
                arrowprops=dict(arrowstyle="->", color=PALETTE["slate"]), fontsize=8.5, fontweight="semibold")
    ax.annotate(f"2022: {gdp_2022:.1f}%", xy=(2022, gdp_2022), xytext=(2020.0, 75.0),
                arrowprops=dict(arrowstyle="->", color=PALETTE["slate"]), fontsize=8.5, fontweight="semibold")

    add_kid_header(
        fig,
        figure_id="FIG-DEBT-002",
        title="Public Debt as a Share of Kenya's GDP (2002–2026)",
        subtitle="Gross public debt scaled to Nominal GDP at current market prices (KNBS Rebased Series)"
    )
    add_kid_footer(
        fig,
        source_text="National Treasury Annual Public Debt Reports & KNBS National Accounts / CBK",
        notes_text="Includes 2014 & 2021 KNBS GDP revisions | Target reflects PFM Act Medium-Term Anchor"
    )
    
    save_kid_figure(fig, FIGURES_FINAL / "FIG-DEBT-002_public_debt_to_gdp")
    save_kid_figure(fig, FIGURES_DRAFTS / "FIG-DEBT-002_public_debt_to_gdp")
    plt.close(fig)

    # -------------------------------------------------------------------------
    # FIG-DEBT-003: Domestic vs External Debt Composition (2002–2026)
    # -------------------------------------------------------------------------
    print("[4/5] Generating FIG-DEBT-003: Domestic vs External Composition...")
    fig, ax = plt.subplots(figsize=(12, 6.75))
    add_administration_shading(ax, y_pos_pct=0.92)
    
    # Plot Stacked Area
    ax.stackplot(
        df["calendar_year"],
        df["domestic_debt_ksh_bn"] / 1000.0,
        df["external_debt_ksh_bn"] / 1000.0,
        labels=["Domestic Debt (Bonds & Bills)", "External Debt (Multilateral, Bilateral, Eurobonds)"],
        colors=[PALETTE["blue"], PALETTE["gold"]],
        alpha=0.75
    )
    
    ax.plot(df["calendar_year"], df["total_public_debt_ksh_bn"] / 1000.0, color=PALETTE["navy"], linewidth=2.0)
    
    ax.set_xlim(2001.5, 2027.8)
    ax.set_ylim(0, 14.0)
    ax.set_ylabel("Gross Debt Stock (KSh Trillions)", fontsize=11, fontweight="bold", labelpad=10)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("KSh %.1f T"))
    
    # Direct annotations within stacked areas
    ax.text(2020.5, 1.8, "Domestic Debt\n(53.5%)", fontsize=10, fontweight="bold", color=PALETTE["white"], ha="center")
    ax.text(2020.5, 5.2, "External Debt\n(46.5%)", fontsize=10, fontweight="bold", color=PALETTE["white"], ha="center")

    add_kid_header(
        fig,
        figure_id="FIG-DEBT-003",
        title="Domestic vs. External Public Debt Mix (2002–2026)",
        subtitle="Evolution of Treasury securities vs foreign loans and Eurobonds in KSh Trillions"
    )
    add_kid_footer(
        fig,
        source_text="National Treasury Public Debt Management Office (PDMO) Reports & CBK",
        notes_text="External debt converted to KES at closing fiscal-year CBK mean exchange rates"
    )
    
    save_kid_figure(fig, FIGURES_FINAL / "FIG-DEBT-003_domestic_vs_external_composition")
    save_kid_figure(fig, FIGURES_DRAFTS / "FIG-DEBT-003_domestic_vs_external_composition")
    plt.close(fig)

    # -------------------------------------------------------------------------
    # FIG-DEBT-004: The Debt Servicing Squeeze (2002–2026)
    # -------------------------------------------------------------------------
    print("[5/5] Generating FIG-DEBT-004: The Debt Servicing Squeeze...")
    fig, ax = plt.subplots(figsize=(12, 6.75))
    add_administration_shading(ax, y_pos_pct=0.92)
    
    # Total Debt Service as % of Revenue
    ax.plot(
        df["calendar_year"], df["debt_service_to_revenue_pct"],
        color=PALETTE["red"], linewidth=3.2, marker="o", markersize=5,
        label="Total Debt Service (% of Tax Revenue)"
    )
    
    # Domestic Interest as % of Revenue
    ax.plot(
        df["calendar_year"], df["domestic_interest_to_revenue_pct"],
        color=PALETTE["purple"], linewidth=2.6, linestyle="--", marker="^", markersize=4.5,
        label="Domestic Interest Alone (% of Tax Revenue)"
    )
    
    # External Interest as % of Revenue
    ax.plot(
        df["calendar_year"], df["external_interest_to_revenue_pct"],
        color=PALETTE["gold"], linewidth=2.2, linestyle=":", marker="v", markersize=4.0,
        label="External Interest Alone (% of Tax Revenue)"
    )
    
    ax.set_xlim(2001.5, 2028.5)
    ax.set_ylim(0, 90.0)
    ax.set_ylabel("% of Ordinary Tax Revenue", fontsize=11, fontweight="bold", labelpad=10)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
    ax.yaxis.set_major_formatter(ticker.PercentFormatter())
    
    # End labels
    last_tot_serv = df["debt_service_to_revenue_pct"].iloc[-1]
    last_dom_int = df["domestic_interest_to_revenue_pct"].iloc[-1]
    last_ext_int = df["external_interest_to_revenue_pct"].iloc[-1]
    
    add_end_line_label(ax, last_year, last_tot_serv, f"Total Debt Service: {last_tot_serv:.1f}%", PALETTE["red"], offset_x=0.4, offset_y=0.5)
    add_end_line_label(ax, last_year, last_dom_int, f"Domestic Interest: {last_dom_int:.1f}%", PALETTE["purple"], offset_x=0.4, offset_y=0.0)
    add_end_line_label(ax, last_year, last_ext_int, f"External Interest: {last_ext_int:.1f}%", PALETTE["gold"], offset_x=0.4, offset_y=-0.5)

    add_kid_header(
        fig,
        figure_id="FIG-DEBT-004",
        title="The Debt Servicing Squeeze on Ordinary Tax Revenue (2002–2026)",
        subtitle="Annual debt service & interest payments as a percentage of KRA ordinary tax collections"
    )
    add_kid_footer(
        fig,
        source_text="National Treasury Annual Public Debt Reports, Controller of Budget & BROP",
        notes_text="Ordinary Revenue excludes appropriation-in-aid (A-i-A) and donor grants"
    )
    
    save_kid_figure(fig, FIGURES_FINAL / "FIG-DEBT-004_debt_service_to_tax_revenue")
    save_kid_figure(fig, FIGURES_DRAFTS / "FIG-DEBT-004_debt_service_to_tax_revenue")
    plt.close(fig)

    print("[SUCCESS] All 4 publication figures generated successfully!")

if __name__ == "__main__":
    generate_all_figures()
