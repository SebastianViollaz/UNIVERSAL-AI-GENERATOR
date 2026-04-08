# Flujo de Ejecución — 8 Fases

El sistema ejecuta un flujo secuencial de 8 fases cuando el usuario describe un proyecto de software. Cada fase produce artefactos que alimentan las fases siguientes.

## Fase 1: Análisis del Dominio

**Skill:** `analizar-dominio-negocio`

Desglosa la descripción del usuario en:
- **Rubro** — Industria, mercado, regulaciones aplicables
- **Procesos** — Flujos de trabajo principales y secundarios
- **Roles** — Stakeholders, usuarios finales, administradores
- **Regulaciones** — Cumplimiento legal, fiscal, sectorial
- **KPIs** — Métricas de éxito del negocio
- **Dolor actual** — Problemas que el software debe resolver

**Output:** Documento de análisis de dominio con componentes de negocio identificados.

## Fase 2: Diseño de Agentes de Negocio

**Skills:** `disenar-agentes-negocio`, `mapear-procesos-negocio`, `formalizar-reglas-negocio`

Crea agentes expertos del dominio:
- **3 obligatorios:** Estratega de Negocio, Operaciones, UX de Negocio
- **Condicionales por rubro:** Compliance, Financiero, Inventario, Marketing, RRHH, Internacionalización

**Output:** Especificación de cada agente con responsabilidades, inputs, outputs y criterios de activación.

## Fase 3: Diseño de Agentes Técnicos

**Skills:** `estructurar-agentes-tecnicos`, `disenar-arquitectura-sistema`, `disenar-seguridad-sistema`

Crea roles técnicos adaptados al contexto:
- **4 obligatorios:** Arquitecto Principal, Backend, Frontend, QA/Testing
- **Condicionales:** DevOps, Seguridad, Datos, Integraciones, Mobile

**Output:** Especificación técnica de cada agente con su stack, patrones y responsabilidades.

## Fase 4: Protocolo de Comunicación

**Skill:** `generar-protocolo-comunicacion`

Define cómo colaboran los agentes entre sí:
- Reglas de conflicto (negocio vs técnica)
- Escalamiento cuando no hay acuerdo
- Formato de intercambio entre agentes
- Dependencias y orden de consulta

**Output:** Protocolo de comunicación inter-agentes con reglas de conflicto.

## Fase 5: Árbol de Documentación

**Skill:** `generar-arbol-documentacion`

Genera el esqueleto completo de archivos `.md` del proyecto:
- ADRs (Architecture Decision Records)
- Glosario del dominio
- Especificaciones de API
- Modelo de datos
- Guías de onboarding

**Output:** Estructura de directorios con archivos de documentación con contenido real.

## Fase 6: Materialización para Vibe Coding

**Skills:** `generar-agentes-ia`, `generar-instrucciones-workspace`, `generar-rules-ia`, `generar-skills-ia`, `optimizar-prompts-ia`

Esta es la fase diferenciadora. Transforma los agentes conceptuales de las fases 2-3 en **archivos funcionales** para la IA de codificación:

| Sub-fase | Qué Produce | Ejemplo |
|----------|-------------|---------|
| 6.1 Agentes IA | `.agent.md` por agente con contexto de negocio inyectado | `@backend` ya sabe las reglas de facturación |
| 6.2 Instrucciones de workspace | `copilot-instructions.md` o `CLAUDE.md` con glosario | La IA entiende el dominio desde el primer prompt |
| 6.3 Reglas de codificación | Restricciones por módulo | "Montos → Decimal, NUNCA float" |
| 6.4 Skills del proyecto | Skills invocables: revisar-regla, consultar-ADR, generar-test | `@qa generar-test-regla RN-FACT-001` |
| 6.5 Prompts reutilizables | Flujos comunes automatizados | implementar-proceso, crear-módulo |
| 6.6 Quick Start Guide | Guía de inicio en < 5 minutos | Copiar → primer prompt útil |

**Output:** Archivos `.agent.md`, rules, skills, prompts, instrucciones de workspace listos para copiar.

## Fase 7: Validación

**Skill:** `validar-entorno-generado`

Verifica calidad con score mínimo de 80/100 en 4 dimensiones:
- **Negocio** — ¿Se capturó todo el dominio?
- **Técnico** — ¿La arquitectura es coherente?
- **Vibe Coding** — ¿Los agentes IA son funcionales?
- **Completitud** — ¿Falta algo crítico?

Checklist de validación (9 items):
1. Cada agente de negocio tiene contraparte técnica
2. Cada regla de negocio tiene restricción de código
3. El glosario cubre todos los términos del dominio
4. Los agentes IA son autónomos (funcionan sin los otros)
5. El token budget se respeta (< 300 líneas instrucciones, < 150 agentes)
6. El Quick Start funciona en < 5 minutos
7. Los archivos son plug & play (copiar al workspace y funciona)
8. Las convenciones de naming son consistentes
9. Los ADRs tienen justificación de negocio

## Fase 8: Exportación

**Skill:** `exportar-entorno`

Empaqueta todo para la IA objetivo usando `export.py`:
```bash
python export.py --target copilot --output ./mi-proyecto
```

Genera la estructura nativa de la IA seleccionada con todos los archivos transformados.
