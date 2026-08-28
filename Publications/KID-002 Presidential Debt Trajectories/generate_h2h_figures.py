#!/usr/bin/env python3
"""
PRJ-001 / KID-002: Uhuru vs Ruto Head-to-Head Visual Engine
============================================================
Generates 5 publication-ready figures in both 16:9 Landscape and 4:5 Mobile SVG formats:
1. FIG-KID002-H2H-001: Head-to-Head Scorecard Hero Card
2. FIG-KID002-H2H-002: Normalized Debt Stock Growth (Base Year 0 = 100)
3. FIG-KID002-H2H-003: Debt-to-GDP Trajectory (First 4 Fiscal Years)
4. FIG-KID002-H2H-004: Composition of Net Debt Stock Added (Domestic vs External)
5. FIG-KID002-H2H-005: The Revenue Squeeze — Interest Payments as % of Ordinary Revenue

Conforms to Kenya in Data Visual Style Guide & Mobile Visualization Standard.
Tightened with technical caveats regarding fiscal windows, debt-stock perimeters, and ordinary revenue.
"""

from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent / "Derivatives" / "Charts"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------------
# BRAND COLOR TOKENS
# -----------------------------------------------------------------------------
NAVY = "#0F172A"         # Obsidian Navy (Text, headers, primary elements)
CANVAS_BG = "#F8FAFC"    # Crisp Ivory Background
CARD_BG = "#FFFFFF"      # White card surface
SLATE = "#64748B"        # Neutral Slate (Subtitles, labels, borders)
SLATE_LIGHT = "#E2E8F0"  # Subtle gridlines / borders
SLATE_DARK = "#334155"   # Dark slate
RED = "#DC2626"          # Alert Crimson / Accent
GREEN = "#059669"        # Emerald Green (Revenue / Anchor)
GOLD = "#D97706"         # Warm Ochre Gold (External debt / Uhuru accent)
BLUE = "#2563EB"         # Royal Blue (Domestic debt / Ruto accent)
PURPLE = "#7C3AED"       # Violet (Interest burden)
AMBER_BG = "#FEF3C7"     # Warning tint
RED_BG = "#FEE2E2"       # Alert tint
BLUE_BG = "#EFF6FF"      # Blue tint

# Common Font Family
FONT_SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

# -----------------------------------------------------------------------------
# SVG BUILDER HELPERS
# -----------------------------------------------------------------------------
def svg_header(w, h):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="background-color:{CANVAS_BG}; font-family:{FONT_SANS};">
<defs>
  <filter id="card-shadow" x="-5%" y="-5%" width="110%" height="110%" filterUnits="userSpaceOnUse">
    <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0F172A" flood-opacity="0.05" />
  </filter>
  <filter id="subtle-shadow" x="-2%" y="-2%" width="104%" height="104%" filterUnits="userSpaceOnUse">
    <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.04" />
  </filter>
</defs>
'''

def svg_footer():
    return "</svg>\n"

def draw_header_landscape(title, subtitle, topic="KENYA IN DATA • PUBLIC DEBT COMPARISON"):
    return f'''
  <!-- Header -->
  <text x="60" y="52" fill="{RED}" font-size="13" font-weight="800" letter-spacing="1.5">{topic}</text>
  <text x="60" y="88" fill="{NAVY}" font-size="24" font-weight="900">{title}</text>
  <text x="60" y="116" fill="{SLATE}" font-size="14" font-weight="500">{subtitle}</text>
'''

def draw_footer_landscape(source_text, note=""):
    note_part = f"  |  {note}" if note else ""
    return f'''
  <!-- Footer -->
  <line x1="60" y1="615" x2="1140" y2="615" stroke="{SLATE_LIGHT}" stroke-width="1.2" />
  <text x="60" y="642" fill="{SLATE}" font-size="11.5" font-style="italic">Data: {source_text}{note_part}</text>
  <text x="1140" y="642" fill="{NAVY}" font-size="11.5" font-weight="700" text-anchor="end">Analysis: Kenya in Data • kenyaindata.org</text>
'''

def draw_header_mobile(title, subtitle, topic="KENYA IN DATA • PUBLIC DEBT"):
    return f'''
  <!-- Mobile Header -->
  <text x="50" y="70" fill="{RED}" font-size="16" font-weight="800" letter-spacing="1.5">{topic}</text>
  <text x="50" y="118" fill="{NAVY}" font-size="34" font-weight="900">{title}</text>
  <text x="50" y="156" fill="{SLATE}" font-size="19" font-weight="500">{subtitle}</text>
'''

def draw_footer_mobile(source_text, note=""):
    note_part = f"  |  {note}" if note else ""
    return f'''
  <!-- Mobile Footer -->
  <line x1="50" y1="1260" x2="1030" y2="1260" stroke="{SLATE_LIGHT}" stroke-width="1.5" />
  <text x="50" y="1295" fill="{SLATE}" font-size="17" font-style="italic">Data: {source_text}{note_part}</text>
  <text x="50" y="1325" fill="{NAVY}" font-size="17.5" font-weight="800">Kenya in Data • kenyaindata.org</text>
'''

# =============================================================================
# FIGURE 1: HEAD-TO-HEAD HERO SCORECARD
# =============================================================================
def build_fig1():
    # Landscape (1200 x 675)
    svg = [svg_header(1200, 675)]
    svg.append(draw_header_landscape(
        "Uhuru vs Ruto: Public Debt in Matched 4-Year Fiscal Windows",
        "Comparing debt stock expansion, GDP tracking, portfolio composition and ordinary revenue absorption"
    ))
    
    # Left Box: Uhuru Kenyatta (Jun 2013 → Jun 2017)
    svg.append(f'''
  <!-- Uhuru Card -->
  <rect x="60" y="140" width="520" height="455" rx="14" fill="{CARD_BG}" stroke="{SLATE_LIGHT}" stroke-width="1.5" filter="url(#card-shadow)" />
  <rect x="60" y="140" width="520" height="70" rx="14" fill="#0F172A" />
  <rect x="60" y="196" width="520" height="14" fill="#0F172A" />
  <text x="90" y="182" fill="#FFFFFF" font-size="19" font-weight="800">UHURU WINDOW (Jun 2013 → Jun 2017)</text>
  
  <!-- Row 1: Stock Change -->
  <rect x="85" y="225" width="470" height="75" rx="8" fill="{CANVAS_BG}" />
  <text x="105" y="250" fill="{SLATE}" font-size="12" font-weight="600">OUTSTANDING DEBT STOCK</text>
  <text x="105" y="282" fill="{NAVY}" font-size="22" font-weight="900">KSh 1.89T → KSh 4.41T</text>
  <rect x="420" y="240" width="120" height="44" rx="6" fill="#FEE2E2" />
  <text x="480" y="267" fill="{RED}" font-size="17" font-weight="900" text-anchor="middle">+132.7%</text>
  <text x="480" y="278" fill="{RED}" font-size="9.5" font-weight="700" text-anchor="middle">(+75.2% real)</text>
  
  <!-- Row 2: Stock Added & Debt/GDP -->
  <g transform="translate(85, 310)">
    <rect x="0" y="0" width="225" height="75" rx="8" fill="{CANVAS_BG}" />
    <text x="15" y="24" fill="{SLATE}" font-size="11" font-weight="600">NET STOCK ADDED</text>
    <text x="15" y="56" fill="{NAVY}" font-size="20" font-weight="800">+KSh 2.51T</text>
  </g>
  <g transform="translate(330, 310)">
    <rect x="0" y="0" width="225" height="75" rx="8" fill="{CANVAS_BG}" />
    <text x="15" y="24" fill="{SLATE}" font-size="11" font-weight="600">DEBT-TO-GDP CHANGE</text>
    <text x="15" y="56" fill="{RED}" font-size="20" font-weight="800">42.1% → 57.2%</text>
    <text x="15" y="68" fill="{RED}" font-size="10.5" font-weight="700">+15.1 pp (outpaced GDP)</text>
  </g>

  <!-- Row 3: Key Driver & Debt Service -->
  <g transform="translate(85, 395)">
    <rect x="0" y="0" width="225" height="85" rx="8" fill="{CANVAS_BG}" />
    <text x="15" y="24" fill="{SLATE}" font-size="11" font-weight="600">DRIVER OF STOCK INCREASE</text>
    <text x="15" y="52" fill="{GOLD}" font-size="16.5" font-weight="800">External Debt (57.7%)</text>
    <text x="15" y="70" fill="{SLATE}" font-size="11">Eurobonds &amp; Bilateral (SGR)</text>
  </g>
  <g transform="translate(330, 395)">
    <rect x="0" y="0" width="225" height="85" rx="8" fill="{CANVAS_BG}" />
    <text x="15" y="24" fill="{SLATE}" font-size="11" font-weight="600">INTEREST / ORDINARY REVENUE</text>
    <text x="15" y="52" fill="{GREEN}" font-size="20" font-weight="900">20.8%</text>
    <text x="15" y="70" fill="{SLATE}" font-size="11">KSh 271B interest (FY16/17)</text>
  </g>
  
  <!-- Uhuru Takeaway Badge -->
  <rect x="85" y="495" width="470" height="75" rx="8" fill="#F1F5F9" stroke="{SLATE_LIGHT}" stroke-width="1" />
  <text x="105" y="525" fill="{NAVY}" font-size="12.5" font-weight="800">CORE CHARACTERISTIC: RAPID ACCUMULATION</text>
  <text x="105" y="548" fill="{SLATE_DARK}" font-size="11.5">Grew stock 2.7x faster; debt outran GDP growth (+15.1 pp); lower carrying cost.</text>
''')

    # Right Box: William Ruto Window (Jun 2022 → Jun 2026*)
    svg.append(f'''
  <!-- Ruto Card -->
  <rect x="620" y="140" width="520" height="455" rx="14" fill="{CARD_BG}" stroke="{SLATE_LIGHT}" stroke-width="1.5" filter="url(#card-shadow)" />
  <rect x="620" y="140" width="520" height="70" rx="14" fill="{BLUE}" />
  <rect x="620" y="196" width="520" height="14" fill="{BLUE}" />
  <text x="650" y="182" fill="#FFFFFF" font-size="19" font-weight="800">RUTO-ERA WINDOW (Jun 2022 → Jun 2026*)</text>
  
  <!-- Row 1: Stock Change -->
  <rect x="645" y="225" width="470" height="75" rx="8" fill="{CANVAS_BG}" />
  <text x="665" y="250" fill="{SLATE}" font-size="12" font-weight="600">OUTSTANDING DEBT STOCK</text>
  <text x="665" y="282" fill="{NAVY}" font-size="22" font-weight="900">KSh 8.76T → ~KSh 13.01T*</text>
  <rect x="980" y="240" width="120" height="44" rx="6" fill="#EFF6FF" />
  <text x="1040" y="267" fill="{BLUE}" font-size="17" font-weight="900" text-anchor="middle">+48.5%*</text>
  <text x="1040" y="278" fill="{BLUE}" font-size="9.5" font-weight="700" text-anchor="middle">(+19.1% real)</text>
  
  <!-- Row 2: Stock Added & Debt/GDP -->
  <g transform="translate(645, 310)">
    <rect x="0" y="0" width="225" height="75" rx="8" fill="{CANVAS_BG}" />
    <text x="15" y="24" fill="{SLATE}" font-size="11" font-weight="600">NET STOCK ADDED</text>
    <text x="15" y="56" fill="{NAVY}" font-size="20" font-weight="800">+KSh 4.25T*</text>
  </g>
  <g transform="translate(890, 310)">
    <rect x="0" y="0" width="225" height="75" rx="8" fill="{CANVAS_BG}" />
    <text x="15" y="24" fill="{SLATE}" font-size="11" font-weight="600">DEBT-TO-GDP CHANGE</text>
    <text x="15" y="56" fill="{GREEN}" font-size="20" font-weight="800">68.7% → ~68.5%*</text>
    <text x="15" y="68" fill="{GREEN}" font-size="10.5" font-weight="700">-0.2 pp (endpoint flat)</text>
  </g>

  <!-- Row 3: Key Driver & Debt Service -->
  <g transform="translate(645, 395)">
    <rect x="0" y="0" width="225" height="85" rx="8" fill="{CANVAS_BG}" />
    <text x="15" y="24" fill="{SLATE}" font-size="11" font-weight="600">DRIVER OF STOCK INCREASE</text>
    <text x="15" y="52" fill="{BLUE}" font-size="16.5" font-weight="800">Domestic Debt (68.3%)</text>
    <text x="15" y="70" fill="{SLATE}" font-size="11">T-Bonds &amp; Local Securities</text>
  </g>
  <g transform="translate(890, 395)">
    <rect x="0" y="0" width="225" height="85" rx="8" fill="{CANVAS_BG}" />
    <text x="15" y="24" fill="{SLATE}" font-size="11" font-weight="600">INTEREST / ORDINARY REVENUE</text>
    <text x="15" y="52" fill="{RED}" font-size="20" font-weight="900">40.8%</text>
    <text x="15" y="70" fill="{RED}" font-size="11" font-weight="600">KSh 988B interest (FY24/25)</text>
  </g>
  
  <!-- Ruto Takeaway Badge -->
  <rect x="645" y="495" width="470" height="75" rx="8" fill="#F1F5F9" stroke="{SLATE_LIGHT}" stroke-width="1" />
  <text x="665" y="525" fill="{NAVY}" font-size="12.5" font-weight="800">CORE CHARACTERISTIC: REVENUE SQUEEZE</text>
  <text x="665" y="548" fill="{SLATE_DARK}" font-size="11.5">Added +KSh 4.25T on a large base; endpoint debt/GDP flat; interest burden doubled to 40.8%.</text>
''')
    
    svg.append(draw_footer_landscape(
        "National Treasury Annual Debt Reports (2016/17, 2024/25), June 2026 Monthly Bulletin; KNBS CPI series",
        "*June 2026 figures are provisional. Ruto took office Sept 2022; June 2022–2026 provides standardized fiscal window."
    ))
    svg.append(svg_footer())
    
    with open(OUTPUT_DIR / "FIG-KID002-H2H-001_head_to_head_scorecard.svg", "w") as f:
        f.write("".join(svg))
    
    # -------------------------------------------------------------------------
    # Mobile Variant (1080 x 1350)
    # -------------------------------------------------------------------------
    m_svg = [svg_header(1080, 1350)]
    m_svg.append(draw_header_mobile(
        "Uhuru vs Ruto: Public Debt Scorecard",
        "Matched 4-year fiscal windows: growth speed, debt-to-GDP and ordinary revenue burden"
    ))
    
    # Uhuru Mobile Card (Top)
    m_svg.append(f'''
  <!-- Uhuru Mobile Card -->
  <g transform="translate(50, 190)">
    <rect x="0" y="0" width="980" height="490" rx="16" fill="{CARD_BG}" stroke="{SLATE_LIGHT}" stroke-width="2" filter="url(#card-shadow)" />
    <rect x="0" y="0" width="980" height="75" rx="16" fill="{NAVY}" />
    <rect x="0" y="50" width="980" height="25" fill="{NAVY}" />
    <text x="35" y="48" fill="#FFFFFF" font-size="25" font-weight="900">UHURU WINDOW (Jun 2013 → Jun 2017)</text>
    
    <!-- Big Stat 1 -->
    <rect x="30" y="100" width="440" height="115" rx="12" fill="{CANVAS_BG}" />
    <text x="50" y="132" fill="{SLATE}" font-size="16" font-weight="700">PUBLIC DEBT STOCK</text>
    <text x="50" y="172" fill="{NAVY}" font-size="27" font-weight="900">KSh 1.89T → 4.41T</text>
    <text x="50" y="200" fill="{RED}" font-size="18" font-weight="800">+132.7% nominal (+75.2% real)</text>
    
    <!-- Big Stat 2 -->
    <rect x="510" y="100" width="440" height="115" rx="12" fill="{CANVAS_BG}" />
    <text x="530" y="132" fill="{SLATE}" font-size="16" font-weight="700">NET STOCK ADDED</text>
    <text x="530" y="172" fill="{NAVY}" font-size="27" font-weight="900">+KSh 2.51 Trillion</text>
    <text x="530" y="200" fill="{SLATE_DARK}" font-size="16" font-weight="600">External-heavy (57.7% of stock added)</text>
    
    <!-- Row 2 -->
    <rect x="30" y="235" width="440" height="115" rx="12" fill="{CANVAS_BG}" />
    <text x="50" y="267" fill="{SLATE}" font-size="16" font-weight="700">DEBT / GDP TRAJECTORY</text>
    <text x="50" y="307" fill="{RED}" font-size="27" font-weight="900">42.1% → 57.2%</text>
    <text x="50" y="335" fill="{RED}" font-size="17" font-weight="700">+15.1 pp (substantially outpaced GDP)</text>
    
    <rect x="510" y="235" width="440" height="115" rx="12" fill="{CANVAS_BG}" />
    <text x="530" y="267" fill="{SLATE}" font-size="16" font-weight="700">INTEREST / ORDINARY REVENUE</text>
    <text x="530" y="307" fill="{GREEN}" font-size="27" font-weight="900">20.8%</text>
    <text x="530" y="335" fill="{SLATE_DARK}" font-size="16" font-weight="600">KSh 271B interest in FY16/17</text>
    
    <rect x="30" y="370" width="920" height="95" rx="12" fill="#F1F5F9" stroke="{SLATE_LIGHT}" stroke-width="1.5" />
    <text x="50" y="405" fill="{NAVY}" font-size="18" font-weight="900">CORE STORY: RAPID ACCUMULATION</text>
    <text x="50" y="435" fill="{SLATE_DARK}" font-size="17">Grew debt stock 2.7x faster than Ruto window, sharply worsening debt-to-GDP (+15.1 pp).</text>
  </g>
''')

    # Ruto Mobile Card (Bottom)
    m_svg.append(f'''
  <!-- Ruto Mobile Card -->
  <g transform="translate(50, 715)">
    <rect x="0" y="0" width="980" height="505" rx="16" fill="{CARD_BG}" stroke="{SLATE_LIGHT}" stroke-width="2" filter="url(#card-shadow)" />
    <rect x="0" y="0" width="980" height="75" rx="16" fill="{BLUE}" />
    <rect x="0" y="50" width="980" height="25" fill="{BLUE}" />
    <text x="35" y="48" fill="#FFFFFF" font-size="25" font-weight="900">RUTO-ERA WINDOW (Jun 2022 → Jun 2026*)</text>
    
    <!-- Big Stat 1 -->
    <rect x="30" y="100" width="440" height="115" rx="12" fill="{CANVAS_BG}" />
    <text x="50" y="132" fill="{SLATE}" font-size="16" font-weight="700">PUBLIC DEBT STOCK</text>
    <text x="50" y="172" fill="{NAVY}" font-size="27" font-weight="900">KSh 8.76T → ~13.01T*</text>
    <text x="50" y="200" fill="{BLUE}" font-size="18" font-weight="800">+48.5% nominal (+19.1% real)</text>
    
    <!-- Big Stat 2 -->
    <rect x="510" y="100" width="440" height="115" rx="12" fill="{CANVAS_BG}" />
    <text x="530" y="132" fill="{SLATE}" font-size="16" font-weight="700">NET STOCK ADDED</text>
    <text x="530" y="172" fill="{NAVY}" font-size="27" font-weight="900">+KSh 4.25 Trillion*</text>
    <text x="530" y="200" fill="{SLATE_DARK}" font-size="16" font-weight="600">Domestic-heavy (68.3% of stock added)</text>
    
    <!-- Row 2 -->
    <rect x="30" y="235" width="440" height="115" rx="12" fill="{CANVAS_BG}" />
    <text x="50" y="267" fill="{SLATE}" font-size="16" font-weight="700">DEBT / GDP TRAJECTORY</text>
    <text x="50" y="307" fill="{GREEN}" font-size="27" font-weight="900">68.7% → ~68.5%*</text>
    <text x="50" y="335" fill="{GREEN}" font-size="17" font-weight="700">-0.2 pp (endpoint-to-endpoint flat)</text>
    
    <rect x="510" y="235" width="440" height="115" rx="12" fill="{CANVAS_BG}" />
    <text x="530" y="267" fill="{SLATE}" font-size="16" font-weight="700">INTEREST / ORDINARY REVENUE</text>
    <text x="530" y="307" fill="{RED}" font-size="27" font-weight="900">40.8%</text>
    <text x="530" y="335" fill="{RED}" font-size="17" font-weight="700">KSh 988B interest in FY24/25 (2x burden)</text>
    
    <rect x="30" y="370" width="920" height="105" rx="12" fill="#F1F5F9" stroke="{SLATE_LIGHT}" stroke-width="1.5" />
    <text x="50" y="405" fill="{NAVY}" font-size="18" font-weight="900">CORE STORY: THE CASH SERVICING SQUEEZE</text>
    <text x="50" y="435" fill="{SLATE_DARK}" font-size="17">Added +KSh 4.25T on a huge base; debt/GDP flat; interest burden doubled to 40.8% of ordinary revenue.</text>
  </g>
''')
    
    m_svg.append(draw_footer_mobile(
        "National Treasury; KNBS",
        "*June 2026 provisional. Matched June-to-June fiscal windows."
    ))
    m_svg.append(svg_footer())
    
    with open(OUTPUT_DIR / "FIG-KID002-H2H-001_head_to_head_scorecard_mobile.svg", "w") as f:
        f.write("".join(m_svg))
    print("[OK] Generated FIG-KID002-H2H-001 (Landscape & Mobile)")

# =============================================================================
# FIGURE 2: INDEXED DEBT GROWTH (BASE = 100)
# =============================================================================
def build_fig2():
    uhuru_nom = [100.0, 127.9, 150.1, 190.7, 232.7]
    uhuru_real = [100.0, 119.1, 130.6, 156.8, 175.2]
    ruto_nom = [100.0, 117.3, 120.8, 134.8, 148.5]
    ruto_real = [100.0, 108.7, 107.0, 115.1, 119.1]
    
    w, h = 1200, 675
    svg = [svg_header(w, h)]
    svg.append(draw_header_landscape(
        "Debt Stock Growth: Indexed to Start of Fiscal Window (Year 0 = 100)",
        "Comparing cumulative nominal and inflation-adjusted growth over matching 4-year fiscal windows"
    ))
    
    x_min, x_max = 120, 960
    y_min, y_max = 570, 160
    
    grid_vals = [100, 150, 200, 250]
    for val in grid_vals:
        y_pos = y_min - (val - 100) / 150 * (y_min - y_max)
        svg.append(f'<line x1="{x_min}" y1="{y_pos}" x2="{x_max}" y2="{y_pos}" stroke="{SLATE_LIGHT}" stroke-width="1" stroke-dasharray="4,4" />')
        svg.append(f'<text x="{x_min - 15}" y="{y_pos + 4}" fill="{SLATE}" font-size="12" font-weight="600" text-anchor="end">{val}</text>')
    
    y_100 = y_min
    svg.append(f'<line x1="{x_min}" y1="{y_100}" x2="{x_max}" y2="{y_100}" stroke="{SLATE}" stroke-width="1.5" />')
    
    x_coords = [x_min + i * (x_max - x_min) / 4 for i in range(5)]
    labels_uhuru = ["Jun 2013", "Jun 2014", "Jun 2015", "Jun 2016", "Jun 2017"]
    labels_ruto = ["Jun 2022", "Jun 2023", "Jun 2024", "Jun 2025", "Jun 2026*"]
    
    for i in range(5):
        cx = x_coords[i]
        svg.append(f'<line x1="{cx}" y1="{y_min}" x2="{cx}" y2="{y_min + 8}" stroke="{SLATE}" stroke-width="1.5" />')
        svg.append(f'<text x="{cx}" y="{y_min + 24}" fill="{NAVY}" font-size="13" font-weight="700" text-anchor="middle">Year {i}</text>')
        svg.append(f'<text x="{cx}" y="{y_min + 40}" fill="{SLATE}" font-size="10.5" text-anchor="middle">U: {labels_uhuru[i]}</text>')
        svg.append(f'<text x="{cx}" y="{y_min + 54}" fill="{SLATE}" font-size="10.5" text-anchor="middle">R: {labels_ruto[i]}</text>')

    def get_y(val):
        return y_min - (val - 100) / 150 * (y_min - y_max)
    
    pts_u_nom = " ".join([f"{x_coords[i]},{get_y(uhuru_nom[i])}" for i in range(5)])
    pts_u_real = " ".join([f"{x_coords[i]},{get_y(uhuru_real[i])}" for i in range(5)])
    
    svg.append(f'<polyline points="{pts_u_real}" fill="none" stroke="{RED}" stroke-width="2.5" stroke-dasharray="6,4" />')
    svg.append(f'<polyline points="{pts_u_nom}" fill="none" stroke="{RED}" stroke-width="4" />')
    
    pts_r_nom = " ".join([f"{x_coords[i]},{get_y(ruto_nom[i])}" for i in range(5)])
    pts_r_real = " ".join([f"{x_coords[i]},{get_y(ruto_real[i])}" for i in range(5)])
    
    svg.append(f'<polyline points="{pts_r_real}" fill="none" stroke="{BLUE}" stroke-width="2.5" stroke-dasharray="6,4" />')
    svg.append(f'<polyline points="{pts_r_nom}" fill="none" stroke="{BLUE}" stroke-width="4" />')

    for i in range(5):
        svg.append(f'<circle cx="{x_coords[i]}" cy="{get_y(uhuru_nom[i])}" r="6" fill="{RED}" stroke="#FFFFFF" stroke-width="2" />')
        svg.append(f'<circle cx="{x_coords[i]}" cy="{get_y(ruto_nom[i])}" r="6" fill="{BLUE}" stroke="#FFFFFF" stroke-width="2" />')

    svg.append(f'''
  <!-- Uhuru End Callout -->
  <g transform="translate({x_coords[4] + 15}, {get_y(uhuru_nom[4]) - 20})">
    <rect x="0" y="0" width="180" height="48" rx="6" fill="#FFFFFF" stroke="{RED}" stroke-width="1.5" filter="url(#subtle-shadow)" />
    <text x="12" y="20" fill="{RED}" font-size="13" font-weight="900">Uhuru: +132.7%</text>
    <text x="12" y="38" fill="{SLATE}" font-size="11" font-weight="600">Index: 232.7 (Real: +75.2%)</text>
  </g>
''')

    svg.append(f'''
  <!-- Ruto End Callout -->
  <g transform="translate({x_coords[4] + 15}, {get_y(ruto_nom[4]) - 14})">
    <rect x="0" y="0" width="180" height="48" rx="6" fill="#FFFFFF" stroke="{BLUE}" stroke-width="1.5" filter="url(#subtle-shadow)" />
    <text x="12" y="20" fill="{BLUE}" font-size="13" font-weight="900">Ruto Window: +48.5%*</text>
    <text x="12" y="38" fill="{SLATE}" font-size="11" font-weight="600">Index: 148.5 (Real: +19.1%)</text>
  </g>
''')

    svg.append(f'''
  <g transform="translate(140, 165)">
    <rect x="0" y="0" width="340" height="60" rx="8" fill="#FFFFFF" fill-opacity="0.9" stroke="{SLATE_LIGHT}" stroke-width="1" />
    <line x1="15" y1="20" x2="45" y2="20" stroke="{RED}" stroke-width="3.5" />
    <text x="55" y="24" fill="{NAVY}" font-size="11.5" font-weight="700">Uhuru Nominal</text>
    <line x1="175" y1="20" x2="205" y2="20" stroke="{RED}" stroke-width="2" stroke-dasharray="4,3" />
    <text x="215" y="24" fill="{SLATE}" font-size="11" font-weight="600">Uhuru Real (CPI-adj)</text>

    <line x1="15" y1="42" x2="45" y2="42" stroke="{BLUE}" stroke-width="3.5" />
    <text x="55" y="46" fill="{NAVY}" font-size="11.5" font-weight="700">Ruto Window Nominal</text>
    <line x1="175" y1="42" x2="205" y2="42" stroke="{BLUE}" stroke-width="2" stroke-dasharray="4,3" />
    <text x="215" y="46" fill="{SLATE}" font-size="11" font-weight="600">Ruto Real (CPI-adj)</text>
  </g>
''')

    svg.append(draw_footer_landscape(
        "National Treasury Annual Debt Reports; KNBS June CPI series (2009=100 & 2019=100)",
        "Year 0 = 100 baseline. Deflated by matching June CPI observations."
    ))
    svg.append(svg_footer())
    
    with open(OUTPUT_DIR / "FIG-KID002-H2H-002_indexed_debt_growth_base100.svg", "w") as f:
        f.write("".join(svg))
        
    # Mobile Variant (1080 x 1350)
    m_svg = [svg_header(1080, 1350)]
    m_svg.append(draw_header_mobile(
        "Debt Stock Growth: Indexed (Base = 100)",
        "Removing base effect: Uhuru grew stock 2.7x faster over 4 years"
    ))
    
    mx_min, mx_max = 140, 940
    my_min, my_max = 980, 280
    
    for val in grid_vals:
        y_pos = my_min - (val - 100) / 150 * (my_min - my_max)
        m_svg.append(f'<line x1="{mx_min}" y1="{y_pos}" x2="{mx_max}" y2="{y_pos}" stroke="{SLATE_LIGHT}" stroke-width="1.5" stroke-dasharray="6,6" />')
        m_svg.append(f'<text x="{mx_min - 20}" y="{y_pos + 6}" fill="{SLATE}" font-size="20" font-weight="700" text-anchor="end">{val}</text>')
        
    m_x_coords = [mx_min + i * (mx_max - mx_min) / 4 for i in range(5)]
    for i in range(5):
        cx = m_x_coords[i]
        m_svg.append(f'<line x1="{cx}" y1="{my_min}" x2="{cx}" y2="{my_min + 12}" stroke="{SLATE}" stroke-width="2" />')
        m_svg.append(f'<text x="{cx}" y="{my_min + 42}" fill="{NAVY}" font-size="22" font-weight="800" text-anchor="middle">Year {i}</text>')
        m_svg.append(f'<text x="{cx}" y="{my_min + 70}" fill="{SLATE}" font-size="16" text-anchor="middle">U: {labels_uhuru[i]}</text>')
        m_svg.append(f'<text x="{cx}" y="{my_min + 92}" fill="{SLATE}" font-size="16" text-anchor="middle">R: {labels_ruto[i]}</text>')

    def get_my(val):
        return my_min - (val - 100) / 150 * (my_min - my_max)

    m_pts_u_nom = " ".join([f"{m_x_coords[i]},{get_my(uhuru_nom[i])}" for i in range(5)])
    m_pts_u_real = " ".join([f"{m_x_coords[i]},{get_my(uhuru_real[i])}" for i in range(5)])
    m_pts_r_nom = " ".join([f"{m_x_coords[i]},{get_my(ruto_nom[i])}" for i in range(5)])
    m_pts_r_real = " ".join([f"{m_x_coords[i]},{get_my(ruto_real[i])}" for i in range(5)])

    m_svg.append(f'<polyline points="{m_pts_u_real}" fill="none" stroke="{RED}" stroke-width="4" stroke-dasharray="8,6" />')
    m_svg.append(f'<polyline points="{m_pts_u_nom}" fill="none" stroke="{RED}" stroke-width="6" />')
    m_svg.append(f'<polyline points="{m_pts_r_real}" fill="none" stroke="{BLUE}" stroke-width="4" stroke-dasharray="8,6" />')
    m_svg.append(f'<polyline points="{m_pts_r_nom}" fill="none" stroke="{BLUE}" stroke-width="6" />')

    for i in range(5):
        m_svg.append(f'<circle cx="{m_x_coords[i]}" cy="{get_my(uhuru_nom[i])}" r="9" fill="{RED}" stroke="#FFFFFF" stroke-width="3" />')
        m_svg.append(f'<circle cx="{m_x_coords[i]}" cy="{get_my(ruto_nom[i])}" r="9" fill="{BLUE}" stroke="#FFFFFF" stroke-width="3" />')

    m_svg.append(f'''
  <g transform="translate(60, 1110)">
    <rect x="0" y="0" width="450" height="110" rx="12" fill="{CARD_BG}" stroke="{RED}" stroke-width="2" filter="url(#card-shadow)" />
    <text x="25" y="38" fill="{RED}" font-size="24" font-weight="900">UHURU: +132.7%</text>
    <text x="25" y="70" fill="{NAVY}" font-size="19" font-weight="700">Index: 232.7 (Real: +75.2%)</text>
    <text x="25" y="94" fill="{SLATE}" font-size="16">Debt grew 2.33x in 4 fiscal years</text>
  </g>
  <g transform="translate(570, 1110)">
    <rect x="0" y="0" width="450" height="110" rx="12" fill="{CARD_BG}" stroke="{BLUE}" stroke-width="2" filter="url(#card-shadow)" />
    <text x="25" y="38" fill="{BLUE}" font-size="24" font-weight="900">RUTO WINDOW: +48.5%*</text>
    <text x="25" y="70" fill="{NAVY}" font-size="19" font-weight="700">Index: 148.5 (Real: +19.1%)</text>
    <text x="25" y="94" fill="{SLATE}" font-size="16">Debt grew 1.49x in 4 fiscal years</text>
  </g>
''')

    m_svg.append(draw_footer_mobile(
        "National Treasury; KNBS CPI series",
        "*June 2026 provisional. Base Year 0 = 100."
    ))
    m_svg.append(svg_footer())
    
    with open(OUTPUT_DIR / "FIG-KID002-H2H-002_indexed_debt_growth_base100_mobile.svg", "w") as f:
        f.write("".join(m_svg))
    print("[OK] Generated FIG-KID002-H2H-002 (Landscape & Mobile)")

# =============================================================================
# FIGURE 3: DEBT-TO-GDP TRAJECTORIES
# =============================================================================
def build_fig3():
    uhuru_gdp = [42.1, 48.0, 49.9, 55.5, 57.2]
    ruto_gdp = [68.7, 72.0, 66.9, 67.8, 68.5]
    
    w, h = 1200, 675
    svg = [svg_header(w, h)]
    svg.append(draw_header_landscape(
        "Debt-to-GDP Trajectory: First 4 Fiscal Years",
        "Uhuru's debt outpaced GDP (+15.1 pp); endpoint-to-endpoint, Ruto-era debt/GDP was virtually unchanged (~68.5%)"
    ))
    
    x_min, x_max = 120, 960
    y_min, y_max = 570, 160
    
    def get_y(val):
        return y_min - (val - 35.0) / 40.0 * (y_min - y_max)
    
    for val in [40, 50, 55, 60, 70]:
        y_pos = get_y(val)
        if val == 55:
            svg.append(f'<line x1="{x_min}" y1="{y_pos}" x2="{x_max}" y2="{y_pos}" stroke="{GREEN}" stroke-width="2" stroke-dasharray="6,4" />')
            svg.append(f'<rect x="{x_max + 10}" y="{y_pos - 12}" width="165" height="24" rx="4" fill="#ECFDF5" stroke="{GREEN}" stroke-width="1" />')
            svg.append(f'<text x="{x_max + 18}" y="{y_pos + 4}" fill="{GREEN}" font-size="11" font-weight="800">55% Statutory Anchor</text>')
        else:
            svg.append(f'<line x1="{x_min}" y1="{y_pos}" x2="{x_max}" y2="{y_pos}" stroke="{SLATE_LIGHT}" stroke-width="1" stroke-dasharray="4,4" />')
            svg.append(f'<text x="{x_min - 15}" y="{y_pos + 4}" fill="{SLATE}" font-size="12" font-weight="600" text-anchor="end">{val}%</text>')

    x_coords = [x_min + i * (x_max - x_min) / 4 for i in range(5)]
    labels_uhuru = ["Jun 2013", "Jun 2014", "Jun 2015", "Jun 2016", "Jun 2017"]
    labels_ruto = ["Jun 2022", "Jun 2023", "Jun 2024", "Jun 2025", "Jun 2026*"]
    
    for i in range(5):
        cx = x_coords[i]
        svg.append(f'<line x1="{cx}" y1="{y_min}" x2="{cx}" y2="{y_min + 8}" stroke="{SLATE}" stroke-width="1.5" />')
        svg.append(f'<text x="{cx}" y="{y_min + 24}" fill="{NAVY}" font-size="13" font-weight="700" text-anchor="middle">Year {i}</text>')
        svg.append(f'<text x="{cx}" y="{y_min + 40}" fill="{SLATE}" font-size="10.5" text-anchor="middle">U: {labels_uhuru[i]}</text>')
        svg.append(f'<text x="{cx}" y="{y_min + 54}" fill="{SLATE}" font-size="10.5" text-anchor="middle">R: {labels_ruto[i]}</text>')

    pts_u = " ".join([f"{x_coords[i]},{get_y(uhuru_gdp[i])}" for i in range(5)])
    pts_r = " ".join([f"{x_coords[i]},{get_y(ruto_gdp[i])}" for i in range(5)])
    
    svg.append(f'<polyline points="{pts_u}" fill="none" stroke="{RED}" stroke-width="4.5" />')
    svg.append(f'<polyline points="{pts_r}" fill="none" stroke="{BLUE}" stroke-width="4.5" />')

    for i in range(5):
        yu = get_y(uhuru_gdp[i])
        svg.append(f'<circle cx="{x_coords[i]}" cy="{yu}" r="6.5" fill="{RED}" stroke="#FFFFFF" stroke-width="2.5" />')
        svg.append(f'<text x="{x_coords[i]}" y="{yu - 12}" fill="{RED}" font-size="12" font-weight="800" text-anchor="middle">{uhuru_gdp[i]}%</text>')

        yr = get_y(ruto_gdp[i])
        svg.append(f'<circle cx="{x_coords[i]}" cy="{yr}" r="6.5" fill="{BLUE}" stroke="#FFFFFF" stroke-width="2.5" />')
        svg.append(f'<text x="{x_coords[i]}" y="{yr - 12}" fill="{BLUE}" font-size="12" font-weight="800" text-anchor="middle">{ruto_gdp[i]}%</text>')

    svg.append(f'''
  <!-- Uhuru End Label -->
  <g transform="translate({x_coords[4] + 15}, {get_y(uhuru_gdp[4]) - 20})">
    <rect x="0" y="0" width="165" height="42" rx="6" fill="#FFFFFF" stroke="{RED}" stroke-width="1.5" filter="url(#subtle-shadow)" />
    <text x="12" y="18" fill="{RED}" font-size="12.5" font-weight="900">Uhuru: 57.2%</text>
    <text x="12" y="34" fill="{RED}" font-size="10.5" font-weight="700">+15.1 pp increase</text>
  </g>
  
  <!-- Ruto End Label -->
  <g transform="translate({x_coords[4] + 15}, {get_y(ruto_gdp[4]) - 20})">
    <rect x="0" y="0" width="165" height="42" rx="6" fill="#FFFFFF" stroke="{BLUE}" stroke-width="1.5" filter="url(#subtle-shadow)" />
    <text x="12" y="18" fill="{BLUE}" font-size="12.5" font-weight="900">Ruto Window: ~68.5%*</text>
    <text x="12" y="34" fill="{GREEN}" font-size="10.5" font-weight="700">-0.2 pp (endpoint flat)</text>
  </g>
''')

    svg.append(draw_footer_landscape(
        "National Treasury Annual Debt Reports; June 2026 Monthly Debt Bulletin",
        "*June 2026 debt-to-GDP is provisional."
    ))
    svg.append(svg_footer())
    
    with open(OUTPUT_DIR / "FIG-KID002-H2H-003_debt_to_gdp_trajectories.svg", "w") as f:
        f.write("".join(svg))
        
    # Mobile Variant (1080 x 1350)
    m_svg = [svg_header(1080, 1350)]
    m_svg.append(draw_header_mobile(
        "Debt-to-GDP: First 4 Fiscal Years",
        "Uhuru outpaced GDP (+15.1 pp); endpoint-to-endpoint, Ruto ratio held virtually flat"
    ))
    
    mx_min, mx_max = 140, 940
    my_min, my_max = 980, 280
    
    def get_my(val):
        return my_min - (val - 35.0) / 40.0 * (my_min - my_max)
        
    for val in [40, 50, 55, 60, 70]:
        y_pos = get_my(val)
        if val == 55:
            m_svg.append(f'<line x1="{mx_min}" y1="{y_pos}" x2="{mx_max}" y2="{y_pos}" stroke="{GREEN}" stroke-width="3" stroke-dasharray="8,6" />')
            m_svg.append(f'<text x="{mx_max}" y="{y_pos - 12}" fill="{GREEN}" font-size="18" font-weight="900" text-anchor="end">55% Statutory Debt Anchor</text>')
        else:
            m_svg.append(f'<line x1="{mx_min}" y1="{y_pos}" x2="{mx_max}" y2="{y_pos}" stroke="{SLATE_LIGHT}" stroke-width="1.5" stroke-dasharray="6,6" />')
            m_svg.append(f'<text x="{mx_min - 20}" y="{y_pos + 6}" fill="{SLATE}" font-size="20" font-weight="700" text-anchor="end">{val}%</text>')

    m_x_coords = [mx_min + i * (mx_max - mx_min) / 4 for i in range(5)]
    for i in range(5):
        cx = m_x_coords[i]
        m_svg.append(f'<line x1="{cx}" y1="{my_min}" x2="{cx}" y2="{my_min + 12}" stroke="{SLATE}" stroke-width="2" />')
        m_svg.append(f'<text x="{cx}" y="{my_min + 42}" fill="{NAVY}" font-size="22" font-weight="800" text-anchor="middle">Year {i}</text>')
        m_svg.append(f'<text x="{cx}" y="{my_min + 70}" fill="{SLATE}" font-size="16" text-anchor="middle">U: {labels_uhuru[i]}</text>')
        m_svg.append(f'<text x="{cx}" y="{my_min + 92}" fill="{SLATE}" font-size="16" text-anchor="middle">R: {labels_ruto[i]}</text>')

    m_pts_u = " ".join([f"{m_x_coords[i]},{get_my(uhuru_gdp[i])}" for i in range(5)])
    m_pts_r = " ".join([f"{m_x_coords[i]},{get_my(ruto_gdp[i])}" for i in range(5)])
    
    m_svg.append(f'<polyline points="{m_pts_u}" fill="none" stroke="{RED}" stroke-width="6.5" />')
    m_svg.append(f'<polyline points="{m_pts_r}" fill="none" stroke="{BLUE}" stroke-width="6.5" />')

    for i in range(5):
        yu = get_my(uhuru_gdp[i])
        m_svg.append(f'<circle cx="{m_x_coords[i]}" cy="{yu}" r="10" fill="{RED}" stroke="#FFFFFF" stroke-width="3" />')
        m_svg.append(f'<text x="{m_x_coords[i]}" y="{yu - 18}" fill="{RED}" font-size="19" font-weight="900" text-anchor="middle">{uhuru_gdp[i]}%</text>')

        yr = get_my(ruto_gdp[i])
        m_svg.append(f'<circle cx="{m_x_coords[i]}" cy="{yr}" r="10" fill="{BLUE}" stroke="#FFFFFF" stroke-width="3" />')
        m_svg.append(f'<text x="{m_x_coords[i]}" y="{yr - 18}" fill="{BLUE}" font-size="19" font-weight="900" text-anchor="middle">{ruto_gdp[i]}%</text>')

    m_svg.append(f'''
  <g transform="translate(60, 1110)">
    <rect x="0" y="0" width="450" height="110" rx="12" fill="{CARD_BG}" stroke="{RED}" stroke-width="2" filter="url(#card-shadow)" />
    <text x="25" y="38" fill="{RED}" font-size="24" font-weight="900">UHURU: 42.1% → 57.2%</text>
    <text x="25" y="70" fill="{RED}" font-size="19" font-weight="700">+15.1 pp Debt-to-GDP surge</text>
    <text x="25" y="94" fill="{SLATE}" font-size="16">Debt accumulated faster than GDP</text>
  </g>
  <g transform="translate(570, 1110)">
    <rect x="0" y="0" width="450" height="110" rx="12" fill="{CARD_BG}" stroke="{BLUE}" stroke-width="2" filter="url(#card-shadow)" />
    <text x="25" y="38" fill="{BLUE}" font-size="24" font-weight="900">RUTO: 68.7% → ~68.5%*</text>
    <text x="25" y="70" fill="{GREEN}" font-size="19" font-weight="700">-0.2 pp (Endpoint flat)</text>
    <text x="25" y="94" fill="{SLATE}" font-size="16">Pathway: 68.7% → 72.0% → 66.9% → 67.8% → 68.5%</text>
  </g>
''')

    m_svg.append(draw_footer_mobile(
        "National Treasury; June 2026 Monthly Bulletin",
        "*June 2026 provisional. Anchor: 55% PV of GDP."
    ))
    m_svg.append(svg_footer())
    
    with open(OUTPUT_DIR / "FIG-KID002-H2H-003_debt_to_gdp_trajectories_mobile.svg", "w") as f:
        f.write("".join(m_svg))
    print("[OK] Generated FIG-KID002-H2H-003 (Landscape & Mobile)")

# =============================================================================
# FIGURE 4: COMPOSITION OF NET DEBT STOCK ADDED
# =============================================================================
def build_fig4():
    w, h = 1200, 675
    svg = [svg_header(w, h)]
    svg.append(draw_header_landscape(
        "Where Did the Net Debt Stock Increase Come From?",
        "Uhuru window was external-debt-led (57.7%); Ruto window pivoted heavily to domestic debt (68.3%)"
    ))
    
    bar_x = 240
    bar_w = 840
    
    u_y = 190
    u_dom_w = bar_w * 0.4226
    u_ext_w = bar_w * 0.5774
    
    svg.append(f'''
  <!-- Uhuru Section -->
  <text x="60" y="{u_y + 28}" fill="{NAVY}" font-size="18" font-weight="900">UHURU WINDOW</text>
  <text x="60" y="{u_y + 50}" fill="{SLATE}" font-size="13" font-weight="600">+KSh 2.51T Stock Added</text>
  
  <rect x="{bar_x}" y="{u_y}" width="{u_dom_w}" height="70" rx="8" fill="{BLUE}" />
  <rect x="{bar_x + u_dom_w}" y="{u_y}" width="{u_ext_w}" height="70" rx="8" fill="{GOLD}" />
  <rect x="{bar_x + u_dom_w - 4}" y="{u_y}" width="8" height="70" fill="{GOLD}" />

  <text x="{bar_x + u_dom_w / 2}" y="{u_y + 36}" fill="#FFFFFF" font-size="15" font-weight="900" text-anchor="middle">DOMESTIC: 42.3%</text>
  <text x="{bar_x + u_dom_w / 2}" y="{u_y + 54}" fill="{BLUE_BG}" font-size="12" font-weight="600" text-anchor="middle">+KSh 1.06 Trillion</text>

  <text x="{bar_x + u_dom_w + u_ext_w / 2}" y="{u_y + 36}" fill="#FFFFFF" font-size="15" font-weight="900" text-anchor="middle">EXTERNAL: 57.7%</text>
  <text x="{bar_x + u_dom_w + u_ext_w / 2}" y="{u_y + 54}" fill="#FEF3C7" font-size="12" font-weight="600" text-anchor="middle">+KSh 1.45 Trillion (Eurobonds &amp; SGR)</text>
''')

    r_y = 330
    r_dom_w = bar_w * 0.6827
    r_ext_w = bar_w * 0.3173
    
    svg.append(f'''
  <!-- Ruto Section -->
  <text x="60" y="{r_y + 28}" fill="{NAVY}" font-size="18" font-weight="900">RUTO WINDOW</text>
  <text x="60" y="{r_y + 50}" fill="{SLATE}" font-size="13" font-weight="600">+KSh 4.25T Stock Added*</text>
  
  <rect x="{bar_x}" y="{r_y}" width="{r_dom_w}" height="70" rx="8" fill="{BLUE}" />
  <rect x="{bar_x + r_dom_w}" y="{r_y}" width="{r_ext_w}" height="70" rx="8" fill="{GOLD}" />
  <rect x="{bar_x + r_dom_w - 4}" y="{r_y}" width="8" height="70" fill="{GOLD}" />

  <text x="{bar_x + r_dom_w / 2}" y="{r_y + 36}" fill="#FFFFFF" font-size="15" font-weight="900" text-anchor="middle">DOMESTIC: 68.3%</text>
  <text x="{bar_x + r_dom_w / 2}" y="{r_y + 54}" fill="{BLUE_BG}" font-size="12" font-weight="600" text-anchor="middle">+KSh 2.90 Trillion (Local T-Bonds)</text>

  <text x="{bar_x + r_dom_w + r_ext_w / 2}" y="{r_y + 36}" fill="#FFFFFF" font-size="15" font-weight="900" text-anchor="middle">EXTERNAL: 31.7%</text>
  <text x="{bar_x + r_dom_w + r_ext_w / 2}" y="{r_y + 54}" fill="#FEF3C7" font-size="12" font-weight="600" text-anchor="middle">+KSh 1.35 Trillion*</text>
''')

    svg.append(f'''
  <g transform="translate(60, 460)">
    <rect x="0" y="0" width="1080" height="110" rx="12" fill="{CARD_BG}" stroke="{SLATE_LIGHT}" stroke-width="1.5" filter="url(#subtle-shadow)" />
    <text x="30" y="38" fill="{NAVY}" font-size="15" font-weight="800">WHY THIS STRUCTURAL SHIFT MATTERS FOR BUDGET SERVICING</text>
    <text x="30" y="65" fill="{SLATE_DARK}" font-size="13">
      • <tspan font-weight="700">Uhuru Window:</tspan> Kenya accessed international Eurobond markets and Chinese bilateral loans, shifting debt outward.
    </text>
    <text x="30" y="90" fill="{SLATE_DARK}" font-size="13">
      • <tspan font-weight="700">Ruto Window:</tspan> Pivoted to domestic debt. At June 2025, Treasury reported a weighted-average interest rate of 13.0% on domestic debt vs 3.9% on external debt.
    </text>
  </g>
''')

    svg.append(draw_footer_landscape(
        "National Treasury Annual Public Debt Reports (2016/17, 2024/25); June 2026 Monthly Bulletin",
        "Calculations reflect net change in outstanding debt stock by category (incorporating FX valuation and repayments)."
    ))
    svg.append(svg_footer())
    
    with open(OUTPUT_DIR / "FIG-KID002-H2H-004_composition_of_debt_added.svg", "w") as f:
        f.write("".join(svg))
        
    # Mobile Variant (1080 x 1350)
    m_svg = [svg_header(1080, 1350)]
    m_svg.append(draw_header_mobile(
        "Composition of Net Debt Added: Uhuru vs Ruto",
        "Uhuru window was external-led (57.7%); Ruto window pivoted to domestic debt (68.3%)"
    ))
    
    m_svg.append(f'''
  <!-- Uhuru Section Mobile -->
  <g transform="translate(50, 200)">
    <rect x="0" y="0" width="980" height="420" rx="16" fill="{CARD_BG}" stroke="{SLATE_LIGHT}" stroke-width="2" filter="url(#card-shadow)" />
    <text x="40" y="55" fill="{NAVY}" font-size="28" font-weight="900">UHURU: +KSh 2.51 Trillion Net Stock Added</text>
    <text x="40" y="90" fill="{SLATE}" font-size="18">Jun 2013 → Jun 2017 (External-Heavy Expansion)</text>
    
    <!-- 100% Bar -->
    <rect x="40" y="120" width="380" height="80" rx="10" fill="{BLUE}" />
    <rect x="420" y="120" width="520" height="80" rx="10" fill="{GOLD}" />
    <rect x="415" y="120" width="10" height="80" fill="{GOLD}" />
    
    <!-- Stat 1: Domestic -->
    <rect x="40" y="230" width="430" height="140" rx="12" fill="{BLUE_BG}" />
    <text x="65" y="270" fill="{BLUE}" font-size="22" font-weight="900">DOMESTIC: 42.3%</text>
    <text x="65" y="308" fill="{NAVY}" font-size="26" font-weight="800">+KSh 1.06 Trillion</text>
    <text x="65" y="340" fill="{SLATE}" font-size="16">Treasury bills and bonds</text>

    <!-- Stat 2: External -->
    <rect x="510" y="230" width="430" height="140" rx="12" fill="{AMBER_BG}" />
    <text x="535" y="270" fill="{GOLD}" font-size="22" font-weight="900">EXTERNAL: 57.7%</text>
    <text x="535" y="308" fill="{NAVY}" font-size="26" font-weight="800">+KSh 1.45 Trillion</text>
    <text x="535" y="340" fill="{SLATE_DARK}" font-size="16">Eurobonds &amp; bilateral loans</text>
  </g>

  <!-- Ruto Section Mobile -->
  <g transform="translate(50, 660)">
    <rect x="0" y="0" width="980" height="420" rx="16" fill="{CARD_BG}" stroke="{SLATE_LIGHT}" stroke-width="2" filter="url(#card-shadow)" />
    <text x="40" y="55" fill="{NAVY}" font-size="28" font-weight="900">RUTO: +KSh 4.25 Trillion Net Stock Added*</text>
    <text x="40" y="90" fill="{SLATE}" font-size="18">Jun 2022 → Jun 2026* (Domestic-Heavy Expansion)</text>
    
    <!-- 100% Bar -->
    <rect x="40" y="120" width="615" height="80" rx="10" fill="{BLUE}" />
    <rect x="655" y="120" width="285" height="80" rx="10" fill="{GOLD}" />
    <rect x="650" y="120" width="10" height="80" fill="{GOLD}" />
    
    <!-- Stat 1: Domestic -->
    <rect x="40" y="230" width="430" height="140" rx="12" fill="{BLUE_BG}" />
    <text x="65" y="270" fill="{BLUE}" font-size="22" font-weight="900">DOMESTIC: 68.3%</text>
    <text x="65" y="308" fill="{NAVY}" font-size="26" font-weight="800">+KSh 2.90 Trillion</text>
    <text x="65" y="340" fill="{SLATE}" font-size="16">Local Treasury bonds &amp; bills</text>

    <!-- Stat 2: External -->
    <rect x="510" y="230" width="430" height="140" rx="12" fill="{AMBER_BG}" />
    <text x="535" y="270" fill="{GOLD}" font-size="22" font-weight="900">EXTERNAL: 31.7%</text>
    <text x="535" y="308" fill="{NAVY}" font-size="26" font-weight="800">+KSh 1.35 Trillion*</text>
    <text x="535" y="340" fill="{SLATE_DARK}" font-size="16">Multilateral funding &amp; commercial</text>
  </g>

  <!-- Explainer Mobile -->
  <g transform="translate(50, 1115)">
    <rect x="0" y="0" width="980" height="110" rx="12" fill="#F1F5F9" stroke="{SLATE_LIGHT}" stroke-width="1.5" />
    <text x="35" y="40" fill="{NAVY}" font-size="18" font-weight="900">THE COST IMPLICATION</text>
    <text x="35" y="72" fill="{SLATE_DARK}" font-size="16.5">At June 2025, Treasury reported a weighted-average interest rate of 13.0% on domestic debt</text>
    <text x="35" y="96" fill="{SLATE_DARK}" font-size="16.5">versus 3.9% on external debt, explaining the sharp rise in budget carrying costs.</text>
  </g>
''')

    m_svg.append(draw_footer_mobile(
        "National Treasury Annual Reports; June 2026 Bulletin",
        "*June 2026 figures are provisional."
    ))
    m_svg.append(svg_footer())
    
    with open(OUTPUT_DIR / "FIG-KID002-H2H-004_composition_of_debt_added_mobile.svg", "w") as f:
        f.write("".join(m_svg))
    print("[OK] Generated FIG-KID002-H2H-004 (Landscape & Mobile)")

# =============================================================================
# FIGURE 5: INTEREST BURDEN (% OF ORDINARY REVENUE)
# =============================================================================
def build_fig5():
    uhuru_interest = [15.6, 14.7, 16.8, 18.6, 20.8]
    uhuru_labels = ["FY12/13", "FY13/14", "FY14/15", "FY15/16", "FY16/17"]
    
    ruto_interest = [30.1, 33.8, 36.9, 40.8, 39.8]
    ruto_labels = ["FY21/22", "FY22/23", "FY23/24", "FY24/25", "FY25/26*"]
    
    w, h = 1200, 675
    svg = [svg_header(w, h)]
    svg.append(draw_header_landscape(
        "The Revenue Squeeze: Interest Payments as % of Ordinary Revenue",
        "At Uhuru's endpoint, interest took 20.8% of ordinary revenue. Under Ruto, interest consumes over 40%."
    ))
    
    def draw_panel(ax_x_min, ax_x_max, data, labels, admin_name, admin_color, is_ruto=False):
        p_svg = []
        ay_min, ay_max = 550, 180
        
        def get_ay(val):
            return ay_min - (val / 50.0) * (ay_min - ay_max)
            
        p_svg.append(f'<text x="{ax_x_min}" y="160" fill="{admin_color}" font-size="16" font-weight="900">{admin_name.upper()}</text>')
        
        for g_val in [10, 20, 30, 40, 50]:
            gy = get_ay(g_val)
            if g_val == 30:
                p_svg.append(f'<line x1="{ax_x_min}" y1="{gy}" x2="{ax_x_max}" y2="{gy}" stroke="{RED}" stroke-width="1.5" stroke-dasharray="4,4" />')
                if not is_ruto:
                    p_svg.append(f'<text x="{ax_x_max - 5}" y="{gy - 6}" fill="{RED}" font-size="10.5" font-weight="700" text-anchor="end">30% Fiscal Stress Line</text>')
            else:
                p_svg.append(f'<line x1="{ax_x_min}" y1="{gy}" x2="{ax_x_max}" y2="{gy}" stroke="{SLATE_LIGHT}" stroke-width="1" stroke-dasharray="3,3" />')
            p_svg.append(f'<text x="{ax_x_min - 10}" y="{gy + 4}" fill="{SLATE}" font-size="11" text-anchor="end">{g_val}%</text>')

        n_bars = len(data)
        bar_step = (ax_x_max - ax_x_min) / n_bars
        bar_w = bar_step * 0.65
        
        for idx in range(n_bars):
            bx = ax_x_min + idx * bar_step + (bar_step - bar_w) / 2
            val = data[idx]
            by = get_ay(val)
            bh = ay_min - by
            
            fill_col = admin_color if idx == (n_bars - 1) or (is_ruto and idx == 3) else (SLATE_DARK if not is_ruto else BLUE)
            opacity = "1.0" if (idx == (n_bars - 1) or (is_ruto and idx == 3)) else "0.7"
            
            p_svg.append(f'<rect x="{bx}" y="{by}" width="{bar_w}" height="{bh}" rx="5" fill="{fill_col}" fill-opacity="{opacity}" />')
            p_svg.append(f'<text x="{bx + bar_w / 2}" y="{by - 8}" fill="{fill_col}" font-size="12" font-weight="800" text-anchor="middle">{val}%</text>')
            p_svg.append(f'<text x="{bx + bar_w / 2}" y="{ay_min + 20}" fill="{SLATE}" font-size="11" font-weight="600" text-anchor="middle">{labels[idx]}</text>')

        return "".join(p_svg)

    svg.append(draw_panel(100, 550, uhuru_interest, uhuru_labels, "Uhuru Window (FY13 → FY17)", RED, is_ruto=False))
    svg.append(draw_panel(670, 1120, ruto_interest, ruto_labels, "Ruto Window (FY22 → FY26*)", RED, is_ruto=True))
    
    svg.append(f'<line x1="610" y1="160" x2="610" y2="570" stroke="{SLATE_LIGHT}" stroke-width="1.5" />')

    svg.append(draw_footer_landscape(
        "National Treasury Annual Debt Reports (2016/17, 2024/25); FY2025/26 Treasury component projections",
        "*FY25/26 (39.8%) is Kenya in Data calculation from Treasury component projections (KSh 1.129T / KSh 2.835T)."
    ))
    svg.append(svg_footer())
    
    with open(OUTPUT_DIR / "FIG-KID002-H2H-005_interest_burden_revenue_absorption.svg", "w") as f:
        f.write("".join(svg))

    # Mobile Variant (1080 x 1350)
    m_svg = [svg_header(1080, 1350)]
    m_svg.append(draw_header_mobile(
        "The Revenue Squeeze: Interest / Revenue",
        "Under Uhuru, interest took 20.8% of ordinary revenue. Under Ruto, it consumes 40.8%."
    ))
    
    def draw_mobile_panel(top_y, data, labels, title, highlight_col, is_ruto=False):
        pm_svg = []
        pm_svg.append(f'''
  <g transform="translate(50, {top_y})">
    <rect x="0" y="0" width="980" height="420" rx="16" fill="{CARD_BG}" stroke="{SLATE_LIGHT}" stroke-width="2" filter="url(#card-shadow)" />
    <text x="35" y="45" fill="{NAVY}" font-size="24" font-weight="900">{title}</text>
''')
        pay_min, pay_max = 340, 80
        def get_pay(val):
            return pay_min - (val / 50.0) * (pay_min - pay_max)

        stress_y = get_pay(30)
        pm_svg.append(f'<line x1="90" y1="{stress_y}" x2="930" y2="{stress_y}" stroke="{RED}" stroke-width="2" stroke-dasharray="6,4" />')
        pm_svg.append(f'<text x="930" y="{stress_y - 8}" fill="{RED}" font-size="14" font-weight="700" text-anchor="end">30% Stress Line</text>')

        for g_val in [10, 20, 30, 40, 50]:
            gy = get_pay(g_val)
            pm_svg.append(f'<line x1="90" y1="{gy}" x2="930" y2="{gy}" stroke="{SLATE_LIGHT}" stroke-width="1.2" stroke-dasharray="4,4" />')
            pm_svg.append(f'<text x="75" y="{gy + 5}" fill="{SLATE}" font-size="15" text-anchor="end">{g_val}%</text>')

        n_bars = len(data)
        bar_step = (930 - 100) / n_bars
        bar_w = bar_step * 0.65
        
        for idx in range(n_bars):
            bx = 100 + idx * bar_step + (bar_step - bar_w) / 2
            val = data[idx]
            by = get_pay(val)
            bh = pay_min - by
            
            f_col = highlight_col if (idx == (n_bars - 1) or (is_ruto and idx == 3)) else (SLATE_DARK if not is_ruto else BLUE)
            pm_svg.append(f'<rect x="{bx}" y="{by}" width="{bar_w}" height="{bh}" rx="8" fill="{f_col}" />')
            pm_svg.append(f'<text x="{bx + bar_w / 2}" y="{by - 10}" fill="{f_col}" font-size="17" font-weight="900" text-anchor="middle">{val}%</text>')
            pm_svg.append(f'<text x="{bx + bar_w / 2}" y="{pay_min + 30}" fill="{SLATE}" font-size="16" font-weight="700" text-anchor="middle">{labels[idx]}</text>')

        pm_svg.append('</g>\n')
        return "".join(pm_svg)

    m_svg.append(draw_mobile_panel(200, uhuru_interest, uhuru_labels, "UHURU WINDOW: Interest / Ordinary Revenue", RED, is_ruto=False))
    m_svg.append(draw_mobile_panel(650, ruto_interest, ruto_labels, "RUTO WINDOW: Interest / Ordinary Revenue", RED, is_ruto=True))
    
    m_svg.append(f'''
  <g transform="translate(50, 1100)">
    <rect x="0" y="0" width="980" height="120" rx="14" fill="{RED_BG}" stroke="{RED}" stroke-width="1.5" />
    <text x="35" y="42" fill="{RED}" font-size="20" font-weight="900">THE REVENUE SQUEEZE TODAY</text>
    <text x="35" y="75" fill="{NAVY}" font-size="17" font-weight="700">More than KSh 4 out of every KSh 10 of ordinary revenue now goes strictly to interest payments,</text>
    <text x="35" y="100" fill="{SLATE_DARK}" font-size="16">severely crowding out development expenditure and county equitable revenue shares.</text>
  </g>
''')

    m_svg.append(draw_footer_mobile(
        "National Treasury Annual Debt Reports; FY25/26 Projections",
        "*FY25/26 is Kenya in Data calculation from Treasury component projections."
    ))
    m_svg.append(svg_footer())
    
    with open(OUTPUT_DIR / "FIG-KID002-H2H-005_interest_burden_revenue_absorption_mobile.svg", "w") as f:
        f.write("".join(m_svg))
    print("[OK] Generated FIG-KID002-H2H-005 (Landscape & Mobile)")

if __name__ == "__main__":
    print("Regenerating PRJ-001 / KID-002 Head-to-Head Visual Package...")
    build_fig1()
    build_fig2()
    build_fig3()
    build_fig4()
    build_fig5()
    print("All 5 figures updated successfully in Derivatives/Charts/")
