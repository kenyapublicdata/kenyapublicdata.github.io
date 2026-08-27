---
title: Kenya in Data Vault Structure and Operating Model
project: Kenya in Data
document_type: architecture
status: active
created: 2026-08-27
last_updated: 2026-08-27
---

# Kenya in Data Vault Structure and Operating Model

## Purpose

This document defines how **Kenya in Data** is organized inside Bosho OS. Kenya in Data is the parent institution and publishing system. Its `Projects/` folder contains bounded research programmes, each with its own sources, datasets, analysis, figures, verification work, and outputs.

Kenya in Data currently lives at:

`Venture Studio/Projects/Kenya in Data/`

## Organizing Model

The hierarchy has three levels:

1. **Kenya in Data** — the institution, standards, shared library, and operating system.
2. **Research projects** — self-contained investigations into a subject, such as public debt.
3. **Publications** — individual charts, threads, briefs, or datasets produced by a research project.

A research project may produce several publications. A publication is therefore an output of a project, not the project itself.

> The dataset becomes the institution.

Every published claim or graphic should be traceable through this chain:

`source → raw data → transformation → indicator → finding → figure → publication`

## Kenya in Data Architecture

```text
Kenya in Data/
├── 00_Kenya in Data Home.md
├── Constitution.md
├── Glossary.md
├── Roadmap.md
├── Vault Structure and Operating Model.md
│
├── Inbox/
│
├── Projects/
│   └── PRJ-001 Kenya Public Debt/
│
├── Indicators/
│   └── Registry.csv
│
├── Sources/
│   └── Source Registry.md
│
├── Code/
│
├── Publications/
│   └── KID-### Publication Title/
│
├── Operations/
│   ├── Style Guide.md
│   ├── Templates/
│   └── Protocols/
│
├── Updates/
│   └── YYYY-MM-DD.md
│
└── Archive/
```

The folders outside `Projects/` form the shared institutional layer. Project material is promoted into them only after it is verified, stable, and useful beyond the immediate investigation.

## Project Architecture

Every substantial investigation receives a stable folder inside `Projects/`:

`PRJ-### Short Descriptive Title/`

The standard internal structure is:

```text
PRJ-### Project Title/
├── 00_Project Home.md
├── Project Brief.md
├── Research Questions.md
│
├── Sources/
│   ├── Source Register.md
│   └── Documents/
│
├── Data/
│   ├── README.md
│   ├── Raw/
│   ├── Interim/
│   ├── Processed/
│   └── Published/
│
├── Indicators/
│   ├── Indicator Plan.md
│   └── Definitions.md
│
├── Methodology/
│   ├── Methodology Plan.md
│   └── Topic-specific method notes.md
│
├── Analysis/
│   ├── Analysis Log.md
│   └── Calculations/
│
├── Figures/
│   ├── Figure Plan.md
│   ├── Drafts/
│   └── Final/
│
├── Publications/
│   ├── Publication Plan.md
│   ├── Drafts/
│   └── Published/
│
├── Verification/
│   ├── Verification Checklist.md
│   └── Issues and Decisions.md
│
├── Code/
│   └── README.md
│
├── Updates/
└── Archive/
```

## Project-Local Versus Shared Material

During research, material belongs inside its project:

- source documents and source notes;
- raw and transformed data;
- proposed indicator definitions;
- calculations and analysis logs;
- draft and final figures;
- publication drafts and released outputs;
- verification records and methodological decisions.

Material moves into the relevant shared top-level area only when it has been verified and is genuinely reusable or ready for release:

- canonical indicator definitions and series go to `Indicators/`;
- reusable source records go to `Sources/`;
- reusable pipelines and chart systems go to `Code/`;
- approved public outputs go to `Publications/`.

Promotion means copying or publishing a stable canonical version; the project retains its historical working version so the original analysis remains reproducible.

Examples of material that may eventually be promoted include a canonical GDP deflator series, population estimates, exchange rates, administration-boundary definitions, reusable chart code, and common source records.

## Shared Institutional Areas

### Glossary

The root `Glossary.md` is the shared vocabulary for all Kenya in Data work. It defines recurring economic, fiscal, statistical, and publishing concepts once at the institutional level. Project-specific definition notes link to the glossary and record only narrower source, indicator, or methodological conventions.

### Indicators

The top-level `Indicators/` folder is the canonical indicator registry for Kenya in Data. It contains verified definitions and stable series that may be used by more than one project. Exploratory or project-specific indicators remain inside their originating project until promoted.

### Sources

The top-level `Sources/` folder records recurring institutions, datasets, documents, release calendars, and provenance information with cross-project value. Detailed extraction notes and project-specific documents stay inside the relevant project.

### Code

The top-level `Code/` folder contains reusable extraction, transformation, verification, and visualization tools. One-off or experimental code begins inside the project that requires it.

### Publications

The top-level `Publications/` folder is the institutional archive of approved public releases. Drafts, supporting analysis, and publication development remain inside the originating project. A final release can be copied or linked into the shared archive without removing the project's reproducible record.

## What Belongs Where Inside a Project

### Project home and planning

- `00_Project Home.md` is the project's command centre: objective, current phase, next action, open questions, outputs, and key links.
- `Project Brief.md` defines scope, audience, intended contribution, exclusions, and completion criteria.
- `Research Questions.md` separates the primary question from secondary and future questions.

### Sources

`Sources/Source Register.md` records every source considered, including its publisher, title, period covered, URL or file, retrieval date, relevant tables or pages, and quality notes. `Sources/Documents/` selectively preserves downloaded source material.

Every published number must be traceable to a specific source table, page, or downloadable dataset. Large documents should not automatically be committed to a future public Git repository; record stable links, filenames, retrieval dates, and checksums where appropriate.

### Data

- `Data/Raw/` contains source data exactly as acquired. Raw files are immutable.
- `Data/Interim/` contains extracted or partially cleaned data that is not yet analysis-ready.
- `Data/Processed/` contains normalized, joined, calculated, or analysis-ready datasets.
- `Data/Published/` contains the precise, versioned data released with a publication.

Canonical observations should live in CSV or Parquet files. Markdown explains the data but is not the authoritative store for time-series observations. Transformations must create new outputs and never overwrite raw data.

### Indicators

`Indicators/` defines the measures the project intends to construct or use. At minimum, every indicator should identify:

- indicator ID and name;
- definition and interpretation;
- date or reporting period;
- value and unit;
- geography and frequency;
- primary source and source document;
- methodology or transformation version;
- revision status, limitations, and notes.

### Methodology

`Methodology/` holds the analytical choices that determine what the numbers mean: definitions, comparison periods, inflation adjustment, rebasing, currency treatment, administration boundaries, missing-data rules, revisions, and limitations.

Methodological decisions should be explicit before the final narrative is written.

### Analysis

`Analysis/Analysis Log.md` records exploratory questions, tests, anomalies, provisional findings, and rejected interpretations. `Analysis/Calculations/` contains notebooks or calculation artifacts that support the findings.

Analysis notes distinguish what the data directly show from interpretation and causal claims.

### Figures

`Figures/Figure Plan.md` lists intended charts, their analytical purpose, required data, visual form, and status. `Drafts/` contains working exports; `Final/` contains approved reproducible figures.

Figures should never be the only surviving representation of a result. Their underlying published data and generating method must be retained.

### Publications

`Publications/` contains distinct public outputs from the research project. Publications use stable IDs such as `KID-001`, `KID-002`, and so on. A single project may yield an X post, a longer brief, a downloadable dataset, and multiple chart releases.

Publication status is recorded in metadata—such as `idea`, `researching`, `drafting`, `verification`, `ready`, `published`, or `corrected`—rather than by repeatedly moving files between workflow folders.

### Verification

`Verification/` provides the evidence gate between analysis and publication. It records checks, unresolved discrepancies, corrections, reviewer notes, and consequential decisions.

### Code

`Code/` contains reproducible extraction, cleaning, calculation, and chart-generation scripts. Code should read from `Data/Raw/` or `Data/Interim/` and write new artifacts to `Data/Processed/`, `Data/Published/`, or `Figures/`.

Secrets, credentials, and API keys must never be stored in the vault or committed to version control.

### Updates and archive

`Updates/YYYY-MM-DD.md` records source acquisitions, completed processing, findings, decisions, and publication events. Past context should not be silently rewritten.

`Archive/` preserves replaced drafts, obsolete outputs, and retired approaches that retain historical value. Archiving is preferred to deletion.

## Project Workflow

1. **Define:** Write the brief and research questions.
2. **Map:** Plan the required indicators, sources, datasets, and figures.
3. **Acquire:** Register and preserve primary sources.
4. **Extract:** Store original files in `Data/Raw/` and extracted material in `Data/Interim/`.
5. **Transform:** Produce documented, reproducible processed data.
6. **Analyze:** Record findings, anomalies, and rejected interpretations.
7. **Visualize:** Create figures whose data and transformations can be reproduced.
8. **Verify:** Check definitions, units, time boundaries, revisions, calculations, and conflicting sources.
9. **Publish:** Release the output with sources, caveats, and supporting data where appropriate.
10. **Preserve:** Record the release and retain the exact published data and figure.
11. **Promote:** Copy verified, reusable assets into the appropriate shared institutional area.
12. **Correct:** Issue visible corrections and retain superseded versions.

## Naming and Identity Standards

- Research projects use `PRJ-###`, for example `PRJ-001 Kenya Public Debt`.
- Public outputs use `KID-###`, for example `KID-001 Nominal vs Real Public Debt`.
- Indicators use stable IDs such as `IND-DEBT-001`.
- IDs do not change when titles are refined.
- Dates in filenames and metadata use `YYYY-MM-DD`.
- Use descriptive filenames; avoid `final`, `final2`, or `latest` without a version or date.
- Project and publication notes include `status`, `created`, and `last_updated` metadata.
- Source, data, and methodology revisions must be documented rather than hidden by overwriting files.

## Verification Standard

Before publication, confirm that:

- the primary source is identified and accessible;
- definitions remain consistent across the comparison period;
- units, nominal or real status, frequency, and geography are explicit;
- transformations can be reproduced from retained inputs;
- calculations have been independently checked;
- important caveats, revisions, and breaks in series are disclosed;
- visual scales and annotations do not mislead;
- the headline follows from the evidence;
- causal language is avoided unless the research design supports it;
- the chart, caption, and released dataset agree.

## First Research Project

The first project is:

`Projects/PRJ-001 Kenya Public Debt/`

Its first objective is to build a fair, reproducible comparison of Kenya's public debt across administrations. The project may produce several publications covering nominal debt, inflation-adjusted debt, debt relative to GDP, domestic and external composition, exchange-rate effects, and the debt-service burden.

The project should establish the minimum working standard for all future Kenya in Data research projects. New top-level systems and automation should be added only when this project or a subsequent one demonstrates a recurring need.

## Graduation to an Independent Vault or Repository

Reconsider Kenya in Data's location when one or more of the following becomes true:

- external contributors need independent access;
- datasets or documents make Bosho OS materially harder to sync;
- the public data and code repository becomes a product in its own right;
- Kenya in Data develops independent governance or release cycles;
- private research notes and public assets require a formal boundary.

Until then, remaining inside `Venture Studio/Projects/` keeps Kenya in Data integrated with Bosho OS while allowing each research project to be intricate and self-contained.
