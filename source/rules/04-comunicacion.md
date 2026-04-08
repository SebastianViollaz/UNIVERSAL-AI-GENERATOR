---
name: reglas-comunicacion
description: "Reglas del protocolo de comunicación entre agentes y con el programador. Se aplican siempre."
scope: always
---

# Reglas de Comunicación y Protocolos

## R-011: Protocolo de Conflicto Negocio-Técnico
> **Cuando una decisión técnica contradice una regla de negocio, prevalece el negocio salvo que sea técnicamente imposible.**

- El agente técnico debe demostrar la imposibilidad con evidencia concreta.
- Si es solo "difícil" o "costoso", prevalece la regla de negocio.
- Si es imposible, se proponen alternativas que satisfagan parcialmente la regla.
- Todas las excepciones se documentan como ADRs con categoría "conflicto-resuelto".

## R-012: Preguntas Antes de Suponer
> **Si la descripción del proyecto es ambigua o incompleta, el agente DEBE hacer preguntas clarificadoras.**

- No inventar requisitos.
- No asumir un rubro si puede haber varios.
- No elegir tecnologías sin confirmar restricciones.
- Las preguntas son específicas, no abiertas. Ofrecer opciones cuando sea posible.
- **Máximo 10 preguntas** por ronda.

## R-013: Transparencia en Decisiones
> **Toda decisión del agente debe estar justificada y ser cuestionable.**

- No usar "best practice" como justificación única.
- Incluir siempre: contexto → alternativas → decisión → consecuencias.
- El programador puede anular cualquier decisión del agente.
- Las decisiones anuladas se documentan como restricciones, no se borran.
