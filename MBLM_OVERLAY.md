# MBLM Overlay (always load with SKILL.md)

Agents must load this file after `SKILL.md` and before SVG authoring. It does
**not** replace MIT attribution files (`LICENSE`, `SPONSORS.md`,
`SPONSORS_CN.md`) or the `attribution_guard.py` gate.

## Hard rules

1. **Only brand**: install `${SKILL_DIR}/templates/brands/mblm/`. Never load
   McKinsey / BCG / Bain / Accenture / other presets (they are not shipped).
2. **Index**: `templates/brands/brands_index.json` contains only `mblm`.
3. **References**: `${SKILL_DIR}/references/mblm/` (not bare `references/` for
   brand tokens).
4. **Assets**: `${SKILL_DIR}/assets/mblm/` for logos, icons, layouts, palette.
5. **Default route**: Path A Quick via `workflows/generate-mblm-pptx.md`.
6. **Freeze**: content titles **47pt**; logos **88.4×44.2 @ 1148.2,39.7**
   (content) and **138×69 @ 40,40** (cover/divider/thanks); margins **1.05 cm**;
   bullets Ø≈**80%** text; **no yellow lines**; white-only on black; no kickers;
   one text object per paragraph.

Full lock list: `SKILL.md` § HARD DESIGN FREEZE and
`references/mblm/RESOLVED_DECISIONS.md` / `LAYOUT_METRICS.md`.
