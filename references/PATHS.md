# Paths & Engine Anchors

Resolve paths from this skill's directory (`SKILL_DIR`) and the master root. Never hardcode usernames or machine-specific absolute paths in skill docs.

## Master root

| Token | Meaning |
|---|---|
| `MBLM_MASTER_ROOT` | Parent folder containing `skill/` and `source/` — resolved at runtime by the agent from context (e.g. the folder that holds `skill/mblm-ppt` and `source/ppt-master-main`) |

Relative tokens below are from `MBLM_MASTER_ROOT` unless noted.

## This skill

| Token | Relative from `MBLM_MASTER_ROOT` | Notes |
|---|---|---|
| `SKILL_DIR` | `skill/mblm-ppt` | This skill folder |
| Brand assets | `skill/mblm-ppt/assets/` | Logos, icons, palette, layouts |

## ppt-master engine (do not modify)

| Token | Relative from `MBLM_MASTER_ROOT` |
|---|---|
| `PPT_MASTER_ROOT` | `source/ppt-master-main` |
| `PPT_MASTER_SKILL` | `source/ppt-master-main/skills/ppt-master` |
| Projects workspace | `source/ppt-master-main/projects` (created by `project_manager.py init`) |

Relative from this skill folder (`skill/mblm-ppt/`):

```text
../../source/ppt-master-main/skills/ppt-master
```

## Official MBLM PPTX template (large; not copied)

```text
source/mblm assets/template/MBLM_Power point _v1.pptx
```

Symlink (Path C): `${SKILL_DIR}/assets/template/MBLM_PowerPoint_v1.pptx`

### Closed policy (2026-09-10)

- Do **not** auto-run Create Template on this ~70MB PPTX.
- **Paths A/B**: generate from skill brand assets + ppt-master engine.
- **Path C**: Edit Native on this PPTX (via the path or symlink above).

## Invocation pattern

Expand absolute paths in each tool call by resolving `MBLM_MASTER_ROOT` first. Prefer:

```bash
PPT_MASTER_SKILL="${MBLM_MASTER_ROOT}/source/ppt-master-main/skills/ppt-master"
python3 "${PPT_MASTER_SKILL}/scripts/project_manager.py" init <project_name> --quick-generate
```

Quote every path that contains spaces (`mblm master`, `mblm assets`, `MBLM_ UI-UX Design.svg`).

## Visual specs (read-only inputs)

| Token | Relative from `MBLM_MASTER_ROOT` |
|---|---|
| Specs original | `MBLM slides and other specs/` |
| Specs ASCII mirror + INDEX | `skill/_spec_screens_ascii/` |
| R2 examples original | `more examples r2/` |
| R2 ASCII mirror | `skill/_examples_r2_ascii/` |
| Catalog / patterns | `${SKILL_DIR}/references/visual-references/` |

Mandatory visual reference pass before SVG authoring — see `SKILL.md` v4.1.1 and `workflows/generate-mblm-pptx.md` A0. Geometry: `LAYOUT_METRICS.md`.
