---
deck_id: mblm-r2
kind: deck
category: consulting
summary: Reusable MBLM consulting layout prototypes derived from R2 proposal examples for apply_template / authoring. Covers agenda TOC, section dividers, multi-column cards, process chevrons, timelines, Gantt, risks tables, org/scope trees, and photo wells.
keywords: [MBLM, consulting, proposal, R2, agenda, roadmap, risks]
primary_color: "#000000"
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: fidelity
native_structure_mode: structured
page_count: 39
---

# MBLM R2 Consulting — Design Specification

## I. Template Overview

| Application context | Definition |
| --- | --- |
| Recurring presentation family | Consulting proposals, situation/complication/resolution decks, approach & timeline pages, risk registers, capability references |
| Intended audiences and outcomes | Client stakeholders and internal reviewers; layouts are semantic SVG prototypes for `apply_template` / authoring, not final client copy |
| Delivery and reading assumptions | 16:9 landscape; meeting projection and PDF handoff; placeholders use `{{TOKEN}}` carriers |
| Representative narrative/page roles | Agenda (r2_40), pillars/cards, process/chevrons, timelines/Gantt, tables/matrices, photo+list, org/scope trees |

These pages are **layout prototypes** distilled from the R2 visual-reference catalog (`CATALOG_R2.md`). Agents should fill placeholders with project content; do not paste proprietary screenshot copy into production decks.

## II. Color Scheme

| Role | Color | Application |
| --- | --- | --- |
| Primary black | #000000 | Circles, headers, body text, chevrons |
| White | #FFFFFF | Master background; text on black fills |
| Accent blue | #00AEFF | Process nodes, down-triangles, sidebar headers |
| Mid blue | #006AF1 | Solution headers, activity bars |
| Navy | #002A60 | Outcomes headers, phase labels, card accent lines |
| Accent blue 2 | #0068EB | Secondary process fills |
| Light grey | #E5E5E5 / #F2F2F2 | Card footers, wells, photo placeholders |
| Risk yellow / red | #F2B75A / #D65F6D | Risk-level dots (fills only) |
| Milestone yellow | #F2B75A | Gantt diamonds / workshop markers (fills only) |

**Hard rules**: no yellow text on black; no blue accent *lines* on black boxes; card accent lines only from the blue family; bullets are round black circles (never blue triangles).

## III. Typography

| Role | Font stack | Application |
| --- | --- | --- |
| Titles | `BentonSansCond, Arial Narrow, Arial, sans-serif` | Light **40pt** (SVG **53.3** when exporter-scaled) (`font-weight="300"`); top aligned with logo |
| Body / bullets | same stack | 16–18pt Regular min; black `#000000` |
| Headers on dark fills | same stack | White text only |

No kickers/eyebrows. No tagline under the logo. Normal kerning.

## IV. Signature Design Elements

- Content logo (light slides): `MBLM_LOGO_White background.svg` at `x=1148.2 y=39.7 w=88.4 h=44.2`
- Section divider / dark gradient (r2_40): dark logo at `x=40 y=40 w=138 h=69`
- Margins ~40px all sides
- Agenda gold standard (SVG catalog): **r2_40** section agenda on blue→navy gradient *(r2_12 Content TOC removed)*
- Photo wells: grey `#E5E5E5` rects with `{{IMAGE}}` carriers (hooks for later image skill)

## V. Page Roster

39 SVG pages named `NN_r2_XX_<slug>.svg` (r2_02 … r2_41; **r2_12 / `11_r2_12_content_toc` removed**). See `SOURCE_MAP.md`.

## VI. Assets

| File | Intended usage |
| --- | --- |
| `MBLM_LOGO_White background.svg` | Content / light slides (top-right) |
| `MBLM_LOGO_dark background.svg` | Dark gradient section dividers (top-left) |
| `MBLM_LOGO_Brand color.svg` | Optional brand-color lockup |
| `MBLM_LOGO_Yellow background.svg` | Optional yellow-field lockup |
