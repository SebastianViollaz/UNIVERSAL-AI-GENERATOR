# BASE-GENERATOR — Instrucciones para Claude Code

Este es el repositorio del **Creador de Entornos Iniciales**, un meta-agente que genera entornos de desarrollo completos para proyectos de software, optimizado para Vibe Coding.

## Arquitectura

```
source/                    ← Fuente canónica (agnóstica de IA)
├── instructions/          ← Instrucciones globales del workspace
├── rules/                 ← 7 archivos con 26 reglas (R-001 a R-026)
├── agents/                ← negocio/ (3), tecnicos/ (4), vibe-coding/ (3)
├── skills/                ← negocio/ (5), tecnico/ (5), orquestacion/ (5), vibe-coding/ (5)
└── prompts/               ← Prompts de ejecución

export.py                  ← Exportador universal (6 IAs: Copilot, Claude, Cursor, Windsurf, Aider, Continue)
templates/                 ← READMEs por formato de exportación
meta/                      ← Configuración del pipeline (export-targets.yml)
docs/                      ← Documentación completa del sistema (9 documentos)
```

## Cómo funciona

1. `source/` contiene archivos con frontmatter YAML universal
2. `export.py` lee source/ y transforma al formato nativo de cada IA
3. El output se copia al workspace del proyecto destino
4. La IA consume los archivos nativos automáticamente

## Convenciones

- **Python:** stdlib only (sin dependencias externas)
- **Markdown:** frontmatter YAML + Markdown estándar
- **Nombres:** kebab-case (`analizar-dominio-negocio.md`)
- **Reglas:** R-NNN secuencial, archivos `{NN}-nombre.md`
- **Skills:** carpeta con `SKILL.md` dentro
- **Agentes:** frontmatter incluye `type:` (negocio/tecnico/vibe-coding)
- **Token budget:** agentes < 150 líneas, instrucciones < 300, rules < 50

## Documentación

- `docs/01-vision-general.md` — Qué es y principios fundamentales
- `docs/02-arquitectura.md` — Pipeline de exportación completo
- `docs/03-flujo-ejecucion.md` — Las 8 fases del sistema
- `docs/04-agentes.md` — Los 10 agentes obligatorios + condicionales
- `docs/05-skills.md` — Las 20 skills con inputs/outputs
- `docs/06-reglas.md` — Las 26 reglas en 7 categorías
- `docs/07-vibe-coding.md` — Materialización de agentes IA
- `docs/08-export-pipeline.md` — Cómo export.py transforma cada formato
- `docs/09-contribucion.md` — Cómo agregar agentes, skills, reglas, targets

## Agentes disponibles para este repositorio

Los agentes en `.claude/agents/` pueden explicar y modificar el sistema:
- `arquitecto-sistema.md` — Explica la arquitectura y funcionamiento
- `desarrollador-sistema.md` — Modifica agentes, skills, reglas, export.py
- `ingeniero-exportacion.md` — Depura y extiende el pipeline de exportación
