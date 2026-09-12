# Image Generation Prompt Template — mblm-illustration

Copy-paste into Image_Generator / Alumni image gen. Lock **one** accent from `PALETTE.md`.

```text
Create a single 16:9 PNG illustration in the MBLM Illustration System: Textured Metaphors style.

SUBJECT / TOPIC: [TOPIC]
METAPHOR ACTION: [what tiny humans / elements are doing]
KEY SHAPES: [oversized structures — towers, grids, portals, stacks, landscapes]

SCALE: tiny faceless abstracted human figures against huge architectural / geometric structures
BACKGROUND: [stark white #FFFFFF | paper gray | deep charcoal] — solid foundation, not a photo
ACCENT: exactly ONE color [Yellow #FFF200 | Orange #FFBA00 | Magenta #EC008C | Violet #9700DC | Blue #006AF1 | Cyan #00AEFF | Green #00D300] — never mix accents
TEXTURE: risograph / halftone / screen-print grain on accent fields; thin architectural linework in black or dark gray
ACTORS: faceless, abstracted — no readable faces, no corporate headshots
OPTIONAL: sparse MBLM-style glyphs or circled marks — not a logo product shot

COMPOSITION: art centered with generous padding from edges — NOT full bleed (unless cover/section hero)
NO: second accent colors, rainbow gradients, cluttered icon soup, photoreal office stock, text paragraphs inside the art

OUTPUT: one clean PNG, metaphorical and minimal, suitable for an MBLM content-slide image well.
```

## Short form (Alumni Prompt C style)

```text
Create one 16:9 PNG illustration:
- Tiny faceless figures + oversized geometric metaphor for: [TOPIC]
- Background stark white (or paper gray / charcoal — pick one)
- Exactly ONE accent: [Yellow #FFF200 | Orange #FFBA00 | Magenta #EC008C | Violet #9700DC | Blue #006AF1 | Cyan #00AEFF | Green #00D300]
- Risograph/halftone texture, thin architectural linework
- Keep art centered with padding — do not go to edges
- Minimal; no random clutter
```

## After generation

1. Save as `images/illustration_<slug>.png` (and `projects/_host_images/` when used).
2. §VIII row: Acquire Via=`ai` or `user`; Type=Illustration; Crop=`no-crop` (or `adaptive` for heroes); Purpose=metaphor illustration.
3. Place per `references/mblm/IMAGES_GEN.md` / `IMAGE_SLOTS.md`.
