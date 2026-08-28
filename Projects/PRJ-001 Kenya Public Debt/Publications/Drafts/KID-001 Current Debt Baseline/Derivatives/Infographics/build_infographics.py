#!/usr/bin/env python3
"""Build selected KID-001 publication assets from the canonical dataset."""

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


def new_figure(figsize):
    apply_kid_theme()
    return plt.figure(figsize=figsize, facecolor=PALETTE["canvas_light"])


def add_brand(fig, topic="PUBLIC DEBT", x=0.08, y=0.95):
    fig.text(
        x, y, f"KENYA IN DATA  •  {topic}",
        color=PALETTE["red"], fontsize=11, fontweight="bold",
        ha="left", va="top",
    )


def add_footer(fig, source, x=0.08, source_y=0.065, brand_y=0.032, fontsize=7.6):
    fig.text(
        x, source_y, f"Data: {source}",
        color=PALETTE["slate"], fontsize=fontsize, fontstyle="italic",
        ha="left", va="bottom",
    )
    fig.text(
        x, brand_y, "Analysis and visualisation: Kenya in Data  •  kenyaindata.org",
        color=PALETTE["navy"], fontsize=fontsize, fontweight="bold",
        ha="left", va="bottom",
    )


def export(fig, stem, png_dpi):
    width, height = fig.get_size_inches()
    exact_canvas = Bbox.from_bounds(0, 0, width, height)
    fig.savefig(HERE / f"{stem}.png", dpi=png_dpi, bbox_inches=exact_canvas)
    fig.savefig(HERE / f"{stem}.svg", bbox_inches=exact_canvas)
    fig.savefig(HERE / f"{stem}.pdf", bbox_inches=exact_canvas)
    plt.close(fig)


def og_hero(df: pd.DataFrame):
    total = value(df, "DEBT_STOCK_TOT_2026M05") / 1000
    domestic = value(df, "DEBT_STOCK_DOM_2026M05") / 1000
    external = value(df, "DEBT_STOCK_EXT_2026M05") / 1000
    domestic_share = domestic / total * 100
    external_share = external / total * 100

    fig = new_figure((12, 6.28))
    add_brand(fig, y=0.93)
    fig.text(
        0.08, 0.82, "Kenya's public debt reached",
        color=PALETTE["navy"], fontsize=25, fontweight="heavy",
        ha="left", va="top",
    )
    fig.text(
        0.08, 0.70, f"KSh {total:.3f} trillion",
        color=PALETTE["navy"], fontsize=39, fontweight="heavy",
        ha="left", va="top",
    )
    fig.text(
        0.08, 0.57, "May 2026  •  latest complete observation  •  provisional",
        color=PALETTE["slate"], fontsize=12, ha="left", va="top",
    )

    ax = fig.add_axes([0.08, 0.27, 0.84, 0.17])
    ax.barh([0], [domestic_share], color=PALETTE["blue"], height=0.74)
    ax.barh([0], [external_share], left=[domestic_share], color=PALETTE["gold"], height=0.74)
    ax.text(
        domestic_share / 2, 0,
        f"DOMESTIC  {domestic_share:.1f}%  •  KSh {domestic:.3f}T",
        color="white", fontsize=12.5, fontweight="bold", ha="center", va="center",
    )
    ax.text(
        domestic_share + external_share / 2, 0,
        f"EXTERNAL  {external_share:.1f}%  •  KSh {external:.3f}T",
        color="white", fontsize=12.5, fontweight="bold", ha="center", va="center",
    )
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.55, 0.55)
    ax.axis("off")

    add_footer(
        fig,
        "Central Bank of Kenya, Monthly Economic Indicators (June 2026), Table 7.1, p. 22; provisional",
        source_y=0.095, brand_y=0.050, fontsize=8.1,
    )
    export(fig, "ASSET-KID001-010_article_og_hero", png_dpi=100)


def domestic_interest_explainer(df: pd.DataFrame):
    domestic_interest = value(df, "SVC_INT_DOM_2025")
    external_interest = value(df, "SVC_INT_EXT_2025")
    domestic_stock = value(df, "DEBT_STOCK_DOM_2025") / 1000
    external_stock = value(df, "DEBT_STOCK_EXT_2025") / 1000
    domestic_rate = value(df, "COST_WAIR_DOMESTIC_2025")
    external_rate = value(df, "COST_WAIR_EXTERNAL_2025")
    multilateral_share = (
        value(df, "COMP_EXT_MULTI_2025") / value(df, "DEBT_STOCK_EXT_2025") * 100
    )

    fig = new_figure((8, 10))
    add_brand(fig, y=0.965)
    fig.text(
        0.08, 0.905, "Why was domestic interest\nmuch higher?",
        color=PALETTE["navy"], fontsize=23, fontweight="heavy",
        ha="left", va="top", linespacing=1.05,
    )
    fig.text(
        0.08, 0.795,
        "FY 2024/25 interest payments  •  KSh billion  •  provisional",
        color=PALETTE["slate"], fontsize=10.5, ha="left", va="top",
    )

    ax = fig.add_axes([0.22, 0.585, 0.68, 0.17])
    labels = ["Domestic", "External"]
    vals = [domestic_interest, external_interest]
    colors = [PALETTE["purple"], PALETTE["gold"]]
    bars = ax.barh([1, 0], vals, color=colors, height=0.56)
    ax.set_xlim(0, 850)
    ax.set_yticks([1, 0], labels, fontweight="bold")
    ax.xaxis.set_major_locator(mtick.MultipleLocator(200))
    ax.grid(axis="x", alpha=0.65)
    ax.grid(axis="y", visible=False)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    for bar, val in zip(bars, vals):
        ax.text(
            val + 18, bar.get_y() + bar.get_height() / 2,
            f"KSh {val:,.1f}B", color=PALETTE["navy"],
            fontsize=10.5, fontweight="bold", ha="left", va="center",
        )
    ax.set_xlabel("Interest payments", fontweight="bold")

    fig.text(
        0.08, 0.535,
        "The difference is consistent with the structure and pricing of the two portfolios:",
        color=PALETTE["navy"], fontsize=10.2, fontweight="bold", ha="left", va="top",
    )

    card_specs = [
        (0.08, "1  STOCK SIZE", "Domestic debt", f"KSh {domestic_stock:.3f}T", "External debt", f"KSh {external_stock:.3f}T"),
        (0.53, "2  AVERAGE RATE", "Domestic debt", f"{domestic_rate:.1f}%", "External debt", f"{external_rate:.1f}%"),
    ]
    for x, heading, left_label, left_value, right_label, right_value in card_specs:
        fig.patches.append(
            patches.FancyBboxPatch(
                (x, 0.335), 0.39, 0.16,
                boxstyle="round,pad=0.012,rounding_size=0.012",
                transform=fig.transFigure, facecolor=PALETTE["white"],
                edgecolor=PALETTE["slate_light"], linewidth=1.0,
            )
        )
        fig.text(x + 0.025, 0.468, heading, color=PALETTE["red"], fontsize=8.5,
                 fontweight="bold", ha="left", va="top")
        fig.text(x + 0.025, 0.425, left_label, color=PALETTE["slate"], fontsize=8.3,
                 ha="left", va="top")
        fig.text(x + 0.025, 0.388, left_value, color=PALETTE["navy"], fontsize=16,
                 fontweight="heavy", ha="left", va="top")
        fig.text(x + 0.205, 0.425, right_label, color=PALETTE["slate"], fontsize=8.3,
                 ha="left", va="top")
        fig.text(x + 0.205, 0.388, right_value, color=PALETTE["navy"], fontsize=16,
                 fontweight="heavy", ha="left", va="top")

    fig.patches.append(
        patches.FancyBboxPatch(
            (0.08, 0.175), 0.84, 0.115,
            boxstyle="round,pad=0.012,rounding_size=0.012",
            transform=fig.transFigure, facecolor="#FFF7ED",
            edgecolor="#FED7AA", linewidth=1.0,
        )
    )
    fig.text(
        0.105, 0.262, "3  EXTERNAL PORTFOLIO MIX",
        color=PALETTE["gold"], fontsize=8.5, fontweight="bold", ha="left", va="top",
    )
    fig.text(
        0.105, 0.224,
        f"Multilateral lenders accounted for {multilateral_share:.1f}% of external debt at June 2025.",
        color=PALETTE["navy"], fontsize=10.2, fontweight="bold", ha="left", va="top",
    )
    fig.text(
        0.105, 0.192,
        "These loans often have more favourable terms than standard market borrowing.",
        color=PALETTE["slate"], fontsize=8.8, ha="left", va="top",
    )
    fig.text(
        0.08, 0.135,
        "Caveat: principal repayments are not interest, and reported domestic principal excludes routine T-bill redemptions.",
        color=PALETTE["navy"], fontsize=8.5, fontweight="bold", ha="left", va="top",
    )
    add_footer(
        fig,
        "National Treasury, Annual Public Debt Management Report FY 2024/25, Tables 3, 4 and 10; Figure 17",
        source_y=0.073, brand_y=0.040, fontsize=6.8,
    )
    export(fig, "ASSET-KID001-012_domestic_interest_explainer", png_dpi=135)


def statutory_anchor(df: pd.DataFrame):
    present_value = value(df, "RATIO_DEBT_GDP_PV_2025")
    anchor = value(df, "STATUTORY_ANCHOR_PV")
    gap = present_value - anchor

    fig = new_figure((8, 8))
    add_brand(fig, y=0.955)
    fig.text(
        0.08, 0.885, "Present-value debt exceeded\nthe statutory anchor",
        color=PALETTE["navy"], fontsize=22, fontweight="heavy",
        ha="left", va="top", linespacing=1.08,
    )
    fig.text(
        0.08, 0.765, "June 2025  •  share of GDP  •  provisional",
        color=PALETTE["slate"], fontsize=10.5, ha="left", va="top",
    )

    fig.text(
        0.08, 0.675, f"{present_value:.1f}%",
        color=PALETTE["red"], fontsize=38, fontweight="heavy", ha="left", va="top",
    )
    fig.text(
        0.31, 0.647, "present-value debt-to-GDP",
        color=PALETTE["navy"], fontsize=11.5, fontweight="bold", ha="left", va="top",
    )

    ax = fig.add_axes([0.10, 0.405, 0.80, 0.15])
    ax.barh([0], [anchor], color="#DCFCE7", height=0.52)
    ax.barh([0], [70 - anchor], left=[anchor], color="#FEE2E2", height=0.52)
    ax.barh([0], [present_value], color=PALETTE["red"], height=0.18)
    ax.axvline(anchor, color=PALETTE["navy"], linewidth=2.2)
    ax.text(anchor, 0.42, f"STATUTORY ANCHOR\n{anchor:.0f}%", color=PALETTE["navy"],
            fontsize=9, fontweight="bold", ha="center", va="bottom")
    ax.text(present_value, -0.42, f"REPORTED\n{present_value:.1f}%", color=PALETTE["red"],
            fontsize=9, fontweight="bold", ha="center", va="top")
    ax.set_xlim(0, 70)
    ax.set_ylim(-0.75, 0.75)
    ax.set_yticks([])
    ax.xaxis.set_major_locator(mtick.MultipleLocator(10))
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    ax.set_xlabel("Present-value debt as a share of GDP", fontweight="bold")
    ax.grid(axis="x", alpha=0.5)
    ax.grid(axis="y", visible=False)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)

    fig.patches.append(
        patches.FancyBboxPatch(
            (0.08, 0.205), 0.84, 0.105,
            boxstyle="round,pad=0.012,rounding_size=0.012",
            transform=fig.transFigure, facecolor=PALETTE["white"],
            edgecolor=PALETTE["slate_light"], linewidth=1.0,
        )
    )
    fig.text(
        0.11, 0.278, f"{gap:.1f} percentage points above the anchor",
        color=PALETTE["red"], fontsize=14.5, fontweight="heavy", ha="left", va="top",
    )
    fig.text(
        0.11, 0.235,
        "This is a comparison with the legal benchmark—not, by itself, a forecast of default.",
        color=PALETTE["slate"], fontsize=8.7, ha="left", va="top",
    )
    add_footer(
        fig,
        "National Treasury, Annual Public Debt Management Report FY 2024/25, Chapter 8, p. 63; PFM Act §50(2A)–(2B)",
        source_y=0.090, brand_y=0.050, fontsize=6.8,
    )
    export(fig, "ASSET-KID001-014_statutory_anchor", png_dpi=135)


def main():
    df = pd.read_csv(DATA_PATH)
    og_hero(df)
    domestic_interest_explainer(df)
    statutory_anchor(df)
    print("Built three KID-001 assets in PNG, SVG and PDF formats.")


if __name__ == "__main__":
    main()
