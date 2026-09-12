# Image Generation Prompt Template — mblm-diagram

Copy-paste into Image_Generator / Alumni image gen. Keep **monochrome** —
do not add MBLM accent colors (those belong to illustration skills, not diagrams).

```text
Create a single process diagram PNG matching the allumni / mblm-diagram monoline contract exactly.

CANVAS: [16:9 1280x720 for three-column | ~1100x280 content strip for horizontal flow, or 1280x720 with diagram centered under a blank title band]
BACKGROUND: pure white #ffffff
STROKE: black #000000 only, ~1–1.5pt, round linecaps and round linejoins
FILL: none on icons EXCEPT solid black social circles with white letterforms
NO: color, gradients, shadows, opacity, blur, decorative boxes around icons, body paragraphs inside the art

ICON RULES: detailed illustrative line icons (not blobs/silhouettes). Use only vocabulary from the mblm-diagram icon library. Each icon ~48–64px; groups of 2–4 on one baseline, ~8px apart.

ARCHETYPE: [Brand Implementation three-column Essence/Story/Experience | Inbound Marketing 5-step | Brand Video 5-step | Generic horizontal N-step]
TOPIC: [PROCESS NAME]
STEPS / SECTIONS:
[LIST LABELS + ICON CLUSTER NAMES FROM LIBRARY]

LAYOUT:
- Three-column: large light serif column titles (~48–56pt); section labels uppercase small-caps ~9pt medium gray; thin #cccccc rules; icon clusters under rules; generous whitespace; ~40px column gaps.
- Horizontal flow: 3–5 steps left-to-right; icon cluster above; uppercase small-caps label below; thin connector arrows (line + arrowhead) between steps.

OUTPUT: one clean PNG, labels only (no paragraph copy), centered composition with padding from edges.
```

## Short form (Alumni Prompt B style)

```text
Generate ONE process diagram PNG matching the allumni monoline contract exactly:
white background, black #000000 strokes ~1–1.5pt, round caps/joins, no color,
no fills except social circles, detailed icons (not simplified blobs).

Archetype: [Brand Implementation three-column Essence/Story/Experience | Inbound 5-step | Video 5-step | Custom horizontal N-step]
Topic: [YOUR PROCESS]
Sections / steps: [LIST]
```

## After generation

1. Save as `images/diagram_<slug>.png` (and `projects/_host_images/` when used).
2. §VIII row: Acquire Via=`ai` or `user`; Type=Illustration; Crop=no-crop; Purpose=process diagram.
3. Place on process/pillar/timeline hosts per `references/mblm/DIAGRAMS.md`.
