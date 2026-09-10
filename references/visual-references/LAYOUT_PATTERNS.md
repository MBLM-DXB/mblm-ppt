# MBLM Layout Patterns (from official specs)

Synthesized from 55 specs screenshots (`_spec_screens_ascii/`) + **R2 consulting examples** (`_examples_r2_ascii/`, 40 PNGs) + user hard rules (**v3.0.0**, 2026-09-10). Agents must **mimic these patterns**, not invent McKinsey/BCG consulting chrome.

Canonical catalogs: [`CATALOG.md`](CATALOG.md) (specs) · [`CATALOG_R2.md`](CATALOG_R2.md) (R2 examples).
- Specs ASCII: `${MBLM_MASTER_ROOT}/skill/_spec_screens_ascii/`
- Specs original: `${MBLM_MASTER_ROOT}/MBLM slides and other specs/`
- R2 ASCII: `${MBLM_MASTER_ROOT}/skill/_examples_r2_ascii/`
- R2 original: `${MBLM_MASTER_ROOT}/more examples r2/`

Canvas for ppt-master authoring remains **1280×720** (16:9). Spec "2:1 Frame" refers to **logo-proportioned content windows / panel ratios**, not a change of slide aspect.

---

## Pattern A — Yellow flood cover / closing

**Seen in**: spec_04, spec_34, spec_54

- Full-bleed solid `#FFF200` (or yellow-dominant mesh).
- Boxed MBLM lockup top-left (black box / white letters, or inverse as needed).
- Primary headline BentonSansCond **Light**, left-aligned, generous negative space.
- Closing may use huge outlined Supertext mood phrase (e.g. THANK YOU) — Black outline **1.25pt** (v3; was ≥2pt) — **must not** duplicate a smaller headline.
- Yellow is a **field**, never a hairline divider.

## Pattern B — 2:1 Frame (logo-proportion window)

**Seen in**: spec_13–16

- Content window that "mimics the proportions of our logo"; used as window into content or section divider.
- Typical vertical split: solid brand field (yellow or black) ~⅔–¾ + opposite bar ~¼–⅓.
- Bar often holds **vertical Supertext** (Black outline) or soft mesh gradient.
- Boxed logo anchors a corner of the solid field.
- Headline **Light**; body **Regular**; optional thin **white** vertical guide inside dark bars (not yellow).

## Pattern C — Photo + black vertical brand bar

**Seen in**: spec_05, spec_16–17, spec_26

- Solid black vertical bar (~20–30% width) left or right.
- Remaining width = full-bleed atmospheric photography (golden hour, silhouette, high contrast OK).
- Bar contains vertical outlined Supertext / MBLM (stroke may be white, yellow, or secondary gradient — stroke ≠ "divider line").
- Optional boxed logo on the photo side (corner).
- Prefer editorial intimacy over stock "handshake" corporate photos.

## Pattern D — Three-panel editorial strip

**Seen in**: spec_19–23, spec_25, spec_28–29

- Vertical panels: brand bar | photo or gradient | content (order varies).
- Brand bar: black + vertical outlined Supertext (MBLM or mood word).
- Content panel: solid brand color (blue `#006AF1`/`#0068EB`, yellow, or mesh gradient) with Light headline → Bold accent (<24) → Regular body.
- Thin **white** vertical guide under headline common; **never** yellow/magenta/green/rainbow card-header bars.
- Soft mesh multi-color (≥3) encouraged on gradient panels.

## Pattern E — Full-bleed photo + Supertext overlay

**Seen in**: spec_30–33, spec_43

- Full-bleed photo or dark graphic field.
- Large outlined Supertext mood word (INSPIRE / ASPIRE / EXPRESSION) as atmospheric layer; may sit behind subject silhouette; may crop at edge.
- Readable headline elsewhere in **Light**; body **Regular**; logo boxed in a corner.
- No consulting-style top accent bar.

## Pattern F — White / black framed masters (official PPTX DNA)

**Seen in**: spec_35–41, spec_53

- Thin structural frames (light gray on white, white on black) defining title band + content well.
- Logo: black box / white MBLM (light slides, top-right) or white-outline box / white MBLM (dark slides).
- Title = Light; subhead/topic = Medium; body = Regular.
- Page number bottom-right.
- Ghosted edge Supertext (faint MBLM repeats) optional atmospheric branding (spec_37, spec_39).
- **No** multi-color bars on top of content cards.

## Pattern G — Gradient field + vertical Supertext

**Seen in**: spec_45–52

- Soft mesh background (pastel cyan/lime, yellow flood mesh, or cyan→navy→black).
- Optional thin inner safe-frame.
- Light headline left or center; large vertical outlined MBLM Supertext on right margin.
- Supertext stroke may be black, white, cyan, or yellow→orange gradient — still not a divider line.

## Pattern H — Ambition / pillar storytelling

**Seen in**: spec_01–02

- Soft warm mesh background.
- Light page title; three columns (WHAT / HOW / WHY) separated by **space only**.
- Medium column headers; Bold key claims; Regular paragraphs; thin-line kit icons.

## Pattern I — Card / module stacks (when used)

When authoring multi-card pages (four_card, KPI tiles, etc.):

- Card fills: white, off-white/cream, black, yellow, or solid blue — from palette.
- If a line sits **above** a square/card, it must be **blue family only**: `#002A60`, `#006AF1`, `#00AEFF`, or kit alias `#0068EB`.
- Forbidden above cards: yellow, magenta, green, rainbow, multi-stop accent bars.
- Prefer spatial separation / thin gray structural hairlines over decorative accent bars.

---

## Recurring geometry signatures

| Element | Rule |
|---|---|
| Vertical brand bar | Black (or solid yellow); ~20–30% width; Supertext or logo |
| Boxed logo | Rectangular lockup; do not free-float wordmark unless Path C native |
| Supertext | Black weight, outline **1.25pt**, edge-to-edge when used; short mood word OR brand name; cropable; ≠ page headline |
| Mesh gradients | ≥3 colors preferred; soft pools; asterisked hexes for gradient construction |
| Structural frames | Thin gray (light slides) or white (dark slides) |
| Pagination / chevrons | Web UI in specs — optional in PPTX; not brand-required |

## Anti-patterns (do not invent)

- McKinsey/BCG navy top bars, teal process chevrons, generic consulting icon grids as the visual system.
- Yellow (`#FFF200`) hairline dividers or accent lines.
- Rainbow / yellow / magenta / green lines sitting on top of colored squares as "card headers."
- Supertext that repeats the slide headline.
- Two-stop-only gradients as the only gradient language (mesh ≥3 is preferred for signature moments).


---

## R2 patterns (consulting proposal examples — v3.0.0)

Source: [`CATALOG_R2.md`](CATALOG_R2.md). Apply User overrides (no kickers; round black bullets; tighter margins; white on black; no tagline with logo).

## Pattern J — Agenda / Content numbered TOC ★ GOLD STANDARD

**Seen in**: r2_12 (primary)

- White field; Light title **"Content"** (or Agenda / Contents / Overview) top-left ≤40pt; logo top-right; tops aligned; **no kicker**
- Horizontal row of solid **black circles** with white numbers **01…N**
- Thin dashed grey horizontal spine through circle centers
- Below each: Bold section name + Regular/Light short description, centered
- Page # bottom-right only; no tagline; no bottom MBLM wordmark
- Margins per `MARGINS.md` (~62 sides / ~45 bottom)
- **This is the structural gold standard** for list/agenda layouts agents must mimic

## Pattern K — Section agenda on gradient ★ GOLD STANDARD (divider)

**Seen in**: r2_40

- Full-bleed blue→navy (or brand) **gradient** — allowed because this is a **section divider**, not ordinary content
- White-outline or negative MBLM lockup top-left; **no tagline**
- Right-aligned vertical stack of section names (active = white; inactive = grey)
- Light weight; **normal kerning**; white/grey on dark only (no yellow text)
- Use at chapter breaks; do not put full-bleed gradients on ordinary white content slides

## Pattern L — Two-column compare / From–To

**Seen in**: r2_03, r2_04

- Light title; logo top-right; no kicker
- Two columns with solid header bars (black and/or blue); white text on dark fills
- Body Regular; optional dashed row separators; diagram triangles OK as connectors
- List bullets (if any) = round black circles

## Pattern M — N-column pillars / cards

**Seen in**: r2_05, r2_09–11, r2_15–16, r2_19–21, r2_24

- Equal columns; solid black/blue/navy headers **or** icon circles
- White text on black/dark fills only
- Bodies: Regular paragraphs or **round black bullets** with hanging indent
- Prefer solid filled modules over stroked rectangle stacks
- Optional thin grey dashed vertical gutters

## Pattern N — Process / SCR / chevron flow

**Seen in**: r2_06–07, r2_22–23, r2_27, r2_30, r2_39

- Solid black/blue chevrons or label boxes with **white** text
- Blue family connectors/nodes OK; yellow only as marker **fills** (not divider lines)
- Avoid adapting stroked empty box stacks (r2_07 anti-pattern) — prefer solid fills + text blocks

## Pattern O — Timeline / Gantt / milestones

**Seen in**: r2_14, r2_25, r2_28–31

- Dark/black header bars with white week/phase labels
- Blue activity bars; yellow dots/diamonds as milestone **fills** OK
- Thin grey grid / dotted guides; Source + page # footer
- No kickers above title

## Pattern P — Table / matrix

**Seen in**: r2_34–36

- Header row: MBLM dark blue / blue / black / grey fill; **white or high-contrast** text; **kerning normal**
- Body: zebra or open rows; thin grey dashed/solid separators
- No yellow text on black; no blue accent lines on black header cells
- Solid header fills — not line-box stacks

## Pattern Q — Photo + list / case strip

**Seen in**: r2_13, r2_37

- Solid grey list well + photo, or photo grid with black title bars (white text) under images
- Round black bullets in list wells

## Pattern R — Org / scope tree

**Seen in**: r2_26, r2_33

- Solid color nodes (black in-scope with white text; grey out-of-scope; blue roots/mgmt)
- Thin connectors; optional round black bullets for responsibilities

## Pattern S — Program overview (chevrons + core elements)

**Seen in**: r2_39

- Multi-phase chevron bar + summary row + numbered columns with round black bullets
- White content field; no full-bleed gradient on this content overview

---

## v3 geometry / anti-pattern updates

| Element | v3 rule |
|---|---|
| Title | ≤40pt Light; top aligned to logo; normal kerning; **no kicker** |
| Margins | ~62 L/R, ~45 bottom (`MARGINS.md`) |
| Bullets | Round **black** circles, Ø ≈ 50% text size (`BULLETS.md`) |
| Supertext | Outline **1.25pt**; edge-to-edge; ≠ page headline |
| Black fills | White text only — no yellow type, no blue accent lines on black |
| Gradients | Mainly section dividers (Pattern K / G); not ordinary content full-bleeds |
| Logo | No tagline when logo present; no bottom MBLM wordmark if logo on slide |
| UI construction | Solid filled boxes + paragraph blocks — **no line-box stacks** |
| Agenda | Mimic Pattern J (r2_12) and/or K (r2_40) |

### Additional anti-patterns (R2)

- Copying blue triangle / checkmark / dash bullets from template screenshots
- Kickers such as "Real-life case example" above or as eyebrow over titles (r2_38)
- Expanded letter-spacing on titles
- Full-bleed mesh/gradient behind dense white consulting content slides
