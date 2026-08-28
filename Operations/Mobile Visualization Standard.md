---
title: Kenya in Data Mobile Visualization Standard
document_type: design-standard
status: active
created: 2026-08-28
last_updated: 2026-08-28
tags: [design-system, mobile, visualization, accessibility, publication]
---

# Kenya in Data — Mobile Visualization Standard

Most Kenya in Data readers will encounter a publication on a phone. Mobile is therefore the primary editorial canvas. Desktop graphics remain valuable for reports, presentations and downloads, but they must not be reduced mechanically into an unreadable inline image.

This standard extends the [Visual Style Guide](Style%20Guide.md).

## 1. Responsive asset pair

Every chart intended for an article should have two deliberate compositions:

| Variant | Canvas | Main use |
|---|---:|---|
| Mobile | 1080 × 1350 px, 4:5 | Article reading, social feeds and messaging apps |
| Landscape | 1920 × 1080 px or larger, 16:9 | Desktop article, slides, reports and downloads |

Use the same figure ID and append `_mobile` to the portrait filename. Example:

- `FIG-KID001-004_june_2025_debt_components.svg`
- `FIG-KID001-004_june_2025_debt_components_mobile.svg`

The two files may use different layouts, but must preserve the same values, definitions, reporting dates and caveats.

## 2. Minimum mobile typography

These sizes apply to a 1080 × 1350 source canvas:

| Element | Minimum source size |
|---|---:|
| Finding-led headline | 42 px |
| Subtitle or reporting label | 26 px |
| Category label | 26 px |
| Direct value label | 28 px |
| Annotation or caveat | 22 px |
| Source and attribution | 18 px |

Do not solve crowding by shrinking text. Shorten labels, wrap them deliberately, reduce the number of categories or split the visual.

## 3. Safe area and density

- Keep at least 72 px between essential content and every canvas edge.
- Use one primary finding per graphic.
- Prefer no more than seven categories. Eight is acceptable for a simple ranked list; larger sets should be split or grouped transparently.
- Avoid legends where direct labels are possible.
- Keep explanatory prose outside the chart when the article caption can carry it.
- A reader should understand the principal message without zooming.

## 4. Mobile chart patterns

| Analytical task | Preferred mobile pattern |
|---|---|
| Two-part composition | Large total, compact 100% bar and two directly labelled rows |
| Three- or four-part composition | Unlabelled 100% bar plus one full-width labelled row per component |
| Ranked categories | Portrait horizontal bars with wrapped labels and values at the bar ends |
| Rate or amount comparison | Three to five horizontal bars on a zero baseline |
| Long time series | Portrait plot with fewer ticks, direct end labels and annotations outside dense areas |
| Several related time series | Stacked small multiples sharing one time axis |
| Benchmark comparison | Bullet chart with an explicit target line and a plain-language gap annotation |
| Concept explanation | Two or three numbered panels with one sentence per panel |

Avoid desktop patterns that fail when narrowed: long horizontal legends, tiny multi-segment labels, wide tables embedded as images, and annotations placed outside the plot boundary.

## 5. Web art direction

Use `<picture>` so the browser selects the portrait composition on a narrow screen:

```html
<picture class="figure-media figure-media--responsive">
  <source media="(max-width: 700px)" srcset="figure_mobile.svg">
  <img src="figure.svg" alt="..." loading="lazy" width="1152" height="648">
</picture>
```

Reserve the image area before lazy loading:

```css
.figure-media { display: block; aspect-ratio: 16 / 9; }
.figure-media img { width: 100%; height: 100%; object-fit: contain; }

@media (max-width: 700px) {
  .figure-media--responsive { aspect-ratio: 4 / 5; }
}
```

Use `figure-media--portrait` for an asset that is always 4:5 and `figure-media--square` for a 1:1 asset. This prevents zero-height lazy-loaded figures and reduces layout shift.

## 6. Article layout on phones

- Test at 360, 390 and 430 px widths.
- Remove decorative figure padding that reduces the usable chart width.
- Keep captions outside the image and at normal article text size.
- Let download actions wrap onto multiple lines.
- Tables may scroll horizontally, but the core finding should also be stated in text.
- Prefer SVG for inline display and provide PNG for common reuse.

## 7. Mobile QA gate

A public graphic does not pass review until all of the following are true:

1. The page has no horizontal overflow at 360 px.
2. The chart is readable at the article's actual rendered width without pinch-to-zoom.
3. No title, label, value, source line or annotation is clipped.
4. Bars begin at zero unless the form is explicitly not a bar chart.
5. Part-to-whole values reconcile to 100% within disclosed rounding.
6. Colour is not the only means of distinguishing categories.
7. Alt text states the main finding and the important values.
8. The desktop layout still works at 1280 px after mobile changes.
9. PNG dimensions, SVG view boxes and download links are verified.
10. The mobile and landscape variants reconcile to the same canonical dataset.

## 8. Publication rule

The responsive figure pair is one analytical asset expressed in two layouts—not two independent sources. Update the canonical article and dataset first, then rebuild and review both versions together.
