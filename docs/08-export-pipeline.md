# Export Pipeline — export.py

## Propósito

`export.py` transforma los archivos fuente canónicos de `source/` al formato nativo de la IA objetivo. Un solo conjunto de archivos fuente → 6 formatos nativos diferentes.

## Uso

```bash
# Exportar para una IA específica
python export.py --target copilot --output ./mi-proyecto
python export.py --target claude --output ./mi-proyecto
python export.py --target cursor --output ./mi-proyecto
python export.py --target windsurf --output ./mi-proyecto
python export.py --target aider --output ./mi-proyecto
python export.py --target continue --output ./mi-proyecto

# Exportar TODOS los formatos
python export.py --target all --output ./exports
```

## Estructura de export.py

```
export.py
├── Constantes: SCRIPT_DIR, SOURCE_DIR, TEMPLATES_DIR, TARGETS
├── Utilidades:
│   ├── read_file(path) → str
│   ├── write_file(path, content)
│   ├── strip_frontmatter(content) → str
│   ├── extract_frontmatter(content) → dict
│   ├── build_frontmatter(fields) → str
│   ├── get_source_files(subdir, ext) → list[Path]
│   └── get_skill_folders() → list[Path]
├── Exportadores (6):
│   ├── export_copilot(output_dir)
│   ├── export_claude(output_dir)
│   ├── export_cursor(output_dir)
│   ├── export_windsurf(output_dir)
│   ├── export_aider(output_dir)
│   └── export_continue(output_dir)
└── main() → argparse CLI
```

## Cómo funciona cada exportador

### `export_copilot`
| Source | Target | Transformación |
|--------|--------|---------------|
| `instructions/workspace.md` | `.github/copilot-instructions.md` | Strip frontmatter |
| `rules/*.md` | `.github/instructions/*.instructions.md` | FM → `{description, applyTo: "**"}` |
| `agents/{negocio,tecnicos,vibe-coding}/*.md` | `.github/agents/*.agent.md` | FM → `{description, tools: [...]}` por tipo |
| `skills/*/SKILL.md` | `.github/skills/*/SKILL.md` | Copia directa |
| `prompts/*.prompt.md` | `.github/prompts/*.prompt.md` | Copia directa |
| `templates/copilot/README.md` | `.github/EXPORT-INFO.md` | Copia directa |

**Tools por tipo de agente:**
- `type: tecnico` → 8 tools (incluye terminal y errors)
- `type: vibe-coding` → 6 tools (lectura + escritura)
- `type: negocio` (default) → 4 tools (solo lectura)

### `export_claude`
| Source | Target | Transformación |
|--------|--------|---------------|
| `instructions/workspace.md` | `CLAUDE.md` | Strip FM + agregar sección de imports |
| `rules/*.md` | `.claude/rules/*.md` | Solo body (sin frontmatter = always active) |
| `agents/*.md` | `.claude/agents/*.md` | FM → `{description}` |
| `skills/*/SKILL.md` | `.claude/skills/*/SKILL.md` | Copia directa |
| — | `.claude/settings.json` | Genera con permissions: allow/ask/deny |

### `export_cursor`
| Source | Target | Transformación |
|--------|--------|---------------|
| `instructions/workspace.md` | `AGENTS.md` | Strip frontmatter |
| `rules/*.md` | `.cursor/rules/*.mdc` | FM → `{description, alwaysApply: true}` |
| `agents/*.md` | `.cursor/rules/agente-*.mdc` | FM → `{description, alwaysApply: false}` |

### `export_windsurf`
| Source | Target | Transformación |
|--------|--------|---------------|
| `instructions/workspace.md` | `AGENTS.md` | Strip frontmatter |
| `rules/*.md` | `.windsurf/rules/*.md` | FM → `{trigger: always_on, description}` |
| `agents/*.md` | `.windsurf/rules/agente-*.md` | FM → `{trigger: model_decision, description}` |
| `skills/*/SKILL.md` | `.windsurf/skills/*/SKILL.md` | Copia directa |

### `export_aider`
| Source | Target | Transformación |
|--------|--------|---------------|
| Todo | `CONVENTIONS.md` | Concatena todo en un solo archivo (sin native agents/rules) |
| — | `.aider.conf.yml` | `read: [CONVENTIONS.md]` |

### `export_continue`
| Source | Target | Transformación |
|--------|--------|---------------|
| `instructions/workspace.md` | `.continue/rules/01-workspace.md` | FM → `{name, description, alwaysApply: true}` |
| `rules/*.md` | `.continue/rules/{NN}-*.md` | FM → `{name, description, alwaysApply: true}` |
| `agents/*.md` | `.continue/rules/agente-*.md` | FM → `{name, description, alwaysApply: false}` |
| — | `.continue/config.yaml` | Config básica de Continue |

## Qué NO hace export.py

- **No instala dependencias** — Solo genera archivos
- **No modifica el source** — Solo lee y transforma
- **No requiere YAML parser** — Parsea frontmatter con regex simple
- **No necesita pip install** — Solo usa stdlib de Python
