# QA & Release Verification Checklist — KID-001 Current Debt Baseline

**Publication ID:** KID-001  
**Package Title:** Kenya's Public Debt: The Current Stock, Composition and Servicing Burden  
**Review Date:** 2026-08-28  
**QA Lead:** Kenya in Data Integrity Gate  
**Status:** ✅ **Passed Pre-Release Verification**

---

## 1. Provenance & Source Audit

| Checkpoint | Requirement | Result | Verified Source Reference |
|:---|:---|:---:|:---|
| **Stock Provenance** | June 2025 stock matches official outturn | ✅ PASS | TNT ADMR FY24/25, Table 3, p. 28 (KSh 11,814.50 B) |
| **Monthly Update** | May 2026 CBK stock matches latest complete table | ✅ PASS | CBK MEI June 2026, Table 7.1, p. 22 (KSh 12,896.40 B) |
| **No Hybrid Observations** | June 2026 domestic debt not mixed with May external debt | ✅ PASS | Explicitly noted; total stock reported through May 2026 |
| **Debt Service Numbers** | Principal, interest, and revenue match official table | ✅ PASS | TNT ADMR FY24/25, Table 4, p. 30 (Service: KSh 1,722.10 B) |
| **Domestic Interest** | Domestic interest matches debt management breakdown | ✅ PASS | TNT ADMR FY24/25, Table 4 & pp. 43–44 (KSh 776.30 B) |
| **Statutory Rule** | Section 50(2A) PFMA threshold cited accurately | ✅ PASS | 55% Present Value of GDP (Cap. 412C) |
| **DSA Assessment** | Joint IMF/WB rating dated and cited accurately | ✅ PASS | October 2024 (IMF Country Report 24/316): High Risk / Sustainable |

---

## 2. Arithmetic & Cross-Format Consistency

| Checkpoint | Requirement | Result | Cross-Check Details |
|:---|:---|:---:|:---|
| **CSV vs Article** | All values in `article.md` match `KID001_current_debt_baseline.csv` | ✅ PASS | 100% numerical agreement across all 28 rows |
| **Social vs Article** | Social copy numbers match article and CSV | ✅ PASS | 100% agreement on stock, ratios, and percentages |
| **Percentages Sum** | Instrument components sum to 100% within rounding tolerance | ✅ PASS | Domestic (53.5%) + External (46.5%) = 100.0% |
| **Interest vs Principal** | Total service equals interest plus principal | ✅ PASS | KSh 987.5B (interest) + KSh 734.6B (principal) = KSh 1,722.1B |
| **Ordinary Revenue Ratio** | Debt service / Ordinary revenue calculation verified | ✅ PASS | 1,722.1 / 2,420.2 = 71.155% → 71.2% |
| **Domestic Interest Ratio**| Domestic interest / Ordinary revenue verified | ✅ PASS | 776.3 / 2,420.2 = 32.075% → 32.1% |

---

## 3. Epistemic Separation & Neutrality Rules

| Checkpoint | Requirement | Result | Notes |
|:---|:---|:---:|:---|
| **Tiers 1–3 Enforced** | Content limited strictly to Facts, Calculations, and Economic Mechanisms | ✅ PASS | Tier 4 moral/political assertions completely avoided |
| **Denominator Discipline** | Nominal figures paired with GDP and revenue ratios | ✅ PASS | GDP (67.8%) and revenue (71.2%) ratios presented |
| **Definition Clarity** | Gross PPG debt defined explicitly | ✅ PASS | Gross vs. net debt explained in Section 1 |
| **Excluded Content** | Historical charts & political comparisons excluded as requested | ✅ PASS | Strictly restricted to current baseline scope |

---

## 4. Release Approval

- **Data Package:** Verified (`01 Data/KID001_current_debt_baseline.csv`)
- **Editorial Text:** Verified (`05 Article/article.md`)
- **Distribution Copy:** Verified (`04 Social/social_copy.md`)
- **Citations Ledger:** Verified (`07 Sources/citation_ledger.md`)
- **Overall Status:** **READY FOR PUBLICATION SIGN-OFF**
