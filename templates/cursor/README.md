# Template de Exportación: Cursor

## Estructura de Archivos Generada

```
proyecto/
├── AGENTS.md                              ← Instrucciones principales (siempre activas)
├── .cursor/
│   └── rules/
│       ├── 01-separacion.mdc
│       ├── 02-calidad.mdc
│       ├── 03-formato.mdc
│       ├── 04-comunicacion.mdc
│       ├── 05-escalabilidad.mdc
│       ├── 06-validacion.mdc
│       ├── agente-estratega-negocio.mdc
│       ├── agente-operaciones.mdc
│       ├── agente-ux-negocio.mdc
│       ├── agente-arquitecto-principal.mdc
│       ├── agente-backend.mdc
│       ├── agente-frontend.mdc
│       ├── agente-qa-testing.mdc
│       └── [agentes-condicionales].mdc
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
(No requiere frontmatter. Se carga siempre.)
```

### .cursor/rules/*.mdc (Reglas always-on)
```markdown
---
description: "Descripción para que Cursor sepa cuándo aplicar"
alwaysApply: true
---

# Contenido de la regla...
```

### .cursor/rules/*.mdc (Agentes como rules)
```markdown
---
description: "Agente Estratega de Negocio: invócame cuando necesites análisis estratégico, priorización o proyección de crecimiento del negocio."
alwaysApply: false
---

# Prompt del agente...

(Cursor no tiene agents nativos. Los agentes se modelan como rules
con alwaysApply=false que el modelo activa inteligentemente según
la description, o que el usuario puede @mencionar manualmente.)
```

### .cursor/rules/*.mdc (Reglas file-scoped)
```markdown
---
description: "Reglas de seguridad para código backend"
globs: "backend/**/*.{ts,js,py}"
---

# Contenido de la regla...
```

## Modos de Activación en Cursor

| Modo | Frontmatter | Comportamiento |
|------|-------------|----------------|
| Siempre | `alwaysApply: true` | Cargada en todo contexto |
| Inteligente | `alwaysApply: false` + `description` | Cursor decide según la tarea |
| Por archivo | `globs: "pattern"` | Solo para archivos matching |
| Manual | Solo `description` | Usuario @menciona la regla |

## Instrucciones de Instalación

1. Copia `AGENTS.md` en la raíz de tu proyecto
2. Copia la carpeta `.cursor/` en la raíz de tu proyecto
3. Copia la carpeta `docs/` en la raíz de tu proyecto
4. Abre el proyecto en Cursor
5. `AGENTS.md` se carga automáticamente
6. Las reglas always-on se aplican siempre
7. Las reglas inteligentes se activan cuando el modelo las necesita
8. Puedes @mencionar cualquier regla manualmente en el chat
