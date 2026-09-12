# STEP 1 — MBLM R2 semantic SVG deck templates

Reusable consulting layout prototypes derived from the R2 example PNGs (`more-examples-r2/`).  
Registered deck id: **`mblm-r2`**. Diagram / image-gen skills are **not** wired yet (later steps).

## What was installed

| Path | Purpose |
| --- | --- |
| `templates/decks/mblm-r2/` | Registered deck pack (design_spec + 40 SVGs + logos + SOURCE_MAP) |
| `templates/decks/mblm-r2/templates/*.svg` | Semantic SVGs `01_r2_02_…` … `40_r2_41_…` |
| `templates/decks/mblm-r2/images/` | MBLM logo variants (copied from `templates/brands/mblm/images/`) |
| `templates/decks/mblm-r2/SOURCE_MAP.md` | SVG ↔ r2 id ↔ source PNG |
| `assets/mblm/layouts/r2/` | Symlinks to the same SVGs for authoring reference |
| `docs/STEP1_R2_SVG_TEMPLATES.md` | This note |

Gold standard (SVG catalog): **r2_40** section agenda on blue→navy gradient. *(r2_12 Content TOC SVG removed.)*

## Local use (this workspace)

```bash
cd /workspace/mblm-ppt-master
python3 scripts/register_template.py mblm-r2 --kind deck
# confirm
python3 -c "import json; print('mblm-r2' in json.load(open('templates/decks/decks_index.json')))"
```

Apply via the skill’s deck / `apply_template` flow with template id **`mblm-r2`**.  
Pick a page by file stem (e.g. `39_r2_40_section_agenda`) or by `data-pptx-layout` (e.g. `section_agenda`).

Authoring reference (open in browser / editor):

```bash
ls assets/mblm/layouts/r2/
```

Catalog authority: `references/mblm/visual-references/CATALOG_R2.md`.

## Alumni / package install

If you receive the lean add-on zip `mblm-ppt-master-step1-r2-svgs.zip`:

1. Unzip into an existing `mblm-ppt-master` (or Alumni skill) root so paths land as:
   - `templates/decks/mblm-r2/…`
   - `assets/mblm/layouts/r2/…`
   - `docs/STEP1_R2_SVG_TEMPLATES.md`
2. From the skill root run:
   ```bash
   python3 scripts/register_template.py mblm-r2 --kind deck
   ```
3. Verify `templates/decks/decks_index.json` contains `mblm-r2`.

If your Alumni tree already merged this pack into `/workspace/mblm-ppt-master`, skip the unzip and only re-register if the index is missing the entry.

**Note:** Symlinks under `assets/mblm/layouts/r2/` use `../../../../templates/decks/mblm-r2/templates/<file>`. On Windows without symlink support, re-copy the SVGs (the STEP 4 media-stack zip ships real copies).

## SVG contract (summary)

- Canvas `1280×720`; root `data-pptx-master="mblm_r2_master"`
- Flat geometry + `{{TOKEN}}` placeholders — not embedded PNG screenshots
- Light slides: logo top-right white-background lockup
- Dark section divider (r2_40): gradient master + dark logo top-left
- Titles: BentonSansCond / Arial Narrow Light **47pt**; round black bullets
- Photo wells: grey rect + `{{IMAGE}}` (image skill later)

## Out of scope (later steps)

- Diagram / chart generation skills → **STEP 2** (`docs/STEP2_MBLM_DIAGRAM.md`)
- Image-generation fill for photo wells
- Full client copy migration from screenshots
