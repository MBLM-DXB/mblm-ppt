# MBLM Typography

Locked **v4.2.1 type freeze** (2026-09-12): content titles **Light 40pt**; body **Regular 16–18pt** min; **Medium / MediumSC banned**. See `LAYOUT_METRICS.md`, `RESOLVED_DECISIONS.md`, `TEXT_BOXES.md`.

## Official family

**BentonSansCond** (Benton Sans Condensed) is the **primary** face. On the user’s Mac it **is installed** under `~/Library/Fonts/` — generation on this machine must use Benton, not fallbacks.

### Allowed faces (user Mac)

| File (under `~/Library/Fonts/`) | PostScript name | Role (v4.2.1) |
|---|---|---|
| `BentonSansCond-Light.otf` | `BentonSansCond-Light` | Cover / content titles; agenda section labels |
| `BentonSansCond-LightIta.otf` | `BentonSansCond-LightItalic` | Light italic |
| `BentonSansCond-Regular.otf` | `BentonSansCond-Regular` | **Body copy** (16 or 18pt) |
| `BentonSansCond-RegIt.otf` | `BentonSansCond-RegularItalic` | Body italic |
| `BentonSansCond-Bold.otf` | `BentonSansCond-Bold` | Emphasis / topic headers / accents (replaces former Medium) |
| `BentonSansCond-BoldIta.otf` | `BentonSansCond-BoldItalic` | Bold italic body emphasis |
| `BentonSansCond-Black.otf` | `BentonSansCond-Black` | Highlighted copy within phrase; **Supertext** (outline) |

### Banned faces (do not use in new work)

| File | PostScript name | Status |
|---|---|---|
| `BentonSansCond-Medium.otf` | `BentonSansCond-Medium` | **BANNED** — use **Bold** instead |
| `BentonSansCond-MedIt.otf` | `BentonSansCond-MediumItalic` | **BANNED** |
| `BentonSansCond-MediumSC.otf` | `BentonSansCond-MediumSC` | **BANNED** |
| `BentonSansCond-MedItSC.otf` | `BentonSansCond-MediumItalicSC` | **BANNED** |

Also installed (non-condensed): Benton Sans Regular / Italic / Bold / Bold Italic. Treat **BentonSansCond** as kit authority.

---

## HARD weight + size rules (v4.2.1 — impossible to miss)

1. **Headers / primary headlines** → BentonSansCond **Light** (not Bold fill for titles, not Black fill).
2. **Cover title** → **60pt or 72pt** Light (prefer **72** when it fits). **Cover only**.
3. **Cover subtitle** → **24pt or 32pt** (prefer **28–32**).
4. **Content-slide titles** (agenda page title, value prop, ICP, tables, **all** non-cover / non-divider / non-thank-you) → Light **40pt only**. Never 47, never 54, never 24–36 as content titles.
5. **Agenda page title** → content slide → **40pt** Light. Section labels on `39_r2_40_section_agenda` → **50pt** Light.
6. **Divider / thank-you titles** → follow their pattern (large display / Supertext); not the content-title band.
7. **Content-slide subtitle** (under title) → **18pt**, fill **`#000000` only**. Place **directly under** the title; left-aligned at **1.05 cm**.
8. **Body / general content text** → **16pt or 18pt** Regular — lock **one** size deck-wide. Prefer **18pt**. Never below **16pt** for body.
9. **Title alignment** → title **top edge** at **1.05 cm / ≈39.7 px**; left at **1.05 cm** — `LAYOUT_METRICS.md`.
10. **Accents / emphasis / topic headers** → **Bold** (never Medium).
11. **Highlighted copy** inside a sentence → **Black**.
12. **Kerning / tracking** → **normal**. Do **not** expand letter-spacing.
13. **No kickers** → never above the title.
14. **Editable text** → one text object per paragraph (`TEXT_BOXES.md`).
15. **Supertext** (atmospheric outline graphic):
    - BentonSansCond **Black**
    - Outline only (no fill), stroke **1.25pt**
    - Size **minimum 150pt**; edge-to-edge within margins
    - Must **NOT** repeat the page headline

### SVG authoring scale (exporter)

PowerPoint often maps SVG `font-size` × **0.75** → pt. Author desired sizes as:

| Desired pt | SVG `font-size` (= pt / 0.75) |
|---|---|
| 40 (content title) | **53.3** |
| 50 (agenda section labels) | **66.7** |
| 18 (body / subtitle) | **24** |
| 16 (body min) | **21.3** |

Templates already using exporter scale (e.g. titles `53.3`, body `21.3`) — **keep scale**. Unscaled “pt-as-SVG” templates — set body ≥**16** and titles to Light face + **40** (or migrate to 53.3 when converting to scaled authoring).

### Hierarchy sheet mapping (v4.2.1)

| Role | Weight |
|---|---|
| Primary Headline | Light |
| Secondary / topic header | **Bold** (not Medium) |
| Highlighted Copy | Black |
| Body Copy | Regular / Reg. Italic / Bold / Bold Italic |

---

## Tagline

Official descriptor: **"The Brand Intimacy Agency"**.

**Hard rule**: when the MBLM **logo is already on the slide**, **do not** place the tagline on that slide. Do not add an MBLM wordmark/text at the bottom either (`LOGOS.md`).

## Size guidance (@ 1280×720) — v4.2.1

| Role | Size | Weight |
|---|---|---|
| **Cover title** | **60 or 72** (prefer 72) — cover only | Light |
| **Cover subtitle** | **24 or 32** (prefer 28–32) | Regular or Light |
| **Content page title** (incl. Agenda page title) | **40 only** (SVG 53.3) | Light |
| **Agenda section labels** (r2_40) | **50** (SVG 66.7) | Light |
| **Divider / thank-you title** | Pattern-specific large / Supertext | Light or Black outline |
| **Content subtitle** under title | **18**; **`#000000`** | Regular |
| **Body / cards / bullets** | **16 or 18** locked deck-wide (**prefer 18**) | Regular |
| Topic header / card label | ~18–22 | **Bold** |
| Accent line &lt;24 | ~12–22 | **Bold** |
| Supertext | **≥150**; edge-to-edge | Black outline **1.25pt** |
| KPI number | large display | Black or Light + small Regular label |
| Table header | ~12–16 | Bold; **normal kerning** |
| Page number | ~12 | Regular |

## Fallbacks (other machines only)

1. `Arial Narrow` → 2. `Arial`  
Record substitution; never claim Benton if substituted. On the user’s Mac, always Benton.

## Voice

- Formality: professional, intimate, confident (agency — not stiff consulting-ese).
- Person: we / you.
- Emoji: forbidden in client decks unless explicitly asked.
- Abbreviations: spell out on first use for client-facing terms; MBLM product names may stay as given.
