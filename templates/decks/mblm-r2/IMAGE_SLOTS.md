# IMAGE_SLOTS — mblm-r2 pages that host photos & illustrations

Use **mblm-cinematic** (`photo_<slug>.png`) and **mblm-illustration** (`illustration_<slug>.png`) on pages with photo wells, galleries, or large `{{IMAGE}}` regions.
Process monoline art stays on `DIAGRAM_SLOTS.md` hosts.

| Priority | r2 id | SVG | Prefer | Why |
|---|---|---|---|---|
| ★ | r2_13 | `12_r2_13_industry_inflection_photo.svg` | cinematic | Photo / inflection hero well |
| ★ | r2_17 | `16_r2_17_solution_gallery.svg` | cinematic or illustration | Gallery / multi-image — one accent if illustration |
| ★ | Cover / section / closing (kit or custom) | hero layouts | cinematic | Full-bleed + dark overlay for title |
| High | editorial_split / title_picture / 2:1 photo+bar | kit patterns | cinematic half-bleed or illustration well | Content-side imagery |
| High | Wide `MBLM_title_content` well | kit | illustration (centered, padded) | Abstract strategy figure |
| Medium | Pillar / card pages with spare well | r2 pillars | small illustration | Only if copy stays sparse |
| Avoid | r2_40 | section agenda | — | Typography-led |
| Avoid | r2_34, r2_35, r2_36 | Risks / matrices | — | Tables |
| Avoid | Process chevrons / timelines for photos | see DIAGRAM_SLOTS | diagram | Use monoline there, not photos |

## Placement rules

* **Cinematic cover/section/closing:** full-bleed OK; reserve dark overlay for title / Supertext contrast; `page_role=hero_page`; Crop often `adaptive`.
* **Cinematic on content:** half-bleed or framed well — not full bleed under dense body.
* **Illustration on content:** centered with padding; Crop `no-crop`; `page_role=local`; never edge-bleed unless cover/section.
* Margins **40px**; content logo lock unchanged; do not collide with **47pt** title band.
* One accent only per illustration PNG; never recolor diagrams.

## §VIII hints

| Asset | Type | Crop | Purpose |
|---|---|---|---|
| `photo_<slug>.png` | Photography | adaptive (heroes) | cinematic photo |
| `illustration_<slug>.png` | Illustration | no-crop (adaptive heroes) | metaphor illustration |
