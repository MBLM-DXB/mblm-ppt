# MBLM Layout Catalog

Canvas for all kit layouts: **1280 × 720** (`viewBox="0 0 1280.16 720"` or `1280.2 720`) — 16:9 widescreen.

Reference SVGs: `${SKILL_DIR}/assets/mblm/layouts/`. Use these as **composition references** when authoring mblm-ppt page SVGs (do not paste placeholder “Title goes here” copy into final decks).

**Specs + R2 patterns** (mandatory adaptation source): [`visual-references/LAYOUT_PATTERNS.md`](visual-references/LAYOUT_PATTERNS.md), [`visual-references/CATALOG.md`](visual-references/CATALOG.md), and [`visual-references/CATALOG_R2.md`](visual-references/CATALOG_R2.md). Prefer those patterns over inventing consulting-deck chrome. **Agenda gold standard (SVG catalog)**: r2_40 (section agenda). *(r2_12 Content TOC SVG removed.)*

| Layout file | Page job | Composition notes |
|---|---|---|
| `MBLM_title_slide.svg` | Cover | Black or yellow flood; Light title; logo — Pattern A |
| `MBLM_title.svg` | Title / chapter | Large Light title on dark field |
| `MBLM_title_content.svg` | Title + body | Light title **40pt** + Regular body; no kicker; margins v4.1 |
| `MBLM_section_header.svg` | Section break | Full black; Light white title; oversized outlined MBLM watermark / Supertext |
| `MBLM_hero_statement.svg` | Quote / manifesto | Large Light quote; optional photo + Supertext — Pattern E |
| `MBLM_four_card.svg` | 2×2 cards | Four modules; **blue-only** accent lines above cards (`#002A60`/`#006AF1`/`#00AEFF`/`#0068EB`) — never yellow |
| `MBLM_process.svg` | Process steps | Flow steps; blue nodes; gray connectors (not yellow lines) |
| `MBLM_process_timeline.svg` | Timeline | Sequential process with timeline spine |
| `MBLM_kpi_dashboard.svg` | Metrics | KPI tiles; blue-gray accents; blue card lines if used |
| `MBLM_table_summary.svg` | Table | Title + table; header dark blue/blue/black/grey + white text; normal kerning; hairline `#BFBFBF` borders |
| `MBLM_chart_insight.svg` | Chart + insight | Chart + callout; yellow `#FFF200` as **fill** highlight only |
| `MBLM_three_picture_caption.svg` | 3-up media | Three image wells + captions |
| `MBLM_four_picture_caption.svg` | 4-up media | Four image wells + captions |
| `MBLM_six_picture_caption.svg` | 6-up media | Dense gallery |
| `MBLM_title_picture.svg` | Title + picture | Split title and imagery — align with photo+bar when possible |
| `MBLM_editorial_split.svg` | Editorial | Asymmetric image/text; 2:1 / three-panel DNA |
| `MBLM_screenshot_focus.svg` | Product UI | Large screenshot focus |
| `MBLM_closing.svg` | Close | Dark or yellow field; logo; optional Supertext thank-you |
| `MBLM_07_blank.svg` | Freeform | Empty branded canvas |

## Spec patterns to map onto kit layouts

| Pattern (LAYOUT_PATTERNS) | Typical kit layout(s) |
|---|---|
| A Yellow flood cover/closing | `title_slide`, `closing` |
| B 2:1 Frame | `editorial_split`, `title_picture`, custom SVG |
| C Photo + black brand bar | `title_picture`, `editorial_split`, `hero_statement` |
| D Three-panel editorial | custom / `editorial_split` |
| E Full-bleed + Supertext | `hero_statement`, `section_header` |
| F Framed masters | `title_content`, `table_summary`, content pages |
| G Gradient + vertical Supertext | `title_slide`, `section_header` |
| H Ambition pillars | `four_card`, `title_content` |
| I Cards / modules | `four_card`, `kpi_dashboard` |
| J Agenda / Content TOC ★ | **REMOVED** — use Pattern K / r2_40 only |
| K Section agenda on gradient ★ | `section_header` / custom — mimic r2_40 |
| L–S R2 consulting patterns | see `LAYOUT_PATTERNS.md` + `CATALOG_R2.md` |

## Rhythm recommendations

1. Title slide (Pattern A)  
2. Agenda / overview — **Pattern K (r2_40)**; also H/I pillars *(Pattern J / r2_12 SVG removed from catalog)*  
3. Section / 2:1 / photo+bar → content cluster  
4. Optional hero Supertext statement  
5. Closing  

Keep geometry signatures consistent within a section (same card treatment, same brand-bar width, same logo corner). Enforce `LINE_RULES.md` and `TYPOGRAPHY.md` on every page.

## Margins + geometry (v4.1.0 @ 1280×720) — see `LAYOUT_METRICS.md` / `MARGINS.md`

- **All sides** inset **1.05 cm ≈ 39.7 px** (practical **40 px**)
- Content-slide logo: **x=1148.2 y=39.7 w=88.4 h=44.2** (2.34×1.17 cm @ 30.38, 1.05 cm)
- Cover / divider / thank-you logo: **x=40 y=40 w=138 h=69** (3.65×~1.825 cm @ 1.05, 1.05 cm)
- Content titles: BentonSansCond Light **40pt only** (incl. Agenda page title); r2_40 section labels **50pt** Light
- Title top aligned to logo top; gutter between cards ≥ 24–32 px
- Bullets: round black circles (`BULLETS.md`); no kickers (`TYPOGRAPHY.md`)

## Official PPTX template

For native PowerPoint editing outside mblm-ppt, start from:

`${MBLM_MASTER_ROOT}/source/mblm assets/template/MBLM_Power point _v1.pptx`

For mblm-ppt Generate, prefer authoring SVG pages that **match** these layouts + specs patterns rather than round-tripping the 70MB PPTX unless the user asks for Edit Native PPTX.

## R2 consulting deck pack (STEP 1)

Registered deck: **`mblm-r2`** → `templates/decks/mblm-r2/` (40 semantic SVGs from R2 examples).  
Authoring mirrors: `assets/mblm/layouts/r2/`. Map: `templates/decks/mblm-r2/SOURCE_MAP.md`.  
Install/use: [`docs/STEP1_R2_SVG_TEMPLATES.md`](../../docs/STEP1_R2_SVG_TEMPLATES.md).  
Agenda gold standard in SVG catalog: **r2_40** (see `CATALOG_R2.md`; r2_12 SVG removed).

## Diagram inserts (STEP 2)

Process monoline diagrams (`skills/mblm-diagram`, `assets/mblm/diagrams/`) fit best on:

| Host | Notes |
|---|---|
| `MBLM_process` / `MBLM_process_timeline` | Dedicated process kit layouts |
| `MBLM_title_content` | Wide centered well under 40pt Light title |
| R2 process / pillar / chevrons / timeline pages | See `templates/decks/mblm-r2/DIAGRAM_SLOTS.md` |

Keep diagrams monochrome; do not collide with title band or content logo. Details: [`DIAGRAMS.md`](DIAGRAMS.md).

