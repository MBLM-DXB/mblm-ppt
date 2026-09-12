# MBLM Process Diagrams

Skill pack: `skills/mblm-diagram/` (allumni-diagram v2.0 compatible).  
SVG fallbacks: `assets/mblm/diagrams/`.  
Host slots: `templates/decks/mblm-r2/DIAGRAM_SLOTS.md`.
Photo / metaphor illustration (STEP 3): see `IMAGES_GEN.md` and `templates/decks/mblm-r2/IMAGE_SLOTS.md` — do not place cinematic photos on process diagram hosts, and do not recolor diagrams.

## When to use mblm-diagram vs native SVG shapes

| Need | Prefer |
|---|---|
| Methodology / phases / brand rollout / inbound / video pipeline as **illustration art** | **mblm-diagram** PNG (Image_Generator) or SVG from `assets/mblm/diagrams/` |
| Simple numbered steps already drawn in kit/r2 templates (blue nodes, chevrons, gantt) | **Native** template geometry — fill labels only |
| Ambition pillars / cards that are layout modules, not icon art | Native R2 pillars / cards |
| Recolored brand accents inside the process art | **Never** — diagrams stay black/white monoline |

Use mblm-diagram when the slide job is “show the process as monoline icon art.”  
Use native shapes when the R2 page already encodes the process structure.

## Mapping methodology / process / phase slides

1. Prefer a **centered content well** under the 47pt title band, or replace a body / `{{IMAGE}}` placeholder.
2. Good hosts:
   - Kit: `MBLM_process`, `MBLM_process_timeline`, wide `MBLM_title_content`
   - R2: process pillars, chevrons, timelines, phase pages — see `DIAGRAM_SLOTS.md`
3. Filenames: `diagram_<slug>.png` in project `images/`; also `projects/_host_images/` when Alumni host images are used.
4. §VIII / Quick row: `Acquire Via: ai` or `user`; Type = Illustration; Crop = no-crop; Purpose = process diagram.

## Color

Diagrams stay **black `#000000` / white `#ffffff` monoline**.  
Do **not** recolor strokes or fills with MBLM yellow, blue family, magenta, etc. Social circles may be solid black with white letterforms only.

## Placement metrics

- Margins: **40 px** (1.05 cm) all sides — unchanged.
- Content logo: **88.4×44.2 @ 1148.2,39.7** — unchanged.
- Title band: BentonSansCond Light **47pt** at top (top edge ~1.05 cm). Diagram must **not** collide with title or logo.
- Keep ~24–32 px gap under subtitle before the diagram well.
- Prefer `crop=no-crop` / `meet` so the full diagram remains visible.

## Alumni two-turn recipe (diagrams first → ppt second)

**Turn 1 — diagrams only**

```text
Use only mblm-diagram (or load skills/mblm-diagram/SKILL.md).
Generate PNGs for [process slides]. Save to projects/_host_images as diagram_<slug>.png.
Do not run mblm-ppt-master in this turn.
```

**Turn 2 — deck only**

```text
Use only mblm-ppt-master.
Init project, apply brand mblm, place existing PNGs from projects/_host_images,
prefer R2/kit process hosts. Export PPTX.
Do not load diagram skills in this turn.
```

## Single-agent recipe (Image_Generator path)

When running inside mblm-ppt-master Quick / Default:

1. Load `skills/mblm-diagram/SKILL.md` (+ `PROMPT_TEMPLATE.md`) as the Image_Generator **style reference**.
2. For each process/methodology/phases image: `Acquire Via=ai`, Type=Illustration, Crop=no-crop, Purpose=process diagram.
3. Build prompts via `scripts/mblm_diagram_prompt.py` or `PROMPT_TEMPLATE.md`.
4. If image gen fails, place SVG from `assets/mblm/diagrams/` instead.

**Never** stack the mblm-diagram Alumni Skill Script with mblm-ppt-master Skill Script in one turn if Alumni returns 400 spawn errors — use two-turn or this single-agent path.

## Prompt helper

```bash
python3 scripts/mblm_diagram_prompt.py --archetype inbound --topic "Inbound engine" --steps "Attract|Convert|Nurture|Close|Delight"
python3 scripts/mblm_diagram_prompt.py --archetype brand-rollout --topic "Brand rollout" --write image_prompts.fragment.json
```
