#!/usr/bin/env python3
"""Build source-labelled KID-001 charts from the canonical publication CSV."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.transforms import Bbox
import pandas as pd


HERE = Path(__file__).resolve().parent
PACKAGE_DIR = HERE.parent.parent
DATA_PATH = PACKAGE_DIR / "Data" / "KID001_current_debt_baseline.csv"

for parent in HERE.parents:
    if (parent / "Code" / "kid_theme.py").exists():
        sys.path.insert(0, str(parent / "Code"))
        break
else:
    raise RuntimeError("Could not locate Code/kid_theme.py")

from kid_theme import PALETTE, apply_kid_theme  # noqa: E402


def value(df: pd.DataFrame, code: str) -> float:
    match = df.loc[df["indicator_code"] == code, "value"]
    if len(match) != 1:
        raise ValueError(f"Expected one row for {code}, found {len(match)}")
    return float(match.iloc[0])


def canvas(left: float = 0.09, bottom: float = 0.20):
    apply_kid_theme()
    fig, ax = plt.subplots(figsize=(12, 6.75))
    fig.subplots_adjust(left=left, right=0.92, top=0.72, bottom=bottom)
    return fig, ax


def add_brand_header(fig, title: str, subtitle: str):
    fig.text(0.08, 0.96, "KENYA IN DATA  •  PUBLIC DEBT", fontsize=10,
             fontweight="bold", color=PALETTE["red"], va="top", ha="left")
    fig.text(0.08, 0.922, title, fontsize=16, fontweight="heavy",
             color=PALETTE["navy"], va="top", ha="left")
    fig.text(0.08, 0.880, subtitle, fontsize=10.5, color=PALETTE["slate"],
             va="top", ha="left")


def add_attribution_footer(fig, data_source: str, note: str = ""):
    source_line = f"Data: {data_source}"
    if note:
        source_line += f"  |  {note}"
    fig.text(0.08, 0.050, source_line, fontsize=8.2, fontstyle="italic",
             color=PALETTE["slate"], va="bottom", ha="left")
    fig.text(0.08, 0.025,
             "Analysis and visualisation: Kenya in Data  •  kenyaindata.org",
             fontsize=8.3, fontweight="bold", color=PALETTE["navy"],
             va="bottom", ha="left")


def clean_axes(ax, grid_axis: str = "x"):
    ax.grid(axis=grid_axis, alpha=0.65)
    ax.grid(axis="y" if grid_axis == "x" else "x", visible=False)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)


def export(fig, stem: str):
    width, height = fig.get_size_inches()
    exact_canvas = Bbox.from_bounds(0, 0, width, height)
    for suffix, options in (
        ("png", {"dpi": 300}),
        ("svg", {}),
        ("pdf", {}),
    ):
        fig.savefig(HERE / f"{stem}.{suffix}", bbox_inches=exact_canvas, **options)
    plt.close(fig)


def chart_current_composition(df: pd.DataFrame):
    total = value(df, "DEBT_STOCK_TOT_2026M05") / 1000
    domestic = value(df, "DEBT_STOCK_DOM_2026M05") / 1000
    external = value(df, "DEBT_STOCK_EXT_2026M05") / 1000
    shares = [domestic / total * 100, external / total * 100]

    fig, ax = canvas()
    add_brand_header(
        fig,
        "Kenya's public debt reached KSh 12.896 trillion",
        "Latest complete domestic and external debt observation • May 2026 • provisional",
    )
    ax.barh([0], [shares[0]], color=PALETTE["blue"], height=0.43)
    ax.barh([0], [shares[1]], left=[shares[0]], color=PALETTE["gold"], height=0.43)
    ax.text(shares[0] / 2, 0, f"DOMESTIC\n{shares[0]:.1f}%\nKSh {domestic:.3f}T",
            ha="center", va="center", color="white", fontsize=15, fontweight="bold")
    ax.text(shares[0] + shares[1] / 2, 0,
            f"EXTERNAL\n{shares[1]:.1f}%\nKSh {external:.3f}T",
            ha="center", va="center", color="white", fontsize=15, fontweight="bold")
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.55, 0.55)
    ax.set_yticks([])
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    ax.set_xlabel("Share of public and publicly guaranteed debt", fontweight="bold")
    clean_axes(ax)
    ax.spines["bottom"].set_visible(False)
    add_attribution_footer(
        fig, "CBK, Monthly Economic Indicators (June 2026), Table 7.1, p. 22",
        "Same-month shares; provisional",
    )
    export(fig, "FIG-KID001-001_current_debt_composition")


def chart_service_components(df: pd.DataFrame):
    items = [
        ("Domestic interest", "SVC_INT_DOM_2025", PALETTE["purple"]),
        ("External interest", "SVC_INT_EXT_2025", PALETTE["gold"]),
        ("Domestic principal*", "SVC_PRIN_DOM_2025", PALETTE["blue"]),
        ("External principal", "SVC_PRIN_EXT_2025", PALETTE["teal"]),
    ]
    labels = [item[0] for item in items]
    values = [value(df, item[1]) for item in items]
    colors = [item[2] for item in items]

    fig, ax = canvas(left=0.18)
    add_brand_header(
        fig,
        "Domestic interest was the largest debt-service component",
        "FY 2024/25 debt service • KSh billion • total KSh 1.722 trillion",
    )
    y = list(range(len(labels)))
    bars = ax.barh(y, values, color=colors, height=0.57)
    ax.set_yticks(y, labels, fontweight="bold")
    ax.invert_yaxis()
    ax.set_xlim(0, 850)
    ax.set_xlabel("KSh billion", fontweight="bold")
    ax.xaxis.set_major_locator(mtick.MultipleLocator(100))
    clean_axes(ax)
    for bar, val in zip(bars, values):
        ax.text(val + 13, bar.get_y() + bar.get_height() / 2, f"KSh {val:,.1f}B",
                va="center", color=PALETTE["navy"], fontsize=11, fontweight="bold")
    ax.text(0.99, 0.03, "Debt service = 71.2% of ordinary revenue",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=11,
            color=PALETTE["red"], fontweight="bold")
    add_attribution_footer(
        fig, "National Treasury, Annual Public Debt Management Report FY 2024/25, Table 4, p. 30",
        "*Domestic principal excludes T-bill redemptions; provisional",
    )
    export(fig, "FIG-KID001-002_debt_service_components")


def chart_domestic_interest(df: pd.DataFrame):
    total = value(df, "SVC_INT_DOM_2025")
    bond = value(df, "SVC_INT_DOM_TBONDS_2025")
    bill = value(df, "SVC_INT_DOM_TBILLS_2025")
    vals = [bond, bill, total - bond - bill]
    labels = ["Treasury bonds", "Treasury bills", "Other charges*"]
    colors = [PALETTE["purple"], PALETTE["blue"], PALETTE["slate"]]

    fig, ax = canvas(left=0.18)
    add_brand_header(
        fig,
        "Treasury bonds generated 87% of domestic interest charges",
        "FY 2024/25 domestic interest and charges • KSh billion • total KSh 776.3 billion",
    )
    y = list(range(len(labels)))
    bars = ax.barh(y, vals, color=colors, height=0.58)
    ax.set_yticks(y, labels, fontweight="bold")
    ax.invert_yaxis()
    ax.set_xlim(0, 760)
    ax.set_xlabel("KSh billion", fontweight="bold")
    ax.xaxis.set_major_locator(mtick.MultipleLocator(100))
    clean_axes(ax)
    for bar, val in zip(bars, vals):
        share = val / total * 100
        ax.text(val + 12, bar.get_y() + bar.get_height() / 2,
                f"KSh {val:,.1f}B  •  {share:.1f}%",
                va="center", color=PALETTE["navy"], fontsize=11, fontweight="bold")
    add_attribution_footer(
        fig, "National Treasury, Annual Public Debt Management Report FY 2024/25, Table 9, p. 44",
        "*CBK commission, pre-1997 debt and other/overdraft charges; provisional",
    )
    export(fig, "FIG-KID001-003_domestic_interest_by_instrument")


def chart_baseline_components(df: pd.DataFrame):
    items = [
        ("Domestic Treasury bonds", "COMP_DOM_TBONDS_2025", PALETTE["blue"]),
        ("External multilateral", "COMP_EXT_MULTI_2025", PALETTE["gold"]),
        ("External commercial", "COMP_EXT_COMM_2025", "#B45309"),
        ("External bilateral", "COMP_EXT_BILAT_2025", "#F59E0B"),
        ("Domestic Treasury bills", "COMP_DOM_TBILLS_2025", "#60A5FA"),
        ("Other domestic debt", "COMP_DOM_OTHER_2025", "#93C5FD"),
        ("External suppliers' credit", "COMP_EXT_SUPP_2025", "#FCD34D"),
    ]
    total = value(df, "DEBT_STOCK_TOT_2025")
    vals = [value(df, code) / total * 100 for _, code, _ in items]

    fig, ax = canvas(left=0.24)
    add_brand_header(
        fig,
        "Treasury bonds made up 43% of the June 2025 debt stock",
        "Public and publicly guaranteed debt by instrument and creditor • share of KSh 11.814 trillion",
    )
    y = list(range(len(items)))
    bars = ax.barh(y, vals, color=[color for _, _, color in items], height=0.58)
    ax.set_yticks(y, [label for label, _, _ in items], fontweight="bold")
    ax.invert_yaxis()
    ax.set_xlim(0, 50)
    ax.set_xlabel("Share of total debt", fontweight="bold")
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    clean_axes(ax)
    for bar, val in zip(bars, vals):
        ax.text(val + 0.7, bar.get_y() + bar.get_height() / 2, f"{val:.1f}%",
                va="center", color=PALETTE["navy"], fontsize=10.5, fontweight="bold")
    add_attribution_footer(
        fig, "National Treasury, Annual Public Debt Management Report FY 2024/25, Tables 5 and 10, pp. 34 and 45",
        "Shares calculated by Kenya in Data; provisional",
    )
    export(fig, "FIG-KID001-004_june_2025_debt_components")


def chart_service_composition(df: pd.DataFrame):
    items = [
        ("DOMESTIC\nINTEREST", "SVC_INT_DOM_2025", PALETTE["purple"]),
        ("EXTERNAL\nINTEREST", "SVC_INT_EXT_2025", PALETTE["gold"]),
        ("DOMESTIC\nPRINCIPAL*", "SVC_PRIN_DOM_2025", PALETTE["blue"]),
        ("EXTERNAL\nPRINCIPAL", "SVC_PRIN_EXT_2025", PALETTE["teal"]),
    ]
    total = value(df, "SVC_TOT_2025")
    vals = [value(df, code) for _, code, _ in items]
    shares = [v / total * 100 for v in vals]

    fig, ax = canvas()
    add_brand_header(
        fig,
        "Interest accounted for 57% of Kenya's debt service",
        "FY 2024/25 debt service composition • total KSh 1.722 trillion • 71.2% of ordinary revenue",
    )
    left = 0
    for (label, _, color), val, share in zip(items, vals, shares):
        ax.barh([0], [share], left=[left], color=color, height=0.48)
        ax.text(left + share / 2, 0, f"{label}\n{share:.1f}%\nKSh {val:,.1f}B",
                ha="center", va="center", color="white", fontsize=10.5, fontweight="bold")
        left += share
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.55, 0.55)
    ax.set_yticks([])
    ax.set_xlabel("Share of total debt service", fontweight="bold")
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    clean_axes(ax)
    ax.spines["bottom"].set_visible(False)
    add_attribution_footer(
        fig, "National Treasury, Annual Public Debt Management Report FY 2024/25, Table 4, p. 30",
        "*Domestic principal excludes T-bill redemptions; provisional",
    )
    export(fig, "FIG-KID001-005_debt_service_composition")


def chart_domestic_interest_composition(df: pd.DataFrame):
    total = value(df, "SVC_INT_DOM_2025")
    bond = value(df, "SVC_INT_DOM_TBONDS_2025")
    bill = value(df, "SVC_INT_DOM_TBILLS_2025")
    vals = [bond, bill, total - bond - bill]
    labels = ["TREASURY BONDS", "TREASURY BILLS", "OTHER*"]
    colors = [PALETTE["purple"], PALETTE["blue"], PALETTE["slate"]]
    shares = [v / total * 100 for v in vals]

    fig, ax = canvas()
    add_brand_header(
        fig,
        "Treasury bonds generated 87% of domestic interest charges",
        "FY 2024/25 domestic interest composition • total KSh 776.3 billion",
    )
    left = 0
    for idx, (label, color, val, share) in enumerate(zip(labels, colors, vals, shares)):
        ax.barh([0], [share], left=[left], color=color, height=0.48)
        if idx < 2:
            ax.text(left + share / 2, 0, f"{label}\n{share:.1f}%\nKSh {val:,.1f}B",
                    ha="center", va="center", color="white", fontsize=11, fontweight="bold")
        left += share
    ax.annotate(f"OTHER CHARGES  {shares[2]:.1f}%  •  KSh {vals[2]:,.1f}B",
                xy=(100 - shares[2] / 2, 0.23), xytext=(99, 0.46),
                ha="right", va="center", fontsize=9.5, fontweight="bold",
                color=PALETTE["navy"], arrowprops=dict(arrowstyle="-", color=PALETTE["slate"]))
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.55, 0.62)
    ax.set_yticks([])
    ax.set_xlabel("Share of domestic interest and charges", fontweight="bold")
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    clean_axes(ax)
    ax.spines["bottom"].set_visible(False)
    add_attribution_footer(
        fig, "National Treasury, Annual Public Debt Management Report FY 2024/25, Table 9, p. 44",
        "*CBK commission, pre-1997 debt and other/overdraft charges; provisional",
    )
    export(fig, "FIG-KID001-006_domestic_interest_composition")


def chart_domestic_holders(df: pd.DataFrame):
    items = [
        ("Commercial banks", "HOLDER_COMM_BANKS_2025"),
        ("Pension funds", "HOLDER_PENSIONS_2025"),
        ("Government and parastatals", "HOLDER_GOV_PARASTATALS_2025"),
        ("Insurance companies", "HOLDER_INSURANCE_2025"),
        ("Other investors", "HOLDER_OTHER_2025"),
        ("Households", "HOLDER_HOUSEHOLDS_2025"),
        ("Non-residents", "HOLDER_NONRESIDENTS_2025"),
        ("Central Bank of Kenya", "HOLDER_CBK_2025"),
    ]
    total = value(df, "DEBT_STOCK_DOM_2025")
    vals = [value(df, code) / total * 100 for _, code in items]

    fig, ax = canvas(left=0.24)
    add_brand_header(
        fig,
        "Commercial banks held 35% of domestic public debt",
        "Holder shares at end-June 2025 • stock holdings, not annual interest receipts",
    )
    y = list(range(len(items)))
    bars = ax.barh(y, vals, color=PALETTE["blue"], height=0.56)
    ax.set_yticks(y, [label for label, _ in items], fontweight="bold")
    ax.invert_yaxis()
    ax.set_xlim(0, 40)
    ax.set_xlabel("Share of domestic debt stock", fontweight="bold")
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    clean_axes(ax)
    for bar, val in zip(bars, vals):
        ax.text(val + 0.6, bar.get_y() + bar.get_height() / 2, f"{val:.1f}%",
                va="center", color=PALETTE["navy"], fontsize=10.5, fontweight="bold")
    add_attribution_footer(
        fig, "National Treasury, Annual Public Debt Management Report FY 2024/25, Table 6, p. 36",
        "Categories may differ from interest recipients; provisional",
    )
    export(fig, "FIG-KID001-007_domestic_debt_holders")


def chart_weighted_interest_rates(df: pd.DataFrame):
    items = [
        ("Domestic debt", "COST_WAIR_DOMESTIC_2025", PALETTE["blue"]),
        ("Total public debt", "COST_WAIR_TOTAL_2025", PALETTE["purple"]),
        ("External debt", "COST_WAIR_EXTERNAL_2025", PALETTE["gold"]),
    ]
    vals = [value(df, code) for _, code, _ in items]

    fig, ax = canvas(left=0.20)
    add_brand_header(
        fig,
        "Domestic debt carried a weighted average rate of 13.0%",
        "Weighted average interest rates • FY 2024/25",
    )
    y = list(range(len(items)))
    bars = ax.barh(y, vals, color=[color for _, _, color in items], height=0.58)
    ax.set_yticks(y, [label for label, _, _ in items], fontweight="bold")
    ax.invert_yaxis()
    ax.set_xlim(0, 15)
    ax.set_xlabel("Weighted average interest rate", fontweight="bold")
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    clean_axes(ax)
    for bar, val in zip(bars, vals):
        ax.text(val + 0.25, bar.get_y() + bar.get_height() / 2, f"{val:.1f}%",
                va="center", color=PALETTE["navy"], fontsize=12, fontweight="bold")
    add_attribution_footer(
        fig, "National Treasury, Annual Public Debt Management Report FY 2024/25, Section 9.3 and Figure 17, p. 68",
        "Provisional outturn",
    )
    export(fig, "FIG-KID001-008_weighted_average_interest_rates")


def main():
    df = pd.read_csv(DATA_PATH)
    chart_current_composition(df)
    chart_service_components(df)
    chart_domestic_interest(df)
    chart_baseline_components(df)
    chart_service_composition(df)
    chart_domestic_interest_composition(df)
    chart_domestic_holders(df)
    chart_weighted_interest_rates(df)
    print("Built eight KID-001 charts in PNG, SVG and PDF formats.")


if __name__ == "__main__":
    main()
