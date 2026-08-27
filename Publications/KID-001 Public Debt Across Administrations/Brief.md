---
post_id: KID-001
title: "Kenya's Public Debt Across Presidencies: Nominal vs Real"
target_date: 2026-08-30
status: drafting
primary_indicator: IND-PF-001
platforms: [X/Twitter, LinkedIn, Substack]
tags: [publications, public-debt, fiscal-policy, kid-001]
---

# Publication Brief: KID-001 — Kenya's Public Debt Across Presidencies

## 1. Core Question & Premise
Public discourse in Kenya routinely compares debt across presidential administrations in raw nominal shillings (*"Kibaki left debt at KSh 1.8T, Uhuru raised it to KSh 8.6T, Ruto reached KSh 11T..."*). 

This comparison is misleading because a shilling in 2003 does not buy what a shilling buys in 2026, nor does nominal debt account for economic expansion (GDP), population growth, or currency depreciation.

## 2. Intended Visual Output (3-Panel Graphic)
- **Panel 1 (Nominal Debt):** Total public debt stock in nominal KSh Trillion (2002–2026) with shaded presidential administrations (Mwai Kibaki, Uhuru Kenyatta, William Ruto).
- **Panel 2 (Inflation-Adjusted Real Debt):** Debt deflated using the GDP deflator (in constant 2024 KSh Trillion).
- **Panel 3 (Debt as % of GDP):** Macroeconomic debt burden relative to economic output over the same 24-year timeline.

## 3. Key Narrative Punchlines
> *"Nominal debt tells you how many shillings the state owes. Real debt tells you what that means over time. Debt-to-GDP tells you how heavy the burden is relative to the national economy."*

## 4. Work Checklist
- [ ] Pull historical debt bulletin series from National Treasury (2002–2026).
- [ ] Pull GDP deflator and nominal GDP series from KNBS Economic Surveys.
- [ ] Calculate real constant price debt series in `Code/pipelines/compute_kid001_debt.py`.
- [ ] Generate visual asset via Python Matplotlib chart generator into `Assets/`.
- [ ] Finalize platform caption in `Caption.md` and complete verification checklist.
