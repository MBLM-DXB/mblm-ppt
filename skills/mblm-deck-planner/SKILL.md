---
name: mblm-deck-planner
description: >
  Alumni deck PLANNER for MBLM presentations. Reads conversation memory,
  attached docs, URLs, summaries, screenshots, datasets, and user instructions;
  outputs an ordered slide PLAN only (JSON/YAML map — never PPTX) for handoff
  to mblm-ppt-master. Prefer photographic / photo-editorial when applicable;
  illustration for metaphors; diagram for process; type-only for agenda /
  tables / matrices. Maps content to mblm-r2 (39 layouts) + core kit layouts.
  Use when the user asks to plan an MBLM deck, outline slides, or prepare a
  handoff for mblm-ppt-master before generating PPTX.
---

# mblm-deck-planner

**Output:** deck **PLAN only** (ordered slide map). **Never** emit PPTX, never
run `svg_to_pptx`, never call `mblm-ppt-master` Skill Script in the same turn
as this planner.

**Handoff target:** `mblm-ppt-master` (Path A Quick) after visuals (if any).

## Inputs (Alumni chat)

Read **all** available context before planning:

| Source | Use |
|---|---|
| Conversation memory | Goals, audience, constraints, prior decisions |
| Attached docs / PDFs / decks | Structure, claims, approved language |
| URLs | Public facts only; cite in `notes` |
| Summaries / briefs | Narrative spine |
| Screenshots | Layout cues / brand moments (do not invent metrics from UI chrome) |
| Datasets / tables | Only numbers present in the data |
| Explicit user instructions | Override defaults (slide count, tone, must-include) |

**Hard rule — facts only:** Never invent KPIs, percentages, dollar figures,
headcount, timelines, or case outcomes. If a metric is missing, omit it or
flag `notes: "METRIC NEEDED: …"` — do not fabricate.

## Brand freeze pointers (planner must respect)

Full authority: parent `mblm-ppt-master` → `SKILL.md` / `MBLM_OVERLAY.md` /
`references/mblm/LAYOUT_METRICS.md` / `TYPOGRAPHY.md`.

| Token | Lock |
|---|---|
| Content titles | BentonSansCond **Light 40pt** (SVG authoring **53.3** = 40/0.75) |
| Body | **Regular 16pt or 18pt** min (SVG **21.3** / **24** when exporter-scaled) |
| Weights allowed | **Light / Regular / Bold / Italic / Black** only |
| **Banned** | **Medium / MediumSC** (and Medium Italic / Medium Italic SC) |
| Section agenda section labels | **50pt Light** (SVG **66.7**) on `39_r2_40_section_agenda` |
| Logos / margins | Per `LAYOUT_METRICS.md` (1.05 cm; content logo 88.4×44.2 @ 1148.2,39.7; cover 138×69 @ 40,40) |
| Agenda gold | **`39_r2_40_section_agenda` only** — `11_r2_12_content_toc` **REMOVED** |

## Visual chooser

| Need | Prefer `visual_mode` | Notes |
|---|---|---|
| Cover / section / closing atmosphere; real-world context; people-as-atmosphere | **`photo`** / photo-editorial | Prefer photographic when the story is human, place, or brand moment |
| Abstract strategy / capability / metaphor | **`illustration`** | Exactly one MBLM accent per image (`mblm-illustration`) |
| Process / methodology / phases as monoline art | **`diagram`** | Black/white only (`mblm-diagram`) |
| Agenda / dense tables / matrices / checklists | **`type`** | Typography-led; no large AI art |
| Small chrome / ornaments | **`kit_icon`** | Kit SVG icons only |
| Native r2 geometry already tells the story | **`none`** | Fill labels; no new asset |

Default bias: **photographic / photo-editorial when applicable**; illustration for
metaphors; diagram for process; type-only for agenda/tables/matrices.

## Layout catalog (map content → layout_id)

### A. mblm-r2 — 39 layouts (`templates/decks/mblm-r2/templates/`)

Use file stem as `layout_id` (e.g. `39_r2_40_section_agenda`). See
`references/LAYOUT_PICKER.md` + parent `SOURCE_MAP.md`.

**Agenda gold:** `39_r2_40_section_agenda` only. Do **not** plan `11_r2_12_content_toc`.

### B. Core kit — 19 layouts (`assets/mblm/layouts/MBLM_*.svg`)

`MBLM_title_slide`, `MBLM_title`, `MBLM_title_content`, `MBLM_section_header`,
`MBLM_hero_statement`, `MBLM_four_card`, `MBLM_process`, `MBLM_process_timeline`,
`MBLM_kpi_dashboard`, `MBLM_table_summary`, `MBLM_chart_insight`,
`MBLM_three_picture_caption`, `MBLM_four_picture_caption`,
`MBLM_six_picture_caption`, `MBLM_title_picture`, `MBLM_editorial_split`,
`MBLM_screenshot_focus`, `MBLM_closing`, `MBLM_07_blank`.

Prefer **r2** when a consulting beat matches; fall back to core kit for cover /
hero / editorial / closing DNA.

## Layout picker by narrative beat

Load [`references/LAYOUT_PICKER.md`](references/LAYOUT_PICKER.md). Summary:

| Beat | Preferred layout_id(s) |
|---|---|
| Cover | `MBLM_title_slide` / photo hero |
| Agenda / section TOC | **`39_r2_40_section_agenda`** |
| Situation / objectives | `01_r2_02_objectives_two_column`, `08_r2_09_executive_summary` |
| From→to / compare | `03_r2_04_from_to_compare` |
| Photo + bullets (inflection) | `12_r2_13_industry_inflection_photo` |
| Pillars / reasons to act | `14_r2_15_time_to_act_pillars`, `15_r2_16_solution_pillars` |
| Process / guiding steps | `21_r2_22_four_step_guiding`, `18_r2_19_strategy_process_pillars` |
| Timeline / Gantt / phases | `22_r2_23_*`, `28_r2_29_*`, `29_r2_30_*`, `30_r2_31_*` |
| Risks / matrices | `33_r2_34_risks_table`, `34_r2_35_risks_matrix`, `35_r2_36_capability_matrix` |
| Closing | `MBLM_closing` |

## Output schema

Emit the plan as YAML or JSON matching
[`references/OUTPUT_SCHEMA.md`](references/OUTPUT_SCHEMA.md).

Each slide **must** include:

- `layout_id` — catalog stem
- `title` — content title (facts/language from context)
- `body` — bullet strings (or structured fields the layout expects)
- `visual_mode` — `photo` | `illustration` | `diagram` | `type` | `kit_icon` | `none`
- `image_prompt` and/or `image_filename` — when visual_mode needs an asset
- `notes` — handoff hints, sources, open metric gaps

## Alumni orchestration after the plan

**Turn 0 (this skill):** plan only → save slide map for the user.

**Turn 1 — visuals:** generate all `photo_` / `illustration_` / `diagram_` PNGs
into `projects/_host_images/` using nested `mblm-cinematic` / `mblm-illustration`
/ `mblm-diagram`. **Do not** run `mblm-ppt-master`.

**Turn 2 — deck:** `mblm-ppt-master` **only** — init, apply brand `mblm`, author
from plan + `_host_images`, export PPTX. Avoid stacking visual Skill Scripts
with ppt Skill Script (Alumni **400 spawn**).

Copy-paste runner: [`PROMPT_ALUMNI.md`](PROMPT_ALUMNI.md).

## Procedure

1. Ingest all chat context / attachments / URLs (facts only).
2. Draft narrative spine (cover → agenda → sections → close); one idea per slide.
3. For each beat: pick `layout_id` via LAYOUT_PICKER; set `visual_mode` via chooser.
4. Fill titles/body from source language; leave gaps marked in `notes`.
5. Emit ordered slide map (OUTPUT_SCHEMA). Stop. Do not generate PPTX.
