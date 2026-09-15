---
name: mblm-cinematic
version: 1.0.0
aka: Cinematic Human Light
compatible: mblm-cinematic@1.0
output: PNG via image generation
trigger: film-still photography for covers, sections, closing, atmospheric human scenes
---

# Skill: `mblm-cinematic` — Cinematic Human Light

**Version:** 1.0.0  
**Output:** PNG via image generation  
**Trigger:** Film-still photography for covers, section moods, closing, people / atmosphere slides

## Purpose

Generate **photographic film stills** for MBLM decks: cool blue-teal base plus **one** warm light source, backlight default, shallow depth of field, faces in profile or obscured — never flat frontal corporate headshots.

Quick loads:

- `PROMPT_TEMPLATE.md` — copy-paste image prompt
- `CHECKLIST.md` — fit / avoid lists
- Engine wiring: `${SKILL_DIR}/references/mblm/IMAGES_GEN.md` (parent package)

***

## The Style Contract (Read Before Every Generation)

### Light & color

* Cool blue-teal base grade across the frame
* Exactly **one** warm light source (low sun, neon, window, practical lamp)
* Backlight as default (rim / silhouette energy); avoid flat frontal key
* Haze / lens flare OK if subtle

### Optics & motion

* Shallow depth of field (subject separation, soft bokeh)
* Either intentional **motion blur** OR deliberate **stillness** — pick one per shot
* Negative space for title overlays on cover / section / closing

### Faces & people

* Faces in **profile**, soft focus, or **obscured** (silhouette, hands, partial)
* No smiling corporate headshots; no stock handshake tropes
* Human presence as atmosphere / intimacy — not LinkedIn portraiture

### Composition for decks

* **Cover / section / closing:** full-bleed OK; plan a dark overlay region for title contrast
* **Content slides:** prefer half-bleed or framed wells per MBLM layouts — not edge-to-edge photos under dense copy

***

## Image Generation Prompt Template

Copy from `PROMPT_TEMPLATE.md`. CLI helper (parent package):

```bash
python3 scripts/mblm_cinematic_prompt.py \
  --subject "two silhouettes" \
  --action "walking toward light" \
  --location "empty urban plaza at dusk" \
  --light "low sun" \
  --motion still \
  --face obscured
```

***

## MBLM PPT Master integration

This skill ships nested under `mblm-ppt-master/skills/mblm-cinematic/`. Engine placement rules live in `references/mblm/IMAGES_GEN.md` and `templates/decks/mblm-r2/IMAGE_SLOTS.md`.

### File destinations

1. After PNG generation, save to the active project as:
   - `<project_path>/images/photo_<slug>.png`
2. When Alumni host-images are in use, also copy to:
   - `projects/_host_images/photo_<slug>.png`

### §VIII / Quick image row pattern

| Field | Value |
|---|---|
| Acquire Via | `ai` (generate) or `user` (after PNG already on disk) |
| Type | Photography |
| Crop | `adaptive` often (heroes); framed wells may use meet / no-crop |
| Purpose | cinematic photo |
| Filename | `photo_<slug>.png` |

### Placement preference

* Cover / section / closing → `page_role=hero_page`, full-bleed + dark overlay for title contrast
* Content → half-bleed or photo wells (`r2_13`, `r2_17`, `title_picture`, `editorial_split`, hero layouts)
* Keep logo / margin / title-band freeze rules

### Alumni spawn safety (critical)

**NEVER** stack `mblm-cinematic` with the `mblm-ppt-master` Skill Script in the
**same Alumni turn** if Alumni returns 400 spawn errors.

Use either:

1. **Two-turn recipe** — Turn 1: all visuals → `_host_images/`. Turn 2: ppt-master only.
2. **Single-agent recipe** — load this `SKILL.md` as Image_Generator style reference when Purpose mentions cinematic / photography / cover hero / atmospheric still.
