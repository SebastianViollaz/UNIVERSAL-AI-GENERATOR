# BASE-GENERATOR — Instrucciones para GitHub Copilot

Este es el repositorio del **Creador de Entornos Iniciales**, un meta-agente que genera entornos de desarrollo completos a partir de descripciones de proyectos de software.

## Arquitectura del Sistema

```
source/                 ← Fuente canónica (agnóstica de IA)
├── instructions/       ← Instrucciones globales del workspace
├── rules/              ← 7 archivos con 26 reglas (R-001 a R-026)
├── agents/             ← negocio/ (3), tecnicos/ (4), vibe-coding/ (3)
├── skills/             ← negocio/ (5), tecnico/ (5), orquestacion/ (5), vibe-coding/ (5)
└── prompts/            ← Prompts de ejecución

export.py               ← Exportador universal (6 IAs soportadas)
templates/              ← READMEs por formato de exportación
meta/                   ← Configuración del pipeline
docs/                   ← Documentación completa del sistema
```

## Cómo funciona

1. Los archivos en `source/` usan frontmatter YAML universal
2. `export.py` lee source/ y transforma al formato nativo de cada IA
3. El output se copia al workspace del proyecto destino
4. La IA de codificación consume los archivos nativos automáticamente

## Convenciones del código

- **Python:** stdlib only (sin dependencias externas)
- **Markdown:** frontmatter YAML + contenido en Markdown estándar
- **Nombres:** kebab-case para archivos (`analizar-dominio-negocio.md`)
- **Reglas:** numeración secuencial R-NNN, archivos `{NN}-nombre.md`
- **Skills:** cada skill es carpeta con `SKILL.md` dentro
- **Agentes:** frontmatter incluye `type:` (negocio/tecnico/vibe-coding)
- **Token budget:** agentes < 150 líneas, instrucciones < 300, rules < 50

## Consultando la documentación

La documentación completa del sistema está en `docs/`:
- `docs/02-arquitectura.md` — Diagrama y pipeline de exportación
- `docs/04-agentes.md` — Los 10 agentes obligatorios + condicionales
- `docs/05-skills.md` — Las 20 skills con inputs/outputs
- `docs/06-reglas.md` — Las 26 reglas en 7 categorías
- `docs/08-export-pipeline.md` — Cómo export.py transforma cada formato
- `docs/09-contribucion.md` — Cómo agregar agentes, skills, reglas, targets
