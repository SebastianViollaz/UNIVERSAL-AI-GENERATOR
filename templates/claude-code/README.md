# Template de Exportación: Claude Code

## Estructura de Archivos Generada

```
proyecto/
├── CLAUDE.md                              ← Instrucciones principales (con @imports)
├── .claude/
│   ├── settings.json                      ← Permisos y configuración
│   ├── rules/
│   │   ├── 01-separacion.md
│   │   ├── 02-calidad.md
│   │   ├── 03-formato.md
│   │   ├── 04-comunicacion.md
│   │   ├── 05-escalabilidad.md
│   │   └── 06-validacion.md
│   ├── agents/
│   │   ├── estratega-negocio.md
│   │   ├── operaciones.md
│   │   ├── ux-negocio.md
│   │   ├── arquitecto-principal.md
│   │   ├── backend.md
│   │   ├── frontend.md
│   │   ├── qa-testing.md
│   │   └── [agentes-condicionales].md
│   └── skills/
│       ├── analizar-dominio-negocio/SKILL.md
│       ├── disenar-agentes-negocio/SKILL.md
│       └── ... (una carpeta por skill)
├── docs/
│   ├── negocio/ ...
│   ├── tecnico/ ...
│   └── agentes/ ...
└── README.md
```

## Formato de Archivos

### CLAUDE.md
```markdown
# [Nombre del Proyecto]

Instrucciones globales del proyecto...

## Documentación
@docs/negocio/vision-proyecto.md
@docs/tecnico/arquitectura/overview.md

## Reglas
Las reglas están en .claude/rules/ y se cargan automáticamente.
```

### .claude/rules/*.md
```markdown
---
paths:
  - "**/*.py"
---

# Contenido de la regla...

(Sin paths = siempre activa. Con paths = solo para esos archivos.)
```

### .claude/agents/*.md
```markdown
---
description: "Descripción del agente"
---

# Prompt del agente...
```

### .claude/settings.json
```json
{
  "permissions": {
    "allow": ["read_file", "list_dir", "grep_search"],
    "ask": ["write_file", "run_command"],
    "deny": ["delete_file"]
  }
}
```

## Instrucciones de Instalación

1. Copia `CLAUDE.md` en la raíz de tu proyecto
2. Copia la carpeta `.claude/` en la raíz de tu proyecto
3. Copia la carpeta `docs/` en la raíz de tu proyecto
4. Abre el proyecto con Claude Code (`claude` en terminal)
5. Las instrucciones de `CLAUDE.md` se cargan al inicio de cada sesión
6. Las reglas de `.claude/rules/` se aplican automáticamente
7. Invoca agentes con `/agent nombre-del-agente`
