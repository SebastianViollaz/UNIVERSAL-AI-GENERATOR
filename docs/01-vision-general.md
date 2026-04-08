# Visión General

## Qué es BASE-GENERATOR

Un **meta-agente** que transforma la descripción de un proyecto de software en un entorno de desarrollo completo y listo para **Vibe Coding**. El sistema genera agentes de negocio, agentes técnicos, skills, reglas y documentación materializados como **archivos funcionales** (.agent.md, .mdc, SKILL.md, rules) que la IA de codificación consume directamente.

## Flujo simplificado

```
Descripción del negocio
   ↓
source/ (fuente canónica, agnóstica de IA)
   ↓
export.py --target <ia>
   ↓
Archivos nativos (.agent.md, .mdc, CLAUDE.md, etc.)
   ↓
Copiar al workspace → IA ya sabe todo del proyecto
```

## Principios Fundamentales

1. **El negocio manda, la técnica habilita** — Toda decisión técnica se traza a una necesidad de negocio
2. **Profundidad dual obligatoria** — Cada tema se aborda desde negocio Y desde técnica
3. **Contexto portable** — El output funciona en cualquier IA soportada sin modificación manual
4. **Output ejecutable** — Cada archivo funciona al copiarlo al workspace, sin configuración manual
5. **Contexto inyectado** — Los agentes IA incluyen contexto de negocio DENTRO del prompt, no como referencia externa
6. **Agentes autónomos** — Cada agente funciona sin que los otros estén activos

## IAs Soportadas

| IA | Formato Nativo |
|----|---------------|
| GitHub Copilot | `.github/agents/`, `.github/instructions/`, `.github/skills/` |
| Claude Code | `CLAUDE.md`, `.claude/rules/`, `.claude/agents/` |
| Cursor | `AGENTS.md`, `.cursor/rules/*.mdc` |
| Windsurf | `AGENTS.md`, `.windsurf/rules/`, `.windsurf/skills/` |
| Aider | `CONVENTIONS.md`, `.aider.conf.yml` |
| Continue.dev | `.continue/rules/`, `.continue/config.yaml` |

## Stack Técnico del Generador

- **Lenguaje:** Python 3.10+ (export.py)
- **Sin dependencias externas** — Solo stdlib (argparse, pathlib, re, shutil)
- **Formato interno:** Markdown con frontmatter YAML
- **Sin base de datos** — Todo es archivos en disco
