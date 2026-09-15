# STEP 2 — MBLM process diagram skill (`mblm-diagram`)

Integrates an Alumni-installable **monoline process diagram** skill into `mblm-ppt-master` so the engine can generate/place diagrams alongside `mblm-r2` SVG templates.

Photo / metaphor-illustration image-gen is **not** wired here (STEP 3).

## What was added

| Path | Purpose |
|---|---|
| `skills/mblm-diagram/SKILL.md` | Nested skill (v2.0.0), allumni-diagram compatible |
| `skills/mblm-diagram/references/ICON_LIBRARY.md` | Icon vocabulary table |
| `skills/mblm-diagram/references/ARCHETYPES.md` | Four process archetypes |
| `skills/mblm-diagram/PROMPT_TEMPLATE.md` | Copy-paste image prompt |
| `assets/mblm/diagrams/*.svg` | SVG-native fallbacks (no image API) |
| `references/mblm/DIAGRAMS.md` | Engine placement + two-turn / single-agent recipes |
| `templates/decks/mblm-r2/DIAGRAM_SLOTS.md` | Which r2 pages host diagrams |
| `scripts/mblm_diagram_prompt.py` | Stdlib CLI → full image-gen prompt |
| `docs/STEP2_MBLM_DIAGRAM.md` | This note |
| `docs/ALUMNI_PROMPTS_IMAGERY.md` | Prompt **B2** for nested skill |

Also updated: `IMAGERY.md`, `LAYOUTS.md`, `workflows/generate-mblm-pptx.md`, `MBLM_OVERLAY.md`, `SKILL.md` freeze bullet 23, `SOURCE_MAP.md` pointer.

## Local use

```bash
cd /workspace/mblm-ppt-master   # or your skill root

# Build an image-gen prompt
python3 scripts/mblm_diagram_prompt.py \
  --archetype inbound \
  --topic "Inbound engine" \
  --steps "Attract|Convert|Nurture|Close|Delight"

# Optional JSON fragment for §VIII / image_prompts
python3 scripts/mblm_diagram_prompt.py \
  --archetype brand-rollout --topic "Brand rollout" \
  --write /tmp/diagram_prompt.json

# SVG fallbacks (no API)
ls assets/mblm/diagrams/
# brand_rollout_essence_story_experience.svg
# inbound_marketing_5_step.svg (+ _1100x280)
# brand_video_production_5_step.svg (+ _1100x280)
# generic_process_5_step.svg  # {{STEP_1}}…{{STEP_5}}
```

Place PNG as `images/diagram_<slug>.png` (and `projects/_host_images/` when used).  
§VIII: Acquire Via=`ai`|`user`; Type=Illustration; Crop=no-crop; Purpose=process diagram.

Prefer hosts in `templates/decks/mblm-r2/DIAGRAM_SLOTS.md` or kit `MBLM_process` / `MBLM_process_timeline`.

## Alumni two-turn (recommended)

1. **Turn 1 — diagrams only** using Prompt B2 turn-1 (or standalone mblm-diagram). Save to `projects/_host_images/`.
2. **Turn 2 — deck only** with `mblm-ppt-master`: apply brand `mblm`, place PNGs, export.

Do **not** stack both Skill Scripts in one turn if Alumni returns 400 spawn errors.

## Connection to mblm-r2

R2 pages remain structural prototypes. Diagrams are **inserts** into large wells / process pages — they do not replace the deck pack. Native chevrons/timelines stay valid when you only need labeled geometry; use mblm-diagram when you need monoline icon art.

## Constraints

- Diagrams stay black/white monoline (no MBLM accent recolor).
- attribution_guard / brand apply unchanged.
- No username paths in docs.
- STEP 3 (illustration / cinematic) not started.

## Lean zip

`mblm-ppt-master-step2-diagram.zip` — skill pack + diagram SVGs + DIAGRAMS.md + STEP2 doc + prompt script (+ DIAGRAM_SLOTS).
