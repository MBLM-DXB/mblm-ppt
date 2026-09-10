---
name: mblm-ppt
description: >
  Generate MBLM-branded PowerPoint decks (The Brand Intimacy Agency) using the
  local ppt-master engine with MBLM palette, BentonSansCond typography, logo
  lockups, layout patterns, and kit icons — driven by visual analysis of official
  specs + R2 consulting examples plus user hard rules (v4.1 persistent layout lock). Use when the user asks
  for an MBLM PPT, PPTX, slide deck, presenter deck, pitch, case study, or agency
  presentation; when branding must match the MBLM brand kit; or when the user
  mentions mblm-ppt / MBLM slides. Prefer this over generic ppt-master branding
  for any MBLM work.
metadata:
  version: "4.1.1"
  brand: "MBLM — The Brand Intimacy Agency"
  engine: "ppt-master (local install)"
---

# MBLM PPT Skill (v4.1.1)

Self-contained skill for **MBLM-branded** decks. Visual identity is driven by **analysis of official specs + R2 consulting examples** (plus user hard feedback), then applied via this folder’s `assets/` + `references/`. Slide generation uses the existing **ppt-master** install — do not reimplement the SVG→PPTX pipeline here. Do **not** invent McKinsey-style decks.

## Mandatory load order

1. Read this file. Retain its absolute directory as `SKILL_DIR`.
2. **STEP 1 — Visual reference pass (mandatory before any SVG authoring)**  
   - Read [`references/visual-references/CATALOG.md`](references/visual-references/CATALOG.md), [`references/visual-references/CATALOG_R2.md`](references/visual-references/CATALOG_R2.md), and [`references/visual-references/LAYOUT_PATTERNS.md`](references/visual-references/LAYOUT_PATTERNS.md).  
   - Consult images under `${MBLM_MASTER_ROOT}/skill/_spec_screens_ascii/` (55 PNGs) **and** `${MBLM_MASTER_ROOT}/skill/_examples_r2_ascii/` (40 PNGs + INDEX.txt). Prefer Read-tool inspection of relevant PNGs for the deck type.  
   - Optionally re-scan `${MBLM_MASTER_ROOT}/MBLM slides and other specs/` and `${MBLM_MASTER_ROOT}/more examples r2/` if newer images appear.  
   - **Agenda**: mimic gold standard **r2_12** (Content numbered TOC) and/or **r2_40** (section agenda on gradient).  
   - **Describe** the layout patterns you will adapt; **adapt** those patterns — do not invent consulting-deck chrome.
3. Read [`references/PATHS.md`](references/PATHS.md) and set `PPT_MASTER_SKILL`.
4. Brand freeze (batch — hard rules):
   - [`references/LINE_RULES.md`](references/LINE_RULES.md) ← no yellow lines; blue-only above cards; **white-only on black fills**
   - [`references/LAYOUT_METRICS.md`](references/LAYOUT_METRICS.md) ← **v4.1 persistent** cm+px geometry (margins / logos / titles)
   - [`references/TYPOGRAPHY.md`](references/TYPOGRAPHY.md) ← cover 60/72; **content titles 47pt only** (top @ 1.05 cm); body 16–20; subtitles 18–20 **`#000000`**; Light headers; Regular body; Bold accents <24; **no kickers**; **normal kerning**; Supertext **≥150pt** stroke **1.25pt**
   - [`references/TEXT_BOXES.md`](references/TEXT_BOXES.md) ← **one text object per paragraph** (no per-line boxes)
   - [`references/MARGINS.md`](references/MARGINS.md) ← **1.05 cm ≈ 39.7 px** all sides (practical **40**)
   - [`references/BULLETS.md`](references/BULLETS.md) ← round **black** circles Ø≈**80%** text
   - [`references/COLORS.md`](references/COLORS.md)
   - [`references/LOGOS.md`](references/LOGOS.md) ← content logo **88.4×44.2 @ 1148.2,39.7**; cover/divider/thanks **138×69 @ 40,40**; **no tagline / no bottom wordmark** when logo present
   - [`references/LAYOUTS.md`](references/LAYOUTS.md)
5. Read [`workflows/generate-mblm-pptx.md`](workflows/generate-mblm-pptx.md) and execute **Path A** (Quick) unless the user asks for Strategist UI (Path B) or native template edit (Path C).
6. Load ppt-master runtime docs only as that workflow requires (`quick-generate.md` or `generate-pptx.md`, plus executor/shared-standards).
7. Consult [`references/ICONS.md`](references/ICONS.md) and [`references/IMAGERY.md`](references/IMAGERY.md) when relevant. Locked decisions: [`references/RESOLVED_DECISIONS.md`](references/RESOLVED_DECISIONS.md).
8. Optional identity brief: [`references/brand_spec.md`](references/brand_spec.md).

**Hard rule — paths**: expand absolute paths every tool call; quote spaces (`mblm master`). Never `cd` into the ppt-master engine as a substitute for absolute paths.

**Hard rule — brand lock**: do not substitute McKinsey/BCG/other engine brand presets. Do not invent colors outside `COLORS.md`.

**Hard rule — engine**: call scripts under `PPT_MASTER_SKILL/scripts/`. Do not modify `ppt-master-main` for ordinary generation.

---

## HARD DESIGN FREEZE (impossible to miss) — v4.1.1

### User v4.1.1 locks (persistent layout — override conflicting v3/v4 geometry)

1. **Editable text**: never one SVG/PPT text box per wrapped line — **one text object per paragraph** (`TEXT_BOXES.md`; tspans OK). Do not export with `--no-merge`.
2. **Layout metrics**: document cm + px in `LAYOUT_METRICS.md`; scale **37.795 px/cm** (1280 / 33.867).
3. **Margins**: **1.05 cm ≈ 39.7 px** on **all sides** (practical **40 px**) — `MARGINS.md`.
4. **Content-slide logo**: **2.34×1.17 cm → ≈88.4×44.2 px** at **x=30.38 cm / ≈1148.2**, **y=1.05 cm / ≈39.7** — identical on **every** content slide (`LOGOS.md`).
5. **Cover / divider / thank-you logo**: **3.65 cm → ≈138 px** wide; height **~1.825 cm / ≈69 px**; left **1.05 cm / ≈40**, top **1.05 cm / ≈40**.
6. **Cover title**: **60pt or 72pt** Light (prefer **72** when it fits) — **cover only**.
7. **Cover subtitles**: **24pt or 32pt** (prefer **28–32**). Not 23.5.
8. **Body**: **16pt or 20pt** Regular — lock one deck-wide; prefer **20pt**.
9. **Content-slide subtitle** (under title): **18pt or 20pt**, consistent (prefer 20); **black `#000000`**; directly under title (normal gap); left margin **1.05 cm**.
10. **Content-slide titles** (incl. Agenda “Content”): Light **47pt only** — never 54 / 24 / 32 / 28–36. **Top edge at 1.05 cm** (same Y as content logo top). Overrides prior agenda ≥72 and content 28–36.
11. **No kickers at all** — never above the title (deck-wide; zero tolerance).
12. **Supertext / outline words**: **≥150pt**; edge-to-edge within margins; stroke **1.25pt**.
13. **Remove tagline** "The Brand Intimacy Agency" when logo is present; **do not add MBLM wordmark/text at the bottom** if logo is already on the slide.
14. **Bullets**: round **black** circles; diameter ≈ **80% of text size**; indent properly.
15. **Kerning normal** — do not expand letter-spacing / tracking.
16. **No black boxes with yellow font or blue lines** — on black fills use **white font only**.
17. **Gradient backgrounds** mainly for **section dividers** — not full-bleed on ordinary content slides.
18. **Tables**: header **only** `#002A60` / `#000000` / `#808080`; white/contrast text; **kerning normal**. Other chrome/bars/accents: primary `#000000` `#FFFFFF` `#FFF200` only.
19. **No line-box stacks** — solid filled boxes + paragraph text blocks.
20. **Agenda** from R2 (**r2_12** + **r2_40**) as structural gold standard (Patterns J/K); title size = **47pt**.

### Still in force from v2

- **Yellow lines forbidden** — never `#FFF200` as divider/accent **lines**. Yellow = fills/floods/chart fills/Supertext strokes/milestone fills only.
- **Lines above squares/cards** — blue family only: `#002A60` (prefer), `#006AF1`, `#00AEFF`, `#0068EB`.
- **Weights**: Light headers / Regular body / Bold accents <24 / Medium topics / Black Supertext.

### Typography + geometry snapshot

| Role | Rule |
|---|---|
| Cover title | BentonSansCond **Light**, **60 or 72** (prefer 72), **normal kerning**, **no kicker** — cover only |
| Cover subtitle | **24 or 32** (prefer 28–32) |
| Content titles (incl. Agenda) | Light **47pt only**; top edge **1.05 cm** |
| Content subtitle | Regular **18 or 20** (prefer 20); **`#000000`**; under title @ left margin |
| Body | Regular **16 or 20** locked (**prefer 20**) |
| Accents <24 | **Bold** |
| Topic headers | **Medium** |
| Supertext | **Black** outline **1.25pt**; **≥150pt**; edge-to-edge; must **NOT** repeat page headline |
| Text boxes | One object per paragraph (`TEXT_BOXES.md`) |
| Content logo | **88.4×44.2 @ 1148.2,39.7** (`LAYOUT_METRICS.md`) |
| Cover/divider/thanks logo | **138×69 @ 40,40** |
| Margins | **1.05 cm / ≈40 px** all sides |
| Bullets | Round black circles Ø≈80% text (`BULLETS.md`) |

### Visual analysis first

Every Path A/B run starts with the visual reference pass (specs **+ R2**). Design output must look like official specs / R2 consulting layouts — not generic McKinsey chrome.

---

## When to use

| Request | Use this skill? |
|---|---|
| “Make an MBLM deck / brand intimacy pitch / agency PPT” | Yes |
| “MBLM colors / Benton / our icons” | Yes |
| Generic ppt-master deck with no MBLM requirement | No — use ppt-master skill directly |
| Edit the official `MBLM_Power point _v1.pptx` | Yes — Path C |

---

## Recipe (condensed)

```text
Visual reference pass (CATALOG + CATALOG_R2 + LAYOUT_PATTERNS + PNGs)
  → brand freeze (LAYOUT_METRICS + LINE + TYPE + TEXT_BOXES + MARGINS + BULLETS + COLORS + LOGOS + LAYOUTS)
  → Sources → attribution_guard → project init (--quick-generate)
  → copy logos/icons from ${SKILL_DIR}/assets into project
  → roster from LAYOUTS.md + LAYOUT_PATTERNS.md (agenda = J/K)
  → author svg_output/*.svg adapting catalog patterns (v4.1 metrics + 47pt titles + locked logos + single-paragraph text)
  → svg_quality_checker (--quick-generate) → svg_to_pptx (--quick-generate)  # never --no-merge
```

Full steps, flags, and Path B/C: [`workflows/generate-mblm-pptx.md`](workflows/generate-mblm-pptx.md).

### Brand freeze tokens (always-on)

| Token | Value |
|---|---|
| Canvas | 1280×720 (scale **37.795 px/cm** vs 33.867×19.05 cm) |
| Margins | **1.05 cm ≈ 39.7 / 40 px** all sides (`LAYOUT_METRICS.md`) |
| Primary | `#000000` `#FFFFFF` `#FFF200` + gray `#BFBFBF` |
| Blue line family | `#002A60` `#006AF1` `#00AEFF` `#0068EB` |
| Type | BentonSansCond — cover 60/72 Light; **content titles 47pt**; body 20 Regular; Supertext **≥150** / 1.25pt |
| Text boxes | One per paragraph |
| Content logo | **88.4×44.2 @ 1148.2,39.7** |
| Cover/divider/thanks logo | **138×69 @ 40,40** |
| Kickers | **Forbidden** |
| Tagline on-slide | **Omit when logo present** |
| Logo lockups | Positive on light; Negative on dark; brand-color = `MBLM_LOGO_Brand color.svg` |
| Bullets | Round black circles |

### Deck spine (default — adapt from patterns)

1. Title / yellow or black cover (Pattern A)  
2. Agenda — **Pattern J (r2_12)** and/or **K (r2_40)**; pillars H/I optional  
3. Section / 2:1 or photo+bar (Patterns B–C) or R2 content cluster (L–S)  
4. Optional hero / Supertext statement (Pattern E)  
5. Closing (Pattern A / Supertext thank-you)

---

## Asset map

```text
assets/
  logos/           # 4 SVG lockups (incl. Brand color)
  palette/         # primary / secondary / Accent swatches
  icons/           # 69 kit icons
  layouts/         # 19 composition reference SVGs
  brand-intimacy/  # V1–V3 graphics
  brand-kit-screenshot.png
  template/        # symlink to official PPTX (Path C only)
references/
  visual-references/  # CATALOG.md + CATALOG_R2.md + LAYOUT_PATTERNS.md
  LAYOUT_METRICS.md LINE_RULES.md MARGINS.md BULLETS.md TEXT_BOXES.md
  COLORS.md TYPOGRAPHY.md LOGOS.md LAYOUTS.md …
workflows/         # generation recipe
```

Specs / R2 mirrors (read-only inputs):

```text
${MBLM_MASTER_ROOT}/skill/_spec_screens_ascii/
${MBLM_MASTER_ROOT}/MBLM slides and other specs/
${MBLM_MASTER_ROOT}/skill/_examples_r2_ascii/
${MBLM_MASTER_ROOT}/more examples r2/
```

---

## Global discipline (adapted from the ppt-master engine)

1. Serial execution of the selected path.  
2. Blocking gates only where ppt-master marks `⛔ BLOCKING` (Quick has none for strategy).  
3. Act at the owning layer on failure (page SVG vs source vs tool).  
4. Match the user’s language.  
5. Keep MBLM identity consistent across every page (geometry signature + palette + line/type/margin/bullet/text-box rules).

---

## Out of scope

- Replacing or modifying ppt-master scripts / `ppt-master-main`  
- Auto-running Create Template on the ~70MB official PPTX (closed policy — Paths A/B use skill assets; Path C = Edit Native via `assets/template/` symlink)  
- Inventing gradient ASE files or installing fonts on remote machines  

On the user’s Mac, BentonSansCond is installed — use it. On other machines, apply the fallback chain and note it in the delivery message.
