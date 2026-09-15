# PROMPT_ALUMNI — copy-paste runner for mblm-deck-planner

Use on Alumni. **Turn 0 = plan only.** Then visuals → ppt (two more turns).

---

## Turn 0 — plan (this skill)

```text
Use skill: mblm-deck-planner ONLY (do not load mblm-ppt-master; do not generate PPTX).

Read: conversation memory, attached docs, URLs, summaries, screenshots, datasets, and my instructions below.

OUTPUT: a deck PLAN only — YAML or JSON slide map per skills/mblm-deck-planner/references/OUTPUT_SCHEMA.md.
Each slide needs: layout_id, title, body, visual_mode, visual_beat, visual_job, image_prompt and/or image_filename, notes; plus chart_spec / diagram_spec / explainer_spec when the beat requires them (see references/VISUAL_BEATS.md).

Rules:
- Prefer photographic / photo-editorial when applicable; illustration for explainers/metaphors; diagram for process; type-only for agenda/tables/matrices
- Assign visual_beat + visual_job per VISUAL_BEATS.md (Kimi-style: charts/process/explainers teach; no filler chrome). ≥40% of body slides should be teaching beats
- Map layout_id from mblm-r2 (39 under templates/decks/mblm-r2/templates) + core kit (assets/mblm/layouts). Agenda gold = 39_r2_40_section_agenda ONLY (11_r2_12_content_toc removed)
- Brand freeze pointers: content titles Light 40pt (SVG 53.3); body Regular 16–18 min (SVG 21.3/24); NO Medium/MediumSC; section agenda sections 50pt Light; logos/margins per LAYOUT_METRICS
- Never invent KPIs — facts from context/docs/URLs only; flag gaps in notes
- After this plan: Turn 1 visuals → Turn 2 mblm-ppt-master only (avoid 400 spawn). ppt-master must NOT re-decide visual beats

BRIEF / INSTRUCTIONS
[PASTE BRIEF]
```

---

## Turn 1 — visuals (after plan approved)

```text
Do NOT load mblm-ppt-master. Use nested style refs only:
  skills/mblm-diagram/SKILL.md
  skills/mblm-illustration/SKILL.md
  skills/mblm-cinematic/SKILL.md

From the approved deck_plan, generate ALL PNGs listed with visual_mode photo|illustration|diagram.
Save to projects/_host_images/ using the plan's image_filename values (photo_ / illustration_ / diagram_ prefixes).
Do NOT init or export PPTX.
```

---

## Turn 2 — PPTX (mblm-ppt-master only)

```text
Use skill: mblm-ppt-master ONLY (no visual Skill Scripts).

1. attribution_guard → project_manager init <name> --quick-generate
2. apply_template <project_path> --root templates/brands/mblm
3. Author slides from the approved deck_plan (layout_id + copy + visual_beat specs); prefer templates/decks/mblm-r2
4. Trust visual_beat/chart_spec/diagram_spec/explainer_spec — do not invent a different visual role. Place _host_images per IMAGE_SLOTS / DIAGRAM_SLOTS; render chart_spec as native chart when possible
5. Freeze: titles Light 40pt; body Regular ≥16/18; no Medium; agenda = 39_r2_40 only; LAYOUT_METRICS logos/margins
6. svg_quality_checker → svg_to_pptx --quick-generate

PASTE deck_plan YAML/JSON below.
```
