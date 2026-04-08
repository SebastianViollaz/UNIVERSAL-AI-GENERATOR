# Template de Exportación: Windsurf (Codeium)

## Estructura de Archivos Generada

```
proyecto/
├── AGENTS.md                              ← Instrucciones principales (always-on)
├── .windsurf/
│   ├── rules/
│   │   ├── 01-separacion.md
│   │   ├── 02-calidad.md
│   │   ├── 03-formato.md
│   │   ├── 04-comunicacion.md
│   │   ├── 05-escalabilidad.md
│   │   ├── 06-validacion.md
│   │   ├── agente-estratega-negocio.md
│   │   ├── agente-operaciones.md
│   │   └── ... (todos los agentes como rules)
│   └── skills/
│       ├── analizar-dominio-negocio/
│       ├── disenar-agentes-negocio/
│       └── ... (una carpeta por skill)
├── docs/
│   ├── negocio/ ...
│   ├── tecnico/ ...
│   └── agentes/ ...
└── README.md
```

## Formato de Archivos

### AGENTS.md
```markdown
# [Nombre del Proyecto]

Instrucciones globales del workspace...
(AGENTS.md en raíz = always-on para Windsurf)
```

### .windsurf/rules/*.md (Reglas always-on)
```markdown
---
trigger: always_on
description: "Descripción de la regla"
---

# Contenido de la regla...
```

### .windsurf/rules/*.md (Agentes como model_decision)
```markdown
---
trigger: model_decision
description: "Agente Estratega de Negocio: actívame para análisis estratégico y proyección de crecimiento."
---

# Prompt del agente...
```

### .windsurf/rules/*.md (Reglas file-scoped)
```markdown
---
trigger: glob
globs:
  - "backend/**/*.py"
  - "backend/**/*.ts"
description: "Reglas de seguridad para backend"
---

# Contenido de la regla...
```

## Triggers de Windsurf

| Trigger | Comportamiento |
|---------|---------------|
| `always_on` | Cargada siempre, máx 6,000 chars por archivo |
| `model_decision` | El modelo decide según la `description` |
| `glob` | Solo para archivos que matcheen los `globs` |
| `manual` | Solo cuando el usuario la invoca explícitamente |

## Instrucciones de Instalación

1. Copia `AGENTS.md` en la raíz de tu proyecto
2. Copia la carpeta `.windsurf/` en la raíz de tu proyecto
3. Copia la carpeta `docs/` en la raíz de tu proyecto
4. Abre el proyecto en Windsurf
5. `AGENTS.md` se carga automáticamente
6. Las rules `always_on` se inyectan en cada conversación
7. Las rules `model_decision` se activan según contexto
