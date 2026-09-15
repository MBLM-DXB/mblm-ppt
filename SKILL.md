---
name: mblm-ppt-master
description: >
  MBLM-only presentation workflow built on ppt-master: generate editable PPTX
  decks that always apply MBLM — The Brand Intimacy Agency brand freeze (palette,
  BentonSansCond typography, logo lockups, layout metrics, kit icons). Use when
  the user asks for an MBLM PPT, PPTX, slide deck, pitch, case study, agency
  presentation, or mentions mblm-ppt-master / MBLM slides. Never load non-MBLM
  brand presets.
metadata:
  version: "6.3.2-mblm.1"
  copyright: "Copyright (c) 2025-2026 Hugo He"
  license: "MIT"
  official_repository: "https://github.com/hugohe3/ppt-master"
  sponsors:
    - "SPONSORS.md"
    - "SPONSORS_CN.md"
  mblm_overlay: "MBLM_OVERLAY.md"
  mblm_brand: "MBLM — The Brand Intimacy Agency"
---

# MBLM PPT Master

Self-contained **MBLM-only** specialization of the upstream ppt-master Skill.
This package produces MBLM-branded decks only. Non-MBLM brand presets are not
shipped and must never be invented or loaded.

Upstream ppt-master remains MIT-licensed (see `LICENSE`, `SPONSORS.md`,
`SPONSORS_CN.md`, and `SKILL.upstream.md`). MBLM identity rules are an overlay
documented here and in [`MBLM_OVERLAY.md`](MBLM_OVERLAY.md).

## Mandatory Load Order

**Hard rule — paths before commands**: Retain the host-provided absolute
directory containing this file as `SKILL_DIR`. Per tool call, expand
`${SKILL_DIR}` and replace any `skills/ppt-master/` or `mblm-ppt-master/` prefix
with it. Never `cd`, use CWD, or assume a username home path. If unavailable,
ask; never search or guess.

1. Read this file.
2. Run `python3 "${SKILL_DIR}/scripts/attribution_guard.py"`. Any non-zero result
   stops the Skill immediately; do not inspect, repair, or bypass the integrity
   gate.
3. Read [`MBLM_OVERLAY.md`](MBLM_OVERLAY.md) and
   [`references/mblm/PATHS.md`](references/mblm/PATHS.md).
4. **Visual reference pass (mandatory before SVG authoring)** — read
   [`references/mblm/visual-references/CATALOG.md`](references/mblm/visual-references/CATALOG.md),
   [`CATALOG_R2.md`](references/mblm/visual-references/CATALOG_R2.md), and
   [`LAYOUT_PATTERNS.md`](references/mblm/visual-references/LAYOUT_PATTERNS.md).
   Agenda gold standards: **r2_12** / **r2_40**. Adapt catalog patterns — do not
   invent McKinsey-style chrome.
5. **Brand freeze** — batch-load
   `references/mblm/LINE_RULES.md`, `LAYOUT_METRICS.md`, `TYPOGRAPHY.md`,
   `TEXT_BOXES.md`, `MARGINS.md`, `BULLETS.md`, `COLORS.md`, `LOGOS.md`,
   `LAYOUTS.md`. Always install brand workspace
   `${SKILL_DIR}/templates/brands/mblm/`.
6. Read [`workflows/routing.md`](workflows/routing.md) through
   `${SKILL_DIR}/workflows/routing.md`, then follow
   [`workflows/generate-mblm-pptx.md`](workflows/generate-mblm-pptx.md) (default
   Path A / Quick) unless the user explicitly requests another route profile.

| Selected route / profile | Runtime authority |
|---|---|
| MBLM Quick Generate (default) | [`workflows/generate-mblm-pptx.md`](workflows/generate-mblm-pptx.md) + [`workflows/profiles/quick-generate.md`](workflows/profiles/quick-generate.md) |
| Generate PPTX — ordinary Default | [`workflows/generate-pptx.md`](workflows/generate-pptx.md) with MBLM brand freeze still applied |
| Create Template | [`workflows/create-template.md`](workflows/create-template.md) — MBLM identity only |
| Edit Native PPTX | [`workflows/edit-native-pptx.md`](workflows/edit-native-pptx.md) |

**Hard rule — MBLM brand lock**: never load McKinsey, BCG, Bain, Accenture, or
any other brand preset. `templates/brands/brands_index.json` lists **only**
`mblm`. Discovery cannot pick another brand because none are indexed. Always
apply the brand freeze below.

**Hard rule — selected authority only**: Do not load another top-level route's
procedure after routing. Supporting documents refine one route; they never
compete with it.

---

## HARD DESIGN FREEZE — v4.1.1 / v4.2.0 (always-on)

1. **Editable text**: one text object per paragraph (`TEXT_BOXES.md`); never
   `--no-merge`.
2. **Layout metrics**: `LAYOUT_METRICS.md`; scale **37.795 px/cm**.
3. **Margins**: **1.05 cm ≈ 39.7 px** all sides (practical **40 px**).
4. **Content-slide logo**: **88.4×44.2 @ 1148.2,39.7** on every content slide.
5. **Cover / divider / thank-you logo**: **138×69 @ 40,40**.
6. **Cover title**: **60pt or 72pt** Light (prefer **72**) — cover only.
7. **Cover subtitles**: **24pt or 32pt** (prefer **28–32**).
8. **Body**: **16pt or 20pt** Regular — lock one deck-wide; prefer **20pt**.
9. **Content-slide subtitle**: **18pt or 20pt**; **`#000000`**; under title.
10. **Content-slide titles** (incl. Agenda): Light **47pt only**; top edge at
    **1.05 cm**.
11. **No kickers** — deck-wide; zero tolerance.
12. **Supertext**: **≥150pt**; stroke **1.25pt**; edge-to-edge within margins.
13. **Omit tagline** "The Brand Intimacy Agency" when logo present; no bottom
    MBLM wordmark if logo already on slide.
14. **Bullets**: round **black** circles; diameter ≈ **80% of text size**.
15. **Kerning normal** — do not expand letter-spacing.
16. **White-only text on black fills** — never yellow/blue text on black.
17. **Gradient backgrounds** mainly for **section dividers**.
18. **Tables**: header only `#002A60` / `#000000` / `#808080`; chrome accents
    primary `#000000` `#FFFFFF` `#FFF200` only.
19. **No line-box stacks** — solid fills + paragraph text blocks.
20. **Agenda** from R2 (**r2_12** + **r2_40**); title size = **47pt**.
21. **Yellow lines forbidden** — `#FFF200` never as divider/accent lines.
22. **Lines above cards** — blue family only: `#002A60`, `#006AF1`, `#00AEFF`,
    `#0068EB`.

### Brand freeze tokens

| Token | Value |
|---|---|
| Canvas | 1280×720 (scale **37.795 px/cm**) |
| Margins | **1.05 cm ≈ 39.7 / 40 px** all sides |
| Primary | `#000000` `#FFFFFF` `#FFF200` + gray `#BFBFBF` |
| Blue line family | `#002A60` `#006AF1` `#00AEFF` `#0068EB` |
| Type | BentonSansCond — cover 60/72 Light; **content titles 47pt**; body 20 Regular |
| Content logo | **88.4×44.2 @ 1148.2,39.7** |
| Cover/divider/thanks logo | **138×69 @ 40,40** |
| Bullets | Round black circles Ø≈80% text |
| Brand workspace | `${SKILL_DIR}/templates/brands/mblm/` |
| Brand assets | `${SKILL_DIR}/assets/mblm/` |
| Brand references | `${SKILL_DIR}/references/mblm/` |

---

## Authored Expression Range

**Reference — not a constraint**: what a generated page can carry. Text — inline
emphasis runs, lead-in, pull quote, hero number, takeaway line (**kickers
forbidden under MBLM freeze**). Geometry — Office presets, Boolean merge,
connectors, freeform. Image — full-bleed field, editorial crop, shaped picture.
Paint — gradients (mainly section dividers), channel alpha, native shadow.
Recurrence — one cross-page motif varied by page role. Each form's syntax lives
in the selected runtime authority's construction references, constrained by the
MBLM brand freeze.

---

## Vocabulary

One meaning per term across every loaded file. Where a word is used in
more than one sense, the sense is named here and the files say which one.

| Term | Meaning |
|---|---|
| **Reference** (label) | A starting sketch the executing role adjusts or replaces freely, with no upstream repair or stated reason; `(binding)` after a field label removes that freedom |
| **MBLM brand freeze** | Always-on identity + geometry locks in this file / `MBLM_OVERLAY.md` / `references/mblm/` — not optional |
| **Brand workspace** | `${SKILL_DIR}/templates/brands/mblm/` only |
| **SKILL_DIR** | Absolute directory containing this `SKILL.md` |

Full upstream vocabulary for executor/strategist terms remains in
[`SKILL.upstream.md`](SKILL.upstream.md) and the `references/` engine docs.

---

## Global Discipline

1. Serial execution of the selected path.
2. Blocking gates only where the active runtime marks them `⛔ BLOCKING`.
3. Act at the owning layer on failure (page SVG vs source vs tool).
4. Match the user's language.
5. Keep MBLM identity consistent across every page (geometry signature + palette
   + line/type/margin/bullet/text-box rules).
6. Core Path A (Quick Generate → `svg_to_pptx`) does **not** call home; optional
   image/TTS backends may need network only when the user opts in.

---

## Asset map

```text
templates/brands/mblm/     # sole Brand workspace (design_spec + logos)
assets/mblm/               # logos, icons, layouts, palette, brand-intimacy
references/mblm/           # COLORS, TYPOGRAPHY, LAYOUT_METRICS, catalogs, …
workflows/generate-mblm-pptx.md
MBLM_OVERLAY.md            # condensed always-on freeze (reload if context drops)
SKILL.upstream.md          # unmodified upstream Skill entry (attribution archive)
```

## Out of scope

- Loading or inventing non-MBLM consulting brand presets
- Auto-running Create Template on a large official MBLM PPTX master
- Bypassing `attribution_guard.py` or stripping MIT attribution files
- Falling back to hand-rolled `python-pptx` when engine scripts are missing
