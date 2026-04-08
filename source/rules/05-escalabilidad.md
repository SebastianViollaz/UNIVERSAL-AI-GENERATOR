---
name: reglas-escalabilidad
description: "Reglas que aseguran que el entorno generado soporte la evolución futura del negocio. Se aplican siempre."
scope: always
---

# Reglas de Escalabilidad y Evolución

## R-014: Diseño para el Futuro
> **El entorno debe soportar la evolución del negocio sin reescrituras.**

- Las fases de escalabilidad del plan de negocio se reflejan en la arquitectura técnica.
- Los módulos tienen boundaries claros para evolucionar independientemente.
- Las decisiones técnicas "preventivas" (tomadas hoy para el futuro) se documentan como ADR.

## R-015: Agentes Evolutivos
> **Los agentes diseñados deben poder evolucionar cuando el negocio cambie.**

- Cada agente tiene un campo `version` y un historial de cambios.
- El protocolo de comunicación soporta la adición de nuevos agentes sin romper los existentes.
- Los prompts de los agentes son parametrizables.
