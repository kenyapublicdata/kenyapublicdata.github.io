"""
Kenya in Data — Canonical Visualization Theme & Plotting Engine (kid_theme)
=============================================================================
Provides consistent styling, branded color palettes, administration shading,
standardized header/footer layout wrappers, direct line labelling, and high-level
plotting helpers for all Kenya in Data publications across projects.

Conforms to: Operations/Style Guide.md and Operations/Data and Analysis Standards.md
"""

import os
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as ticker

# -------------------------------------------------------------------------
# 1. Official Kenya in Data Color Tokens
# -------------------------------------------------------------------------
PALETTE = {
    # Core Canvas & Text
    "navy": "#0F172A",          # Deep Obsidian Navy (Primary text, headers, dark backgrounds)
    "canvas_light": "#F8FAFC",  # Crisp Ivory White (Default chart background)
    "white": "#FFFFFF",         # Pure white (Plot card background)
    "slate": "#64748B",         # Neutral Muted Grey (Subtitles, gridlines, footers)
    "slate_light": "#E2E8F0",   # Soft border and subtle dividers
    
    # Accent Series
    "green": "#059669",         # Emerald Green (Revenue, positive growth, primary series)
    "red": "#DC2626",           # Alert Crimson (Debt, deficits, inflation, fiscal distress)
    "gold": "#D97706",          # Warm Ochre Gold (External debt, secondary indicators)
    "blue": "#2563EB",          # Royal Blue (Domestic debt, institutional measures)
    "purple": "#7C3AED",        # Violet Purple (Special interventions, interest burden)
    "teal": "#0D9488",          # Teal Green (Per-capita series, alternative deflators)
    
    # Administration Timeline Shading (Subtle backgrounds)
    "shading_kibaki": "#CBD5E1",  # 2002–2013 (Mwai Kibaki)
    "shading_uhuru": "#94A3B8",   # 2013–2022 (Uhuru Kenyatta)
    "shading_ruto": "#CBD5E1",    # 2022–Present (William Ruto)
}

# -------------------------------------------------------------------------
# 2. Standard Aspect Ratio Dimension Presets
# -------------------------------------------------------------------------
ASPECT_RATIOS = {
    "16:9": (12.0, 6.75),       # Landscape / Presentation / Widescreen
    "1:1": (8.5, 8.5),          # Square Social Card (LinkedIn, Instagram)
    "4:5": (8.0, 10.0),         # Mobile Portrait / Feed Carousel
    "1.91:1": (12.0, 6.28),     # X (Twitter) Summary Card
}

# -------------------------------------------------------------------------
# 3. Administration Temporal Landmarks (Kenyan Historical Transitions)
# -------------------------------------------------------------------------
ADMINISTRATIONS = [
    {
        "name": "Kibaki",
        "full_name": "Mwai Kibaki",
        "start_year": 2002.99,  # Dec 2002
        "end_year": 2013.25,    # Apr 2013
        "color": PALETTE["shading_kibaki"],
        "alpha": 0.22,
        "label_pos": 2008.0
    },
    {
        "name": "Uhuru",
        "full_name": "Uhuru Kenyatta",
        "start_year": 2013.25,  # Apr 2013
        "end_year": 2022.68,    # Sep 2022
        "color": PALETTE["shading_uhuru"],
        "alpha": 0.15,
        "label_pos": 2017.5
    },
    {
        "name": "Ruto",
        "full_name": "William Ruto",
        "start_year": 2022.68,  # Sep 2022
        "end_year": 2026.50,    # Ongoing
        "color": PALETTE["shading_ruto"],
        "alpha": 0.22,
        "label_pos": 2024.5
    }
]

# -------------------------------------------------------------------------
# 4. Theme Application & Runtime Configuration
# -------------------------------------------------------------------------
def apply_kid_theme():
    """
    Configures Matplotlib runtime parameters with Kenya in Data visual standards.
    """
    plt.rcParams.update({
        # Figure & Axes
        "figure.facecolor": PALETTE["canvas_light"],
        "axes.facecolor": PALETTE["white"],
        "axes.edgecolor": PALETTE["slate_light"],
        "axes.linewidth": 1.0,
        "axes.grid": True,
        "grid.color": "#E2E8F0",
        "grid.linestyle": "--",
        "grid.linewidth": 0.7,
        "grid.alpha": 0.8,
        
        # Typography
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans", "Liberation Sans", "sans-serif"],
        "text.color": PALETTE["navy"],
        "axes.labelcolor": PALETTE["navy"],
        "xtick.color": PALETTE["slate"],
        "ytick.color": PALETTE["slate"],
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "axes.labelsize": 11,
        "axes.titlesize": 13,
        
        # Lines & Markers
        "lines.linewidth": 2.5,
        "lines.solid_capstyle": "round",
        "lines.solid_joinstyle": "round",
        
        # Legend (Fallback styling)
        "legend.frameon": False,
        "legend.fontsize": 10,
        "legend.labelcolor": PALETTE["navy"],
        
        # Savefig Defaults
        "savefig.dpi": 300,
        "savefig.facecolor": PALETTE["canvas_light"],
        "savefig.edgecolor": "none",
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.3,
    })

# -------------------------------------------------------------------------
# 5. Canvas Factory
# -------------------------------------------------------------------------
def create_kid_figure(aspect_ratio: str = "16:9"):
    """
    Initializes a themed figure and axes pair using standardized dimension presets.
    """
    apply_kid_theme()
    figsize = ASPECT_RATIOS.get(aspect_ratio, (12.0, 6.75))
    fig, ax = plt.subplots(figsize=figsize)
    return fig, ax

# -------------------------------------------------------------------------
# 6. Standard Header and Footer Wrappers
# -------------------------------------------------------------------------
def add_kid_header(fig, figure_id: str, title: str, subtitle: str, top_y: float = 0.96):
    """
    Renders the standardized 3-tier Kenya in Data publication header.
    """
    # Publication / Figure ID tag
    fig.text(
        0.08, top_y,
        f"KENYA IN DATA  •  {figure_id}".upper(),
        fontsize=10,
        fontweight="bold",
        color=PALETTE["red"],
        va="top",
        ha="left"
    )
    # Main Headline
    fig.text(
        0.08, top_y - 0.038,
        title,
        fontsize=16,
        fontweight="heavy",
        color=PALETTE["navy"],
        va="top",
        ha="left"
    )
    # Core Research Question / Subtitle
    fig.text(
        0.08, top_y - 0.080,
        subtitle,
        fontsize=10.5,
        fontweight="normal",
        color=PALETTE["slate"],
        va="top",
        ha="left"
    )

def add_kid_footer(fig, source_text: str, notes_text: str = "", website: str = "kenyaindata.org  •  @KenyaInData", bottom_y: float = 0.035):
    """
    Renders the standardized Kenya in Data provenance footer.
    """
    full_source = f"Source: {source_text}"
    if notes_text:
        full_source += f"  |  {notes_text}"
        
    fig.text(
        0.08, bottom_y,
        full_source,
        fontsize=8.5,
        fontstyle="italic",
        color=PALETTE["slate"],
        va="bottom",
        ha="left"
    )
    fig.text(
        0.92, bottom_y,
        website,
        fontsize=8.5,
        fontweight="bold",
        color=PALETTE["navy"],
        va="bottom",
        ha="right"
    )

# -------------------------------------------------------------------------
# 7. Timeline Shading Helper (Presidential Regimes)
# -------------------------------------------------------------------------
def add_administration_shading(ax, y_pos_pct: float = 0.94, show_labels: bool = True):
    """
    Adds subtle background vertical spans for Kenyan presidential administrations.
    """
    y_min, y_max = ax.get_ylim()
    text_y = y_min + (y_max - y_min) * y_pos_pct
    
    for admin in ADMINISTRATIONS:
        ax.axvspan(
            admin["start_year"],
            admin["end_year"],
            color=admin["color"],
            alpha=admin["alpha"],
            zorder=0,
            linewidth=0
        )
        if show_labels:
            ax.text(
                admin["label_pos"],
                text_y,
                admin["name"].upper(),
                ha="center",
                va="center",
                fontsize=9,
                fontweight="bold",
                color="#64748B",
                alpha=0.8,
                zorder=1
            )

# -------------------------------------------------------------------------
# 8. Direct Line End Labeling Helper
# -------------------------------------------------------------------------
def add_end_line_label(ax, x_val, y_val, label: str, color: str, offset_x: float = 0.3, offset_y: float = 0.0):
    """
    Labels a line series directly at its final data point, eliminating legend confusion.
    """
    ax.annotate(
        label,
        xy=(x_val, y_val),
        xytext=(x_val + offset_x, y_val + offset_y),
        fontsize=9.5,
        fontweight="bold",
        color=color,
        va="center",
        ha="left",
        bbox=dict(boxstyle="square,pad=0.2", fc=PALETTE["white"], ec="none", alpha=0.85)
    )

# -------------------------------------------------------------------------
# 9. Export Utility (Dual PNG + SVG)
# -------------------------------------------------------------------------
def save_kid_figure(fig, filepath_without_ext: Path or str):
    """
    Saves figure in both high-res PNG (300 DPI) and scalable vector SVG formats.
    """
    p = Path(filepath_without_ext)
    p.parent.mkdir(parents=True, exist_ok=True)
    
    png_path = p.with_suffix(".png")
    svg_path = p.with_suffix(".svg")
    
    fig.savefig(png_path, dpi=300, bbox_inches="tight")
    fig.savefig(svg_path, bbox_inches="tight")
    print(f"[OK] Saved figure: {png_path.name} & {svg_path.name}")
