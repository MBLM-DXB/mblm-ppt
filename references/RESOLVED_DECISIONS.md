# Resolved Decisions (locked 2026-09-10)

All former open items are closed. Do not re-open or invent interim alternatives.

## 1. Brand-color logo

- Official brand-color lockup = **black wordmark on solid `#FFF200`, NO rectangular frame** (matches brand-kit screenshot).
- File: `assets/logos/MBLM_LOGO_Brand color.svg` (letterform paths from `MBLM_LOGO_White background.svg` on a yellow `#FFF200` rectangle; outer frame path omitted).
- `MBLM_LOGO_Yellow background.svg` = **Framed inverse (legacy export name)** — white mark in black frame. Use **only** when matching an existing layout that embeds that exact asset. **Not** for brand-color fields.

## 2. Dark magenta

- Always `#C1004B`. No alternate / screenshot-approx language.

## 3. Typography / fonts

- **BentonSansCond IS installed** on the user’s Mac under `~/Library/Fonts/` (Light, Regular, Medium, Bold, Black + italics; also Benton Sans Regular/Bold/Italic).
- Primary face for generation on this Mac: **BentonSansCond** (see PostScript/file names in `TYPOGRAPHY.md`).
- Fallback only if Benton is missing on *another* machine: **Arial Narrow → Arial**. Record substitution if used.

## 4. Gradients

- Canonical **two-stop horizontal** gradients, even stops **0% → 100%** (brand-intimacy / palette SVGs had no machine-readable stop offsets; even stops locked):

| From | HEX | To | HEX |
|---|---|---|---|
| magenta | `#FF008E` | orange | `#FFBA00` |
| yellow | `#FFF200` | light-green | `#00D200` |
| light-blue | `#00B1F5` | light-purple | `#8C01D7` |
| blue | `#0068EB` | purple | `#60009A` |
| dark-magenta | `#C1004B` | magenta | `#FF008E` |

## 5. Official PPTX

- Do **not** auto-run Create Template on the ~70MB `MBLM_Power point _v1.pptx`.
- Paths A/B: skill brand assets + ppt-master engine.
- Path C: Edit Native on that PPTX via symlink at `assets/template/`.
- Policy also documented in `workflows/generate-mblm-pptx.md` and `PATHS.md`.

## 6. No MD brand manual in kit

- Closed fact: there is no Markdown brand manual inside the source `mblm assets` kit. Rules were derived from SVGs, brand-kit screenshot, and layout compositions. Provenance noted in `brand_spec.md` / README.

## 7. Icon `MBLM_ UI-UX Design.svg` leading space

- Filename leading space is intentional. **Always quote the path** in shell and tool calls.

## 8. Blue

- Always `#0068EB` for new work.
- `#006AF1` in layouts = **alias of blue** (same family); do not treat as a separate token.


---

## 9. Visual-analysis-first workflow (locked 2026-09-10 afternoon, Asia/Dubai)

- Skill **must** start with a visual reference pass: consult `references/visual-references/CATALOG.md` + `LAYOUT_PATTERNS.md` and the 55 ASCII-mirrored specs PNGs (and optionally re-scan `MBLM slides and other specs/`) **before** authoring SVGs.
- Design adapts official MBLM patterns (2:1 frames, black bars, Supertext, photo+bar, mesh gradients) — **not** McKinsey/BCG presets.

## 10. Yellow lines forbidden (locked 2026-09-10 afternoon)

- Do **not** use yellow (`#FFF200` or other yellows) as vertical or horizontal divider/accent **lines**.
- Yellow remains primary for **fills**, floods, chart highlight fills, and Supertext outline strokes.
- Documented in `LINE_RULES.md`. If a screenshot shows a yellow guide line, agents substitute blue family or omit.

## 11. Lines above squares/cards = blue only (locked 2026-09-10 afternoon)

- Lines sitting on top of colored squares/cards must be MBLM dark blue / blue family only: `#002A60` (prefer), `#006AF1`, `#00AEFF`, `#0068EB`.
- Never rainbow / yellow / magenta / green multi-color bars as card headers.
- Documented in `LINE_RULES.md`.

## 12. Typography weight locks (locked 2026-09-10 afternoon; sizes updated in §16)

From type hierarchy screenshot + user feedback:

| Role | Weight |
|---|---|
| Headers / primary headlines | BentonSansCond **Light** |
| Body | **Regular** |
| Accents when size &lt; ~24px @ 1280 | **Bold** |
| Topic headers | **Medium** |
| Medium otherwise | Only to emphasize within a phrase |
| Supertext | **Black** outline — **1.25pt** edge-to-edge; short mood words; must not repeat page headline |

## 13. Official palette expansion + hex conflict resolution (locked 2026-09-10 afternoon)

- Main palette per specs: Yellow `#FFF200`, Black `#000000`, Gray `#BFBFBF`, White `#FFFFFF`.
- Secondary ramps + asterisk = gradients-only (see `COLORS.md` / specs 10–11).
- Prefer official screenshot hexes for **new** work:
  - Cyan `#00AEFF` over kit `#00B1F5`
  - Mid blue `#006AF1` with kit `#0068EB` as alias (both OK)
  - Magenta `#EC008C` over kit `#FF008E`
  - Green `#00D300` over kit `#00D200`
  - Dark magenta `#D00049*` for gradients; `#C1004B` retained for flat kit continuity
  - Purple `#9700DC` / `#6A009D*` over kit `#60009A` / `#8C01D7`
- Gradients: prefer soft mesh ≥3 colors (spec_12); legacy even two-stop pairs remain allowed for simple accents.
- Kit SVG assets/logos unchanged; docs map aliases rather than rewriting asset files.

---

## 14. v3.0.0 hard rules retained where not overridden (2026-09-10 evening Asia/Dubai)

Still in force unless §16 says otherwise:

1. **Margins**: L/R and bottom **30% less** than prior (~80–96 → **56–67** prefer 62; bottom ~64 → **~45**). `MARGINS.md`.
2. **No kickers** — never above the title (zero tolerance).
3. **Supertext**: edge-to-edge; stroke **1.25pt**.
4. **No tagline** "The Brand Intimacy Agency" when logo present; **no bottom MBLM wordmark** if logo already on slide.
5. **Bullets**: round **black** circles; Ø ≈ **50%** of text size; proper indent (`BULLETS.md`).
6. **Kerning normal** — no expanded tracking on titles or body.
7. **No yellow text / blue accent lines on black boxes** — white font only on black fills.
8. **Gradients** mainly for **section dividers** — not full-bleed on ordinary content slides.
9. **Tables**: header dark blue/blue/black/grey; white/contrast text; normal kerning.
10. **No line-box stacks** — solid fills + paragraph blocks.
11. **Agenda gold standard**: r2_12 Content TOC + r2_40 section agenda (`CATALOG_R2.md`, Patterns J–K).
12. No yellow divider lines; blue-only lines above cards; Light headers / Regular body / Bold accents <24.

Visual pass must include R2 catalog + `more examples r2` / `_examples_r2_ascii/`.

## 15. R2 example set ingested

- 40 PNGs catalogued in `visual-references/CATALOG_R2.md`
- `LAYOUT_PATTERNS.md` extended with Patterns J–S
- Conflicts with v2 resolved in favor of user feedback above

## 16. User v4.0.0 hard rules (locked 2026-09-10 evening Asia/Dubai) — OVERRIDE conflicting v3

These **override** v3 title-cap and related size guidance:

1. **Editable text**: Never split a multi-line paragraph into one SVG/PPT text box per line. Use **one text object per paragraph** (tspans / soft breaks inside a single `<text>`). Documented in `TEXT_BOXES.md`. Do not export with `--no-merge`.
2. **Logo size**: Corner framed logo = **50% of v3 linear size**. Cap typical corner logo ~**70–80px wide** (was ~140–160). `LOGOS.md`.
3. **Cover title**: **60pt or 72pt** BentonSansCond Light (prefer **72** when it fits). Overrides v3 ≤40pt for covers.
4. **Cover subtitles**: **24pt or 32pt** (prefer **28–32**). Not 23.5.
5. **Body / general content**: **16pt or 20pt** Regular — lock one deck-wide; prefer **20pt** primary body.
6. **Content-slide subtitle** (under title): **18pt or 20pt**, consistent (prefer 20 with 20pt body).
7. **Agenda title** (e.g. “Content”): **at least 72pt** Light.
8. **Content-slide titles** (non-cover, non-agenda): Light **28–36pt**. Cover/agenda sizes win for those slide types.
9. All other v3 locks in §14 remain in force.

Scrub: no Twitter/X handles in skill docs; avoid unnecessary personal username callouts in prose — refer to **the user**.


## 17. User v4.1.0 persistent layout lock (locked 2026-09-10 evening Asia/Dubai) — OVERRIDE conflicting v4 geometry / title sizes

Documented in [`LAYOUT_METRICS.md`](LAYOUT_METRICS.md). Scale: SVG 1280×720 ↔ PPT 33.867×19.05 cm → **37.795 px/cm**.

1. **Margins**: **1.05 cm ≈ 39.7 px** on **all sides** (practical **40 px**). Revokes v3/v4 L/R ~62 / bottom ~45.
2. **Content-slide logo** (every content slide incl. agenda): **2.34×1.17 cm** → **≈88.4×44.2 px** at **x=30.38 cm / ≈1148.2 px**, **y=1.05 cm / ≈39.7 px**. Identical on every content slide.
3. **Cover / section divider / thank-you logo**: **3.65 cm** wide → **≈138 px**; height **~1.825 cm / ≈69 px** (≈2:1); **left-aligned** at **1.05 cm / ≈40 px**, top **1.05 cm / ≈40 px**.
4. **Content-slide titles**: BentonSansCond Light **47pt only** — never 54, 24, 32, or 28–36. Agenda “Content” is a content slide → **47pt** (overrides v4 ≥72 agenda rule).
5. **Cover / hero titles**: **60–72** Light still OK **only on cover**.
6. **Supertext**: **minimum 150pt**; increase for edge-to-edge within margins; stroke **1.25pt**.
7. All other v4 locks in §16 remain (single paragraph text boxes; body 16–20; content subtitles 18–20; no kickers; no yellow lines; blue-only card lines; white-on-black; gradients for dividers; black round bullets; normal kerning; no tagline/bottom MBLM with logo) except where geometry/title sizes above override.

## 18. User v4.1.1 polish (locked 2026-09-10 evening Asia/Dubai)

1. **Content title top edge** at **1.05 cm / ≈39.7 px** (aligned with content logo top / top margin); left-aligned at **1.05 cm**. Subtitle directly under with normal gap; left-aligned.
2. **Subtitles** fill **`#000000` only** — never dark grey.
3. **Bullets** diameter ≈ **80%** of adjacent body font size (overrides prior 50%).
4. **Table headers** fill only `#002A60` / `#000000` / `#808080`.
5. **Graphics chrome** (bars, accents, icon fills used as chrome): primary `#000000` `#FFFFFF` `#FFF200` only (plus table-header tokens above). Do not invent extra greys for chrome.
6. Skill docs: no username absolute paths; `PATHS.md` defines `MBLM_MASTER_ROOT`.
