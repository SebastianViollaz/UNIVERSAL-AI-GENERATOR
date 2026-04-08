# Template de Exportación: Continue.dev

## Estructura de Archivos Generada

```
proyecto/
├── .continue/
│   ├── config.yaml                        ← Configuración de Continue
│   └── rules/
│       ├── 01-workspace.md                ← Instrucciones globales
│       ├── 02-separacion.md
│       ├── 03-calidad.md
│       ├── 04-formato.md
│       ├── 05-comunicacion.md
│       ├── 06-escalabilidad.md
│       ├── 07-validacion.md
│       ├── agente-estratega-negocio.md
│       ├── agente-operaciones.md
│       └── ... (todos los agentes como rules)
├── docs/
│   ├── negocio/ ...
│   ├── tecnico/ ...
│   └── agentes/ ...
└── README.md
```

## Formato de Archivos

### .continue/config.yaml
```yaml
# Configuración mínima de Continue.dev
# Ajustar modelos según preferencia del usuario
models:
  - name: "default"
    provider: "anthropic"  # o openai, ollama, etc.

rules:
  # Las reglas se cargan automáticamente de .continue/rules/
```

### .continue/rules/*.md (Always-on)
```markdown
---
name: "reglas-separacion"
description: "Separación entre lógica de negocio e implementación técnica"
alwaysApply: true
---

# Contenido de la regla...
```

### .continue/rules/*.md (Agentes como rules)
```markdown
---
name: "agente-estratega-negocio"
description: "Agente Estratega de Negocio: invócame para análisis estratégico y proyección de crecimiento."
alwaysApply: false
---

# Prompt del agente...
```

### .continue/rules/*.md (File-scoped)
```markdown
---
name: "seguridad-backend"
description: "Reglas de seguridad para código backend"
globs: "backend/**/*.{ts,js,py}"
---

# Contenido de la regla...
```

## Instrucciones de Instalación

1. Copia la carpeta `.continue/` en la raíz de tu proyecto
2. Copia la carpeta `docs/` en la raíz de tu proyecto
3. Configura tu modelo en `.continue/config.yaml`
4. Instala la extensión Continue.dev en VS Code
5. Las rules always-on se cargan automáticamente
6. Las rules inteligentes se activan según la description
