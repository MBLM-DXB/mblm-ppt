# MBLM Line Rules (HARD — v2 + v3.0.0)

These rules override any conflicting usage visible in older kit SVGs or occasional composition / R2 screenshots.

## 1. Yellow lines forbidden

- Do **not** use yellow (`#FFF200` or any other yellow/gold/amber) as:
  - vertical divider lines
  - horizontal divider lines
  - accent hairlines
  - underlines meant as structural rules
- Yellow **is** allowed as:
  - large background fills / floods
  - chart highlight fills
  - milestone marker **fills** (dots/diamonds)
  - Supertext **outline strokes** (graphic, not a divider) at **1.25pt**
  - mesh gradient stops

If a visual-reference screenshot shows a yellow vertical guide under a headline, **do not copy that line color** — substitute blue family (below) or omit the line.

## 2. Lines above squares / cards

- If a line sits **on top of** a colored square, card, or module as a header accent:
  - It must be **MBLM dark blue or blue only**.
  - Preferred tokens:
    - `#002A60` — dark navy (preferred default for card-header lines)
    - `#006AF1` — mid blue
    - `#00AEFF` — cyan
    - `#0068EB` — kit secondary blue (alias of mid-blue family; OK for new work)
- **Never** use rainbow, yellow, magenta, green, orange, or multi-color bars as card headers / lines-above-shapes.

## 3. Black-box text & accents (v3 HARD)

On **black fills** (header bars, chevrons, logo-adjacent black modules, KPI tiles, table headers when black):

- Use **white font only**
- **No yellow text** on black
- **No blue accent lines** on / attached as decoration to black boxes

Blue may still be used as **separate** filled modules (e.g. adjacent blue column header) — not as a stroke/line ornament on the black box itself.

## 4. Allowed non-yellow structural lines

| Context | Allowed |
|---|---|
| White on black / blue panels | Thin white vertical guides |
| Black on yellow / white fields | Thin black structural rules |
| Light content masters | Light gray hairlines / frames (`#BFBFBF` family / lighter); dashed grey row/column separators (R2) |
| Spec callouts (docs only) | Blue callout lines as in type hierarchy sheet |
| Logo boxes | Black or white rectangular frames per `LOGOS.md` |
| Process connectors | Blue family strokes / nodes OK |

## 5. Prefer space over decoration

Official Ambition / pillar layouts and R2 executive layouts separate columns with **margin**, not heavy rules. Prefer breathing room; add a line only when it clarifies hierarchy — and then only per rules 1–4.

## 6. No line-box stacks (v3)

Do **not** build UI as many stroked rectangles stacked "box line by box line". Prefer **solid filled boxes** and paragraph text blocks (see agenda r2_12 + consulting content slides in `CATALOG_R2.md`).

## 7. Checklist before export

- [ ] No `#FFF200` (or yellow) used as a line/stroke divider
- [ ] Any line above a card/square is blue-family only
- [ ] Black fills use white text only — no yellow type, no blue accent lines on black
- [ ] Supertext outlines are intentional graphics (1.25pt), not mistaken for dividers
- [ ] No multi-color "rainbow" header bars on modules
- [ ] No stroked rectangle stacks as primary UI
