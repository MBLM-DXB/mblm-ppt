# Paths & Engine Anchors

Resolve paths from this skill's absolute directory (`SKILL_DIR`). This package
**is** the ppt-master engine specialized for MBLM — scripts live at package root
`scripts/`, not under a nested `engine/` folder.

## This skill

| Token | Value |
|---|---|
| `SKILL_DIR` | Absolute path of this skill folder (directory containing `SKILL.md`) |
| `PPT_MASTER_SKILL` | `${SKILL_DIR}` (same — this package) |
| `PPT_MASTER_ROOT` | `${SKILL_DIR}` |
| Brand workspace | `${SKILL_DIR}/templates/brands/mblm/` |
| Brand assets | `${SKILL_DIR}/assets/mblm/` |
| Brand references | `${SKILL_DIR}/references/mblm/` |

Do **not** embed username home paths. Always expand from `SKILL_DIR`.

## Hard prerequisite (fail closed)

Before generating:

```bash
test -f "${SKILL_DIR}/scripts/svg_to_pptx.py"
python3 "${SKILL_DIR}/scripts/attribution_guard.py"
```

If either fails: **stop**. Do **not** fall back to hand-built `python-pptx`
decks. Tell the user the package is incomplete or integrity-failed and to
reinstall the complete `mblm-ppt-master` package (including `LICENSE` /
`SPONSORS.md` / `SPONSORS_CN.md`).

Core Path A does not call home. Optional image/TTS backends may use network
only when explicitly configured (see `.env.example`).

## Visual specs

Catalogs ship in `${SKILL_DIR}/references/mblm/visual-references/`. Composition
SVGs: `${SKILL_DIR}/assets/mblm/layouts/`. If optional PNG banks are absent,
follow catalogs + layouts — do not invent non-MBLM consulting chrome.

## Invocation pattern

```bash
SKILL_DIR="/workspace/mblm-ppt-master"   # folder that contains SKILL.md
python3 "${SKILL_DIR}/scripts/attribution_guard.py"
python3 "${SKILL_DIR}/scripts/project_manager.py" init <project_name> --quick-generate
# Install MBLM brand into the project:
python3 "${SKILL_DIR}/scripts/apply_template.py" <project_path> \
  --root "${SKILL_DIR}/templates/brands/mblm"
```

Quote paths that contain spaces.
