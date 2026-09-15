# STEP 3 — MBLM illustration + cinematic image skills

Integrates nested **metaphor illustration** and **cinematic photography** skills into `mblm-ppt-master` so the engine can generate/place textured metaphors and film stills alongside `mblm-r2` SVG templates and STEP 2 process diagrams.

STEP 2 `skills/mblm-diagram/` is unchanged.

## What was added

| Path | Purpose |
|---|---|
| `skills/mblm-illustration/SKILL.md` | Textured Metaphors skill (one accent) |
| `skills/mblm-illustration/PALETTE.md` | Accent hex table + never-mix |
| `skills/mblm-illustration/PROMPT_TEMPLATE.md` | Copy-paste image prompt |
| `skills/mblm-illustration/EXAMPLES.md` | Brand / marketing / web examples |
| `skills/mblm-cinematic/SKILL.md` | Cinematic Human Light skill |
| `skills/mblm-cinematic/PROMPT_TEMPLATE.md` | Copy-paste photo prompt |
| `skills/mblm-cinematic/CHECKLIST.md` | Fit / avoid lists |
| `references/mblm/IMAGES_GEN.md` | Chooser + placement + two-turn recipes |
| `templates/decks/mblm-r2/IMAGE_SLOTS.md` | Photo/illustration host pages |
| `scripts/mblm_illustration_prompt.py` | Stdlib CLI → illustration prompt |
| `scripts/mblm_cinematic_prompt.py` | Stdlib CLI → cinematic prompt |
| `assets/mblm/images/README.md` | Naming (`diagram_` / `illustration_` / `photo_`) |
| `docs/STEP3_MBLM_IMAGES.md` | This note |
| `docs/ALUMNI_PROMPTS_IMAGERY.md` | Prompt **C2** / **D2** + nested preference |

Also updated: `IMAGERY.md`, `DIAGRAMS.md` (cross-link), `DIAGRAM_SLOTS.md`, `SOURCE_MAP.md`, `workflows/generate-mblm-pptx.md`, `MBLM_OVERLAY.md`, `SKILL.md` freeze bullets 24–25.

## Local use

```bash
cd /workspace/mblm-ppt-master   # or your skill root

# Illustration prompt
python3 scripts/mblm_illustration_prompt.py \
  --topic "Brand system as a city" \
  --accent yellow \
  --background white \
  --action "tiny figures walk between typography blocks" \
  --shapes "towers, grids, arched portals"

# Cinematic prompt
python3 scripts/mblm_cinematic_prompt.py \
  --subject "two silhouettes" \
  --action "walking toward light" \
  --location "empty urban plaza at dusk" \
  --light "low sun" \
  --motion still \
  --face obscured

# Optional JSON fragments
python3 scripts/mblm_illustration_prompt.py --topic "Signal landscape" --accent magenta --write /tmp/illust.json
python3 scripts/mblm_cinematic_prompt.py --subject "hands at a window" --action "holding still" \
  --location "loft interior" --light window --motion still --face soft --write /tmp/photo.json
```

Place PNGs as:

* `images/illustration_<slug>.png` / `images/photo_<slug>.png`
* and `projects/_host_images/` when Alumni host images are used

§VIII: illustration → Type=Illustration, Crop=no-crop; cinematic → Type=Photography, Crop=adaptive (heroes).

## Alumni two-turn (recommended)

1. **Turn 1 — all visuals** using C2/D2/B2 turn-1 (or style refs). Save to `projects/_host_images/`.
2. **Turn 2 — deck only** with `mblm-ppt-master`: apply brand `mblm`, place PNGs, export.

Do **not** stack visual Skill Scripts with ppt Skill Script in one turn if Alumni returns 400 spawn errors.

## Role map

| Role | Skill |
|---|---|
| Cover / section / closing | cinematic |
| Abstract strategy metaphor | illustration (one accent) |
| Process / methodology | diagram (STEP 2) |
| Chrome / small marks | kit icons |

## Constraints

- Scripts **emit prompts only** — they do not call image APIs.
- Never mix illustration accents; never recolor diagrams.
- attribution_guard / brand apply unchanged.
- No username paths in docs.
- STEP 2 diagram files left intact.

## Lean zip

`mblm-ppt-master-step3-images.zip` — both skills + IMAGES_GEN.md + scripts + STEP3 doc + IMAGE_SLOTS + prompt doc updates.
