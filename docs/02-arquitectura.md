# Arquitectura del Sistema

## Diagrama de Alto Nivel

```
BASE-GENERATOR/
│
├── source/                    ← FUENTE CANÓNICA (agnóstica de IA)
│   ├── instructions/          ← Instrucciones globales del workspace
│   ├── rules/                 ← 7 archivos con 26 reglas (R-001 a R-026)
│   ├── agents/                ← 3 categorías: negocio, tecnicos, vibe-coding
│   ├── skills/                ← 4 categorías: negocio, tecnico, orquestacion, vibe-coding
│   └── prompts/               ← Prompts de ejecución reutilizables
│
├── templates/                 ← READMEs descriptivos de cada formato de exportación
├── meta/                      ← Configuración del pipeline (export-targets.yml)
│
├── export.py                  ← Script de exportación universal
├── AGENTS.md                  ← Punto de entrada universal (Copilot, Cursor, Windsurf)
├── system-prompt.md           ← System prompt completo de referencia
└── README.md                  ← Documentación del repositorio
```

## Concepto Central: Fuente Canónica

Todos los archivos fuente viven en `source/` con un formato universal de frontmatter YAML:

```yaml
---
name: "identificador-unico"
description: "Descripción para discovery por la IA"
scope: "always"                    # always | file_pattern | manual
file_patterns: "**/*.py"           # Solo si scope = file_pattern
type: "negocio"                    # negocio | tecnico | vibe-coding (solo agentes)
---
```

Este formato es **agnóstico de IA**. El script `export.py` lee estos archivos y transforma el frontmatter al formato nativo de cada herramienta:

| Campo Universal | Copilot | Claude | Cursor | Windsurf | Continue |
|----------------|---------|--------|--------|----------|----------|
| `scope: always` | `applyTo: "**"` | sin `paths` | `alwaysApply: true` | `trigger: always_on` | `alwaysApply: true` |
| `scope: file_pattern` | `applyTo: "{pat}"` | `paths: ["{pat}"]` | `globs: "{pat}"` | `trigger: glob` | `globs: "{pat}"` |
| `scope: manual` | sin `applyTo` | sin `paths` | `alwaysApply: false` | `trigger: manual` | `alwaysApply: false` |

## Pipeline de Exportación

```
source/*.md  ──→  extract_frontmatter()  ──→  transform to native  ──→  write to target dir
                                              ↓
                                     build_frontmatter() con campos específicos de la IA
```

### Funciones clave de export.py

| Función | Propósito |
|---------|-----------|
| `strip_frontmatter(content)` | Remueve YAML frontmatter del Markdown |
| `extract_frontmatter(content)` | Extrae frontmatter como dict (sin dependencia de PyYAML) |
| `build_frontmatter(fields)` | Construye nuevo frontmatter YAML desde dict |
| `get_source_files(subdir, ext)` | Lista archivos de un subdirectorio de source/ |
| `get_skill_folders()` | Lista todos los SKILL.md recursivamente |
| `export_<target>(output_dir)` | 6 funciones exportadoras (una por IA) |

### Asignación de Tools por Tipo de Agente (Copilot)

| Tipo | Tools Asignados |
|------|----------------|
| `tecnico` | read_file, create_file, replace_string_in_file, run_in_terminal, grep_search, semantic_search, list_dir, get_errors |
| `vibe-coding` | read_file, create_file, replace_string_in_file, grep_search, semantic_search, list_dir |
| `negocio` (default) | read_file, grep_search, semantic_search, list_dir |

## Estructura de Archivos por Tipo

### Rules (`source/rules/`)
- 7 archivos numerados: `01-separacion.md` a `07-vibe-coding.md`
- Contienen múltiples reglas por archivo (ej: R-001 a R-003 en `01-separacion.md`)
- Se exportan como reglas individuales siempre activas

### Agents (`source/agents/`)
- 3 subdirectorios: `negocio/`, `tecnicos/`, `vibe-coding/`
- Archivos `condicionales.md` son catálogos (no se exportan como agentes)
- Cada agente tiene frontmatter con `type:` que determina sus tools

### Skills (`source/skills/`)
- 4 subdirectorios: `negocio/`, `tecnico/`, `orquestacion/`, `vibe-coding/`
- Cada skill es una carpeta con `SKILL.md` dentro
- Se copian tal cual (formato compatible con Copilot y Claude)

### Prompts (`source/prompts/`)
- Solo se exportan en Copilot (`.github/prompts/`)
- Otras IAs no tienen un mecanismo nativo de prompts reutilizables
