# Generate MBLM-Branded PPTX

MBLM-locked recipe on top of mblm-ppt's Generate engine. Default path is **Quick Generate** with MBLM brand constraints pre-applied (no free-design color exploration). Use **Default Generate** only when the user explicitly wants Strategist confirmation UI.

Locked brand decisions: `${SKILL_DIR}/references/RESOLVED_DECISIONS.md` (includes **v4.1.1** persistent layout lock + R2 catalog). See also `LAYOUT_METRICS.md`.

## Prerequisites

1. Read `${SKILL_DIR}/SKILL.md` and `${SKILL_DIR}/references/PATHS.md`.
2. Set:
   - `SKILL_DIR` = this skill's absolute path
   - `MBLM_MASTER_ROOT` = parent of `skill/` + `source/` (resolve at runtime)
   - `PPT_MASTER_SKILL` = `${MBLM_MASTER_ROOT}/source/mblm-ppt-main/skills/mblm-ppt`
3. Run mblm-ppt integrity gate once per session:
   ```bash
   python3 "${PPT_MASTER_SKILL}/scripts/attribution_guard.py"
   ```
   Non-zero → stop; do not bypass.

---

## Path A — Quick Generate (default)

Uses **skill brand assets** + mblm-ppt engine (not the official ~70MB PPTX).

Follow mblm-ppt Quick profile at
`${MBLM_MASTER_ROOT}/source/mblm-ppt-main/skills/mblm-ppt/workflows/profiles/quick-generate.md`
with these MBLM bindings:

### A0. Visual reference pass (MANDATORY — before brand freeze / project init / SVG authoring)

1. Read `${SKILL_DIR}/references/visual-references/CATALOG.md`.
2. Read `${SKILL_DIR}/references/visual-references/CATALOG_R2.md`.
3. Read `${SKILL_DIR}/references/visual-references/LAYOUT_PATTERNS.md`.
4. Inspect relevant PNGs under:
   - `${MBLM_MASTER_ROOT}/skill/_spec_screens_ascii/`
   - `${MBLM_MASTER_ROOT}/skill/_examples_r2_ascii/` (and/or originals under `more examples r2/` / `MBLM slides and other specs/` if newer)
5. For agenda/list slides, explicitly adapt **r2_12** (Content TOC) and/or **r2_40** (section agenda).
6. Briefly note which patterns (A–S) the deck will adapt. Do **not** invent McKinsey-style layouts.

### A0b. Brand freeze (incl. line + type + text-box + margin + bullet hard rules)

Lock these without asking (unless User overrides):

| Decision | MBLM default |
|---|---|
| Canvas | 1280×720 (`--format` only if mblm-ppt registers an exact match; else author viewBox `0 0 1280 720`); scale **37.795 px/cm** vs 33.867×19.05 cm |
| **Layout metrics** | `references/LAYOUT_METRICS.md` — cm + px locks for margins / logos / titles |
| **Margins** | **1.05 cm ≈ 39.7 px** all sides (practical **40**) — `references/MARGINS.md` |
| Primary colors | `#000000`, `#FFFFFF`, `#FFF200`, gray `#BFBFBF` |
| Neutrals / secondary | Full tables in `references/COLORS.md` |
| **Lines** | `references/LINE_RULES.md` — **no yellow lines**; lines above cards = `#002A60` / `#006AF1` / `#00AEFF` / `#0068EB` only; **white-only text on black fills** |
| Gradients | Soft mesh ≥3 for **section dividers** / covers; **not** full-bleed on ordinary content slides |
| **Type** | BentonSansCond per `TYPOGRAPHY.md` v4.1.1: cover **60/72** Light; content titles **47pt only** (incl. agenda) with **top edge at 1.05 cm**; content subtitle **18/20** **`#000000`** under title; body **16 or 20** locked (**prefer 20**); Bold accents <24; Medium topics; Black Supertext **≥150pt** stroke **1.25pt**; **no kickers**; **normal kerning** |
| **Text boxes** | One `<text>` per paragraph; wrap with `<tspan dy>`; never per-line sibling `<text>`s — `TEXT_BOXES.md`. **Never** pass `--no-merge` to `svg_to_pptx`. |
| **Bullets** | Round **black** circles, Ø≈80% text — `BULLETS.md` |
| Logo | Content: **88.4×44.2 @ 1148.2,39.7**; cover/divider/thanks: **138×69 @ 40,40** (`LOGOS.md`); **no tagline / no bottom MBLM wordmark** when logo present; brand-color = `MBLM_LOGO_Brand color.svg` |
| Icons | Prefer `assets/icons/` (`ICONS.md`); always quote `MBLM_ UI-UX Design.svg` |
| Layout spine | `LAYOUTS.md` + `LAYOUT_PATTERNS.md` + `CATALOG_R2.md` (agenda J/K; R2 L–S) |
| Imagery | `IMAGERY.md` + composition specs |
| Tables | Header **only** `#002A60` / `#000000` / `#808080`; white/contrast text; normal kerning. Chrome/bars/accents: primary `#000000` `#FFFFFF` `#FFF200` only |
| UI construction | Solid fills + paragraph blocks — **no line-box stacks** |

Do **not** load competing engine brand presets (McKinsey, BCG, etc.) for an MBLM deck.

### A1. Sources

| User provides | Action |
|---|---|
| Files / URLs | `python3 "${PPT_MASTER_SKILL}/scripts/source_to_md.py" <inputs...>` |
| Markdown / chat brief | Read directly |
| Topic only | Run mblm-ppt topic-research stage, then import the research pair |

### A2. Init project

```bash
python3 "${PPT_MASTER_SKILL}/scripts/project_manager.py" init <project_name> --quick-generate
python3 "${PPT_MASTER_SKILL}/scripts/project_manager.py" import-sources <project_path> <sources...>
```

Retain the printed absolute `<project_path>` (under `${PPT_MASTER_ROOT}/projects/`).

### A3. Install MBLM brand into the project

```bash
mkdir -p "<project_path>/images" "<project_path>/icons"
cp "${SKILL_DIR}/assets/logos/"*.svg "<project_path>/images/"
cp "${SKILL_DIR}/assets/icons/"*.svg "<project_path>/icons/"
```

Write optional `<project_path>/mblm_brand_lock.md` pointing at LAYOUT_METRICS, COLORS, LINE_RULES, TYPOGRAPHY, TEXT_BOXES, MARGINS, BULLETS, LOGOS, and chosen layout patterns (include J/K for agenda).

### A4. Plan roster in context (no design_spec.md in Quick)

Decide page list using MBLM layouts + visual patterns, e.g.:

1. `title_slide` — yellow or black cover (Pattern A)  
2. Agenda — **Pattern J (r2_12)** and/or **K (r2_40)**; or pillars H/I  
3. `section_header` or 2:1 / photo+bar — chapter (Patterns B–C / K)  
4. Content — R2 patterns L–S / `process` / `kpi_dashboard` / `chart_insight` / `table_summary` / picture layouts (blue-only card lines; round black bullets)  
5. `hero_statement` — Supertext / intimacy quote (Pattern E; stroke 1.25pt)  
6. `closing` — thank you / Supertext (Pattern A)

### A5. Author SVGs

Hand-author `<project_path>/svg_output/P01.svg` … following mblm-ppt executor / shared-standards **and** MBLM brand references. For each page:

- Adapt a pattern from `LAYOUT_PATTERNS.md` / CATALOG / CATALOG_R2 (composition, not placeholder copy).
- Apply logo rule from `LOGOS.md` / `LAYOUT_METRICS.md` (content 88.4×44.2 @ 1148.2,39.7; cover/divider/thanks 138×69 @ 40,40; no tagline / no bottom wordmark with logo).
- Use only palette tokens from `COLORS.md`.
- Enforce `LINE_RULES.md` + `TYPOGRAPHY.md` + `TEXT_BOXES.md` + `MARGINS.md` + `BULLETS.md`.
- Prefer kit icons from `icons/`.
- No kickers; content titles **47pt**; Supertext **≥150**; normal kerning; solid fills not line-box stacks; **one text object per paragraph**.

Load:

- `${PPT_MASTER_SKILL}/references/executor-base.md`
- `${PPT_MASTER_SKILL}/references/shared-standards-core.md`

### A6. Quality check + export

```bash
python3 "${PPT_MASTER_SKILL}/scripts/svg_quality_checker.py" "<project_path>" --canonical-authoring --stage final --quick-generate --json
python3 "${PPT_MASTER_SKILL}/scripts/svg_to_pptx.py" "<project_path>" --quick-generate
```

Do **not** pass `--no-merge` (that splits every visual line into its own text frame — violates `TEXT_BOXES.md`).

(Use exact flags from the installed mblm-ppt Quick profile if they differ slightly — the profile file wins for exporter flags, except never add `--no-merge` for MBLM.)

Deliver the PPTX path from the exporter output.

---

## Path B — Default Generate (confirmation UI)

Only when the user asks for full Strategist / Confirm UI. Same brand-asset policy as Path A (skill assets + mblm-ppt; **not** Create Template on the official PPTX).

1. Run **A0 + A0b** (visual reference pass + brand freeze) first.
2. Follow `${PPT_MASTER_SKILL}/workflows/generate-pptx.md` Steps 1–7.
3. At Stage 1, force MBLM branding with LINE + TYPE + TEXT_BOX + MARGIN + BULLET hard rules as non-negotiable.
4. Prefer installing colors/logos/icons from `${SKILL_DIR}/assets/` before Stage 2.
5. Do not select a different firm's brand preset.

---

## Path C — Edit Native from official MBLM PPTX

**Closed policy:** Do **not** auto-run Create Template on the ~70MB official file. Path C = Edit Native only.

When the user wants to fill/edit the official template, use the source PPTX or the skill symlink `${SKILL_DIR}/assets/template/MBLM_PowerPoint_v1.pptx`:

```bash
python3 "${PPT_MASTER_SKILL}/scripts/pptx_to_svg.py" \
  "${MBLM_MASTER_ROOT}/source/mblm assets/template/MBLM_Power point _v1.pptx" \
  -o "<project_slug>_mblm_native" \
  --inheritance-mode both --roundtrip
```

Then follow mblm-ppt `edit-native-pptx.md`: change only planned pages; export via roundtrip. Warn that the source PPTX is very large (~70MB). Still apply v4.1 LAYOUT_METRICS + LINE + TYPE + TEXT_BOX + MARGIN + BULLET hard rules on authored content.

---

## Done criteria

- Visual reference pass completed (specs **+ R2**) before authoring
- Agenda (if any) mimics r2_12 and/or r2_40; agenda title **47pt** (content slide)
- Every page uses MBLM palette + Benton v4.1 sizes (cover 60/72; body 20; **content titles 47pt**; Supertext ≥150)
- One text object per paragraph; no `--no-merge`
- Content logo **88.4×44.2 @ 1148.2,39.7** on every content slide; cover/divider/thanks **138×69 @ 40,40**
- Margins **1.05 cm / ≈40 px** all sides; no kickers; normal kerning
- Round black bullets; no yellow divider lines; blue-only lines above cards
- White-only text on black fills; no tagline/bottom wordmark with logo
- Gradients reserved for section dividers / covers — not ordinary content full-bleeds
- No line-box stacks; tables per Rule 11
- Logo lockup matches background (`Brand color` SVG for yellow fields)
- Spot-check **every** SVG for locked logo coords + content title 47pt before export
- Layout rhythm recognizable from specs + R2 catalogs (not consulting presets)
- PPTX exported via mblm-ppt scripts
- No competing brand system mixed in
- Official PPTX untouched except intentional Path C Edit Native
- mblm-ppt-main unmodified
