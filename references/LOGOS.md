# MBLM Logo Usage

Bundled lockups live in `assets/logos/`. **v4.1.0 persistent geometry** — see [`LAYOUT_METRICS.md`](LAYOUT_METRICS.md) for cm + px. Visual examples: specs 03–04, 13–16, 34+; R2 content slides (logo top-right, no tagline).

| File | Appearance | When to use |
|---|---|---|
| `MBLM_LOGO_White background.svg` | Black wordmark + black rectangular frame on transparent/white | Light backgrounds (white, off-white, cream) |
| `MBLM_LOGO_dark background.svg` | White wordmark + white rectangular frame | Dark / black backgrounds |
| `MBLM_LOGO_Brand color.svg` | Black wordmark on solid `#FFF200`, **no** rectangular frame | Official **brand-color** lockup (yellow fields) |
| `MBLM_LOGO_Yellow background.svg` | White wordmark inside black rectangle | **Framed inverse (legacy export name)** — use only when matching an existing layout that embeds this exact asset; **not** for brand-color fields |

## Brand-kit + specs lockups (authority for naming)

1. **Positive** — black mark + border on white → `MBLM_LOGO_White background.svg`
2. **Negative** — white mark + border on black → `MBLM_LOGO_dark background.svg`
3. **Brand color** — black mark on solid yellow `#FFF200`, no border → `MBLM_LOGO_Brand color.svg`
4. **Solid / Keyline / Supertext** (spec_03) — horizontal logo as bold anchor, cornerstone, or portal/Supertext to images; black, white, or transparent to background

## Placement by slide type (v4.1.0 HARD)

| Page role | Logo behavior |
|---|---|
| **Content** (agenda, value prop, ICP, tables, cards, etc.) | Top-**right** framed mark — **fixed** metrics below |
| **Cover / section divider / thank-you** | Top-**left** larger mark — **fixed** metrics below |
| Photo + brand bar | Prefer content or cover rule for the primary lockup; vertical Supertext in bar OK |
| Framed masters | Atmospheric outlined MBLM Supertext at edges OK sparingly (not a substitute for the corner lockup) |

## Size + position (v4.1.0 — persistent on EVERY slide)

Scale: **37.795 px/cm** (1280 / 33.867).

### Content-slide logo (NOT cover / divider / thank-you)

| Property | cm | px |
|---|---|---|
| Width | **2.34** | **≈88.4** |
| Height | **1.17** | **≈44.2** |
| X (left) | **30.38** | **≈1148.2** |
| Y (top) | **1.05** | **≈39.7** |

Apply **identically** on every content slide.

```xml
<image href="../images/logo-light.svg" x="1148.2" y="39.7" width="88.4" height="44.2"/>
```

### Cover / section divider / thank-you logo

| Property | cm | px |
|---|---|---|
| Width | **3.65** | **≈138** |
| Height | **~1.825** (≈2:1) | **≈69** |
| X (left) | **1.05** (left-aligned at margin) | **≈40** |
| Y (top) | **1.05** | **≈40** |

```xml
<image href="../images/logo-dark.svg" x="40" y="40" width="138" height="69"/>
```

**Supersedes** v4 ~70–80px corner and v3 ~140×72 — do not use those sizes on new decks.

## Rules

- Keep the rectangular frame with the wordmark when using positive/negative lockups — do not crop to letters alone unless matching Supertext/keyline treatments the user asks for.
- Brand-color lockup intentionally has **no** frame (black letters on `#FFF200` only).
- Never recolor the logo to arbitrary secondary hues (no blue logo, no magenta logo).
- Clear space: keep at least ~0.5× logo-height padding from other content (within `MARGINS.md` / `LAYOUT_METRICS.md` insets).
- Yellow behind the logo is a **field**, not a line accent.

### HARD — tagline & bottom wordmark

1. When the logo **is present** on a slide: **remove / do not add** the tagline **"The Brand Intimacy Agency"**.
2. When the logo **is present**: **do not add** an MBLM wordmark or "MBLM" text at the **bottom** of the slide (footer = page # / Source / footnotes only).
3. Title top aligns with logo top (`TYPOGRAPHY.md`).
