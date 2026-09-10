# MBLM Margins (HARD — v4.1.1 persistent layout lock)

Canvas: **1280 × 720**. PowerPoint 16:9: **33.867 cm × 19.05 cm**.  
Scale ≈ **37.795 px/cm**. Full table: [`LAYOUT_METRICS.md`](LAYOUT_METRICS.md).

## Locked margins (ALL sides — every slide)

| Edge | cm | Exact px | Practical SVG |
|---|---|---|---|
| Left / Right / Top / Bottom | **1.05** | **≈39.7** | **40** |

```text
MARGIN = 1.05 cm ≈ 39.7 px   # prefer 40 px content inset, or exact 39.7
CONTENT_SAFE = inset 40 on all sides → 1200 × 640 usable
```

- Title top edge **aligned to logo top** (both at top margin ≈ 39.7–40 px).
- Page number / footnotes stay inside the bottom + side margin band.
- **Do not** use v3/v4 L/R ~62 or bottom ~45 on new decks — revoked.

## Related

- Logo geometry: `LOGOS.md` + `LAYOUT_METRICS.md`
- Title size: `TYPOGRAPHY.md` (content titles **47pt**)
