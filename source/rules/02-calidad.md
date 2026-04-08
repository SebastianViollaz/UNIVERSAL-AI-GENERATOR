---
name: reglas-calidad
description: "Reglas de profundidad y calidad que aseguran cobertura completa tanto en negocio como en técnica. Se aplican siempre."
scope: always
---

# Reglas de Profundidad y Calidad

## R-004: Profundidad Dual Obligatoria
> **Cada aspecto del proyecto debe tener cobertura profunda tanto desde el negocio como desde la técnica.**

- Si se identifica un módulo de "Facturación":
  - **Negocio:** Reglas fiscales del país, tipos de comprobante, políticas de crédito, flujos de aprobación, auditoría.
  - **Técnico:** Modelo de datos, API de facturación electrónica, colas para procesamiento asíncrono, idempotencia, reconciliación.
- La profundidad es proporcional a la criticidad del proceso.
- **Métrica:** Un proceso con criticidad "crítica" requiere mínimo 10 reglas de negocio formalizadas y 3 ADRs técnicos.

## R-005: Nada Queda Implícito
> **Toda la documentación generada debe ser comprensible por una IA que nunca ha visto el proyecto.**

- No usar "como es habitual en el sector" sin explicar qué es habitual.
- No asumir que el lector conoce las regulaciones del país.
- No referirse a "el proceso normal" sin describir cuál es.
- Cada archivo incluye el contexto necesario para ser leído de forma independiente.

## R-006: Capacidad Propositiva de los Agentes de Negocio
> **Los agentes de negocio DEBEN proponer mejoras activamente, no solo describir el estado actual.**

- Por cada proceso analizado, al menos una propuesta de mejora.
- Categorías: optimización, automatización, nueva funcionalidad, reducción de riesgo.
- Cada propuesta incluye: impacto estimado, esfuerzo estimado y dependencias.
- **Prohibido:** Crear agentes de negocio que solo documenten sin proponer.

## R-007: Profundidad Técnica Real
> **Los agentes técnicos deben demostrar conocimiento profundo, no genérico.**

- Prohibido: "se usará una base de datos relacional".
- Correcto: "PostgreSQL 16 con particionamiento por fecha en tablas de transacciones, índices GIN para full-text, y pg_cron para jobs de reconciliación nocturna."
- Cada decisión técnica incluye alternativas y trade-offs.
- Los patrones de diseño se justifican con el contexto específico.
