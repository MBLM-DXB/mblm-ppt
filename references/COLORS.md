# MBLM Color Tokens

Provenance (v2 — 2026-09-10 afternoon; **v3.0.0** margin/gradient/black-box locks; **v4.1.1** table/chrome locks):
1. Official palette screenshots `spec_09`–`spec_12` (authority for main/secondary/gradient system).
2. Kit `assets/palette/**/*.svg` + brand-kit screenshot (prior lock; kept where still valid).
3. Line rules — see **`LINE_RULES.md`** (yellow never as lines; blue-only lines above cards).

## Primary (main palette — spec_09)

| Token | HEX | Role |
|---|---|---|
| `yellow` | `#FFF200` | Primary brand color (PMS Process Yellow C). **Fills / floods / highlights — NOT divider lines.** |
| `black` | `#000000` | Primary brand, section/title backgrounds, wordmark |
| `gray` | `#BFBFBF` | Main gray (borders, muted UI, table lines) |
| `white` | `#FFFFFF` | Light backgrounds, reverse text |

## Secondary ramps (spec_10–11)

Asterisk (`*`) = **for constructing gradients only** (official footnote).

### Neutrals / grayscale

`#FFFFFF` · `#BFBFBF` · `#808080` · `#404040` · `#000000`

### Warm / yellow ramp

| HEX | Notes |
|---|---|
| `#FCF5EB*` | Cream (gradient) |
| `#FFF68E*` | Pale yellow (gradient) |
| `#FFF200` | Yellow (primary) |
| `#FFB300*` | Amber (gradient) |
| `#552A00*` | Dark brown (gradient) |

### Green ramp

| HEX | Notes |
|---|---|
| `#E6F2E6*` | Pale mint (gradient) |
| `#A0EC93*` | Light lime (gradient) |
| `#00D300` | Vibrant green (spec; see conflict note) |
| `#00A400*` | Forest green |
| `#005000*` | Dark evergreen |

### Cyan / blue ramp (also **line-above-card** family)

| HEX | Notes |
|---|---|
| `#E3F8FA*` | Pale cyan |
| `#8DE1F5*` | Light cyan |
| `#00AEFF` | **Cyan** (PMS Process Cyan C) — line OK |
| `#006AF1*` | Mid blue — line OK |
| `#002A60*` | **Dark navy** — **preferred** card-header line |
| `#0068EB` | Kit secondary blue — **alias of mid-blue family**; line OK |

### Purple ramp

| HEX | Notes |
|---|---|
| `#F0E2F5*` | Pale lavender |
| `#E3B8F3*` | Light purple |
| `#9700DC` | Purple (spec primary purple) |
| `#6A009D*` | Mid purple |
| `#370050*` | Dark purple |

### Magenta ramp

| HEX | Notes |
|---|---|
| `#FBE2ED*` | Pale pink |
| `#FFA9DA*` | Light magenta |
| `#EC008C` | **Magenta** (PMS Process Magenta C) |
| `#D00049*` | Dark magenta (spec) |
| `#5E0021*` | Deep maroon |

## Kit aliases still valid for assets

These remain in `assets/palette/` and prior decks — map to nearest official token; do not invent new semantics:

| Prior kit token | HEX | Resolution |
|---|---|---|
| `off-white` | `#F3EEE5` | Keep for warm surfaces; cream `#FCF5EB*` is official gradient cream |
| `blue` | `#0068EB` | Alias of `#006AF1` family — OK for new work |
| `light-blue` / Accent | `#00B1F5` | Prefer official Cyan `#00AEFF` for new work; `#00B1F5` OK if matching old asset |
| `light-green` | `#00D200` | Prefer official `#00D300` for new work |
| `magenta` | `#FF008E` | Prefer official `#EC008C` for new work |
| `dark-magenta` | `#C1004B` | Prefer official `#D00049*` for gradients; `#C1004B` OK for flat kit continuity |
| `purple` / `light-purple` | `#60009A` / `#8C01D7` | Prefer `#9700DC` / `#6A009D*` for new work |
| `orange` | `#FFBA00` | Near `#FFB300*` — OK |

## Background defaults

| Surface | Prefer |
|---|---|
| Title / section / closing | `#000000` or yellow flood `#FFF200` |
| **Section dividers** | Full-bleed mesh/gradient OK (Pattern K) |
| **Ordinary content slides** | `#FFFFFF` or warm cream / `#F3EEE5` — **no full-bleed gradients** (v3) |
| Chart highlight fill | `#FFF200` (fill, not line) |
| **Table header** | **Only** MBLM Dark Blue `#002A60`, Black `#000000`, or **50% black** `#808080`; **white** (or high-contrast) text; normal kerning. No mid-blue `#006AF1` / cyan for table headers. |
| Table zebra / borders | light gray / `#EDEEEF`; borders `#BFBFBF` |
| **Graphics chrome** (bars, accents, icon fills used as chrome) | **MBLM primary colors only**: `#000000`, `#FFFFFF`, `#FFF200` (plus `#002A60` / `#808080` when the fill is a **table header**). Do **not** invent extra greys for chrome. |
| Blue content panels | Prefer dark navy `#002A60` for header-like panels; mid-blue family remains for lines-above-cards per `LINE_RULES.md` |
| Black fills (bars/chevrons) | **White text only** — no yellow type; no blue accent lines on black (`LINE_RULES.md`) |

## Gradients (v2 mesh preferred; **v3 — mainly section dividers**)

Official rule (spec_12): when creating gradients, **encourage more than 3 colors**; two of three in proximity of hue/tone + one unique blend for a soft mesh / aura (not only 2-stop linears).

Use asterisked ramp stops for gradient construction. Dark atmospheric meshes (black → color → highlight) appear in specs and compositions.

**v3**: Full-bleed gradients are **mainly for section dividers** (and signature cover/closing moments). Do **not** use full-bleed gradients as the background of ordinary consulting content slides — prefer white / off-white / photo / solid.

### Legacy two-stop pairs (still allowed for simple accents)

Even horizontal 0%→100% pairs from prior lock remain OK for simple accents, but **prefer mesh ≥3** for signature moments:

| Name | Start | End |
|---|---|---|
| magenta → orange | `#EC008C` or `#FF008E` | `#FFB300` / `#FFBA00` |
| yellow → light-green | `#FFF200` | `#00D300` / `#00D200` |
| cyan → purple | `#00AEFF` | `#9700DC` |
| blue → purple | `#006AF1` / `#0068EB` | `#9700DC` / `#60009A` |
| dark-magenta → magenta | `#D00049` / `#C1004B` | `#EC008C` / `#FF008E` |

## Contrast rules

- On black: text/logo/icons **white** (v3 — no yellow **text** on black); yellow OK as separate fills elsewhere; Supertext outlines white or gradient (stroke 1.25pt).
- On white / cream: text/logo black; accents from secondary.
- On yellow: black logo/text (brand-color lockup).
- Never low-contrast gray text on yellow or magenta.
- **Lines**: see `LINE_RULES.md` — no yellow lines; blue-only above cards.

## Do not

- Invent traffic-light success/warning/error tokens outside this palette.
- Use yellow as a divider/accent **line**.
- Put rainbow/yellow/magenta/green bars on top of cards.

- Put yellow **text** or blue accent **lines** on black boxes.
- Use full-bleed gradients on ordinary content slides (reserve for section dividers / covers).
- Use table header fills outside `#002A60` / `#000000` / `#808080`.
- Invent extra greys for bars / accents / chrome (use primary `#000000` `#FFFFFF` `#FFF200` only).
