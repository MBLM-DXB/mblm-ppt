# Alumni prompt series — MBLM PPT + imagery / diagrams / illustrations

**Canonical orchestration:** [`STEP4_INTEGRATION.md`](STEP4_INTEGRATION.md) (end-to-end flow, chooser, install).  
This file holds **copy-paste stacks**. Prefer nested skills under `mblm-ppt-master/skills/mblm-*` when present.

Load order when Alumni asks:

0. **`mblm-deck-planner`** first (plan only) — see `skills/mblm-deck-planner/PROMPT_ALUMNI.md`.
1. Visual skill(s) **or** `mblm-ppt-master` — never both Skill Scripts in one turn if you hit 400 spawn (use **Prompt MASTER** after the plan).
2. Then generate / place assets into the deck.

**Hard rules for every deck prompt**
- Follow MBLM brand freeze (layout metrics, **40pt Light** content titles, body Regular 16–18, **no Medium**, logo positions, no yellow lines, black subtitles, agenda **r2_40 only**, etc.)
- Do **not** skip `apply_template` for brand `mblm`
- Install PyYAML; use the fixed package (`paths.py` + valid `design_spec.md`)
- Facts only from my brief — no invented metrics
- Prefer one idea per slide; imagery full-bleed only on cover / section / closing unless I say otherwise

---

## Prompt MASTER — Alumni plan + two-turn (default; avoids 400 spawn)

Use this for any mixed-visual MBLM deck on Alumni.
**Turn 0** = `mblm-deck-planner` (plan only) → **Turn A** = nested image skills only → **Turn B** = ppt-master only.

### Turn 0 — plan only

```text
Use skill: mblm-deck-planner ONLY.
Output YAML/JSON deck_plan per skills/mblm-deck-planner/references/OUTPUT_SCHEMA.md.
Agenda layout_id = 39_r2_40_section_agenda only. No PPTX. Facts only — no invented KPIs.
BRIEF
[PASTE BRIEF]
```

### Turn A — visuals only

```text
Use nested skills as style refs (do NOT load mblm-ppt-master Skill Script this turn):
  skills/mblm-diagram/SKILL.md
  skills/mblm-illustration/SKILL.md
  skills/mblm-cinematic/SKILL.md
(Fall back to top-level allumni-diagram / MBLM Illustration System / Cinematic Human Light only if nested pack missing.)

From the brief below, generate ALL needed PNGs for the deck. Save to projects/_host_images/:
  - diagram_<slug>.png   — process / methodology (white bg, black monoline only)
  - illustration_<slug>.png — strategy metaphors (exactly ONE accent; centered padding)
  - photo_<slug>.png     — cover / section / closing cinematic stills (cool base + one warm source)

Do NOT init a PPT project. Do NOT export PPTX. Do NOT apply brand templates this turn.

BRIEF
[PASTE BRIEF]

SHOT LIST (edit)
- Cover: photo_…
- Section dividers: photo_… and/or illustration_…
- Methodology: diagram_…
- Capability metaphors: illustration_… (accents: yellow|orange|magenta|violet|blue|cyan|green — one per file)
```

### Turn B — deck only

```text
Use skill: mblm-ppt-master ONLY (no visual Skill Scripts).

1. attribution_guard → project_manager init <name> --quick-generate
2. apply_template <project_path> --root templates/brands/mblm  (required)
3. Plan 12–16 slides; prefer templates/decks/mblm-r2 layouts via SOURCE_MAP.md
4. Place existing projects/_host_images PNGs:
   - photos → IMAGE_SLOTS (full-bleed only cover/section/closing + dark overlay)
   - illustrations → centered content wells (IMAGE_SLOTS)
   - diagrams → DIAGRAM_SLOTS / MBLM_process hosts
5. §VIII: Acquire Via=user; Type/Crop/Purpose per asset class (see IMAGES_GEN.md)
6. MBLM metrics: 1.05 cm margins; content logo 88.4×44.2 @ 1148.2,39.7; titles 40pt Light; body Regular ≥16/18; no Medium; agenda r2_40 only; subtitles black; no yellow lines; no kickers
7. Export: svg_quality_checker → svg_to_pptx --quick-generate

BRIEF (same as Turn A)
[PASTE BRIEF]
```

Details: `docs/STEP4_INTEGRATION.md` § Alumni TWO-TURN.

---

## Prompt LOCAL — single-agent / local engine (Image_Generator)

One chat; engine owns image gen. Nested SKILL.md files are **style references** only — do not spawn parallel Alumni visual skill scripts.

```text
Use skill: mblm-ppt-master.
Load as Image_Generator style refs (do not spawn separate visual Skill Scripts):
  skills/mblm-diagram/SKILL.md (+ PROMPT_TEMPLATE.md)
  skills/mblm-illustration/SKILL.md (+ PROMPT_TEMPLATE.md, PALETTE.md)
  skills/mblm-cinematic/SKILL.md (+ PROMPT_TEMPLATE.md, CHECKLIST.md)

PROCESS
1. Guard → init --quick-generate → apply brand templates/brands/mblm
2. Visual chooser (IMAGES_GEN + DIAGRAMS): cinematic | illustration | diagram | kit icons | typography-led
3. Emit prompts via scripts if helpful:
   python3 scripts/mblm_diagram_prompt.py …
   python3 scripts/mblm_illustration_prompt.py …
   python3 scripts/mblm_cinematic_prompt.py …
   (scripts emit prompts only — they do not call image APIs)
4. Generate into project images/ (and projects/_host_images/ if used) with diagram_ / illustration_ / photo_ prefixes
5. Author/reuse mblm-r2 pages (SOURCE_MAP / IMAGE_SLOTS / DIAGRAM_SLOTS); place assets; §VIII Acquire Via=ai
6. If diagram gen fails, place SVG from assets/mblm/diagrams/
7. Export editable PPTX via svg_to_pptx --quick-generate

BRIEF
[PASTE BRIEF]

VISUAL MAP (edit)
- Cover: cinematic full-bleed + dark overlay
- Agenda: r2_12 Content TOC — no large AI art
- Methodology: mblm-diagram
- Strategy metaphors: mblm-illustration (one accent)
- Closing: cinematic or black + Supertext
```

---

## Prompt A — Full deck with mixed visuals (master stack)



```text
Use skills: mblm-ppt-master (prefer nested skills/mblm-diagram, skills/mblm-illustration, skills/mblm-cinematic as style refs; fall back to top-level allumni-diagram / MBLM Illustration System / Cinematic Human Light only if nested pack missing).

Build an MBLM-branded PPTX from the brief below.

PROCESS
1. Init project --quick-generate and apply brand workspace templates/brands/mblm (do not skip).
2. Plan a 12–16 slide roster (cover, agenda, sections, content, closing) using MBLM layout patterns.
3. For each slide, choose ONE visual mode:
   - Photo: skills/mblm-cinematic (cool base + one warm source, backlight, shallow DOF)
   - Metaphor illustration: skills/mblm-illustration (one accent color only, risograph/halftone, tiny faceless figures, centered in white space — not edge-bleed)
   - Process diagram: skills/mblm-diagram (white bg, black monoline icons only — no color)
4. Generate missing visuals first as PNG assets into the project images/ folder with clear filenames.
5. Author SVGs / slides with MBLM metrics (1.05 cm margins; content logo 2.34×1.17 cm at 30.38×1.05 cm; content titles 47pt Light; subtitles black; bullets round black Ø≈80% text).
6. Gradients only on section dividers. No kickers. No tagline if logo present.
7. Export editable PPTX via svg_to_pptx --quick-generate.

BRIEF
[PASTE BRIEF]

VISUAL MAP (edit as needed)
- Cover: Cinematic Human Light photo, full-bleed + dark overlay
- Agenda: no photo; clean MBLM Content TOC
- Section dividers: MBLM Illustration System OR gradient divider + Supertext ≥150pt
- Methodology / process slides: allumni-diagram PNG (Essence/Story/Experience OR horizontal flow)
- Capability / abstract idea slides: MBLM Illustration System, one accent from #FFF200 / #FFBA00 / #EC008C / #9700DC / #006AF1 / #00AEFF / #00D300
- Closing: Cinematic Human Light or black + Supertext
```

---

## Prompt B — Process / methodology diagram only (then drop into deck)

```text
Use skill: allumni-diagram (v2).

Generate ONE process diagram PNG matching the allumni monoline contract exactly:
white background, black #000000 strokes ~1–1.5pt, round caps/joins, no color, no fills except social circles, detailed icons (not simplified blobs).

Archetype: [Brand Implementation three-column Essence/Story/Experience | Inbound 5-step | Video 5-step | Custom horizontal N-step]
Topic: [YOUR PROCESS]
Sections / steps: [LIST]

Then use skill mblm-ppt-master:
Add this PNG to an MBLM content slide titled “[TITLE]” (47pt Light), subtitle black 18–20pt, 1.05 cm margins, content logo locked position. No yellow lines. Export updated PPTX.
```

---



## Prompt B2 — Process diagram via nested `skills/mblm-diagram` (in-package)

Use when the Alumni package already includes `mblm-ppt-master` with the nested diagram skill (STEP 2). Prefer this over a separate top-level `allumni-diagram` install when both exist.

```text
Use skill: mblm-ppt-master (load nested skills/mblm-diagram/SKILL.md as diagram style reference).

TWO-TURN SAFE MODE (recommended if prior runs returned 400 spawn errors):
Turn 1 — diagrams only:
  Follow skills/mblm-diagram contract. Generate ONE process diagram PNG.
  Archetype: [brand-rollout | inbound | video | generic]
  Topic: [YOUR PROCESS]
  Steps: [LIST]
  Save as projects/_host_images/diagram_<slug>.png
  Do not export PPTX in this turn.

Turn 2 — deck only:
  Use only mblm-ppt-master. Init --quick-generate, apply brand mblm.
  Place diagram_<slug>.png on a process/pillar/timeline slide (R2 DIAGRAM_SLOTS or MBLM_process).
  §VIII row: Acquire Via=user; Type=Illustration; Crop=no-crop; Purpose=process diagram.
  Title 47pt Light; 1.05 cm margins; content logo locked. Export PPTX.

SINGLE-AGENT MODE (engine owns Image_Generator):
  Load skills/mblm-diagram/SKILL.md + PROMPT_TEMPLATE.md as style reference.
  Or run: python3 scripts/mblm_diagram_prompt.py --archetype inbound --topic "..." --steps "A|B|C"
  Acquire Via=ai; Type=Illustration; Crop=no-crop; Purpose=process diagram.
  If image gen unavailable, place SVG from assets/mblm/diagrams/.
```

Local prompt helper:

```bash
python3 scripts/mblm_diagram_prompt.py --archetype inbound --topic "Inbound engine" --steps "Attract|Convert|Nurture|Close|Delight"
```

## Prompt C — Metaphor illustration for a strategy idea

```text
Use skill: MBLM Illustration System (Textured Metaphors).

Create one 16:9 PNG illustration:
- Tiny faceless figures + oversized geometric metaphor for: [TOPIC]
- Background stark white (or paper gray / charcoal — pick one)
- Exactly ONE accent: [Yellow #FFF200 | Orange #FFBA00 | Magenta #EC008C | Violet #9700DC | Blue #006AF1 | Cyan #00AEFF | Green #00D300]
- Risograph/halftone texture, thin architectural linework
- Keep art centered with padding — do not go to edges
- Minimal; no random clutter

Then use skill mblm-ppt-master:
Place on slide “[TITLE]” as a centered figure on white/off-white content slide (not full-bleed unless I say so). MBLM brand lock. Export PPTX.
```

---


## Prompt C2 — Metaphor illustration via nested `skills/mblm-illustration`

Use when the Alumni package includes nested illustration skill (STEP 3). Prefer over a separate top-level “MBLM Illustration System” install when both exist.

```text
Use skill: mblm-ppt-master (load nested skills/mblm-illustration/SKILL.md as illustration style reference).

TWO-TURN SAFE MODE (recommended if prior runs returned 400 spawn errors):
Turn 1 — visuals only:
  Follow skills/mblm-illustration contract. Generate ONE 16:9 PNG metaphor illustration.
  Topic: [TOPIC]
  Accent: [yellow|orange|magenta|violet|blue|cyan|green] — exactly one
  Background: [white|paper|charcoal]
  Action / shapes: [SPEC]
  Save as projects/_host_images/illustration_<slug>.png
  Do not export PPTX in this turn.

Turn 2 — deck only:
  Use only mblm-ppt-master. Init --quick-generate, apply brand mblm.
  Place illustration_<slug>.png centered on a content well (IMAGE_SLOTS / local page_role).
  §VIII row: Acquire Via=user; Type=Illustration; Crop=no-crop; Purpose=metaphor illustration.
  Title 47pt Light; 1.05 cm margins; content logo locked. Export PPTX.

SINGLE-AGENT MODE (engine owns Image_Generator):
  Load skills/mblm-illustration/SKILL.md + PROMPT_TEMPLATE.md + PALETTE.md as style reference.
  Or run: python3 scripts/mblm_illustration_prompt.py --topic "..." --accent yellow --background white --action "..." --shapes "..."
  Acquire Via=ai; Type=Illustration; Crop=no-crop; Purpose=metaphor illustration.
```

Local prompt helper:

```bash
python3 scripts/mblm_illustration_prompt.py --topic "Brand system as a city" --accent yellow --background white \
  --action "tiny figures walk between typography blocks" --shapes "towers, grids, arched portals"
```

## Prompt D — Cinematic photo slides (cover / people / atmosphere)

```text
Use skill: Cinematic Human Light.

Generate [N] 16:9 photographic stills for an MBLM deck about [TOPIC]:
- Cool blue-teal base + one warm backlight source
- Shallow DOF, haze/flare OK, faces in profile or obscured
- Mix motion blur and stillness
- Avoid smiling corporate headshots and flat frontal light

Shots needed:
1. Cover hero — [SCENE]
2. Section mood — [SCENE]
3. Closing — [SCENE]

Then use skill mblm-ppt-master:
Build/update the deck: full-bleed photos only on cover, section dividers, and closing with dark overlay for title contrast. Content slides stay light. Apply MBLM metrics and brand template. Export PPTX.
```

---


## Prompt D2 — Cinematic photos via nested `skills/mblm-cinematic`

Use when the Alumni package includes nested cinematic skill (STEP 3). Prefer over a separate top-level “Cinematic Human Light” install when both exist.

```text
Use skill: mblm-ppt-master (load nested skills/mblm-cinematic/SKILL.md as photography style reference).

TWO-TURN SAFE MODE:
Turn 1 — visuals only:
  Follow skills/mblm-cinematic contract. Generate cover/section/closing stills.
  Subject / action / location / light / motion / face per shot list.
  Save as projects/_host_images/photo_<slug>.png
  Do not export PPTX in this turn.

Turn 2 — deck only:
  Use only mblm-ppt-master. Full-bleed photos on cover/section/closing with dark overlay.
  Content slides: half-bleed or framed wells (r2_13, r2_17, title_picture, editorial_split).
  §VIII: Acquire Via=user; Type=Photography; Crop=adaptive; Purpose=cinematic photo.
  Apply MBLM metrics; export PPTX.

SINGLE-AGENT MODE:
  Load skills/mblm-cinematic/SKILL.md + PROMPT_TEMPLATE.md + CHECKLIST.md as style reference.
  Or run: python3 scripts/mblm_cinematic_prompt.py --subject "..." --action "..." --location "..." --light "low sun" --motion still --face obscured
  Acquire Via=ai; Type=Photography; Crop=adaptive; Purpose=cinematic photo.
```

Local prompt helper:

```bash
python3 scripts/mblm_cinematic_prompt.py --subject "two silhouettes" --action "walking toward light" \
  --location "empty urban plaza at dusk" --light "low sun" --motion still --face obscured
```

## Prompt E — Diagram + illustration + photo in one narrative deck

```text
Stack: mblm-ppt-master + nested skills/mblm-diagram + skills/mblm-illustration + skills/mblm-cinematic (or top-level equivalents if nested missing).

Create an MBLM PPTX for [AUDIENCE] on [TOPIC].

Slide plan:
1. Cover — Cinematic Human Light full-bleed
2. Agenda — MBLM Content pattern (47pt “Content”)
3. Challenge — short copy + Cinematic still (half or full per MBLM layout)
4. Approach overview — MBLM Illustration System metaphor (one accent)
5. Methodology — allumni-diagram three-column OR horizontal flow PNG
6–10. Content clusters — light slides, kit icons, optional small illustrations
11. Section — illustration or photo divider + Supertext
12. Next steps — clean content
13. Closing — photo or black + Supertext

Rules: MBLM brand apply required; facts only from brief; no invented KPIs; no yellow divider lines; body 16–20pt; subtitles #000000.

BRIEF:
[PASTE]
```

---

## Prompt F — Fix / regenerate visuals without rebuilding the whole deck

```text
Use mblm-ppt-master on existing project [PATH OR NAME].

Replace visuals only:
- Regenerate diagram for slide [N] with allumni-diagram: [SPEC]
- Regenerate illustration for slide [N] with MBLM Illustration System: accent [COLOR], topic [TOPIC]
- Keep all typography, logo positions, and layout metrics unchanged.
Re-export PPTX.
```

---

## Quick chooser

| Need | Use |
|---|---|
| **Alumni default (any mixed deck)** | **Prompt MASTER** (two-turn A/B) |
| **Local / single agent** | **Prompt LOCAL** |
| Whole branded deck + mixed art (legacy one-shot) | Prompt A or E |
| Process / phases diagram | Prompt B or **B2** (nested skill) |
| Abstract strategy metaphor | Prompt C or **C2** (nested skill) |
| Human / atmospheric photos | Prompt D or **D2** (nested skill) |
| Swap art on an existing deck | Prompt F |

Canonical flow: [`STEP4_INTEGRATION.md`](STEP4_INTEGRATION.md).
