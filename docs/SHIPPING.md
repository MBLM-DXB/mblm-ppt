# Shipping — MBLM PPT Master packages

## STEP 4 media stack add-on (preferred for chat / Alumni merge)

**File:** `/workspace/mblm-ppt-master-step4-media-stack.zip` (also ship beside the skill)

**Contains:**

- `templates/decks/mblm-r2/` (full deck: SVGs, images, SOURCE_MAP, IMAGE_SLOTS, DIAGRAM_SLOTS)
- `skills/mblm-diagram`, `mblm-illustration`, `mblm-cinematic`
- `assets/mblm/diagrams/`, `assets/mblm/layouts/r2/` (real files — symlinks materialized)
- `references/mblm/DIAGRAMS.md`, `IMAGES_GEN.md`, `LAYOUTS.md`
- `scripts/mblm_diagram_prompt.py`, `mblm_illustration_prompt.py`, `mblm_cinematic_prompt.py`
- `docs/STEP1`…`STEP4`, `ALUMNI_PROMPTS_IMAGERY.md`, `INSTALL_ALUMNI.md`, `CHANGELOG_MBLM.md`, `SHIPPING.md`

**Does not contain:** the full ~70MB+ engine (`scripts/` bulk, brand kit binaries, multi-MB `assets/mblm/layouts/MBLM_*.svg` illustrator dumps, node_modules, project outputs).

**Install:** unzip into an existing `mblm-ppt-master` skill root → register `mblm-r2` → run `attribution_guard`. See `INSTALL_ALUMNI.md`.

Target size: well under ~25MB (SVGs + markdown + small skills).

## Full engine

| Artifact | Role |
|---|---|
| `/workspace/mblm-ppt-master` | Live authoritative tree |
| `mblm-ppt-master-full-fixed.zip` | Prior full package (~70MB+) — engine + brand + paths fix |
| `mblm-ppt-master-full.zip` / `mblm-ppt-master.zip` | Earlier snapshots |

Do **not** rebuild the full engine zip for every media-stack change unless Alumni needs a single one-shot upload. Prefer step4 add-on + merge instructions.

## Step-specific lean zips (superseded by step4 for new installs)

- `mblm-ppt-master-step1-r2-svgs.zip`
- `mblm-ppt-master-step2-diagram.zip`
- `mblm-ppt-master-step3-images.zip`

Keep for incremental diffs; new Alumni installs should use **step4-media-stack**.

## Orchestration

Canonical flow + prompts: `docs/STEP4_INTEGRATION.md` + `docs/ALUMNI_PROMPTS_IMAGERY.md`.
