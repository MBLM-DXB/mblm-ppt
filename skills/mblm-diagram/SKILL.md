---
name: mblm-diagram
version: 2.0.0
aka: allumni-diagram
compatible: allumni-diagram@2.0
output: PNG via image generation; SVG-native fallbacks in assets/mblm/diagrams/
trigger: process, methodology, or phase-based workflow diagrams
---

# Skill: `mblm-diagram` (allumni-diagram compatible)

**Version:** 2.0.0  
**Output:** PNG via image generation **or** SVG-native diagrams from `${SKILL_DIR}/assets/mblm/diagrams/` when image gen is unavailable  
**Trigger:** Any prompt describing a process, methodology, or phase-based workflow

## Purpose

Generate process and methodology diagrams that match the allumni monoline
illustration system. Primary output is a single PNG: white background, black
line-art icons grouped into labeled sections, no color, no decorative fills,
no body text paragraphs inside the diagram (labels and section titles only).

Handles: brand rollouts, inbound marketing, video production, campaign
planning, website builds, any sequential or phase-based process.

When Alumni / Image_Generator cannot produce a PNG, place or inline an SVG
from `assets/mblm/diagrams/` (or copy icons into page SVGs). Keep the same
monoline contract.

Quick loads:

- `references/ICON_LIBRARY.md` — icon vocabulary
- `references/ARCHETYPES.md` — four process archetypes + icon clusters
- `PROMPT_TEMPLATE.md` — copy-paste image prompt
- Engine wiring: `${SKILL_DIR}/references/mblm/DIAGRAMS.md` (parent package)

***

## The Style Contract (Read Before Every Generation)

Every output must match ALL of these rules. They are derived directly from
the allumni reference diagram.

### Stroke & Surface

* All lines: black `#000000`, ~1–1.5pt stroke weight
* Linecap: round. Linejoin: round
* Background: white `#ffffff`
* Fill: none on all icons EXCEPT solid black fill on social media circles
  (white letterforms inside)
* No gradients, shadows, opacity, blur, or color of any kind

### Icon Character (Critical — Never Simplify)

Icons are DETAILED and ILLUSTRATIVE. Every icon has internal structure.
Minimum complexity rules:

* **Monitor:** rectangular screen body + inner bezel rectangle + content
  (lines, R mark, or WWW) on screen + short vertical neck + wide horizontal
  base line
* **Document:** page outline with folded top-right corner + 2–3 horizontal
  ruled content lines inside, sometimes a circled-R or image placeholder on
  the face
* **Open book:** two pages with center spine line + ruled content lines on
  each page, sometimes a circled-R on the right page
* **Person:** circle head + vertical torso line + angled arm polyline + two
  leg lines splayed at base. Never a blob or silhouette.
* **Person group:** 3–5 person figures drawn side by side, outer figures
  slightly smaller, all sharing the same baseline
* **Camera:** rounded rect body + circle lens + smaller inner circle +
  viewfinder bump top-left + small shutter button circle top-right
* **Gear:** center circle + inner hole circle + 8 rectangular tooth stubs
  around perimeter at cardinal and diagonal positions
* **Magnifier:** circle lens + short diagonal handle extending bottom-right
* **Circled-R:** outer circle + inner circle (double ring) + R drawn as
  vector strokes: vertical bar left side, two arc bumps right side, diagonal
  leg from mid-bump to bottom-right. NEVER a font glyph.
* **Package/box:** rectangular box body + flat lid rectangle on top +
  cross ribbon lines (vertical + horizontal)
* **Megaphone:** tapered horn shape widening right + rectangular mouthpiece
  left + 2 curved sound wave arcs on right
* **Speech bubble:** rounded rectangle + small downward tail bottom-left +
  2 short content lines inside
* **Bar chart:** X axis line + Y axis line + 3 vertical bars of ascending
  heights, each bar is an outlined rectangle
* **Line chart:** X axis + Y axis + upward-trending polyline across the field
* **Grid layout:** outer rectangle + header row rect + 2-column grid rects
  below + footer row rect
* **Presentation screen:** wide landscape rectangle on two legs/stand +
  content (bar chart or lines) visible inside
* **Trifold brochure:** three vertical panels side by side, slightly fanned,
  each with ruled content lines
* **Type specimen document:** page outline + large "ABCDE" style letterform
  lines + smaller sub-lines below
* **Design system grid:** outer frame + 3 swatch squares top row (one filled
  black, one with X, one with A) + ruled type specimen lines below
* **Social circle (Facebook):** solid black filled circle + white "f"
  letterform strokes inside
* **Social circle (X):** solid black filled circle + white "X" diagonal
  cross strokes inside
* **Social circle (LinkedIn):** solid black filled circle + white "in"
  letterform strokes inside
* **Adobe Illustrator icon:** document outline with folded corner + "Ai"
  letterform strokes on face (no color)
* **Server/infrastructure stack:** 3 horizontal stacked rectangles with
  rounded ends, each with small circle indicator left side
* **Code/programming icon:** document or monitor with `< >` bracket
  symbols inside

### Icon Sizing & Grouping

* Each icon: ~48–64px square in the final output
* Groups of 2–4 icons sit side by side on the same baseline, ~8px apart
* No borders, boxes, backgrounds, or drop shadows around icon groups
* Icons within a group are all the same height

### Section Structure (Exact — Match the Reference)

Each section block contains exactly:

1. **Section label** — uppercase, small-caps weight, ~9pt, sans-serif,
   left-aligned, medium gray
2. **Thin horizontal rule** — full column width, light gray `#cccccc`,
   ~0.75pt, immediately below the label
3. **Icon cluster** — 1–4 icons, left-aligned, ~20px below the rule
4. **Bullet list** (Story and Experience columns only) — small sans-serif
   text, left of or right of icons depending on column

### Column Structure (Three-Column Layout)

* **Column title** — large serif font ~48–56pt, e.g. "Essence", "Story",
  "Experience". Light weight, not bold.
* 5–6 section blocks stacked vertically per column
* ~40px horizontal gap between columns
* ~32–40px vertical gap between sections
* Generous whitespace: sections breathe, never cramped

### Horizontal Flow Layout (Linear Processes)

* Steps left to right, connected by thin arrow lines
* Each step: icon cluster above, small-caps label below
* Arrow: horizontal line + small arrowhead pointing right
* 3–5 steps maximum

***

## Icon Library (Prompt Vocabulary)

See `references/ICON_LIBRARY.md` for the full table. Use those exact
descriptions when specifying icons in image prompts (`circled-R`, `magnifier`,
`document`, `monitor`, `person`, `camera`, `gear`, etc.).

***

## Process Archetypes

See `references/ARCHETYPES.md`:

1. **Brand Implementation & Roll-out** — three-column Essence / Story / Experience
2. **Inbound Marketing Methodology** — horizontal 5-step
3. **Brand Video Production** — horizontal 5-step
4. **Generic Process Flow** — horizontal N-step (3–5) with library icons only

***

## Image Generation Prompt Template

Copy from `PROMPT_TEMPLATE.md`. Keep diagrams monochrome per this contract —
never inject MBLM accent colors into process diagrams.

CLI helper (parent package):

```bash
python3 scripts/mblm_diagram_prompt.py --archetype inbound --topic "Inbound engine" --steps "Attract|Convert|Nurture|Close|Delight"
```

***

## MBLM PPT Master integration

This skill ships nested under `mblm-ppt-master/skills/mblm-diagram/`. Engine
placement rules live in `references/mblm/DIAGRAMS.md`.

### File destinations

1. After PNG generation, save to the active project as:
   - `<project_path>/images/diagram_<slug>.png`
2. When Alumni host-images are in use, also copy to:
   - `projects/_host_images/diagram_<slug>.png`
3. Prefer SVG fallbacks from `assets/mblm/diagrams/` when image gen is offline.

### §VIII / Quick image row pattern

| Field | Value |
|---|---|
| Acquire Via | `ai` (generate) or `user` (after PNG already on disk) |
| Type | Illustration |
| Crop | no-crop |
| Purpose | process diagram |
| Filename | `diagram_<slug>.png` |

### Placement preference

Prefer large content wells or dedicated process hosts:

* Kit: `MBLM_process`, `MBLM_process_timeline`, `MBLM_title_content` (wide well)
* R2: process / pillar / chevrons / timeline pages — see
  `templates/decks/mblm-r2/DIAGRAM_SLOTS.md`

Keep **40px** margins; content logo rules unchanged; do not collide with the
**47pt** title band at top. Diagrams stay black/white monoline — **do not
recolor** with MBLM yellow/blue accents.

### Alumni spawn safety (critical)

**NEVER** stack `mblm-diagram` with the `mblm-ppt-master` Skill Script in the
**same Alumni turn** if Alumni returns 400 spawn errors.

Use either:

1. **Two-turn recipe** — Turn 1: diagrams only → `_host_images/`. Turn 2:
   `mblm-ppt-master` only, place existing PNGs, export.
2. **Single-agent recipe** — load this `SKILL.md` as an Image_Generator style
   reference when `Acquire Via=ai` and Purpose mentions process / methodology /
   phases; the ppt-master agent invokes prompts via the Image_Generator path
   without spawning a second skill script.
