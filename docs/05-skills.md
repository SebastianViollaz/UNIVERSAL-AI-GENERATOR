# Skills del Sistema (30)

## Negocio (7)

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

### `generar-user-stories`
- **Archivo:** `source/skills/negocio/generar-user-stories/SKILL.md`
- **Input:** Procesos de negocio mapeados + reglas formalizadas
- **Output:** User stories con IDs `US-NNN`, criterios de aceptación en Gherkin, prioridad MoSCoW
- **Fase:** 2

### `priorizar-backlog-inicial`
- **Archivo:** `source/skills/negocio/priorizar-backlog-inicial/SKILL.md`
- **Input:** User stories generadas
- **Output:** Backlog priorizado con MoSCoW, sprints estimados, riesgos de alcance
- **Fase:** 2

## Técnico (9)

### `seleccionar-stack-tecnologico`
- **Archivo:** `source/skills/tecnico/seleccionar-stack-tecnologico/SKILL.md`
- **Input:** Análisis de dominio + restricciones del negocio
- **Output:** `stack_consolidado` — objeto único con lenguaje, frameworks, BD, infra, servicios externos
- **Fase:** 3

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

### `generar-modelo-datos-fisico`
- **Archivo:** `source/skills/tecnico/generar-modelo-datos-fisico/SKILL.md`
- **Input:** Arquitectura + reglas de negocio + stack_consolidado
- **Output:** SQL ejecutable con tipos, índices, constraints, migrations, diagrama Mermaid ER
- **Fase:** 3

### `generar-contrato-api`
- **Archivo:** `source/skills/tecnico/generar-contrato-api/SKILL.md`
- **Input:** Arquitectura + user stories + stack_consolidado
- **Output:** OpenAPI 3.0 por módulo + colección Postman
- **Fase:** 3

### `generar-convenciones-git`
- **Archivo:** `source/skills/tecnico/generar-convenciones-git/SKILL.md`
- **Input:** Stack consolidado + equipo (tamaño y distribución)
- **Output:** Branching model, formato de commits, PR templates, .gitignore
- **Fase:** 3

## Orquestación (7)

### `verificar-trazabilidad`
- **Archivo:** `source/skills/orquestacion/verificar-trazabilidad/SKILL.md`
- **Input:** Requerimientos + procesos + reglas + módulos + tests
- **Output:** Matriz de trazabilidad requerimiento → proceso → regla → módulo → test; gaps identificados
- **Fase:** 7

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

### `generar-quick-start-guide`
- **Archivo:** `source/skills/orquestacion/generar-quick-start-guide/SKILL.md`
- **Input:** Entorno validado completo
- **Output:** Guía de onboarding < 5 minutos: copiar al workspace → abrir IDE → primer prompt
- **Fase:** 7

### `exportar-entorno`
- **Archivo:** `source/skills/orquestacion/exportar-entorno/SKILL.md`
- **Input:** Entorno validado + IA objetivo
- **Output:** Paquete exportado en formato nativo de la IA
- **Fase:** 8

## Vibe Coding (7)

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

### `generar-ejemplos-interaccion`
- **Archivo:** `source/skills/vibe-coding/generar-ejemplos-interaccion/SKILL.md`
- **Input:** Agentes IA generados + procesos de negocio
- **Output:** Conversaciones reales de dominio por agente + instrucciones de context reload
- **Fase:** 6

### `generar-contexto-comprimido`
- **Archivo:** `source/skills/vibe-coding/generar-contexto-comprimido/SKILL.md`
- **Input:** Entorno completo generado
- **Output:** Contexto comprimido ≤ 2000 tokens para IAs con ventana limitada (Aider, terminal)
- **Fase:** 6
