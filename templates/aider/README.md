# Template de Exportación: Aider

## Estructura de Archivos Generada

```
proyecto/
├── CONVENTIONS.md                         ← Todo concatenado en un solo archivo
├── .aider.conf.yml                        ← Config con read: CONVENTIONS.md
├── docs/
│   ├── negocio/ ...
│   ├── tecnico/ ...
│   └── agentes/ ...
└── README.md
```

## Formato de Archivos

### .aider.conf.yml
```yaml
read:
  - CONVENTIONS.md
  - docs/negocio/vision-proyecto.md
  - docs/tecnico/arquitectura/overview.md
```

### CONVENTIONS.md
```markdown
# [Nombre del Proyecto] — Convenciones

(Aider no tiene sistema de agents, rules o skills nativos.
Todo se concatena en un solo archivo CONVENTIONS.md que se 
carga como contexto de solo lectura.)

## Instrucciones del Workspace
[Contenido de source/instructions/workspace.md]

## Reglas
### Separación Negocio / Técnica
[Contenido de rules/01-separacion.md]

### Calidad y Profundidad
[Contenido de rules/02-calidad.md]

... (todas las reglas concatenadas)

## Agentes Disponibles
### Agentes de Negocio
[Resumen de cada agente de negocio]

### Agentes Técnicos
[Resumen de cada agente técnico]

## Skills del Sistema
[Lista y descripción de cada skill]

## Protocolo de Comunicación
[Contenido del protocolo]
```

## Instrucciones de Instalación

1. Copia `CONVENTIONS.md` en la raíz de tu proyecto
2. Copia `.aider.conf.yml` en la raíz de tu proyecto
3. Copia la carpeta `docs/` en la raíz de tu proyecto
4. Ejecuta `aider` en la raíz del proyecto
5. El archivo CONVENTIONS.md se carga automáticamente como contexto read-only
6. Puedes agregar más archivos de `docs/` a la sección `read:` del `.aider.conf.yml`
