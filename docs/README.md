# Kenya in Data — Public Website (`docs/`)

This directory contains the public-facing static website for **Kenya in Data**, configured for instant deployment via **GitHub Pages**.

## Structure

```text
docs/
├── index.html          # Public single-page civic data desk and KID-001 publication
├── .nojekyll           # Bypasses Jekyll processing so all assets/folders are served
├── README.md           # Documentation for this public build folder
└── assets/
    ├── data/           # Verified public datasets (.csv, .xlsx)
    │   ├── KID001_Kenya_Public_Debt_2002_2026.csv
    │   └── KID001_Kenya_Public_Debt_2002_2026.xlsx
    └── figures/        # High-DPI charts (.svg, 300-DPI .png)
        ├── FIG-DEBT-001_nominal_vs_real_public_debt.svg
        ├── FIG-DEBT-002_public_debt_to_gdp.svg
        ├── FIG-DEBT-003_domestic_vs_external_composition.svg
        └── FIG-DEBT-004_debt_service_to_tax_revenue.svg
```

## Local Preview

From the root project directory:
```bash
python3 -m http.server 8000 --directory docs
```
Then open `http://localhost:8000` in your web browser.

## Deployment on GitHub Pages

1. Push this repository to GitHub.
2. In GitHub, go to **Settings** → **Pages**.
3. Under **Build and deployment > Source**, select **Deploy from a branch**.
4. Choose Branch: `main` and Folder: `/docs`.
5. Click **Save**.
