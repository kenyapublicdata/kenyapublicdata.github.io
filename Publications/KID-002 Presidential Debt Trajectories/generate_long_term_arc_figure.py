#!/usr/bin/env python3
"""Generate Figure 9: 24-Year Debt-to-GDP & Debt Service Arc (2002–2026)."""

from pathlib import Path
import pandas as pd

OUTPUT_DIR = Path(__file__).resolve().parent / "Derivatives" / "Charts"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
DATA_PATH = Path(__file__).resolve().parent / "Data" / "KID002_historical_debt_timeseries_2002_2026.csv"

NAVY = "#0F172A"
CANVAS_BG = "#F8FAFC"
CARD_BG = "#FFFFFF"
SLATE = "#64748B"
SLATE_LIGHT = "#E2E8F0"
SLATE_DARK = "#334155"
RED = "#DC2626"
BLUE = "#2563EB"
GREEN = "#059669"
GOLD = "#D97706"
PURPLE = "#7C3AED"
FONT_SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"

def build():
    df = pd.read_csv(DATA_PATH)
    
    # 1. Landscape (1200 x 675)
    w, h = 1200, 675
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="background-color:{CANVAS_BG}; font-family:{FONT_SANS};">']
    
    svg.append(f'<text x="60" y="52" fill="{RED}" font-size="13" font-weight="800" letter-spacing="1.5">KENYA IN DATA • 24-YEAR MACRO ARC</text>')
    svg.append(f'<text x="60" y="88" fill="{NAVY}" font-size="24" font-weight="900">Kenya\'s Public Debt &amp; Revenue Burden (2002–2026)</text>')
    svg.append(f'<text x="60" y="116" fill="{SLATE}" font-size="14" font-weight="500">Long-run trajectory of Debt-to-GDP (%) and Debt Service as % of Ordinary Revenue across presidential eras</text>')
    
    # Plot area
    x_start = 100
    x_end = 1140
    plot_w = x_end - x_start
    y_top = 170
    y_bottom = 540
    plot_h = y_bottom - y_top
    max_val = 80.0
    
    # Background shading for 3 Presidential Regimes
    # 2002 to 2013 = 11 years (index 0 to 11)
    # 2013 to 2022 = 9 years (index 11 to 20)
    # 2022 to 2026 = 4 years (index 20 to 24)
    n_pts = len(df)
    
    def get_x(idx):
        return x_start + (idx / (n_pts - 1)) * plot_w
        
    def get_y(val):
        return y_bottom - (val / max_val) * plot_h
        
    x_kibaki_end = get_x(11) # 2013
    x_uhuru_end = get_x(20)  # 2022
    
    # Regime bands
    svg.append(f'<rect x="{x_start}" y="{y_top}" width="{x_kibaki_end - x_start}" height="{plot_h}" fill="#F1F5F9" opacity="0.7" />')
    svg.append(f'<rect x="{x_kibaki_end}" y="{y_top}" width="{x_uhuru_end - x_kibaki_end}" height="{plot_h}" fill="#FEF3C7" opacity="0.4" />')
    svg.append(f'<rect x="{x_uhuru_end}" y="{y_top}" width="{x_end - x_uhuru_end}" height="{plot_h}" fill="#EFF6FF" opacity="0.6" />')
    
    # Regime labels at top of bands
    svg.append(f'<text x="{(x_start + x_kibaki_end)/2}" y="{y_top + 25}" fill="{SLATE_DARK}" font-size="13" font-weight="800" text-anchor="middle">KIBAKI (2002–2013)</text>')
    svg.append(f'<text x="{(x_start + x_kibaki_end)/2}" y="{y_top + 42}" fill="{SLATE}" font-size="11" text-anchor="middle">Debt/GDP fell from 61% → 36%</text>')
    
    svg.append(f'<text x="{(x_kibaki_end + x_uhuru_end)/2}" y="{y_top + 25}" fill="{GOLD}" font-size="13" font-weight="800" text-anchor="middle">UHURU (2013–2022)</text>')
    svg.append(f'<text x="{(x_kibaki_end + x_uhuru_end)/2}" y="{y_top + 42}" fill="{SLATE}" font-size="11" text-anchor="middle">Debt/GDP rose from 36% → 64%</text>')
    
    svg.append(f'<text x="{(x_uhuru_end + x_end)/2}" y="{y_top + 25}" fill="{BLUE}" font-size="13" font-weight="800" text-anchor="middle">RUTO (2022–2026*)</text>')
    svg.append(f'<text x="{(x_uhuru_end + x_end)/2}" y="{y_top + 42}" fill="{SLATE}" font-size="11" text-anchor="middle">Service hit 71.2% of rev</text>')
    
    # Statutory Anchor 55%
    y_55 = get_y(55.0)
    svg.append(f'<line x1="{x_start}" y1="{y_55}" x2="{x_end}" y2="{y_55}" stroke="{RED}" stroke-width="1.5" stroke-dasharray="6,4" />')
    svg.append(f'<text x="{x_end - 10}" y="{y_55 - 8}" fill="{RED}" font-size="11.5" font-weight="800" text-anchor="end">55% Statutory Debt Anchor (PFM Act)</text>')
    
    # Horizontal grid
    for gv in [20, 40, 60, 80]:
        gy = get_y(gv)
        svg.append(f'<line x1="{x_start}" y1="{gy}" x2="{x_end}" y2="{gy}" stroke="{SLATE_LIGHT}" stroke-width="1" stroke-dasharray="3,3" />')
        svg.append(f'<text x="{x_start - 12}" y="{gy + 4}" fill="{SLATE}" font-size="11" font-weight="600" text-anchor="end">{gv}%</text>')

    # 1. Line 1: Debt to GDP (%) (Navy Blue)
    pts_gdp = []
    for idx, row in df.iterrows():
        val = row.get("debt_to_gdp_pct")
        if pd.notna(val):
            pts_gdp.append(f"{get_x(idx):.1f},{get_y(float(val)):.1f}")
    svg.append(f'<polyline points="{" ".join(pts_gdp)}" fill="none" stroke="{NAVY}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />')

    # 2. Line 2: Debt Service / Ordinary Revenue (%) (Purple / Red)
    pts_svc = []
    for idx, row in df.iterrows():
        val = row.get("debt_service_to_revenue_pct")
        if pd.notna(val):
            pts_svc.append(f"{get_x(idx):.1f},{get_y(float(val)):.1f}")
    svg.append(f'<polyline points="{" ".join(pts_svc)}" fill="none" stroke="{PURPLE}" stroke-width="3" stroke-dasharray="6,3" stroke-linecap="round" stroke-linejoin="round" />')

    # X axis years
    for idx in range(0, n_pts, 4):
        yr = df.iloc[idx]["calendar_year"]
        svg.append(f'<text x="{get_x(idx)}" y="{y_bottom + 22}" fill="{SLATE}" font-size="11.5" font-weight="600" text-anchor="middle">{yr}</text>')
    # Always show latest year
    svg.append(f'<text x="{get_x(n_pts - 1)}" y="{y_bottom + 22}" fill="{SLATE}" font-size="11.5" font-weight="600" text-anchor="middle">2026*</text>')

    # Legend at bottom center
    svg.append(f'<g transform="translate(340, 575)">')
    svg.append(f'<line x1="0" y1="10" x2="30" y2="10" stroke="{NAVY}" stroke-width="3.5" />')
    svg.append(f'<text x="40" y="14" fill="{NAVY}" font-size="13" font-weight="750">Public Debt as % of GDP</text>')
    
    svg.append(f'<line x1="240" y1="10" x2="270" y2="10" stroke="{PURPLE}" stroke-width="3" stroke-dasharray="6,3" />')
    svg.append(f'<text x="280" y="14" fill="{PURPLE}" font-size="13" font-weight="750">Total Debt Service as % of Ordinary Revenue</text>')
    svg.append('</g>')

    svg.append(f'<line x1="60" y1="615" x2="1140" y2="615" stroke="{SLATE_LIGHT}" stroke-width="1.2" />')
    svg.append(f'<text x="60" y="642" fill="{SLATE}" font-size="11.5" font-style="italic">Data: National Treasury Annual Public Debt Reports (2002–2025); CBK Monthly Bulletins  |  *Provisional</text>')
    svg.append(f'<text x="1140" y="642" fill="{NAVY}" font-size="11.5" font-weight="700" text-anchor="end">Analysis: Kenya in Data • kenyaindata.org</text>')
    svg.append("</svg>\n")
    
    with open(OUTPUT_DIR / "FIG-KID002-H2H-009_long_term_debt_to_gdp_and_service.svg", "w") as f:
        f.write("".join(svg))
        
    # 2. Mobile (1080 x 1350)
    m_w, m_h = 1080, 1350
    m_svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {m_w} {m_h}" width="{m_w}" height="{m_h}" style="background-color:{CANVAS_BG}; font-family:{FONT_SANS};">']
    m_svg.append(f'<text x="50" y="70" fill="{RED}" font-size="16" font-weight="800" letter-spacing="1.5">KENYA IN DATA • 24-YEAR MACRO ARC</text>')
    m_svg.append(f'<text x="50" y="118" fill="{NAVY}" font-size="34" font-weight="900">Kenya\'s 24-Year Debt Trajectory</text>')
    m_svg.append(f'<text x="50" y="156" fill="{SLATE}" font-size="19" font-weight="500">Debt-to-GDP (%) &amp; Debt Service / Revenue (2002–2026)</text>')
    
    # Mobile Plot Area
    mx_start = 90
    mx_end = 990
    m_plot_w = mx_end - mx_start
    my_top = 220
    my_bottom = 860
    m_plot_h = my_bottom - my_top
    
    def get_mx(idx):
        return mx_start + (idx / (n_pts - 1)) * m_plot_w
        
    def get_my(val):
        return my_bottom - (val / max_val) * m_plot_h

    # Regime bands
    mx_k = get_mx(11)
    mx_u = get_mx(20)
    m_svg.append(f'<rect x="{mx_start}" y="{my_top}" width="{mx_k - mx_start}" height="{m_plot_h}" fill="#F1F5F9" opacity="0.7" />')
    m_svg.append(f'<rect x="{mx_k}" y="{my_top}" width="{mx_u - mx_k}" height="{m_plot_h}" fill="#FEF3C7" opacity="0.4" />')
    m_svg.append(f'<rect x="{mx_u}" y="{my_top}" width="{mx_end - mx_u}" height="{m_plot_h}" fill="#EFF6FF" opacity="0.6" />')
    
    # 55% anchor
    my_55 = get_my(55.0)
    m_svg.append(f'<line x1="{mx_start}" y1="{my_55}" x2="{mx_end}" y2="{my_55}" stroke="{RED}" stroke-width="2" stroke-dasharray="8,4" />')
    m_svg.append(f'<text x="{mx_end - 10}" y="{my_55 - 10}" fill="{RED}" font-size="16" font-weight="800" text-anchor="end">55% Legal Anchor</text>')

    # Polylines
    m_pts_gdp = [f"{get_mx(idx):.1f},{get_my(float(row['debt_to_gdp_pct'])):.1f}" for idx, row in df.iterrows() if pd.notna(row.get('debt_to_gdp_pct'))]
    m_pts_svc = [f"{get_mx(idx):.1f},{get_my(float(row['debt_service_to_revenue_pct'])):.1f}" for idx, row in df.iterrows() if pd.notna(row.get('debt_service_to_revenue_pct'))]
    
    m_svg.append(f'<polyline points="{" ".join(m_pts_gdp)}" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />')
    m_svg.append(f'<polyline points="{" ".join(m_pts_svc)}" fill="none" stroke="{PURPLE}" stroke-width="4.5" stroke-dasharray="8,4" stroke-linecap="round" stroke-linejoin="round" />')

    # Mobile 3 Summary Cards below plot
    m_svg.append(f'''
  <g transform="translate(50, 920)">
    <rect x="0" y="0" width="980" height="305" rx="16" fill="{CARD_BG}" stroke="{SLATE_LIGHT}" stroke-width="2" />
    <text x="35" y="42" fill="{NAVY}" font-size="22" font-weight="900">THE THREE REGIME PHASES</text>
    
    <g transform="translate(35, 70)">
      <rect x="0" y="0" width="285" height="130" rx="10" fill="{CANVAS_BG}" />
      <text x="20" y="32" fill="{SLATE_DARK}" font-size="16" font-weight="800">KIBAKI (2002–13)</text>
      <text x="20" y="65" fill="{GREEN}" font-size="24" font-weight="900">61% → 36%</text>
      <text x="20" y="95" fill="{SLATE}" font-size="13">Debt/GDP cut nearly in half</text>
      <text x="20" y="115" fill="{SLATE}" font-size="13">via strong GDP growth</text>
    </g>

    <g transform="translate(345, 70)">
      <rect x="0" y="0" width="285" height="130" rx="10" fill="{CANVAS_BG}" />
      <text x="20" y="32" fill="{GOLD}" font-size="16" font-weight="800">UHURU (2013–22)</text>
      <text x="20" y="65" fill="{RED}" font-size="24" font-weight="900">36% → 64%</text>
      <text x="20" y="95" fill="{SLATE}" font-size="13">Aggressive borrowing surge</text>
      <text x="20" y="115" fill="{SLATE}" font-size="13">Eurobonds &amp; SGR rail</text>
    </g>

    <g transform="translate(655, 70)">
      <rect x="0" y="0" width="285" height="130" rx="10" fill="{CANVAS_BG}" />
      <text x="20" y="32" fill="{BLUE}" font-size="16" font-weight="800">RUTO (2022–26*)</text>
      <text x="20" y="65" fill="{PURPLE}" font-size="24" font-weight="900">71.2% Service</text>
      <text x="20" y="95" fill="{SLATE}" font-size="13">Debt/GDP flat (~68%)</text>
      <text x="20" y="115" fill="{SLATE}" font-size="13">Interest absorbs revenue</text>
    </g>

    <g transform="translate(35, 220)">
      <line x1="0" y1="12" x2="30" y2="12" stroke="{NAVY}" stroke-width="4" />
      <text x="40" y="18" fill="{NAVY}" font-size="15" font-weight="800">Debt / GDP (%)</text>
      <line x1="220" y1="12" x2="250" y2="12" stroke="{PURPLE}" stroke-width="4" stroke-dasharray="6,3" />
      <text x="260" y="18" fill="{PURPLE}" font-size="15" font-weight="800">Debt Service / Revenue (%)</text>
    </g>
  </g>
''')

    m_svg.append(f'<line x1="50" y1="1260" x2="1030" y2="1260" stroke="{SLATE_LIGHT}" stroke-width="1.5" />')
    m_svg.append(f'<text x="50" y="1295" fill="{SLATE}" font-size="17" font-style="italic">Data: National Treasury &amp; CBK (2002–2026)  |  *Provisional</text>')
    m_svg.append(f'<text x="50" y="1325" fill="{NAVY}" font-size="17.5" font-weight="800">Kenya in Data • kenyaindata.org</text>')
    m_svg.append("</svg>\n")
    
    with open(OUTPUT_DIR / "FIG-KID002-H2H-009_long_term_debt_to_gdp_and_service_mobile.svg", "w") as f:
        f.write("".join(m_svg))
        
    print("[OK] Generated FIG-KID002-H2H-009 (Landscape & Mobile)")

if __name__ == "__main__":
    build()
