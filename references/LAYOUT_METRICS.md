# MBLM Layout Metrics (HARD — v4.1.1 persistent lock)

**Canvas:** SVG **1280 × 720**  
**PowerPoint 16:9 slide:** **33.867 cm × 19.05 cm** (13.333″ × 7.5″)

## Scale

```text
scale = 1280 / 33.867 = 720 / 19.05 ≈ 37.795 px/cm
```

Convert: `px = cm × 37.795` · `cm = px / 37.795`  
Document **both** units everywhere geometry is locked. Prefer exact cm→px products below; authoring may round to nearest 0.1 px or use the **practical px** token in the rightmost column.

---

## Margins (ALL sides — every slide)

| Edge | cm | Exact px (×37.795) | Practical SVG token |
|---|---|---|---|
| Left | **1.05** | **≈39.7** | **40** |
| Right | **1.05** | **≈39.7** | **40** |
| Top | **1.05** | **≈39.7** | **40** |
| Bottom | **1.05** | **≈39.7** | **40** |

```text
MARGIN = 1.05 cm ≈ 39.7 px   # use 40 px inset for content safe area, or exact 39.7
CONTENT_SAFE_X = 40
CONTENT_SAFE_Y = 40
CONTENT_SAFE_W = 1280 − 80 = 1200
CONTENT_SAFE_H = 720 − 80 = 640
```

Content and logo **vertical** alignment use this **top** margin (title top ≈ logo top ≈ `MARGIN_T`).

**Supersedes** v3/v4 L/R ~62 / bottom ~45 — those are revoked for new work.

---

## Content-slide logo (NOT cover / section divider / thank-you)

Identical on **every** content slide (agenda, value prop, ICP, tables, checklists, etc.):

| Property | cm | Exact px | Practical SVG |
|---|---|---|---|
| Width | **2.34** | **≈88.4** | **88.4** (or **88**) |
| Height | **1.17** | **≈44.2** | **44.2** (or **44**) |
| X (left) | **30.38** from left | **≈1148.2** | **1148.2** (or **1148**) |
| Y (top) | **1.05** from top | **≈39.7** | **39.7** (or **40**) |

Aspect ≈ **2:1**. Lockup: positive (light bg) or negative (dark bg) per `LOGOS.md`.

```xml
<!-- Content slide — top-right framed logo (LOCKED) -->
<image href="../images/logo-light.svg" x="1148.2" y="39.7" width="88.4" height="44.2"/>
```

Right edge check: `1148.2 + 88.4 = 1236.6`; inset from right `1280 − 1236.6 = 43.4` ≈ margin band.

---

## Cover / section divider / thank-you logo

| Property | cm | Exact px | Practical SVG |
|---|---|---|---|
| Width | **3.65** | **≈138** | **138** |
| Height | **~1.825** (2:1 lockup) | **≈69** | **69** |
| X (left) | **1.05** (left-aligned at margin) | **≈39.7** | **40** |
| Y (top) | **1.05** | **≈39.7** | **40** |

```xml
<!-- Cover / divider / thank-you — top-left larger logo (LOCKED) -->
<image href="../images/logo-dark.svg" x="40" y="40" width="138" height="69"/>
```

On yellow flood covers use brand-color or framed inverse per `LOGOS.md`; position/size still match this table.

---

## Content-slide titles + subtitles (vertical alignment)

| Role | Rule |
|---|---|
| **Content page title** | BentonSansCond **Light** **47pt only** — never 54, never 24, never 32, never 28–36 |
| Agenda “Content” title | **Content slide** → **47pt** (overrides prior ≥72pt agenda rule) |
| Cover / hero title | **60–72** Light still allowed **only on cover** |
| Divider / thank-you titles | Follow their pattern (large display / Supertext); **not** content-title band |
| **Title top edge** | **1.05 cm** from slide top (same Y as content logo top / top margin ≈ **39.7 px**) |
| **Title / subtitle X** | Left-aligned in content area at left margin **1.05 cm ≈ 39.7 / 40 px** |
| **Subtitle** | Directly under title with normal gap; color **black `#000000`** (never dark grey) |

With alphabetic SVG baseline, set title `y` so the **visual top** of 47pt caps sits at ≈39.7 px (≈ `y ≈ 75` for BentonSansCond Light 47). Subtitle baseline follows with a normal gap (~40 px below title baseline). Do **not** leave title baseline at 90 when the logo top is at 39.7.

---

## Supertext

| Token | Lock |
|---|---|
| Minimum size | **≥150pt** |
| Fit | Increase as needed so word(s) run **edge-to-edge** vertically or horizontally (within margins) |
| Stroke | **1.25pt** (keep unless clearly wrong at 150pt+ — default keep **1.25pt**) |
| Weight | BentonSansCond **Black**, outline only; must **not** repeat page headline |

---

## Authoring checklist (every SVG)

1. Margins ≥ 1.05 cm / ~40 px on all sides for content.  
2. Content slides: logo at **x=1148.2 y=39.7 w=88.4 h=44.2** (or practical integers above).  
3. Cover / divider / thank-you: logo at **x=40 y=40 w=138 h=69**.  
4. Every content title: `font-size="47"`; top edge at **1.05 cm / ≈39.7**; left at margin.  
5. Content subtitle under title (normal gap); fill **`#000000`**.  
6. Supertext (if present): `font-size` ≥ **150**.  
7. Spot-check **every** SVG before export.

## Related

- `MARGINS.md` · `LOGOS.md` · `TYPOGRAPHY.md` · `LAYOUTS.md` · `SKILL.md` hard freeze v4.1.1
