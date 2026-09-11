---
brand_id: mblm
kind: brand
summary: MBLM — The Brand Intimacy Agency identity for client and internal PowerPoint decks
primary_color: "#000000"
---

# MBLM Brand Specification

> Identity-only preset for MBLM PPT Master. Page composition follows
> `${SKILL_DIR}/references/mblm/LAYOUTS.md` +
> `references/mblm/visual-references/LAYOUT_PATTERNS.md` +
> `CATALOG_R2.md` and the MBLM brand freeze in `SKILL.md` / `MBLM_OVERLAY.md`.
> Decisions locked through **v4.1.1 / v4.2.0**. Full token tables live under
> `${SKILL_DIR}/references/mblm/` (COLORS, TYPOGRAPHY, LOGOS, LAYOUT_METRICS, …).

## I. Brand Overview

| Property | Value |
|---|---|
| Brand Name | MBLM |
| Tagline | The Brand Intimacy Agency (**omit on slides when logo is present**) |
| Use Cases | Agency pitches, brand strategy readouts, capability decks, workshops, case studies, consulting proposals |
| Tone | Confident, intimate, modern, human |
| Sources | Official specs + R2 consulting examples + brand kit assets in `${SKILL_DIR}/assets/mblm/` |

### Provenance note

Brand rules were derived from official slides/specs screenshots, R2 consulting
examples, SVGs, the brand-kit screenshot, layout compositions, and locked user
geometry (v4.1.1). Agents must **analyze** visual references under
`references/mblm/visual-references/` before authoring.

## II. Color Scheme

| Role | HEX | Provenance | Notes |
|---|---|---|---|
| primary | `#000000` | official | Black — primary brand, section/title backgrounds |
| primary-inverse | `#FFFFFF` | official | White — light backgrounds, reverse text |
| brand-accent | `#FFF200` | official | Yellow — fills/floods **not lines**; **not text on black** |
| main-gray | `#BFBFBF` | official | Borders, muted UI, table lines |
| bg-warm | `#F3EEE5` | kit | Warm surface (cream `#FCF5EB*` for gradients) |
| cyan | `#00AEFF` | official | Line OK |
| mid-blue | `#006AF1` / `#0068EB` | official | Mid blue family; line OK |
| dark-navy | `#002A60` | official | Preferred card-header line |
| secondary greens / magentas / purples | see `references/mblm/COLORS.md` | official | Asterisk = gradients only |

**Lines**: `references/mblm/LINE_RULES.md` — no yellow lines; blue-only above cards;
white-only text on black fills. **Gradients**: mainly section dividers —
see `COLORS.md`.

## III. Typography

| Role | Family | Weight / size |
|---|---|---|
| cover title | BentonSansCond | **Light 60 or 72** (prefer 72) |
| cover subtitle | BentonSansCond | **24 or 32** (prefer 28–32) |
| agenda / content page title | BentonSansCond | **Light 47 only** |
| content subtitle | BentonSansCond | **Regular 18 or 20** (prefer 20); `#000000` |
| body | BentonSansCond | **Regular 16 or 20** locked deck-wide (**prefer 20**) |
| accents < ~24px @ 1280 | BentonSansCond | **Bold** |
| topic headers | BentonSansCond | **Medium** |
| Supertext | BentonSansCond | **Black** outline **1.25pt**, ≥150pt, edge-to-edge |

**Editable text**: one object per paragraph — `TEXT_BOXES.md`. Normal kerning;
**no kickers**. Fallback when Benton unavailable: Arial Narrow → Arial
(`TYPOGRAPHY.md`).

## IV. Logo

- Files (workspace-relative):
  - `../images/MBLM_LOGO_White background.svg` — positive on light
  - `../images/MBLM_LOGO_dark background.svg` — negative on dark
  - `../images/MBLM_LOGO_Brand color.svg` — black mark on `#FFF200`
  - `../images/MBLM_LOGO_Yellow background.svg` — framed inverse (legacy)
- Package copies also live under `${SKILL_DIR}/assets/mblm/logos/`
- Usage: every cover + closing; content pages: corner mark top-right
- **v4.1 size**: content logo **88.4×44.2 @ 1148.2,39.7**; cover/divider/thanks
  **138×69 @ 40,40** (`LAYOUT_METRICS.md`)
- No tagline when logo present; no bottom MBLM wordmark if logo on slide
- Rules: `references/mblm/LOGOS.md`

## V. Voice & Tone

- Formality: professional-intimate (agency)
- Person: we / you
- Emoji: forbidden (default)
- Abbreviations: spell-out-first for client terms; MBLM product names as provided

## VI. Icon Style

- Preference: linear / thin-stroke geometric (kit icons)
- Prefer `${SKILL_DIR}/assets/mblm/icons/` over generic libraries for MBLM service metaphors
- Always quote paths for `MBLM_ UI-UX Design.svg` (leading space in filename)
