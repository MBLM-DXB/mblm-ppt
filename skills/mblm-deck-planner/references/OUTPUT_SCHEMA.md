# OUTPUT_SCHEMA — deck plan slide map

Emit **YAML or JSON**. Plan only — no PPTX binaries.

## Top level

```yaml
deck_plan:
  title: "Working deck title from brief"
  audience: "Who this is for"
  narrative_spine: "One-sentence story arc"
  brand: mblm
  source_facts: "conversation|docs|urls|datasets only"
  slide_count: 12
  slides: []  # ordered
```

## Slide object (required fields)

| Field | Type | Rule |
|---|---|---|
| `order` | int | 1-based position |
| `layout_id` | string | Catalog stem (r2 or `MBLM_*`) |
| `title` | string | Content title; Light 40pt when built |
| `body` | string[] | Bullets / short lines from context only |
| `visual_mode` | enum | `photo` \| `illustration` \| `diagram` \| `type` \| `kit_icon` \| `none` |
| `image_prompt` | string \| null | Prompt for Turn 1 when generating |
| `image_filename` | string \| null | e.g. `photo_cover_city.png` under `_host_images` |
| `notes` | string | Sources, open gaps, layout fill hints |

### Optional fields

| Field | Type | Use |
|---|---|---|
| `subtitle` | string | Under-title; black Regular 18 |
| `section_label` | string | For agenda / divider |
| `fields` | object | Extra carriers (`ITEM_1`, `REASON_01`, table cells, …) |
| `diagram_slot` | string | When `visual_mode: diagram` |
| `image_slot` | string | When photo/illustration host known |
| `full_bleed` | bool | Cover / section / closing only |

## Example (YAML)

```yaml
deck_plan:
  title: "Brand intimacy readout"
  audience: "Client steering committee"
  narrative_spine: "Context → inflection → pillars → approach → next steps"
  brand: mblm
  source_facts: "brief + attached PDF"
  slide_count: 6
  slides:
    - order: 1
      layout_id: MBLM_title_slide
      title: "Brand Intimacy Readout"
      body: []
      visual_mode: photo
      image_prompt: "Cinematic cool blue-teal city dusk, one warm window light, no faces toward camera"
      image_filename: photo_cover_dusk.png
      notes: "Full-bleed cover; logo top-left per LAYOUT_METRICS"
    - order: 2
      layout_id: 39_r2_40_section_agenda
      title: "Agenda"
      body: ["Context", "Opportunity", "Approach", "Next steps"]
      visual_mode: type
      image_prompt: null
      image_filename: null
      notes: "Section labels 50pt Light; agenda gold r2_40 only"
    - order: 3
      layout_id: 12_r2_13_industry_inflection_photo
      title: "The industry is at an inflection"
      body:
        - "Shift described in brief §2"
        - "Customer expectation change (from deck)"
      visual_mode: photo
      image_prompt: "Editorial photo, cool grade, single warm practical light"
      image_filename: photo_inflection.png
      notes: "Bullets only from brief — no invented stats"
    - order: 4
      layout_id: 14_r2_15_time_to_act_pillars
      title: "Why act now"
      body: ["Reason A from brief", "Reason B from brief"]
      fields:
        REASON_01: "Reason A"
        DESC_01: "Supporting line from brief"
      visual_mode: none
      image_prompt: null
      image_filename: null
      notes: "Fill remaining pillars only if facts exist"
    - order: 5
      layout_id: 21_r2_22_four_step_guiding
      title: "Guiding approach"
      body: []
      visual_mode: diagram
      image_prompt: "Monoline four-phase process, white bg, black lines only"
      image_filename: diagram_guiding_four.png
      notes: "Turn 1 diagram; Turn 2 place in DIAGRAM_SLOTS"
    - order: 6
      layout_id: MBLM_closing
      title: "Thank you"
      body: []
      visual_mode: photo
      image_prompt: null
      image_filename: photo_cover_dusk.png
      notes: "Reuse cover still OK"
```

## Validation checklist

- [ ] Every `layout_id` exists in r2 (39) or core (19)
- [ ] No `11_r2_12_content_toc`
- [ ] No invented KPIs
- [ ] `visual_mode` matches chooser; filenames use `photo_` / `illustration_` / `diagram_` prefixes
- [ ] Ordered `slides` cover cover → agenda → body → close (unless user waived)
