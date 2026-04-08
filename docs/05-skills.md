# Skills del Sistema (20)

## Negocio (5)

### `analizar-dominio-negocio`
- **Archivo:** `source/skills/negocio/analizar-dominio-negocio/SKILL.md`
- **Input:** Descripción del proyecto
- **Output:** Desglose por rubro, procesos, roles, regulaciones, KPIs, dolor actual
- **Fase:** 1

### `disenar-agentes-negocio`
- **Archivo:** `source/skills/negocio/disenar-agentes-negocio/SKILL.md`
- **Input:** Análisis de dominio
- **Output:** Especificación de agentes expertos del dominio (obligatorios + condicionales activados)
- **Fase:** 2

### `mapear-procesos-negocio`
- **Archivo:** `source/skills/negocio/mapear-procesos-negocio/SKILL.md`
- **Input:** Procesos identificados
- **Output:** Flujos detallados con estados, excepciones, métricas, responsables
- **Fase:** 2

### `analizar-escalabilidad-negocio`
- **Archivo:** `source/skills/negocio/analizar-escalabilidad-negocio/SKILL.md`
- **Input:** Análisis de dominio + stakeholders
- **Output:** Proyecciones de crecimiento, fases de evolución, bottlenecks anticipados
- **Fase:** 2

### `formalizar-reglas-negocio`
- **Archivo:** `source/skills/negocio/formalizar-reglas-negocio/SKILL.md`
- **Input:** Reglas implícitas del dominio
- **Output:** Reglas atómicas, testables, versionadas con ID (RN-XXX-NNN)
- **Fase:** 2

## Técnico (5)

### `estructurar-agentes-tecnicos`
- **Archivo:** `source/skills/tecnico/estructurar-agentes-tecnicos/SKILL.md`
- **Input:** Agentes de negocio + análisis de dominio
- **Output:** Roles técnicos con stack, patrones, responsabilidades, coordinación
- **Fase:** 3

### `disenar-arquitectura-sistema`
- **Archivo:** `source/skills/tecnico/disenar-arquitectura-sistema/SKILL.md`
- **Input:** Requerimientos de negocio + agentes técnicos
- **Output:** Arquitectura, ADRs, estructura de módulos, modelo de datos, estrategia de API
- **Fase:** 3

### `definir-estrategia-testing`
- **Archivo:** `source/skills/tecnico/definir-estrategia-testing/SKILL.md`
- **Input:** Arquitectura + reglas de negocio
- **Output:** Pirámide de testing, priorización por riesgo de negocio, CI gates, cobertura
- **Fase:** 3

### `disenar-seguridad-sistema`
- **Archivo:** `source/skills/tecnico/disenar-seguridad-sistema/SKILL.md`
- **Input:** Datos sensibles + regulaciones + arquitectura
- **Output:** Threat model, estrategia de auth/authz, OWASP, compliance
- **Fase:** 3

### `planificar-infraestructura`
- **Archivo:** `source/skills/tecnico/planificar-infraestructura/SKILL.md`
- **Input:** Arquitectura + SLAs + presupuesto
- **Output:** CI/CD, monitoring, deployment strategy, estimación de costos
- **Fase:** 3

## Orquestación (5)

### `generar-protocolo-comunicacion`
- **Archivo:** `source/skills/orquestacion/generar-protocolo-comunicacion/SKILL.md`
- **Input:** Agentes de negocio + agentes técnicos
- **Output:** Reglas de comunicación inter-agentes, resolución de conflictos, escalamiento
- **Fase:** 4

### `generar-prompts-agentes`
- **Archivo:** `source/skills/orquestacion/generar-prompts-agentes/SKILL.md`
- **Input:** Especificación de agentes
- **Output:** Prompts completos para cada agente en formato nativo de la IA
- **Fase:** 5

### `generar-arbol-documentacion`
- **Archivo:** `source/skills/orquestacion/generar-arbol-documentacion/SKILL.md`
- **Input:** Todas las fases anteriores
- **Output:** Esqueleto completo de archivos `.md` del proyecto con contenido real
- **Fase:** 5

### `validar-entorno-generado`
- **Archivo:** `source/skills/orquestacion/validar-entorno-generado/SKILL.md`
- **Input:** Todo el entorno generado
- **Output:** Score ≥ 80/100 en 4 dimensiones (negocio, técnico, vibe coding, completitud)
- **Fase:** 7

### `exportar-entorno`
- **Archivo:** `source/skills/orquestacion/exportar-entorno/SKILL.md`
- **Input:** Entorno validado + IA objetivo
- **Output:** Paquete exportado en formato nativo de la IA
- **Fase:** 8

## Vibe Coding (5)

### `generar-agentes-ia`
- **Archivo:** `source/skills/vibe-coding/generar-agentes-ia/SKILL.md`
- **Input:** Agentes diseñados (negocio + técnicos)
- **Output:** Archivos `.agent.md`/`.mdc` funcionales con frontmatter, tools y contexto de negocio inyectado
- **Fase:** 6

### `generar-instrucciones-workspace`
- **Archivo:** `source/skills/vibe-coding/generar-instrucciones-workspace/SKILL.md`
- **Input:** Análisis de dominio + arquitectura + convenciones
- **Output:** `copilot-instructions.md` / `CLAUDE.md` con glosario, convenciones, stack, referencias
- **Fase:** 6

### `generar-rules-ia`
- **Archivo:** `source/skills/vibe-coding/generar-rules-ia/SKILL.md`
- **Input:** Reglas de negocio formalizadas
- **Output:** Restricciones de código por módulo (ej: "Montos → Decimal, NUNCA float")
- **Fase:** 6

### `generar-skills-ia`
- **Archivo:** `source/skills/vibe-coding/generar-skills-ia/SKILL.md`
- **Input:** Reglas, ADRs, patrones del proyecto
- **Output:** Skills invocables: revisar-regla, consultar-ADR, generar-test, auditar-seguridad, crear-módulo
- **Fase:** 6

### `optimizar-prompts-ia`
- **Archivo:** `source/skills/vibe-coding/optimizar-prompts-ia/SKILL.md`
- **Input:** Todos los archivos generados para la IA
- **Output:** Versión optimizada: deduplicación, compresión semántica, token budget, ordenado por prioridad
- **Fase:** 6
