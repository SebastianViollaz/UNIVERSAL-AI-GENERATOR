# Agentes del Sistema

## Agentes Obligatorios (10)

### Negocio (3)

#### Estratega de Negocio
- **Archivo:** `source/agents/negocio/estratega-negocio.md`
- **Tipo:** negocio
- **Rol:** Visión estratégica, modelo de monetización, escalabilidad, ROI, análisis de mercado
- **Cuándo actúa:** Fase 1 (análisis) y Fase 2 (diseño de negocio)
- **Output:** Análisis estratégico, proyecciones de crecimiento, modelo de negocio

#### Operaciones
- **Archivo:** `source/agents/negocio/operaciones.md`
- **Tipo:** negocio
- **Rol:** Procesos operativos, automatización, supply chain, optimización de flujos
- **Cuándo actúa:** Fase 2 (mapeo de procesos)
- **Output:** Mapas de procesos, puntos de automatización, métricas operativas

#### UX de Negocio
- **Archivo:** `source/agents/negocio/ux-negocio.md`
- **Tipo:** negocio
- **Rol:** User journeys, puntos de fricción, accesibilidad, satisfacción del usuario
- **Cuándo actúa:** Fase 2 (diseño de experiencia)
- **Output:** Journeys de usuario, wireframes conceptuales, criterios de acepatción UX

### Técnicos (4)

#### Arquitecto Principal
- **Archivo:** `source/agents/tecnicos/arquitecto-principal.md`
- **Tipo:** tecnico
- **Rol:** Arquitectura del sistema, ADRs, DDD, modelo de datos, patterns de diseño
- **Cuándo actúa:** Fase 3 (diseño técnico)
- **Output:** Diagramas de arquitectura, ADRs, modelo de datos, estrategia de APIs

#### Backend
- **Archivo:** `source/agents/tecnicos/backend.md`
- **Tipo:** tecnico
- **Rol:** APIs, base de datos, migraciones, integraciones externas, lógica de negocio
- **Cuándo actúa:** Fase 3 (implementación server-side)
- **Output:** Especificaciones de API, esquemas de DB, contratos de integración

#### Frontend
- **Archivo:** `source/agents/tecnicos/frontend.md`
- **Tipo:** tecnico
- **Rol:** UI/UX técnico, componentes, estados, accesibilidad web, responsive
- **Cuándo actúa:** Fase 3 (implementación client-side)
- **Output:** Componentes, estados, rutas, estrategia de accesibilidad

#### QA/Testing
- **Archivo:** `source/agents/tecnicos/qa-testing.md`
- **Tipo:** tecnico
- **Rol:** Estrategia de testing, pirámide de tests, CI gates, performance testing
- **Cuándo actúa:** Fase 3 y Fase 7 (validación)
- **Output:** Plan de testing, cobertura por riesgo, configuración de CI

### Vibe Coding (3)

#### Generador de Agentes IA
- **Archivo:** `source/agents/vibe-coding/generador-agentes-ia.md`
- **Tipo:** vibe-coding
- **Rol:** Transforma cada agente diseñado (negocio/técnico) en un archivo `.agent.md` funcional con frontmatter, tools configurados y contexto de negocio inyectado
- **Cuándo actúa:** Fase 6 (materialización)
- **Output:** Archivos `.agent.md` funcionales listos para el IDE

#### Configurador de Entorno IA
- **Archivo:** `source/agents/vibe-coding/configurador-entorno-ia.md`
- **Tipo:** vibe-coding
- **Rol:** Genera instrucciones de workspace, reglas de codificación, glosario, convenciones
- **Cuándo actúa:** Fase 6 (materialización)
- **Output:** `copilot-instructions.md`, `CLAUDE.md`, reglas por módulo, glosario

#### Orquestador de Vibe Coding
- **Archivo:** `source/agents/vibe-coding/orquestador-vibe.md`
- **Tipo:** vibe-coding
- **Rol:** Coordina el flujo completo de materialización y genera el Quick Start Guide
- **Cuándo actúa:** Fase 6 (coordinación) y Fase 7 (validación de Vibe Coding)
- **Output:** Quick Start Guide, validación de completitud, empaquetado final

## Agentes Condicionales

### Negocio (se activan según el rubro)
- **Regulación y Compliance** — Rubros regulados (salud, finanzas, educación)
- **Analista Financiero** — Proyectos con facturación, pagos, contabilidad
- **Gestión de Inventario** — Manufactura, retail, logística
- **Marketing Digital** — E-commerce, SaaS, marketplaces
- **RRHH y Cultura** — Empresas con >20 empleados
- **Internacionalización** — Operaciones multi-país

**Catálogo:** `source/agents/negocio/condicionales.md`

### Técnicos (se activan según requerimientos)
- **Ingeniero de Datos** — BI, analytics, reportes complejos
- **Especialista Mobile** — Apps nativas o PWA
- **Ingeniero DevOps/SRE** — SLAs críticos, alta disponibilidad
- **Especialista en Integraciones** — >3 sistemas externos
- **Ingeniero de Seguridad** — Datos sensibles (salud, finanzas, PII)

**Catálogo:** `source/agents/tecnicos/condicionales.md`
