# Creador de Entornos Iniciales — Universal AI Generator

## Qué es esto

Un **meta-agente** que transforma la descripción de un proyecto de software en un entorno de desarrollo completo y **listo para Vibe Coding**: agentes de negocio, agentes técnicos, skills, reglas y documentación que se materializan como **archivos funcionales** (.agent.md, .mdc, SKILL.md, rules) que tu IA de codificación consume directamente.

**El resultado:** describes tu negocio → se genera la estructura → copias al workspace → tu IA ya sabe del dominio, las reglas, la arquitectura y los patrones desde el primer prompt.

## IAs Soportadas

| IA | Formato Nativo | Comando de Exportación |
|----|---------------|----------------------|
| **GitHub Copilot** | `.github/agents/`, `.github/instructions/`, `.github/skills/` | `python export.py --target copilot --output ./proyecto` |
| **Claude Code** | `CLAUDE.md`, `.claude/rules/`, `.claude/agents/` | `python export.py --target claude --output ./proyecto` |
| **Cursor** | `AGENTS.md`, `.cursor/rules/*.mdc` | `python export.py --target cursor --output ./proyecto` |
| **Windsurf** | `AGENTS.md`, `.windsurf/rules/`, `.windsurf/skills/` | `python export.py --target windsurf --output ./proyecto` |
| **Aider** | `CONVENTIONS.md`, `.aider.conf.yml` | `python export.py --target aider --output ./proyecto` |
| **Continue.dev** | `.continue/rules/`, `.continue/config.yaml` | `python export.py --target continue --output ./proyecto` |
| **Todas** | Genera las 6 variantes | `python export.py --target all --output ./exports` |

## Estructura del Repositorio

```
BASE-GENERATOR/
├── source/                              ← FUENTE CANÓNICA (agnóstica de IA)
│   ├── instructions/
│   │   └── workspace.md                 ← Instrucciones globales del agente
│   ├── rules/
│   │   ├── 01-separacion.md             ← R-001 a R-003
│   │   ├── 02-calidad.md               ← R-004 a R-007
│   │   ├── 03-formato.md               ← R-008 a R-010
│   │   ├── 04-comunicacion.md          ← R-011 a R-013
│   │   ├── 05-escalabilidad.md         ← R-014 a R-015
│   │   ├── 06-validacion.md            ← R-016 a R-018
│   │   └── 07-vibe-coding.md           ← R-019 a R-026 (Vibe Coding)
│   ├── agents/
│   │   ├── negocio/                     ← 3 obligatorios + catálogo condicionales
│   │   ├── tecnicos/                    ← 4 obligatorios + catálogo condicionales
│   │   └── vibe-coding/                ← 3 agentes de materialización IA
│   │       ├── generador-agentes-ia.md  ← Produce archivos .agent.md funcionales
│   │       ├── configurador-entorno-ia.md ← Produce instrucciones y reglas de workspace
│   │       └── orquestador-vibe.md      ← Coordina todo el flujo de Vibe Coding
│   ├── skills/
│   │   ├── negocio/                     ← 5 skills de análisis de negocio
│   │   ├── tecnico/                     ← 5 skills de diseño técnico
│   │   ├── orquestacion/               ← 5 skills de documentación y orquestación
│   │   └── vibe-coding/                ← 5 skills de materialización para IA
│   │       ├── generar-agentes-ia/      ← Produce .agent.md con contexto inyectado
│   │       ├── generar-instrucciones-workspace/ ← Produce copilot-instructions/CLAUDE.md
│   │       ├── generar-rules-ia/        ← Traduce reglas negocio → código
│   │       ├── generar-skills-ia/       ← Crea skills del proyecto (ADRs, tests)
│   │       └── optimizar-prompts-ia/    ← Optimiza tokens y efectividad
│   └── prompts/
│       └── generar-entorno.prompt.md    ← Prompt principal de ejecución
│
├── templates/                           ← Documentación de cada formato de exportación
├── meta/
│   └── export-targets.yml               ← Mapeo detallado de frontmatter por IA
│
├── export.py                            ← Script de exportación universal
├── AGENTS.md                            ← Punto de entrada universal (Copilot, Cursor, Windsurf)
├── system-prompt.md                     ← System prompt completo (referencia)
└── README.md                            ← Este archivo
```

## Cómo Usar

### Paso 1: Elegir tu IA

Decide qué herramienta de IA usarás para desarrollar tu proyecto.

### Paso 2: Exportar al formato nativo

```bash
# Ejemplo para GitHub Copilot
python export.py --target copilot --output ./mi-proyecto-erp

# Ejemplo para Claude Code
python export.py --target claude --output ./mi-proyecto-erp

# Generar TODOS los formatos
python export.py --target all --output ./exports
```

### Paso 3: Inyectar el system prompt

Carga `system-prompt.md` como contexto de tu IA y describe tu proyecto:

```
"Necesito un ERP para una empresa familiar de manufactura de muebles
con 50 empleados en México. Actualmente usan Excel para todo."
```

### Paso 4: La IA genera el entorno

El agente ejecutará las 8 secciones obligatorias:
1. **Análisis del Dominio** — Rubro, procesos, regulaciones, KPIs
2. **Agentes de Negocio Diseñados** — Especializados por rubro
3. **Agentes Técnicos Diseñados** — Adaptados al contexto
4. **Mapa de Comunicación Inter-Agentes** — Protocolo de colaboración
5. **Árbol de Documentación Generado** — Todos los `.md` del proyecto
6. **Entorno de Vibe Coding Generado** — Archivos funcionales para tu IA:
   - Agentes IA (.agent.md) con contexto de negocio inyectado
   - Instrucciones de workspace con glosario y convenciones
   - Reglas de codificación por módulo
   - Skills del proyecto (revisar reglas, consultar ADRs, generar tests)
   - Prompts reutilizables para flujos comunes
   - Quick Start Guide
7. **Checklist de Validación** — Score ≥ 80/100 en 4 dimensiones
8. **Próximos Pasos Recomendados** — Qué hacer primero

### Paso 5: Copiar al workspace del proyecto

Copia los archivos generados a la raíz de tu proyecto. La IA leerá automáticamente las instrucciones, reglas y agentes en su formato nativo.

## Formato Canónico Universal

Todos los archivos fuente usan **YAML frontmatter universal** que `export.py` transforma:

```yaml
---
name: "identificador-unico"
description: "Descripción para discovery por la IA"
scope: "always"                    # always | file_pattern | manual
file_patterns: "**/*.py"           # Solo si scope = file_pattern
---
```

### Transformación de frontmatter por IA

| Campo Universal | Copilot | Claude | Cursor | Windsurf | Continue |
|----------------|---------|--------|--------|----------|----------|
| `scope: always` | `applyTo: "**"` | sin `paths` | `alwaysApply: true` | `trigger: always_on` | `alwaysApply: true` |
| `scope: file_pattern` | `applyTo: "{pattern}"` | `paths: ["{pattern}"]` | `globs: "{pattern}"` | `trigger: glob` | `globs: "{pattern}"` |
| `scope: manual` | sin `applyTo` | sin `paths` | `alwaysApply: false` | `trigger: manual` | `alwaysApply: false` |

## Inventario Completo

### 20 Skills

| # | Categoría | Skill | Propósito |
|---|-----------|-------|-----------|
| 1 | Negocio | `analizar-dominio-negocio` | Desglosar proyecto en componentes de negocio |
| 2 | Negocio | `disenar-agentes-negocio` | Crear agentes expertos del dominio |
| 3 | Negocio | `mapear-procesos-negocio` | Detallar flujos con excepciones y métricas |
| 4 | Negocio | `analizar-escalabilidad-negocio` | Proyectar fases de crecimiento |
| 5 | Negocio | `formalizar-reglas-negocio` | Convertir reglas en specs testeables |
| 6 | Técnico | `estructurar-agentes-tecnicos` | Definir roles técnicos |
| 7 | Técnico | `disenar-arquitectura-sistema` | Arquitectura, ADRs, modelo de datos |
| 8 | Técnico | `definir-estrategia-testing` | Testing priorizado por riesgo de negocio |
| 9 | Técnico | `disenar-seguridad-sistema` | Threat model, auth, OWASP |
| 10 | Técnico | `planificar-infraestructura` | CI/CD, monitoring, deployment |
| 11 | Orquestación | `generar-arbol-documentacion` | Esqueleto completo del proyecto |
| 12 | Orquestación | `generar-prompts-agentes` | Prompts listos para cada agente |
| 13 | Orquestación | `generar-protocolo-comunicacion` | Reglas de comunicación inter-agentes |
| 14 | Orquestación | `validar-entorno-generado` | Validación de calidad pre-entrega |
| 15 | Orquestación | `exportar-entorno` | Empaquetar para IA objetivo |
| 16 | **Vibe Coding** | `generar-agentes-ia` | Producir .agent.md funcionales con contexto inyectado |
| 17 | **Vibe Coding** | `generar-instrucciones-workspace` | Producir copilot-instructions.md/CLAUDE.md |
| 18 | **Vibe Coding** | `generar-rules-ia` | Traducir reglas negocio → restricciones de código |
| 19 | **Vibe Coding** | `generar-skills-ia` | Crear skills del proyecto (ADRs, tests, auditoría) |
| 20 | **Vibe Coding** | `optimizar-prompts-ia` | Optimizar tokens, deduplicar, ordenar por prioridad |

### 10 Agentes Obligatorios

| Agente | Tipo | Rol |
|--------|------|-----|
| Estratega de Negocio | Negocio | Visión estratégica, escalabilidad, ROI |
| Operaciones | Negocio | Procesos operativos, automatización |
| UX (Negocio) | Negocio | Journeys de usuario, puntos de fricción |
| Arquitecto Principal | Técnico | Arquitectura, ADRs, DDD |
| Backend | Técnico | APIs, base de datos, integraciones |
| Frontend | Técnico | UI, componentes, accesibilidad |
| QA/Testing | Técnico | Estrategia de testing, CI gates |
| **Generador de Agentes IA** | **Vibe Coding** | Materializa agentes como archivos .agent.md funcionales |
| **Configurador de Entorno IA** | **Vibe Coding** | Genera instrucciones, reglas y glosario del workspace |
| **Orquestador de Vibe Coding** | **Vibe Coding** | Coordina la materialización y genera Quick Start |

### 26 Reglas de Ejecución

| Categoría | Reglas | IDs |
|-----------|--------|-----|
| Separación Negocio/Técnica | 3 | R-001 a R-003 |
| Calidad y Profundidad | 4 | R-004 a R-007 |
| Formato y Estructura | 3 | R-008 a R-010 |
| Comunicación | 3 | R-011 a R-013 |
| Escalabilidad | 2 | R-014 a R-015 |
| Validación | 3 | R-016 a R-018 |
| **Vibe Coding** | **8** | **R-019 a R-026** |

## Qué Produce el Vibe Coding

Cuando describes tu proyecto, el sistema genera archivos **funcionales** listos para tu IA:

| Archivo Generado | Qué Hace | Ejemplo |
|------------------|----------|---------|
| `.agent.md` por agente | Agente IA con contexto de negocio inyectado y tools configurados | `@backend` ya sabe las reglas de facturación de tu país |
| Instrucciones de workspace | La IA entiende el proyecto desde el primer prompt | Glosario, convenciones, stack, referencias |
| Reglas de codificación | Previenen violaciones de reglas de negocio en código | "Montos → Decimal, NUNCA float (RN-FACT-001)" |
| Skills del proyecto | Los agentes pueden consultar reglas, ADRs, generar tests | `@qa generar-test-regla-negocio RN-FACT-001` |
| Prompts reutilizables | Flujos de trabajo cubiertos | "Implementar proceso de negocio end-to-end" |
| Quick Start Guide | < 5 minutos para empezar a codificar | Copiar → abrir IDE → primer prompt |

## Principio Central

> **El negocio manda, la técnica habilita. El Vibe Coding lo materializa.**
> Cada agente de negocio propone mejoras. Cada agente técnico justifica con necesidades de negocio.
> Cada agente de Vibe Coding produce archivos funcionales que tu IA consume desde el primer prompt.
> El resultado: describes tu negocio → tu IA ya sabe TODO al abrir el proyecto.
