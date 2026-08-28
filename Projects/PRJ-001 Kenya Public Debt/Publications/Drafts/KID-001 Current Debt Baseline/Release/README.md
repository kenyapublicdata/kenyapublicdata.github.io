# QA and release gate

Current status: **Draft — data and copy corrected; visual and deployment gates remain open.**

Release approval applies to the canonical article at [`KID-001 Current Debt Baseline.md`](../KID-001%20Current%20Debt%20Baseline.md) and every derivative generated from it.

Required checks before publication:

- Data reconciled to the cited official tables.
- Actual, provisional, revised and projected observations labelled correctly.
- CSV, workbook, charts, article and PDFs agree numerically.
- No clipped, overlapping or unreadable text.
- Fonts, colors, spacing and dimensions conform to the visual publishing system.
- SVG, PDF and PNG outputs inspected at their intended sizes.
- Color contrast and color-blind distinguishability checked.
- Alt text and downloadable data supplied.
- Local and public links tested.
- Release manifest and checksums generated.

See [`release_checklist.md`](release_checklist.md) for completed checks and remaining blockers. Do not describe this package as release-ready until every pending item is closed.
