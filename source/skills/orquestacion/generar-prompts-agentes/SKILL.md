---
name: generar-prompts-agentes
description: "Genera los prompts completos y listos para usar de cada agente (negocio y técnico) en el formato nativo de la IA objetivo."
---

# Skill: generar_prompts_agentes

## Propósito
Genera los prompts completos de cada agente en el formato nativo de la IA objetivo (Copilot .agent.md, Claude .claude/agents/, Cursor .mdc, etc.).

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `agentes_negocio` | object[] | Sí | Output de `disenar_agentes_negocio` |
| `agentes_tecnicos` | object[] | Sí | Output de `estructurar_agentes_tecnicos` |
| `protocolo_comunicacion` | object | Sí | Reglas de comunicación |
| `analisis_dominio` | object | Sí | Para contexto del dominio |
| `ia_objetivo` | string | No | "copilot", "claude", "cursor", "windsurf", "generic" |

## Outputs

```yaml
prompts_agentes:
  negocio:
    - agente_id: string
      nombre_archivo: string
      ruta: string
      prompt_completo: string
      frontmatter: object
      ejemplo_interaccion: string
  tecnicos:
    - agente_id: string
      nombre_archivo: string
      ruta: string
      prompt_completo: string
      frontmatter: object
      ejemplo_interaccion: string
  orquestador:
    prompt_completo: string
    ruta: string
    flujo_decisiones: string
```

## Formatos por IA Objetivo

| IA | Formato Agente | Ruta | Extension |
|----|---------------|------|-----------|
| GitHub Copilot | YAML frontmatter + Markdown body | `.github/agents/` | `.agent.md` |
| Claude Code | YAML frontmatter + Markdown body | `.claude/agents/` | `.md` |
| Cursor | YAML frontmatter + Markdown body | `.cursor/rules/` | `.mdc` |
| Windsurf | YAML frontmatter + Markdown body | `.windsurf/rules/` | `.md` |
| Aider | Concatenado en CONVENTIONS.md | raíz | `.md` |
| Continue | YAML frontmatter + Markdown body | `.continue/rules/` | `.md` |

## Reglas Internas
1. Cada prompt incluye: identidad, contexto del dominio, responsabilidades, restricciones y formato de respuesta.
2. Los prompts de negocio funcionan sin conocimiento técnico.
3. Los prompts técnicos referencian decisiones de negocio como restricciones.
4. Generar un prompt orquestador que sepa cuándo activar cada agente.
