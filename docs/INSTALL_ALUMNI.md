# Install — Alumni / local (MBLM media stack)

## Prerequisites

1. An existing **mblm-ppt-master** skill root (flat layout: `SKILL.md`, `scripts/`, `templates/brands/mblm/` at the root).
2. Python deps: `pip install -r requirements.txt` (**PyYAML** required for brand `design_spec.md`).
3. Do **not** skip `apply_template` for brand `mblm`.

If `project_manager.py init` errors with `Permission denied: '/projects'`, you have an unpatched nested-layout `paths.py` — use the full-fixed package’s `scripts/project_management/paths.py`.

## Media stack add-on (STEP 4 zip)

Zip: `mblm-ppt-master-step4-media-stack.zip`  
Purpose: merge Steps 1–4 (r2 deck + diagram/illustration/cinematic skills + docs) into an existing install.  
**Not** a full engine replacement — see `docs/SHIPPING.md`.

### Merge

```bash
# From the directory that contains your skill folder:
SKILL_ROOT="/path/to/mblm-ppt-master"
ZIP="/path/to/mblm-ppt-master-step4-media-stack.zip"

unzip -o "$ZIP" -d "$SKILL_ROOT"
# Zip entries are rooted at the skill paths (templates/, skills/, …).
# If the archive has a single top folder, unzip then:
#   cp -a /tmp/extracted/{templates,skills,assets,references,scripts,docs} "$SKILL_ROOT/"

cd "$SKILL_ROOT"
python3 scripts/register_template.py mblm-r2 --kind deck
python3 -c "import json; assert 'mblm-r2' in json.load(open('templates/decks/decks_index.json'))"
python3 scripts/attribution_guard.py
```

### Expected tree after merge

```text
skills/mblm-deck-planner/   # Turn 0 plan-only Alumni skill
skills/mblm-diagram/
skills/mblm-illustration/
skills/mblm-cinematic/
templates/decks/mblm-r2/          # 40 SVGs + SOURCE_MAP / IMAGE_SLOTS / DIAGRAM_SLOTS
assets/mblm/diagrams/
assets/mblm/layouts/r2/          # materialized SVGs (not symlinks in the zip)
references/mblm/DIAGRAMS.md
references/mblm/IMAGES_GEN.md
references/mblm/LAYOUTS.md
scripts/mblm_diagram_prompt.py
scripts/mblm_illustration_prompt.py
scripts/mblm_cinematic_prompt.py
docs/STEP1_R2_SVG_TEMPLATES.md
docs/STEP2_MBLM_DIAGRAM.md
docs/STEP3_MBLM_IMAGES.md
docs/STEP4_INTEGRATION.md
docs/ALUMNI_PROMPTS_IMAGERY.md
docs/INSTALL_ALUMNI.md
docs/CHANGELOG_MBLM.md
docs/SHIPPING.md
```

### Windows note

Earlier step1 packs used symlinks under `assets/mblm/layouts/r2/`. The STEP 4 zip **copies real SVG files** into that folder so Windows unzip works without Developer Mode.

## Nested planner skill

Ensure `skills/mblm-deck-planner/` is present (SKILL.md + `references/LAYOUT_PICKER.md` +
`OUTPUT_SCHEMA.md` + `PROMPT_ALUMNI.md`). Alumni should load it as a **nested skill**
alongside diagram/illustration/cinematic — plan first, then media stack.

## After install — run a deck

Canonical flow: [`docs/STEP4_INTEGRATION.md`](STEP4_INTEGRATION.md).

- **Alumni default:** Turn 0 `mblm-deck-planner` → Turn 1 visuals → Turn 2 ppt (Prompt **MASTER** in `ALUMNI_PROMPTS_IMAGERY.md`).
- **Local / single agent:** Prompt **LOCAL** (engine owns Image_Generator).

```bash
python3 scripts/attribution_guard.py
python3 scripts/project_manager.py init my-deck --quick-generate
# retain <project_path>
python3 scripts/apply_template.py <project_path> --root templates/brands/mblm
# author svg_output from mblm-r2; place images from projects/_host_images
python3 scripts/svg_quality_checker.py <project_path> --quick-generate
python3 scripts/svg_to_pptx.py <project_path> --quick-generate
```

## Full package vs add-on

| Artifact | What it is |
|---|---|
| `mblm-ppt-master-full-fixed.zip` (~70MB+) | Full engine + brand + this stack (when rebuilt) |
| `mblm-ppt-master-step4-media-stack.zip` | Lean add-on: templates + nested skills + refs + prompt CLIs + docs |
| Workspace `/workspace/mblm-ppt-master` | Authoritative live tree for development |

Prefer merging the step4 zip into an existing skill root over rebuilding the full engine zip unless you need a single one-shot Alumni upload of everything.
