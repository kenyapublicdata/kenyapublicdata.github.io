# Magazine PDF and presentation plan

Canonical source: [`KID-001 Current Debt Baseline.md`](../../KID-001%20Current%20Debt%20Baseline.md).

Status: **Parked until the quick post is published.**

## Engine decision: Typst

Use **Typst** as the primary document engine for Kenya in Data PDF reports and briefs.

Typst is the better fit for this publication because it provides programmable page layout, fast design iteration, native SVG and PDF placement, bibliographies, document metadata and modern PDF accessibility options without the complexity of a large LaTeX toolchain.

Use LaTeX as a secondary compatibility path when:

- a journal or external publisher supplies a mandatory LaTeX class;
- a collaborator requires a TeX source package;
- the publication contains extensive mathematical notation or relies on a specialist TeX package.

LaTeX is capable of equally high or higher typesetting quality. The choice is based on workflow, maintainability and design iteration—not on a claim that LaTeX cannot produce magazine-quality work.

Official references:

- [Typst layout reference](https://typst.app/docs/reference/layout/)
- [Typst PDF export and accessibility](https://typst.app/docs/reference/pdf/)
- [Typst bibliography support](https://typst.app/docs/reference/model/bibliography/)
- [Typst SVG export](https://typst.app/docs/reference/svg/)
- [LaTeX Project documentation](https://www.latex-project.org/help/documentation/)

## Planned output

Create one A4 portrait report, initially **8–12 pages**:

1. Cover and publication metadata
2. Key findings spread
3. Reporting scope and dates
4. Current debt stock and composition
5. Detailed June 2025 composition
6. Debt service and interest rates
7. Domestic interest and debt holders
8. Statutory comparison and limitations
9. Glossary
10. Sources, methodology and project-page link

The final page count should follow the content rather than forcing every section onto a separate page.

## Magazine-quality design specification

- Build a custom Kenya in Data template; do not begin from a generic academic-paper layout.
- Use Inter or Plus Jakarta Sans for headings and body text, with clear weight and size contrast.
- Use an A4 grid with consistent margins, baseline spacing and modular chart blocks.
- Allow selected figures to occupy a full page or full-width spread.
- Place SVG charts directly to preserve vector quality.
- Use the Kenya in Data navy, ivory, blue, ochre, violet and slate tokens.
- Use finding-led page titles rather than generic labels.
- Keep paragraphs moderately narrow for comfortable reading.
- Distinguish data source, Kenya in Data analysis and methodological notes.
- Include page numbers, running section labels, document metadata and a stable citation.
- Target PDF/UA-1 when the selected Typst version and document structure permit it.

## Reproducible build structure

When work resumes, create:

```text
PDF and Deck/
├── typst/
│   ├── main.typ
│   ├── kid-report-template.typ
│   ├── references.bib
│   └── assets/
├── output/
│   └── KID-001-kenya-public-debt-current-baseline.pdf
└── README.md
```

The Typst source should read publication metadata from one clearly defined block and reference the existing SVG charts rather than copying them.

## Required QA

1. Compile the PDF reproducibly from the saved Typst source.
2. Confirm fonts are embedded and figures remain vector where possible.
3. Render every page to PNG.
4. Inspect every page for clipped text, poor line breaks, inconsistent spacing, low-resolution images and broken links.
5. Check the table of contents, references, page numbers and PDF metadata.
6. Confirm that all figure captions reproduce the article's dates, caveats and source locations.
7. Test the final PDF on desktop and mobile readers.

## Local environment note

At the time of this decision, neither Typst nor a LaTeX engine was installed in the project environment. Installation is deferred until PDF production resumes.
