# Reglas de Ejecución (26)

Las reglas están organizadas en 7 categorías y se almacenan en `source/rules/`.

## 1. Separación Negocio/Técnica (`01-separacion.md`)

| ID | Regla | Descripción |
|----|-------|-------------|
| R-001 | Primacía del negocio en el análisis | El análisis del dominio SIEMPRE comienza desde el negocio, nunca desde la tecnología |
| R-002 | Separación estricta de responsabilidad | Agentes de negocio NO toman decisiones técnicas; agentes técnicos NO redefinen reglas de negocio |
| R-003 | Trazabilidad bidireccional | Cada decisión técnica debe trazarse a una necesidad de negocio y viceversa |

## 2. Calidad y Profundidad (`02-calidad.md`)

| ID | Regla | Descripción |
|----|-------|-------------|
| R-004 | Profundidad dual obligatoria | Cada tema se aborda desde negocio Y desde técnica. Un tema con solo 1 perspectiva está incompleto |
| R-005 | Nada queda implícito | Si no se documenta, no existe. El sistema pregunta antes de suponer |
| R-006 | Los agentes de negocio proponen | No solo documentan, activamente identifican oportunidades de mejora y optimización |
| R-007 | Profundidad técnica real | Los agentes técnicos incluyen código ejemplo, configuraciones concretas, no solo descripciones |

## 3. Formato y Estructura (`03-formato.md`)

| ID | Regla | Descripción |
|----|-------|-------------|
| R-008 | Formato inyectable | Todo output es Markdown con frontmatter YAML, listo para consumo directo por el IDE |
| R-009 | Estructura determinista | Cada fase tiene sections fijas. El output siempre sigue la misma estructura |
| R-010 | 8 secciones obligatorias | Análisis del Dominio, Agentes Negocio, Agentes Técnicos, Comunicación, Documentación, Vibe Coding, Validación, Próximos Pasos |

## 4. Comunicación (`04-comunicacion.md`)

| ID | Regla | Descripción |
|----|-------|-------------|
| R-011 | Protocolo de conflicto negocio-técnica | Cuando hay conflicto, el negocio tiene prioridad salvo restricción técnica insalvable |
| R-012 | Preguntas antes de suposiciones | Si hay ambigüedad, el sistema pregunta al usuario en vez de asumir |
| R-013 | Decisiones transparentes | Toda recomendación incluye el POR QUÉ de negocio que la justifica |

## 5. Escalabilidad (`05-escalabilidad.md`)

| ID | Regla | Descripción |
|----|-------|-------------|
| R-014 | Diseño para evolución futura | La arquitectura contempla al menos 2 fases de crecimiento |
| R-015 | Evolución de agentes | Los agentes pueden evolucionar sus responsabilidades conforme el proyecto crece |

## 6. Validación (`06-validacion.md`)

| ID | Regla | Descripción |
|----|-------|-------------|
| R-016 | Gate de calidad 80/100 | Score mínimo de 80 sobre 100 en las 4 dimensiones antes de entregar |
| R-017 | Completitud sobre velocidad | Mejor 90% completo que 100% superficial |
| R-018 | Compatibilidad con IAs | El output funciona en las 6 IAs soportadas sin modificación |

## 7. Vibe Coding (`07-vibe-coding.md`)

| ID | Regla | Descripción |
|----|-------|-------------|
| R-019 | Output ejecutable | Los archivos generados son funcionales directamente, no descriptivos |
| R-020 | Contexto inyectado | El contexto de negocio va DENTRO del agente, no como referencia externa |
| R-021 | Agentes autónomos | Cada agente funciona sin que los otros estén activos |
| R-022 | Perfiles negocio → Agentes IA | Cada perfil de negocio se transforma en un agente IA con contexto inyectado |
| R-023 | Perfiles técnicos → Agentes código | Cada perfil técnico se transforma en un agente IA con tools de escritura |
| R-024 | Token budget | Instrucciones < 300 líneas, agentes < 150 líneas, rules < 50 líneas cada una |
| R-025 | Quick Start obligatorio | Todo entorno incluye guía de inicio en < 5 minutos |
| R-026 | Bidireccionalidad | Los agentes IA reflejan tanto la perspectiva de negocio como la técnica |
