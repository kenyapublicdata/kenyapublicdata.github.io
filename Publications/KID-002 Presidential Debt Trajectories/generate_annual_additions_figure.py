#!/usr/bin/env python3
"""Generate Figure 8: Annual Year-by-Year Net Debt Additions."""

from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent / "Derivatives" / "Charts"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

NAVY = "#0F172A"
CANVAS_BG = "#F8FAFC"
CARD_BG = "#FFFFFF"
SLATE = "#64748B"
SLATE_LIGHT = "#E2E8F0"
SLATE_DARK = "#334155"
RED = "#DC2626"
BLUE = "#2563EB"
FONT_SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"

def build():
    # 1. Landscape (1200 x 675)
    w, h = 1200, 675
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="background-color:{CANVAS_BG}; font-family:{FONT_SANS};">']
    
    # Header
    svg.append(f'<text x="60" y="52" fill="{RED}" font-size="13" font-weight="800" letter-spacing="1.5">KENYA IN DATA • ANNUAL DEBT FLOWS</text>')
    svg.append(f'<text x="60" y="88" fill="{NAVY}" font-size="24" font-weight="900">Annual Net Debt Additions: Year-by-Year Comparison</text>')
    svg.append(f'<text x="60" y="116" fill="{SLATE}" font-size="14" font-weight="500">Net billions added to public debt stock in each successive fiscal year • Uhuru (2013–17) vs Ruto (2022–26*)</text>')
    
    # Legend
    svg.append(f'<rect x="840" y="65" width="14" height="14" rx="3" fill="{RED}" />')
    svg.append(f'<text x="862" y="77" fill="{NAVY}" font-size="12" font-weight="700">Uhuru Kenyatta</text>')
    svg.append(f'<rect x="990" y="65" width="14" height="14" rx="3" fill="{BLUE}" />')
    svg.append(f'<text x="1012" y="77" fill="{NAVY}" font-size="12" font-weight="700">William Ruto</text>')
    
    years_data = [
        ("YEAR 1", "FY13/14 vs FY22/23", 476.0, 1517.9, "+KSh 476B", "+KSh 1,518B", "KES depreciated to 140.5"),
        ("YEAR 2", "FY14/15 vs FY23/24", 473.4, 278.0, "+KSh 473B", "+KSh 278B", "KES rebounded to 129.0"),
        ("YEAR 3", "FY15/16 vs FY24/25", 767.6, 1257.8, "+KSh 768B", "+KSh 1,258B", "Domestic bond surge"),
        ("YEAR 4", "FY16/17 vs FY25/26*", 795.0, 1198.5, "+KSh 795B", "+KSh 1,198B*", "Provisional estimate"),
    ]
    
    col_w = 230
    col_gap = 25
    x_start = 80
    y_zero = 530
    y_top = 170
    max_val = 1800.0
    plot_h = y_zero - y_top
    
    for gv in [400, 800, 1200, 1600]:
        gy = y_zero - (gv / max_val) * plot_h
        svg.append(f'<line x1="{x_start}" y1="{gy}" x2="{x_start + 4*col_w + 3*col_gap}" stroke="{SLATE_LIGHT}" stroke-width="1" stroke-dasharray="4,4" />')
        svg.append(f'<text x="{x_start - 15}" y="{gy + 4}" fill="{SLATE}" font-size="11" font-weight="600" text-anchor="end">+KSh {gv}B</text>')
        
    svg.append(f'<line x1="{x_start}" y1="{y_zero}" x2="{x_start + 4*col_w + 3*col_gap}" stroke="{SLATE}" stroke-width="1.5" />')
    svg.append(f'<text x="{x_start - 15}" y="{y_zero + 4}" fill="{SLATE}" font-size="11" font-weight="600" text-anchor="end">0</text>')
    
    bar_w = 42
    
    for i, (yr_title, yr_sub, u_val, r_val, u_str, r_str, note) in enumerate(years_data):
        cx = x_start + i * (col_w + col_gap)
        svg.append(f'<rect x="{cx}" y="150" width="{col_w}" height="425" rx="10" fill="{CARD_BG}" stroke="{SLATE_LIGHT}" stroke-width="1" />')
        svg.append(f'<text x="{cx + col_w/2}" y="178" fill="{NAVY}" font-size="15" font-weight="900" text-anchor="middle">{yr_title}</text>')
        svg.append(f'<text x="{cx + col_w/2}" y="196" fill="{SLATE}" font-size="11" font-weight="500" text-anchor="middle">{yr_sub}</text>')
        
        u_h = (u_val / max_val) * plot_h
        u_y = y_zero - u_h
        u_x = cx + col_w/2 - bar_w - 6
        svg.append(f'<rect x="{u_x}" y="{u_y}" width="{bar_w}" height="{u_h}" rx="4" fill="{RED}" />')
        svg.append(f'<text x="{u_x + bar_w/2}" y="{u_y - 8}" fill="{RED}" font-size="11.5" font-weight="800" text-anchor="middle">{u_str}</text>')
        
        r_h = (r_val / max_val) * plot_h
        r_y = y_zero - r_h
        r_x = cx + col_w/2 + 6
        svg.append(f'<rect x="{r_x}" y="{r_y}" width="{bar_w}" height="{r_h}" rx="4" fill="{BLUE}" />')
        svg.append(f'<text x="{r_x + bar_w/2}" y="{r_y - 8}" fill="{BLUE}" font-size="11.5" font-weight="800" text-anchor="middle">{r_str}</text>')
        
        svg.append(f'<rect x="{cx + 10}" y="538" width="{col_w - 20}\" height=\"28\" rx=\"5\" fill=\"{CANVAS_BG}\" />')
        svg.append(f'<text x="{cx + col_w/2}" y="556" fill="{SLATE_DARK}" font-size="9.5" font-weight="600" text-anchor="middle">{note}</text>')

    svg.append(f'<line x1="60" y1="615" x2="1140" y2="615" stroke="{SLATE_LIGHT}" stroke-width="1.2" />')
    svg.append(f'<text x="60" y="642" fill="{SLATE}" font-size="11.5" font-style="italic">Data: National Treasury Annual Public Debt Reports &amp; June 2026 Monthly Bulletin  |  *FY25/26 provisional</text>')
    svg.append(f'<text x="1140" y="642" fill="{NAVY}" font-size="11.5" font-weight="700" text-anchor="end">Analysis: Kenya in Data • kenyaindata.org</text>')
    svg.append("</svg>\n")
    
    with open(OUTPUT_DIR / "FIG-KID002-H2H-008_annual_debt_additions_year_by_year.svg", "w") as f:
        f.write("".join(svg))
        
    # 2. Mobile (1080 x 1350)
    m_w, m_h = 1080, 1350
    m_svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {m_w} {m_h}" width="{m_w}" height="{m_h}" style="background-color:{CANVAS_BG}; font-family:{FONT_SANS};">']
    m_svg.append(f'<text x="50" y="70" fill="{RED}" font-size="16" font-weight="800" letter-spacing="1.5">KENYA IN DATA • ANNUAL DEBT FLOWS</text>')
    m_svg.append(f'<text x="50" y="118" fill="{NAVY}" font-size="34" font-weight="900">Annual Net Debt Additions</text>')
    m_svg.append(f'<text x="50" y="156" fill="{SLATE}" font-size="19" font-weight="500">Net KSh billions added in each successive fiscal year</text>')
    
    row_y_start = 200
    row_h = 240
    row_gap = 20
    
    for i, (yr_title, yr_sub, u_val, r_val, u_str, r_str, note) in enumerate(years_data):
        ry = row_y_start + i * (row_h + row_gap)
        m_svg.append(f'<g transform="translate(50, {ry})">')
        m_svg.append(f'<rect x="0" y="0" width="980" height="{row_h}" rx="14" fill="{CARD_BG}" stroke="{SLATE_LIGHT}" stroke-width="1.5" />')
        m_svg.append(f'<text x="30" y="38" fill="{NAVY}" font-size="20" font-weight="900">{yr_title} ({yr_sub})</text>')
        m_svg.append(f'<text x="950" y="38" fill="{SLATE}" font-size="15" font-weight="600" text-anchor="end">{note}</text>')
        
        m_svg.append(f'<text x="30" y="80" fill="{RED}" font-size="15" font-weight="800">Uhuru: {u_str}</text>')
        m_svg.append(f'<rect x="30" y="92" width="{(u_val / 1600.0) * 800}" height="36" rx="6" fill="{RED}" />')
        
        m_svg.append(f'<text x="30" y="158" fill="{BLUE}" font-size="15" font-weight="800">Ruto: {r_str}</text>')
        m_svg.append(f'<rect x="30" y="170" width="{(r_val / 1600.0) * 800}" height="36" rx="6" fill="{BLUE}" />')
        m_svg.append('</g>')

    m_svg.append(f'<line x1="50" y1="1260" x2="1030" y2="1260" stroke="{SLATE_LIGHT}" stroke-width="1.5" />')
    m_svg.append(f'<text x="50" y="1295" fill="{SLATE}" font-size="17" font-style="italic">Data: National Treasury Annual Debt Reports; June 2026 Bulletin  |  *Provisional</text>')
    m_svg.append(f'<text x="50" y="1325" fill="{NAVY}" font-size="17.5" font-weight="800">Kenya in Data • kenyaindata.org</text>')
    m_svg.append("</svg>\n")
    
    with open(OUTPUT_DIR / "FIG-KID002-H2H-008_annual_debt_additions_year_by_year_mobile.svg", "w") as f:
        f.write("".join(m_svg))
        
    print("[OK] Generated FIG-KID002-H2H-008 (Landscape & Mobile)")

if __name__ == "__main__":
    build()
