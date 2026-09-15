# Brand Identity Presets (MBLM-only)

This package is **MBLM PPT Master**. The only registered brand workspace is
[`mblm/`](./mblm/). Discovery reads [`brands_index.json`](./brands_index.json) —
never invent or load McKinsey, BCG, Bain, Accenture, or any other consulting
preset.

## Brand schema

```text
templates/brands/<brand_id>/
├── templates/design_spec.md   # required — identity spec with YAML frontmatter `kind: brand`
├── images/                    # optional — logo.<ext>, alternate lockups, visual assets
├── icons/                     # optional — branded icon overrides
└── exports/                   # normally absent; Git-ignored derived artifacts only
```

The six required sections are I Brand Overview / II Color Scheme / III Typography /
IV Logo / V Voice & Tone / VI Icon Style.

## Discovery index

[brands_index.json](./brands_index.json) maps `brand_id → { summary, primary_color }`.
This distribution lists **only** `mblm`. Stage-1 controls and chat discovery read
this index only; a bare ID never resolves implicitly. Agents must always install
`${SKILL_DIR}/templates/brands/mblm/` for generation.
