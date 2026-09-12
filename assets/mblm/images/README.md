# MBLM generated imagery — naming

AI / host images for decks live in the **project**, not as permanent PNGs in this folder:

* `<project_path>/images/` — working copies used by the deck
* `projects/_host_images/` — Alumni / shared host drop when two-turn visual generation is used

## Filename prefixes

| Prefix | Skill | Example |
|---|---|---|
| `diagram_` | `skills/mblm-diagram` | `diagram_inbound_marketing.png` |
| `illustration_` | `skills/mblm-illustration` | `illustration_brand_system_city.png` |
| `photo_` | `skills/mblm-cinematic` | `photo_cover_plaza_dusk.png` |

Kit logos and icons remain under `assets/mblm/logos/` and `assets/mblm/icons/`.  
SVG diagram fallbacks: `assets/mblm/diagrams/`.

Do not commit fake placeholder PNGs here — generate or drop real assets per project.
