# MBLM Text Boxes (HARD — v4.0.0)

**Never split a multi-line paragraph into one SVG/`<text>` object per visual line.** That becomes one PowerPoint text box per line and makes editing painful.

## Rule

| Situation | Authoring |
|---|---|
| One paragraph (even if wrapped across lines) | **One** `<text>` element. Soft-wrap with nested `<tspan dy="…">` (same `x`), or one long string if it fits. |
| Separate paragraphs / distinct labels | Separate `<text>` objects (one per paragraph / label). |
| Title vs subtitle | Separate objects (different roles). |
| Bullet list | One `<text>` per bullet line is OK **only** when each bullet is its own short paragraph; never explode a single bullet’s wrap into multiple sibling `<text>`s. |

## Preferred SVG pattern (preserve mode → one editable PPT frame)

```xml
<text x="82" y="290" font-size="20" fill="#000000"
      font-family="BentonSansCond-Regular, BentonSansCond, Arial Narrow, Arial, sans-serif">
  <tspan x="82" dy="0">Make complex products easier to explore,</tspan>
  <tspan x="82" dy="28">configure, and understand.</tspan>
</text>
```

- Default `svg_to_pptx` text flow is **`preserve`**: dy-stacked tspans inside one `<text>` become **one** DrawingML text frame with hard line breaks.
- Do **not** pass `--no-merge` for MBLM decks (that emits one frame per visual line — forbidden).
- Optional: `--reflow-text` / `--merge-paragraphs` if the user wants PowerPoint auto-reflow instead of authored breaks.
- Optional markers (engine-supported): `data-paragraph-soft-break`, `data-paragraph-line-break`, `data-paragraph-line-height`.

## Forbidden anti-pattern (v3 decks)

```xml
<!-- BAD: three PPT text boxes for one paragraph -->
<text x="82" y="290" …>Make complex products</text>
<text x="82" y="318" …>easier to explore,</text>
<text x="82" y="346" …>configure, and understand.</text>
```

## Cover / long titles

Prefer a **single** title `<text>` (one paragraph). If the headline must wrap, use tspans inside that one element — never two sibling title `<text>`s.

## Related

- Sizes: `TYPOGRAPHY.md`
- Export: `workflows/generate-mblm-pptx.md` (do not use `--no-merge`)
