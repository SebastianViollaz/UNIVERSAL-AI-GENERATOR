---
name: generar-convenciones-git
description: "Produce el branching model, formato de commit messages, PR templates y reglas de branch protection del proyecto."
---

# Skill: generar_convenciones_git

## Propósito
Sin convenciones de Git definidas, cada desarrollador hace git a su manera. Esta skill produce los archivos de configuración de Git y las reglas editoriales que el equipo adopta desde el día uno.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `analisis_dominio` | object | Sí | Para el contexto del proyecto |
| `stack` | object | Sí | Para inferir CI/CD platform |
| `plan_escalabilidad` | object | Sí | Para el modelo de branching (MVP simple vs. multi-env) |

## Outputs

```yaml
convenciones_git:
  branching_model:
    estrategia: enum[gitflow, trunk_based, github_flow]
    justificacion: string
    ramas_permanentes: string[]        # main, develop, etc.
    ramas_temporales:
      - tipo: string                   # feature/, fix/, hotfix/, release/
        formato: string                # ej: feature/US-{id}-{descripcion-kebab}
        desde: string                  # desde qué rama se crea
        merge_hacia: string            # hacia dónde se integra
  commit_format:
    estandar: enum[conventional_commits, angular, custom]
    prefijos_permitidos:
      - prefijo: string                # feat, fix, docs, chore, test, etc.
        cuando_usar: string
    scope_validos: string[]            # Módulos del sistema
    ejemplo_valido: string
    ejemplo_invalido: string
    longitud_minima_mensaje: number
  pull_request_template: string        # Markdown del template de PR
  issue_templates:
    - nombre: string
      contenido: string
  branch_protection:
    rama: string
    reglas: string[]                   # Ej: "2 approvals requeridos", "CI debe pasar"
  gitignore_base: string               # .gitignore pre-configurado para el stack
  commitlint_config: string            # commitlint.config.js si aplica
```

## Reglas Internas
1. Trunk-based development para equipos pequeños (<5 devs) o MVP con iteración rápida.
2. Gitflow para proyectos con release cycles definidos o múltiples ambientes.
3. El PR template incluye: descripción, US relacionada, checklist de calidad, testing instructions.
4. `branch_protection` en `main` es obligatoria: mínimo CI passing + 1 approval.
5. El `.gitignore` incluye: secretos (`.env`), artefactos de build, dependencias, logs.
