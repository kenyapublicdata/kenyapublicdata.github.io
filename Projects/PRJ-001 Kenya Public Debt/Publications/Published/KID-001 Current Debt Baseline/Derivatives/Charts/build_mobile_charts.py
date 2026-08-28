#!/usr/bin/env python3
"""Build 4:5 mobile variants for all KID-001 publication charts."""

from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
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


def canvas():
    apply_kid_theme()
    return plt.figure(figsize=(8, 10), facecolor=PALETTE["canvas_light"])


def header(fig, title: str, subtitle: str, title_size: float = 24):
    fig.text(
        0.08, 0.965, "KENYA IN DATA  •  PUBLIC DEBT",
        color=PALETTE["red"], fontsize=13, fontweight="bold",
        ha="left", va="top",
    )
    fig.text(
        0.08, 0.905, title,
        color=PALETTE["navy"], fontsize=title_size, fontweight="heavy",
        ha="left", va="top", linespacing=1.06,
    )
    fig.text(
        0.08, 0.795, subtitle,
        color=PALETTE["slate"], fontsize=15,
        ha="left", va="top",
    )


def footer(fig, source: str, note: str = ""):
    line = f"Data: {source}"
    if note:
        line += f"\nNote: {note}"
    fig.text(
        0.08, 0.067, line,
        color=PALETTE["slate"], fontsize=10.5, fontstyle="italic",
        ha="left", va="bottom", linespacing=1.3,
    )
    fig.text(
        0.08, 0.027, "Analysis and visualisation: Kenya in Data  •  kenyaindata.org",
        color=PALETTE["navy"], fontsize=10.5, fontweight="bold",
        ha="left", va="bottom",
    )


def export(fig, stem: str):
    width, height = fig.get_size_inches()
    exact_canvas = Bbox.from_bounds(0, 0, width, height)
    fig.savefig(HERE / f"{stem}_mobile.png", dpi=135, bbox_inches=exact_canvas)
    svg_path = HERE / f"{stem}_mobile.svg"
    fig.savefig(svg_path, bbox_inches=exact_canvas)
    svg_path.write_text(
        "\n".join(line.rstrip() for line in svg_path.read_text().splitlines()) + "\n"
    )
    fig.savefig(HERE / f"{stem}_mobile.pdf", bbox_inches=exact_canvas)
    plt.close(fig)


def clean_axes(ax, grid_axis="x"):
    ax.grid(axis=grid_axis, alpha=0.65)
    ax.grid(axis="y" if grid_axis == "x" else "x", visible=False)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)


def component_row(fig, y, label, value_text, share_text, color):
    fig.patches.append(
        patches.FancyBboxPatch(
            (0.08, y - 0.033), 0.84, 0.078,
            boxstyle="round,pad=0.008,rounding_size=0.010",
            transform=fig.transFigure, facecolor=PALETTE["white"],
            edgecolor=PALETTE["slate_light"], linewidth=1.0,
        )
    )
    fig.patches.append(
        patches.Rectangle(
            (0.08, y - 0.033), 0.018, 0.078,
            transform=fig.transFigure, facecolor=color, edgecolor="none",
        )
    )
    fig.text(0.12, y + 0.006, label, fontsize=15.5, fontweight="bold",
             color=PALETTE["navy"], ha="left", va="center")
    fig.text(0.72, y + 0.006, value_text, fontsize=15.5, fontweight="bold",
             color=PALETTE["navy"], ha="right", va="center")
    fig.text(0.885, y + 0.006, share_text, fontsize=15.5, fontweight="heavy",
             color=color, ha="right", va="center")


def chart_001(df):
    total = value(df, "DEBT_STOCK_TOT_2026M05") / 1000
    domestic = value(df, "DEBT_STOCK_DOM_2026M05") / 1000
    external = value(df, "DEBT_STOCK_EXT_2026M05") / 1000
    shares = [domestic / total * 100, external / total * 100]

    fig = canvas()
    header(
        fig,
        "Kenya's public debt reached\nKSh 12.896 trillion",
        "May 2026  •  latest complete observation  •  provisional",
    )
    fig.text(0.08, 0.705, f"KSh {total:.3f}T", fontsize=38, fontweight="heavy",
             color=PALETTE["navy"], ha="left", va="top")
    fig.text(0.08, 0.655, "public and publicly guaranteed debt", fontsize=15,
             color=PALETTE["slate"], ha="left", va="top")

    ax = fig.add_axes([0.08, 0.515, 0.84, 0.085])
    ax.barh([0], [shares[0]], color=PALETTE["blue"], height=0.80)
    ax.barh([0], [shares[1]], left=[shares[0]], color=PALETTE["gold"], height=0.80)
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.55, 0.55)
    ax.axis("off")

    component_row(fig, 0.410, "Domestic debt", f"KSh {domestic:.3f}T", f"{shares[0]:.1f}%", PALETTE["blue"])
    component_row(fig, 0.285, "External debt", f"KSh {external:.3f}T", f"{shares[1]:.1f}%", PALETTE["gold"])
    fig.text(0.08, 0.175, "The two shares use the same reporting month and total.",
             fontsize=13.5, color=PALETTE["navy"], ha="left", va="top")
    footer(fig, "CBK, Monthly Economic Indicators (June 2026), Table 7.1, p. 22")
    export(fig, "FIG-KID001-001_current_debt_composition")


def ranked_chart(fig, labels, vals, colors, x_max, x_step, xlabel, value_format,
                 left=0.30, bottom=0.155, height=0.57, label_size=14.5, value_size=15):
    ax = fig.add_axes([left, bottom, 0.92 - left, height])
    y = list(range(len(labels)))
    bars = ax.barh(y, vals, color=colors, height=0.55)
    ax.set_yticks(y, labels, fontweight="bold", fontsize=label_size)
    ax.invert_yaxis()
    ax.set_xlim(0, x_max)
    ax.xaxis.set_major_locator(mtick.MultipleLocator(x_step))
    ax.set_xlabel(xlabel, fontweight="bold", fontsize=15)
    clean_axes(ax)
    for bar, val in zip(bars, vals):
        ax.text(
            val + x_max * 0.022, bar.get_y() + bar.get_height() / 2,
            value_format(val), va="center", ha="left",
            color=PALETTE["navy"], fontsize=value_size, fontweight="bold",
        )
    return ax


def chart_002(df):
    items = [
        ("Domestic\ninterest", "SVC_INT_DOM_2025", PALETTE["purple"]),
        ("Domestic\nprincipal*", "SVC_PRIN_DOM_2025", PALETTE["blue"]),
        ("External\nprincipal", "SVC_PRIN_EXT_2025", PALETTE["teal"]),
        ("External\ninterest", "SVC_INT_EXT_2025", PALETTE["gold"]),
    ]
    vals = [value(df, code) for _, code, _ in items]
    fig = canvas()
    header(fig, "Domestic interest was the largest\ndebt-service component",
           "FY 2024/25  •  KSh billion  •  total KSh 1.722 trillion")
    ranked_chart(
        fig, [x[0] for x in items], vals, [x[2] for x in items],
        900, 200, "KSh billion", lambda v: f"{v:,.1f}", left=0.30,
        bottom=0.17, height=0.54, label_size=15.5, value_size=15.5,
    )
    footer(fig, "National Treasury, Annual Public Debt Management Report FY 2024/25, Table 4, p. 30",
           "Domestic principal excludes routine T-bill redemptions; provisional")
    export(fig, "FIG-KID001-002_debt_service_components")


def chart_003(df):
    total = value(df, "SVC_INT_DOM_2025")
    items = [
        ("Treasury\nbonds", value(df, "SVC_INT_DOM_TBONDS_2025"), PALETTE["purple"]),
        ("Treasury\nbills", value(df, "SVC_INT_DOM_TBILLS_2025"), PALETTE["blue"]),
        ("Other\ncharges*", total - value(df, "SVC_INT_DOM_TBONDS_2025") - value(df, "SVC_INT_DOM_TBILLS_2025"), PALETTE["slate"]),
    ]
    fig = canvas()
    header(fig, "Treasury bonds generated 87% of\ndomestic interest charges",
           "FY 2024/25  •  KSh billion  •  total KSh 776.3 billion")
    ranked_chart(
        fig, [x[0] for x in items], [x[1] for x in items], [x[2] for x in items],
        780, 200, "KSh billion", lambda v: f"{v:,.1f}", left=0.29,
        bottom=0.20, height=0.47, label_size=16, value_size=16,
    )
    footer(fig, "National Treasury, Annual Public Debt Management Report FY 2024/25, Table 9, p. 44",
           "Other includes CBK commission, pre-1997 debt and overdraft charges; provisional")
    export(fig, "FIG-KID001-003_domestic_interest_by_instrument")


def chart_004(df):
    items = [
        ("Domestic\nTreasury bonds", "COMP_DOM_TBONDS_2025", PALETTE["blue"]),
        ("External\nmultilateral", "COMP_EXT_MULTI_2025", PALETTE["gold"]),
        ("External\ncommercial", "COMP_EXT_COMM_2025", "#B45309"),
        ("External\nbilateral", "COMP_EXT_BILAT_2025", "#F59E0B"),
        ("Domestic\nTreasury bills", "COMP_DOM_TBILLS_2025", "#60A5FA"),
        ("Other\ndomestic debt", "COMP_DOM_OTHER_2025", "#93C5FD"),
        ("Suppliers'\ncredit", "COMP_EXT_SUPP_2025", "#FCD34D"),
    ]
    total = value(df, "DEBT_STOCK_TOT_2025")
    vals = [value(df, code) / total * 100 for _, code, _ in items]
    fig = canvas()
    header(fig, "Treasury bonds made up 43% of\nthe June 2025 debt stock",
           "Debt by domestic instrument and external creditor  •  provisional")
    ax = ranked_chart(
        fig, [x[0] for x in items], vals, [x[2] for x in items],
        50, 10, "Share of total debt", lambda v: f"{v:.1f}%", left=0.36,
        bottom=0.15, height=0.585, label_size=16.0, value_size=16.5,
    )
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    footer(fig, "National Treasury, Annual Public Debt Management Report FY 2024/25, Tables 5 and 10",
           "Shares calculated by Kenya in Data; provisional")
    export(fig, "FIG-KID001-004_june_2025_debt_components")


def parts_chart(fig, items, total, bar_y, row_start, row_gap):
    shares = [val / total * 100 for _, val, _ in items]
    ax = fig.add_axes([0.08, bar_y, 0.84, 0.075])
    left = 0
    for (_, _, color), share in zip(items, shares):
        ax.barh([0], [share], left=[left], color=color, height=0.82)
        left += share
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.55, 0.55)
    ax.axis("off")
    for idx, ((label, val, color), share) in enumerate(zip(items, shares)):
        component_row(fig, row_start - idx * row_gap, label, f"KSh {val:,.1f}B", f"{share:.1f}%", color)


def chart_005(df):
    total = value(df, "SVC_TOT_2025")
    items = [
        ("Domestic interest", value(df, "SVC_INT_DOM_2025"), PALETTE["purple"]),
        ("External interest", value(df, "SVC_INT_EXT_2025"), PALETTE["gold"]),
        ("Domestic principal*", value(df, "SVC_PRIN_DOM_2025"), PALETTE["blue"]),
        ("External principal", value(df, "SVC_PRIN_EXT_2025"), PALETTE["teal"]),
    ]
    fig = canvas()
    header(fig, "Interest accounted for 57% of\nKenya's debt service",
           "FY 2024/25  •  total KSh 1.722 trillion  •  71.2% of ordinary revenue")
    parts_chart(fig, items, total, bar_y=0.665, row_start=0.555, row_gap=0.105)
    footer(fig, "National Treasury, Annual Public Debt Management Report FY 2024/25, Table 4, p. 30",
           "Domestic principal excludes routine T-bill redemptions; provisional")
    export(fig, "FIG-KID001-005_debt_service_composition")


def chart_006(df):
    total = value(df, "SVC_INT_DOM_2025")
    bond = value(df, "SVC_INT_DOM_TBONDS_2025")
    bill = value(df, "SVC_INT_DOM_TBILLS_2025")
    items = [
        ("Treasury bonds", bond, PALETTE["purple"]),
        ("Treasury bills", bill, PALETTE["blue"]),
        ("Other charges*", total - bond - bill, PALETTE["slate"]),
    ]
    fig = canvas()
    header(fig, "Treasury bonds generated 87% of\ndomestic interest charges",
           "FY 2024/25  •  total KSh 776.3 billion  •  provisional")
    parts_chart(fig, items, total, bar_y=0.645, row_start=0.520, row_gap=0.120)
    fig.text(0.08, 0.165, "Bonds dominate both the domestic debt stock and its interest cost.",
             fontsize=13.5, color=PALETTE["navy"], ha="left", va="top")
    footer(fig, "National Treasury, Annual Public Debt Management Report FY 2024/25, Table 9, p. 44",
           "Other includes CBK commission, pre-1997 debt and overdraft charges")
    export(fig, "FIG-KID001-006_domestic_interest_composition")


def chart_007(df):
    items = [
        ("Commercial\nbanks", "HOLDER_COMM_BANKS_2025"),
        ("Pension\nfunds", "HOLDER_PENSIONS_2025"),
        ("Government and\nparastatals", "HOLDER_GOV_PARASTATALS_2025"),
        ("Insurance\ncompanies", "HOLDER_INSURANCE_2025"),
        ("Other\ninvestors", "HOLDER_OTHER_2025"),
        ("Households", "HOLDER_HOUSEHOLDS_2025"),
        ("Non-residents", "HOLDER_NONRESIDENTS_2025"),
        ("Central Bank\nof Kenya", "HOLDER_CBK_2025"),
    ]
    total = value(df, "DEBT_STOCK_DOM_2025")
    vals = [value(df, code) / total * 100 for _, code in items]
    fig = canvas()
    header(fig, "Commercial banks held 35% of\ndomestic public debt",
           "Holder shares at June 2025  •  stock holdings, not interest receipts")
    ax = ranked_chart(
        fig, [x[0] for x in items], vals, [PALETTE["blue"]] * len(items),
        40, 10, "Share of domestic debt stock", lambda v: f"{v:.1f}%", left=0.35,
        bottom=0.145, height=0.595, label_size=15.5, value_size=16.0,
    )
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    footer(fig, "National Treasury, Annual Public Debt Management Report FY 2024/25, Table 6, p. 36",
           "Holder shares are not annual interest receipts; provisional")
    export(fig, "FIG-KID001-007_domestic_debt_holders")


def chart_008(df):
    items = [
        ("Domestic\ndebt", "COST_WAIR_DOMESTIC_2025", PALETTE["blue"]),
        ("Total public\ndebt", "COST_WAIR_TOTAL_2025", PALETTE["purple"]),
        ("External\ndebt", "COST_WAIR_EXTERNAL_2025", PALETTE["gold"]),
    ]
    vals = [value(df, code) for _, code, _ in items]
    fig = canvas()
    header(fig, "Domestic debt carried a weighted\naverage rate of 13.0%",
           "Weighted average interest rates  •  FY 2024/25  •  provisional")
    ax = ranked_chart(
        fig, [x[0] for x in items], vals, [x[2] for x in items],
        15, 3, "Weighted average interest rate", lambda v: f"{v:.1f}%", left=0.29,
        bottom=0.20, height=0.47, label_size=16, value_size=17,
    )
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    footer(fig, "National Treasury, Annual Public Debt Management Report FY 2024/25, Figure 17, p. 68")
    export(fig, "FIG-KID001-008_weighted_average_interest_rates")


def main():
    df = pd.read_csv(DATA_PATH)
    chart_001(df)
    chart_002(df)
    chart_003(df)
    chart_004(df)
    chart_005(df)
    chart_006(df)
    chart_007(df)
    chart_008(df)
    print("Built eight mobile KID-001 charts in PNG, SVG and PDF formats.")


if __name__ == "__main__":
    main()
