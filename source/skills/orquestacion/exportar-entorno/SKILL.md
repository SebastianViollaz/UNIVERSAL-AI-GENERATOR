---
name: exportar-entorno
description: "Empaqueta el entorno generado en el formato nativo de la IA objetivo: Copilot, Claude, Cursor, Windsurf, Aider o genérico."
---

# Skill: exportar_entorno

## Propósito
Empaqueta todo el entorno generado en el formato final que el programador puede inyectar directamente en su workspace, adaptado a la IA que use.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `validacion` | object | Sí | Output de `validar_entorno_generado` (debe ser ≥80) |
| `arbol_documentacion` | object | Sí | Output de `generar_arbol_documentacion` |
| `prompts_agentes` | object | Sí | Output de `generar_prompts_agentes` |
| `ia_objetivo` | string | Sí | "copilot", "claude", "cursor", "windsurf", "aider", "continue", "generic" |

## Outputs

```yaml
entorno_exportado:
  formato: string
  archivos:
    - ruta: string
      contenido: string
  instrucciones_instalacion: string[]
  primer_paso_recomendado: string
  comando_verificacion: string         # Primer prompt para validar que la IA reconoce el contexto
  prioridad_contexto: string[]         # Para IAs con context limitado: orden de carga prioritario

## Mapeo de Rutas por IA

### GitHub Copilot
```
.github/copilot-instructions.md    ← instrucciones workspace
.github/instructions/*.instructions.md  ← reglas
.github/agents/*.agent.md          ← agentes
.github/skills/*/SKILL.md          ← skills
.github/prompts/*.prompt.md        ← prompts
docs/                               ← documentación
```

### Claude Code
```
CLAUDE.md                           ← instrucciones workspace (con @imports)
.claude/rules/*.md                  ← reglas
.claude/agents/*.md                 ← agentes
.claude/skills/*/SKILL.md           ← skills
.claude/settings.json               ← permisos
docs/                               ← documentación
```

### Cursor
```
AGENTS.md                           ← instrucciones workspace
.cursor/rules/*.mdc                 ← reglas + agentes (como rules)
docs/                               ← documentación
```

### Windsurf
```
AGENTS.md                           ← instrucciones workspace (always-on)
.windsurf/rules/*.md                ← reglas
.windsurf/skills/*/                 ← skills
docs/                               ← documentación
```

### Aider
```
CONVENTIONS.md                      ← todo concatenado en orden de prioridad:
                                       1. Stack y convenciones
                                       2. Reglas de seguridad
                                       3. Top-10 reglas de negocio críticas
                                       4. Arquitectura resumida
                                       5. Glosario (solo términos ambiguos)
.aider.conf.yml                     ← config con read: CONVENTIONS.md
docs/                               ← documentación
```

### Continue.dev
```
.continue/rules/*.md                ← reglas + agentes
.continue/config.yaml               ← configuración
docs/                               ← documentación
```

## Reglas Internas
1. Solo exportar si la validación pasó con 80+ puntos.
2. Incluir instrucciones de instalación paso a paso.
3. El primer paso recomendado da el mayor valor inmediato.
4. Adaptar la estructura de archivos al IDE objetivo.
5. La carpeta `docs/` es siempre igual sin importar la IA.
6. El `comando_verificacion` es el primer mensaje que el desarrollador enviará para confirmar que el contexto fue cargado.
7. Para Aider y Continue, el `prioridad_contexto` determina qué incluir si se excede el context window.
