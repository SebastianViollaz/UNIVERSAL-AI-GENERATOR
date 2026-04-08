# Template de Exportación: GitHub Copilot

## Estructura de Archivos Generada

```
proyecto/
├── .github/
│   ├── copilot-instructions.md         ← Instrucciones globales del workspace
│   ├── instructions/
│   │   ├── 01-separacion.instructions.md
│   │   ├── 02-calidad.instructions.md
│   │   ├── 03-formato.instructions.md
│   │   ├── 04-comunicacion.instructions.md
│   │   ├── 05-escalabilidad.instructions.md
│   │   └── 06-validacion.instructions.md
│   ├── agents/
│   │   ├── estratega-negocio.agent.md
│   │   ├── operaciones.agent.md
│   │   ├── ux-negocio.agent.md
│   │   ├── arquitecto-principal.agent.md
│   │   ├── backend.agent.md
│   │   ├── frontend.agent.md
│   │   ├── qa-testing.agent.md
│   │   └── [agentes-condicionales].agent.md
│   ├── skills/
│   │   ├── analizar-dominio-negocio/SKILL.md
│   │   ├── disenar-agentes-negocio/SKILL.md
│   │   ├── mapear-procesos-negocio/SKILL.md
│   │   └── ... (una carpeta por skill)
│   └── prompts/
│       └── generar-entorno.prompt.md
├── docs/
│   ├── negocio/
│   │   ├── vision-proyecto.md
│   │   ├── modelo-negocio.md
│   │   ├── procesos/
│   │   ├── roles-usuario/
│   │   ├── reglas-negocio/
│   │   └── kpis-metricas.md
│   ├── tecnico/
│   │   ├── arquitectura/
│   │   ├── stack-tecnologico.md
│   │   ├── base-de-datos/
│   │   ├── api/
│   │   ├── testing/
│   │   ├── seguridad/
│   │   └── infraestructura/
│   └── agentes/
│       ├── indice-agentes.md
│       └── protocolo-comunicacion.md
└── README.md
```

## Formato de Archivos

### copilot-instructions.md
```markdown
# [Nombre del Proyecto]

Instrucciones globales para GitHub Copilot...
(Sin frontmatter YAML)
```

### *.instructions.md
```markdown
---
description: "Descripción para que Copilot sepa cuándo aplicar estas instrucciones"
applyTo: "**"
---

# Contenido de la regla...
```

### *.agent.md
```markdown
---
description: "Descripción del rol del agente para discovery"
tools:
  - read_file
  - grep_search
  - semantic_search
---

# Prompt del agente...
```

### SKILL.md (dentro de carpeta)
```markdown
---
name: nombre-skill
description: "Descripción para activación"
---

# Contenido de la skill...
```

## Instrucciones de Instalación

1. Copia la carpeta `.github/` en la raíz de tu proyecto
2. Copia la carpeta `docs/` en la raíz de tu proyecto
3. Abre el proyecto en VS Code con GitHub Copilot activo
4. Los agentes aparecerán en el chat al escribir `@`
5. Los prompts aparecerán al escribir `/`
6. Las instrucciones se cargan automáticamente según el `applyTo`
