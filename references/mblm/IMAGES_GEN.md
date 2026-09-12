# MBLM Image Generation — Illustration, Cinematic, Diagram, Icons

Nested skills:

| Skill | Path | Filename prefix |
|---|---|---|
| Metaphor illustration | `skills/mblm-illustration/` | `illustration_<slug>.png` |
| Cinematic photo | `skills/mblm-cinematic/` | `photo_<slug>.png` |
| Process diagram | `skills/mblm-diagram/` | `diagram_<slug>.png` |
| Kit icons | `assets/mblm/icons/` | SVG icons in layouts (not AI art) |

Also: `templates/decks/mblm-r2/IMAGE_SLOTS.md` (photo/illustration hosts), `DIAGRAM_SLOTS.md` (process hosts).

## When to use which

| Need | Prefer |
|---|---|
| Cover / section / closing atmosphere, human light, film still | **mblm-cinematic** |
| Abstract strategy / capability metaphor, textured landscape, one accent | **mblm-illustration** |
| Process / methodology / phases as monoline icon art | **mblm-diagram** |
| Small UI chrome, bullets, layout ornaments | **Kit icons** (SVG) — not AI generation |
| Simple numbered steps already in r2/kit geometry | Native template shapes — fill labels only |

## Slide role mapping

| Slide role | Visual mode |
|---|---|
| Cover / section / closing | **Cinematic** (full-bleed + dark overlay for title contrast) |
| Abstract strategy / idea / capability metaphor | **Illustration** (one accent; centered with padding) |
| Process / methodology / phases | **Diagram** (black/white monoline) |
| Agenda / dense tables / matrices | Typography-led — avoid large AI art |

Do **not** mix illustration accents in one PNG. Do **not** recolor diagrams with MBLM accents.

## Placement into mblm-r2 / kit

* Photo / illustration wells: `{{IMAGE}}` placeholders and photo layouts — `r2_13` (industry inflection photo), `r2_17` (solution gallery), kit `title_picture`, `editorial_split`, hero / 2:1 photo+bar patterns.
* Process diagrams: see `DIAGRAM_SLOTS.md` / `DIAGRAMS.md`.
* Content illustrations: large centered well under 47pt title; **40px** margins; logo lock unchanged; prefer `crop=no-crop` for illustrations, `adaptive` for cinematic heroes.
* Full-bleed photos only on cover / section / closing unless brief says otherwise.

## Destinations & §VIII

| Mode | File | Acquire Via | Type | Crop | Purpose |
|---|---|---|---|---|---|
| Illustration | `images/illustration_<slug>.png` (+ `_host_images/`) | `ai` or `user` | Illustration | no-crop (adaptive for heroes) | metaphor illustration |
| Cinematic | `images/photo_<slug>.png` (+ `_host_images/`) | `ai` or `user` | Photography | adaptive often | cinematic photo |
| Diagram | `images/diagram_<slug>.png` (+ `_host_images/`) | `ai` or `user` | Illustration | no-crop | process diagram |

## Alumni two-turn recipe (all visuals first → ppt alone)

**Turn 1 — visuals only**

```text
Load nested skills as style refs (do not stack ppt Skill Script if 400 errors):
  skills/mblm-illustration/SKILL.md
  skills/mblm-cinematic/SKILL.md
  skills/mblm-diagram/SKILL.md (if process art needed)
Generate PNGs → projects/_host_images/ with illustration_ / photo_ / diagram_ prefixes.
Do not export PPTX in this turn.
```

**Turn 2 — deck only**

```text
Use only mblm-ppt-master.
Init project, apply brand mblm, place existing PNGs into IMAGE_SLOTS / DIAGRAM_SLOTS hosts.
Export PPTX. Do not spawn visual Skill Scripts in this turn.
```

## Single-agent recipe (Image_Generator)

When running inside mblm-ppt-master Quick / Default:

1. Load the matching nested `SKILL.md` (+ prompt template) as Image_Generator **style reference**.
2. Or emit prompts via:
   - `scripts/mblm_illustration_prompt.py`
   - `scripts/mblm_cinematic_prompt.py`
   - `scripts/mblm_diagram_prompt.py`
3. Scripts **only emit prompts** — they do not call image APIs.
4. Set §VIII rows per table above; place into r2/kit wells.

**Never** stack visual Alumni Skill Scripts with mblm-ppt-master Skill Script in one turn if Alumni returns 400 spawn errors — use two-turn or this single-agent path.

## Hard constraints

* Never mix two illustration accents in one image.
* Never recolor monoline diagrams.
* Do not invent connectors or claim these prompt scripts run image APIs.
* attribution_guard / brand apply unchanged.
