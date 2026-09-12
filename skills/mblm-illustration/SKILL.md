---
name: mblm-illustration
version: 1.0.0
aka: MBLM Illustration System
compatible: mblm-illustration@1.0
output: PNG via image generation
trigger: abstract strategy metaphors, textured brand landscapes, one-accent illustrations
---

# Skill: `mblm-illustration` — MBLM Illustration System: Textured Metaphors

**Version:** 1.0.0  
**Output:** PNG via image generation  
**Trigger:** Abstract corporate processes as physical landscapes; strategy / capability metaphors; brand-system scenes that need one MBLM accent

## Purpose

Turn abstract corporate processes into **physical landscapes** — tiny humans against huge structures — using risograph / halftone texture, architectural linework, and **exactly one** MBLM accent color on a stark foundation.

Handles: brand systems, digital marketing engines, web development stacks, capability metaphors, strategy “idea” slides where a diagram would be too literal.

Quick loads:

- `PALETTE.md` — accent hex table + never-mix rule
- `PROMPT_TEMPLATE.md` — copy-paste image prompt
- `EXAMPLES.md` — brand systems / digital marketing / web development
- Engine wiring: `${SKILL_DIR}/references/mblm/IMAGES_GEN.md` (parent package)

***

## The Style Contract (Read Before Every Generation)

Every output must match ALL of these rules.

### Metaphorical scale

* Tiny faceless human figures vs oversized geometric / architectural structures
* One clear metaphor per image — not a collage of competing ideas
* Actors are abstracted (no readable faces, no stock “business smile”)

### Color — palette lock

* Foundation: stark white `#FFFFFF` / paper gray / deep black (pick **one** background)
* Exactly **ONE** MBLM accent per image (never mix accents in one frame):

| Name | Hex |
|---|---|
| Yellow | `#FFF200` |
| Orange | `#FFBA00` |
| Magenta | `#EC008C` |
| Violet | `#9700DC` |
| Blue | `#006AF1` |
| Cyan | `#00AEFF` |
| Green | `#00D300` |

* No second accent. No rainbow. Grays / black / white for structure only.

### Texture & line

* Risograph / halftone / screen-print grain on accent fields
* Thin architectural linework (plan, elevation, scaffold, grid)
* Optional MBLM glyphs (circled marks, simple geometry) — sparse, not logos as product shots

### Composition

* Keep art **centered with padding** — do **not** go to edges / full bleed unless the slide role is cover or section divider
* Generous negative space; minimal clutter
* Prefer 16:9 canvas for deck wells

***

## Image Generation Prompt Template

Copy from `PROMPT_TEMPLATE.md`. CLI helper (parent package):

```bash
python3 scripts/mblm_illustration_prompt.py \
  --topic "Brand system as a city" \
  --accent yellow \
  --background white \
  --action "tiny figures walk between oversized typography blocks" \
  --shapes "towers, grids, arched portals"
```

***

## MBLM PPT Master integration

This skill ships nested under `mblm-ppt-master/skills/mblm-illustration/`. Engine placement rules live in `references/mblm/IMAGES_GEN.md` and `templates/decks/mblm-r2/IMAGE_SLOTS.md`.

### File destinations

1. After PNG generation, save to the active project as:
   - `<project_path>/images/illustration_<slug>.png`
2. When Alumni host-images are in use, also copy to:
   - `projects/_host_images/illustration_<slug>.png`

### §VIII / Quick image row pattern

| Field | Value |
|---|---|
| Acquire Via | `ai` (generate) or `user` (after PNG already on disk) |
| Type | Illustration |
| Crop | `no-crop` (default); `adaptive` for hero / section uses |
| Purpose | metaphor illustration |
| Filename | `illustration_<slug>.png` |

### Placement preference

* Content slides: centered figure in a light well — **not** edge-bleed (`page_role=local`)
* Cover / section: may use larger / adaptive crop (`page_role=hero_page`) with care for title contrast
* R2 / kit: `{{IMAGE}}` wells, editorial splits — see `IMAGE_SLOTS.md`
* Keep **40px** margins; content logo rules unchanged; do not collide with the **47pt** title band

### Alumni spawn safety (critical)

**NEVER** stack `mblm-illustration` with the `mblm-ppt-master` Skill Script in the
**same Alumni turn** if Alumni returns 400 spawn errors.

Use either:

1. **Two-turn recipe** — Turn 1: all visuals (illustration / cinematic / diagram) → `_host_images/`. Turn 2: `mblm-ppt-master` only, place existing PNGs, export.
2. **Single-agent recipe** — load this `SKILL.md` as an Image_Generator style reference when `Acquire Via=ai` and Purpose mentions metaphor / illustration / textured landscape; the ppt-master agent invokes prompts via the Image_Generator path without spawning a second skill script.
