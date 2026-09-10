# mblm-ppt

Cursor/agent skill: generate **MBLM-branded** PowerPoint decks via the local **mblm-ppt** engine.

- Entry: [`SKILL.md`](SKILL.md) (**v4.1.1**)
- Workflow: [`workflows/generate-mblm-pptx.md`](workflows/generate-mblm-pptx.md)
- Brand rules: [`references/`](references/) — locked decisions in [`references/RESOLVED_DECISIONS.md`](references/RESOLVED_DECISIONS.md)
- **Persistent layout**: [`references/LAYOUT_METRICS.md`](references/LAYOUT_METRICS.md) (cm + px @ 37.795 px/cm)
- Visual refs: [`references/visual-references/CATALOG.md`](references/visual-references/CATALOG.md) + [`CATALOG_R2.md`](references/visual-references/CATALOG_R2.md) + [`LAYOUT_PATTERNS.md`](references/visual-references/LAYOUT_PATTERNS.md)
- Assets: [`assets/`](assets/)

**Provenance:** There is no Markdown brand manual inside the source `mblm assets` kit. Rules here were derived from SVGs, the brand-kit screenshot, layout compositions, official specs screenshots, R2 consulting examples, and user hard feedback (closed fact, 2026-09-10).

Engine path (do not move this skill into the mblm-ppt engine):

`${MBLM_MASTER_ROOT}/source/mblm-ppt-main/skills/mblm-ppt`

## v4.1.1 (2026-09-10 evening Asia/Dubai) — title/subtitle + chrome polish

- **Content title top edge** at **1.05 cm** (aligned with content logo top / top margin); subtitle directly under, left-aligned, **black `#000000`**.
- **Bullets**: diameter ≈ **80%** of adjacent body text size (was 50%).
- **Table headers**: only `#002A60` / `#000000` / `#808080`.
- **Graphics chrome**: primary `#000000` `#FFFFFF` `#FFF200` only (plus table-header tokens above).
- Scrubbed skill docs: no username absolute paths; `PATHS.md` defines `MBLM_MASTER_ROOT`.

## v4.1.0 (2026-09-10 evening Asia/Dubai) — persistent layout lock

- **Margins**: **1.05 cm ≈ 39.7 px** all sides (practical **40**).
- **Content logo**: **2.34×1.17 cm → 88.4×44.2 px** at **1148.2, 39.7** — identical on every content slide.
- **Cover / divider / thank-you logo**: **3.65×~1.825 cm → 138×69 px** at **40, 40** (left-aligned).
- **Content titles**: BentonSansCond Light **47pt only** (incl. Agenda “Content”); cover may still use 60–72.
- **Supertext**: **≥150pt**, stroke 1.25pt, edge-to-edge within margins.
- Scale documented: SVG 1280×720 ↔ PPT 33.867×19.05 cm → **37.795 px/cm** (`LAYOUT_METRICS.md`).
- Retains prior locks: single-paragraph text boxes; body 16–20; subtitles 18–20; no kickers; no yellow lines; blue-only card lines; white-on-black; gradients for dividers; black round bullets; normal kerning; no tagline/bottom MBLM with logo.

## v4.0.0 (2026-09-10 evening Asia/Dubai)

- Editable text: one text object per paragraph; corner logo ~70–80px; cover 60/72; agenda ≥72; content titles 28–36; body 16/20. **Geometry and title sizes superseded by v4.1.0.**

## v3.0.0 (2026-09-10 evening Asia/Dubai)

- Ingested **R2** examples; agenda gold standard r2_12 / r2_40; margins −30%; no kickers; Supertext 1.25pt; etc.

## v2.0.0 (2026-09-10 afternoon)

Design output driven by visual analysis of official specs screenshots plus hard rules (yellow lines forbidden; blue-only above cards; Benton weight locks). Superseded in part by v3/v4/v4.1 above.
