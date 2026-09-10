---
brand_id: mblm
kind: brand
summary: MBLM — The Brand Intimacy Agency identity for client and internal PowerPoint decks
primary_color: "#000000"
---

# MBLM Brand Specification

> Identity preset for this skill. Page composition follows `LAYOUTS.md` + `visual-references/LAYOUT_PATTERNS.md` + `CATALOG_R2.md` + ppt-master authoring; this file locks identity only. Decisions locked through **v4.1.0** (2026-09-10) — see `RESOLVED_DECISIONS.md` + `LAYOUT_METRICS.md`.

## I. Brand Overview

| Property | Value |
|---|---|
| Brand Name | MBLM |
| Tagline | The Brand Intimacy Agency (**omit on slides when logo is present**) |
| Use Cases | Agency pitches, brand strategy readouts, capability decks, workshops, case studies, consulting proposals |
| Tone | Confident, intimate, modern, human |
| Sources | Specs (55) `_spec_screens_ascii/`; R2 examples (40) `_examples_r2_ascii/` + `more examples r2/`; local brand kit; user hard feedback through v4 |

### Provenance note

There is **no Markdown brand manual** inside the source `mblm assets` kit. Brand rules were derived from official slides/specs screenshots, R2 consulting examples, SVGs, the brand-kit screenshot, layout compositions, and user locks. Agents must **analyze** visual references (specs **and** R2) before authoring.

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| primary | `#000000` | Black |
| primary-inverse | `#FFFFFF` | White |
| brand-accent | `#FFF200` | Yellow — fills/floods **not lines**; **not text on black** |
| main-gray | `#BFBFBF` | Official main gray |
| bg-warm | `#F3EEE5` | Kit warm surface (cream `#FCF5EB*` for gradients) |
| cyan | `#00AEFF` | Official cyan; line OK |
| mid-blue | `#006AF1` / `#0068EB` | Mid blue family; line OK |
| dark-navy | `#002A60` | Preferred card-header line |
| secondary greens / magentas / purples | see `COLORS.md` | Asterisk = gradients only |

**Lines**: `LINE_RULES.md` — no yellow lines; blue-only above cards; white-only text on black fills.
**Gradients**: mainly section dividers — see `COLORS.md`.

## III. Typography (v4)

| Role | Family | Weight / size |
|---|---|---|
| cover title | BentonSansCond | **Light 60 or 72** (prefer 72) |
| cover subtitle | BentonSansCond | **24 or 32** (prefer 28–32) |
| agenda / content page title | BentonSansCond | **Light 47** |
| content page title | BentonSansCond | **Light 47 only** |
| content subtitle | BentonSansCond | **Regular 18 or 20** (prefer 20) |
| body | BentonSansCond | **Regular 16 or 20** locked deck-wide (**prefer 20**) |
| accents < ~24px @ 1280 | BentonSansCond | **Bold** |
| topic headers | BentonSansCond | **Medium** |
| Supertext | BentonSansCond | **Black** outline **1.25pt**, edge-to-edge (≠ page headline) |

**Editable text**: one object per paragraph — `TEXT_BOXES.md`. Normal kerning; **no kickers**.

User Mac: Benton installed — use it. Fallback elsewhere: Arial Narrow → Arial (`TYPOGRAPHY.md`).

## IV. Logo

- Files: `../assets/logos/MBLM_LOGO_White background.svg`, `MBLM_LOGO_dark background.svg`, `MBLM_LOGO_Brand color.svg`, `MBLM_LOGO_Yellow background.svg` (framed inverse, legacy export name)
- Usage: every cover + closing; section headers / brand bars may use oversized outlined watermark or vertical Supertext; content pages: corner mark top-right (R2)
- **v4.1 size**: content logo **88.4×44.2 @ 1148.2,39.7**; cover/divider/thanks **138×69 @ 40,40** (`LAYOUT_METRICS.md`)
- No tagline when logo present; no bottom MBLM wordmark if logo on slide
- Rules: `LOGOS.md`

## V. Layout DNA

- Specs: 2:1 Frame, black brand bars, photo+bar, mesh (section dividers), Supertext
- R2: agenda J/K (r2_12, r2_40), solid card headers, tables, Gantt, pillars — see `LAYOUT_PATTERNS.md`
- Margins: `MARGINS.md` / `LAYOUT_METRICS.md` (**1.05 cm ≈ 39.7/40 px** all sides)
- Bullets: `BULLETS.md` (round black circles)
- Text boxes: `TEXT_BOXES.md`

## VI. Voice & Tone

- Formality: professional-intimate (agency)
- Person: we / you
- Emoji: forbidden (default)
- Abbreviations: spell-out-first for client terms; MBLM product names as provided

## VII. Icon Style

- Preference: linear / thin-stroke geometric (kit icons + Black Glyphs reference spec_55)
- Prefer kit icons over generic libraries for MBLM service metaphors
- Always quote paths for `MBLM_ UI-UX Design.svg` (leading space in filename)

## VIII. Visual Assets

- Layouts: `../assets/layouts/*.svg`
- Brand intimacy graphics: `../assets/brand-intimacy/`
- Photography direction: `IMAGERY.md` + composition specs
- Specs catalog: `visual-references/CATALOG.md`
- R2 catalog: `visual-references/CATALOG_R2.md`
- Screenshot board: `../assets/brand-kit-screenshot.png`
