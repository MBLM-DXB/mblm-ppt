# MBLM PPT Master

Local, self-contained **MBLM-only** specialization of
[ppt-master](https://github.com/hugohe3/ppt-master) (MIT).

This package always produces **MBLM — The Brand Intimacy Agency** decks. Other
consulting brand presets (McKinsey, BCG, Bain, Accenture, …) are **not**
shipped and must not be loaded.

## Layout

```text
mblm-ppt-master/
├── SKILL.md                 # MBLM entry (keeps upstream attribution metadata)
├── SKILL.upstream.md        # Unmodified upstream Skill archive
├── MBLM_OVERLAY.md          # Always-on brand freeze summary
├── PATHS.md                 # SKILL_DIR anchors
├── LICENSE / SPONSORS*.md   # Upstream MIT attribution (required by guard)
├── templates/brands/mblm/   # Sole Brand workspace
├── assets/mblm/             # Logos, icons, layouts, palette
├── references/mblm/         # Brand token docs + visual catalogs
├── scripts/                 # ppt-master engine scripts
└── workflows/               # Routing + generate-mblm-pptx Path A
```

## Integrity gate

```bash
cd /workspace/mblm-ppt-master   # or your install path
python3 scripts/attribution_guard.py
# must exit 0
```

## Quick generate (Path A)

```bash
SKILL_DIR="/workspace/mblm-ppt-master"
python3 "${SKILL_DIR}/scripts/attribution_guard.py"
python3 "${SKILL_DIR}/scripts/project_manager.py" init my-deck --quick-generate
# retain printed <project_path>, then:
python3 "${SKILL_DIR}/scripts/apply_template.py" <project_path> \
  --root "${SKILL_DIR}/templates/brands/mblm"
# author svg_output/*.svg under MBLM freeze, then:
python3 "${SKILL_DIR}/scripts/svg_quality_checker.py" <project_path> --quick-generate
python3 "${SKILL_DIR}/scripts/svg_to_pptx.py" <project_path> --quick-generate
```

Full recipe: [`workflows/generate-mblm-pptx.md`](workflows/generate-mblm-pptx.md).
Agents: load `SKILL.md` → guard → `MBLM_OVERLAY.md` → `references/mblm/*` freeze.

## Network / call-home

**Core Path A** (project init → SVG authoring → `svg_to_pptx`) does **not** call
home. Optional image search / TTS / cloud backends are opt-in via `.env.example`
only.

## License

- Engine / Skill tooling: MIT — Copyright (c) 2025-2026 Hugo He
  (`LICENSE`, `SPONSORS.md`, `SPONSORS_CN.md`). Official repository:
  https://github.com/hugohe3/ppt-master
- MBLM brand assets and brand reference docs: MBLM identity materials bundled for
  authorized MBLM deck generation; do not treat as a grant to rebrand as other
  firms.

## Install checklist (Alumni / local)

1. This package is **flat** (`scripts/` at the skill root). `scripts/project_management/paths.py` must resolve `REPO_ROOT` to the skill folder (not `/`). If `project_manager.py init` errors with `Permission denied: '/projects'`, you have an unpatched nested-layout path — use this package’s patched `paths.py`.
2. Install Python deps: `pip install -r requirements.txt` (needs **PyYAML** for brand `design_spec.md` frontmatter). Without PyYAML, `apply_template.py` fails with a SpecParseError that agents may misread as a “broken template.”
3. Then: `python3 scripts/attribution_guard.py` → init project → `apply_template.py … --root templates/brands/mblm`.

Do **not** skip brand apply for MBLM-only generation — fix deps/paths and retry.
