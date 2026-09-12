# MBLM overlay changelog

Versions refer to the MBLM specialization overlay on upstream ppt-master (`SKILL.md` metadata `version`), not necessarily upstream patch numbers.

## 2026-09-12 — `6.3.2-mblm.3` (deck planner + type freeze)

### Added

- Nested Alumni skill **`skills/mblm-deck-planner/`** — plan-only slide maps for handoff to `mblm-ppt-master` (`SKILL.md`, `PROMPT_ALUMNI.md`, `references/LAYOUT_PICKER.md`, `OUTPUT_SCHEMA.md`).
- Alumni **Turn 0** orchestration in `docs/STEP4_INTEGRATION.md`, `ALUMNI_PROMPTS_IMAGERY.md`, `INSTALL_ALUMNI.md`.

### Changed

- **Type freeze v4.2.1**: content titles **Light 40pt** (SVG **53.3**); body **Regular 16–18** min; **Medium / MediumSC banned** (use Bold); agenda section labels **50pt** Light on r2_40.
- Agenda gold = **`39_r2_40_section_agenda` only**; **`11_r2_12_content_toc` removed** (templates + broken `layouts/r2` symlink).
- Docs aligned: `SKILL.md`, `MBLM_OVERLAY.md`, `TYPOGRAPHY.md`, `RESOLVED_DECISIONS.md`, `LAYOUT_METRICS.md`, `LAYOUTS.md`, `brand_spec.md`, r2 `design_spec.md`.
- SVG sweep: Medium→Bold / weight 600→700; unscaled body &lt;16 bumped where clearly body; locked slides 12/14/39/21 geometry preserved.

### Notes

- PPTX font-size gate reminder: author SVG `font-size` as `desired_pt / 0.75` when using exporter scale.

## 2026-09-11 — `6.3.2-mblm.2` (Steps 1–4 media stack)

Final integration of the MBLM media + r2 template stack.

### Added

- **STEP 1** — Deck `templates/decks/mblm-r2/` (40 semantic SVGs), `SOURCE_MAP.md`, `assets/mblm/layouts/r2/`, `docs/STEP1_R2_SVG_TEMPLATES.md`.
- **STEP 2** — Nested `skills/mblm-diagram/`, `assets/mblm/diagrams/`, `references/mblm/DIAGRAMS.md`, `DIAGRAM_SLOTS.md`, `scripts/mblm_diagram_prompt.py`, `docs/STEP2_MBLM_DIAGRAM.md`.
- **STEP 3** — Nested `skills/mblm-illustration/`, `skills/mblm-cinematic/`, `references/mblm/IMAGES_GEN.md`, `IMAGE_SLOTS.md`, `scripts/mblm_illustration_prompt.py`, `scripts/mblm_cinematic_prompt.py`, `docs/STEP3_MBLM_IMAGES.md`.
- **STEP 4** — `docs/STEP4_INTEGRATION.md` (orchestration authority), Alumni Prompt **MASTER** (two-turn) + **LOCAL** (single-agent), `docs/INSTALL_ALUMNI.md`, `docs/SHIPPING.md`, lean zip `mblm-ppt-master-step4-media-stack.zip`.

### Changed

- `docs/ALUMNI_PROMPTS_IMAGERY.md` — MASTER / LOCAL prompts; STEP4 as canonical.
- `README.md` — MBLM media stack section linking STEP1–4.
- `SKILL.md` / `MBLM_OVERLAY.md` — pointer to STEP4 as media orchestration authority; version → `6.3.2-mblm.2`.

### Notes

- Alumni default remains **two-turn** (visuals → `_host_images`, then ppt alone) to avoid 400 spawn.
- Step4 zip materializes `layouts/r2` SVGs (no symlinks) and excludes multi-MB kit layout binaries under `assets/mblm/layouts/*.svg`.

## Earlier

- `6.3.2-mblm.1` — MBLM-only brand freeze package baseline (full-fixed zip era).

## 2026-09-12 — PPTX font size gate
- Added `scripts/pptx_font_size_gate.py` (audits DrawingML `a:rPr sz`, not SVG attrs).
- Author SVG `font-size` as `desired_pt / 0.75` (47→62.7, 18→24, 40→53.3).
- PresentationOS photo-editorial v3 regenerated with corrected sizes.
