# VISUAL_BEATS — Kimi-style visual intelligence (planner-owned)

**Authority:** this file is owned by `mblm-deck-planner`.  
`mblm-ppt-master` **executes** the plan; it must **not** re-decide visual beats.

Goal: every body slide has an **intentional visual job** — diagram, chart, explainer, photo, or type — not filler chrome.

---

## 1. Fields (add to every slide that needs a visual)

| Field | Required when | Values / shape |
|---|---|---|
| `visual_mode` | always | `photo` \| `illustration` \| `diagram` \| `type` \| `kit_icon` \| `none` |
| `visual_beat` | always (new) | `atmosphere` \| `explainer` \| `process` \| `chart` \| `comparison` \| `proof` \| `structure` \| `chrome_none` |
| `visual_job` | always (new) | One sentence: what the visual must make the audience *see* |
| `chart_spec` | `visual_beat: chart` | See §4 |
| `diagram_spec` | `visual_beat: process` or comparison-as-diagram | See §5 |
| `explainer_spec` | `visual_beat: explainer` | See §6 |
| `image_prompt` / `image_filename` | asset needed | Unchanged prefixes: `photo_` / `illustration_` / `diagram_` / `chart_` |

---

## 2. Decision tree (run per slide, after layout pick)

Ask in order; stop at first hard match:

1. **Agenda / dense table / matrix / checklist** → `visual_beat: structure`, `visual_mode: type`, `chrome_none` for art.
2. **Numbers that already exist in context** (time series, share, funnel, before/after deltas) → `visual_beat: chart`, prefer layout `MBLM_chart_insight` or a type-led r2 with a chart slot; **never invent series**.
3. **Sequence / phases / methodology / “how we work”** → `visual_beat: process`, `visual_mode: diagram` (monoline) unless the chosen r2 layout *is* the process chrome (`21_r2_22`, chevrons, timelines) → then `visual_mode: none` and `visual_beat: process` with `diagram_spec.kind: layout_native`.
4. **Mechanism / “why this works” / metaphor for a capability** → `visual_beat: explainer`, `visual_mode: illustration` (one MBLM accent).
5. **Human / place / brand atmosphere (cover, inflection, closing)** → `visual_beat: atmosphere`, `visual_mode: photo`.
6. **Proof quote / single KPI already in facts** → `visual_beat: proof`, usually `type` or photo well — no decorative diagram.
7. **Else** → `visual_beat: structure` + `type`, or `none` if the layout geometry already carries the story.

**Anti-patterns (reject in plan review):**
- Decorative photo on a process slide when a diagram would teach faster
- Chart with no `chart_spec.data` sourced from context
- Illustration that restates the title without explaining a mechanism
- Two competing large visuals on one slide
- `kit_icon` as the hero (icons = chrome only)

---

## 3. `visual_beat` → default `visual_mode`

| visual_beat | Default visual_mode | Turn 1 asset? |
|---|---|---|
| `atmosphere` | `photo` | yes (`photo_`) |
| `explainer` | `illustration` | yes (`illustration_`) |
| `process` | `diagram` or `none` if layout_native | diagram PNG only if not layout_native |
| `chart` | `type` (+ native chart in PPT) or `diagram` if conceptual only | Prefer **spec for ppt-master** over AI image; use `chart_` PNG only if native chart unavailable |
| `comparison` | `type` / `diagram` | rare illustration |
| `proof` | `type` or `photo` | optional |
| `structure` | `type` | no |
| `chrome_none` | `none` / `kit_icon` | no |

---

## 4. `chart_spec` (facts only)

```yaml
chart_spec:
  kind: bar | line | pie | stacked_bar | funnel | waterfall | scatter  # pick simplest that fits
  title: "Short chart title from context"
  unit: "%"  # or currency / count
  categories: ["A", "B"]          # from source
  series:
    - name: "Series from source"
      values: [10, 20]            # ONLY numbers present in context
  insight: "One line the slide must land"  # paraphrase of source, not invented
  source_ref: "brief §3 / table X"
```

If any value is missing → omit the chart beat; use `notes: "METRIC NEEDED: …"` and fall back to type/proof.

---

## 5. `diagram_spec`

```yaml
diagram_spec:
  kind: layout_native | flow | cycle | pyramid | org | swimlane | before_after
  nodes: ["Discover", "Configure", "Deploy", "Prove"]  # from brief language
  edges: []   # optional; keep ≤ one idea per connector
  emphasis: "Deploy"  # optional focal node
  style: monoline_bw   # MBLM diagram lock when generating PNG
```

`layout_native`: r2/kit geometry *is* the diagram — do not also generate a competing PNG.

---

## 6. `explainer_spec`

```yaml
explainer_spec:
  mechanism: "What causal story the picture must show"
  must_show: ["element A", "relationship B"]
  must_avoid: ["faces toward camera", "extra accents", "text in image"]
  accent_rule: "exactly one MBLM accent"
```

`image_prompt` must encode `mechanism` + `must_show` / `must_avoid`.

---

## 7. Density & rhythm (Kimi-like decks)

Across the full plan:

- Aim for **≥40%** of body slides (non-cover/agenda/close) to carry a **teaching** beat: `process` | `chart` | `explainer` | `comparison`.
- Avoid three `atmosphere` photos in a row.
- After a dense `structure`/`chart` slide, prefer an `explainer` or `process` so the deck breathes.
- One visual job per slide — if two jobs compete, split into two slides.

---

## 8. Handoff contract (what ppt-master may assume)

When Turn 2 runs `mblm-ppt-master`:

1. Trust `visual_beat` + specs; **do not** invent a different visual role.
2. For `chart_spec` → render as editable chart or typed callout using **only** provided data.
3. For `diagram_spec.kind: layout_native` → fill layout labels; skip extra diagram PNG.
4. For Turn-1 filenames → place per IMAGE_SLOTS / DIAGRAM_SLOTS only.
5. Never “upgrade” a type slide with decorative AI art during export.

---

## 9. Quick examples

| Slide intent | visual_beat | visual_mode | Spec |
|---|---|---|---|
| Four-phase approach | process | none | `diagram_spec.kind: layout_native` on `21_r2_22` |
| Market share from brief table | chart | type | `chart_spec` bar + insight |
| Why brand intimacy compounds | explainer | illustration | `explainer_spec.mechanism` |
| Industry inflection | atmosphere | photo | cinematic prompt |
| Agenda | structure | type | no asset |
