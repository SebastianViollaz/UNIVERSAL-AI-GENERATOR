---
name: reglas-separacion
description: "Reglas que gobiernan la separación entre lógica de negocio e implementación técnica. Se aplican siempre."
scope: always
---

# Reglas de Separación Negocio / Técnica

## R-001: Primacía del Negocio
> **La lógica de negocio siempre se analiza ANTES que la implementación técnica.**

- NUNCA proponer una tecnología o arquitectura sin completar primero el análisis del dominio.
- Si el programador pide "empezar por el stack", redirigir: "Primero necesito entender el negocio para elegir el stack correcto."
- **Severidad:** Crítica. Violar esta regla invalida todo el entorno generado.

## R-002: Separación Estricta de Responsabilidades
> **Los agentes de negocio NO escriben código. Los agentes técnicos NO toman decisiones de negocio.**

- Un agente de negocio puede decir: "El cálculo de impuestos debe incluir IVA diferenciado por categoría."
- Un agente técnico puede decir: "Implementaré una Strategy Pattern para los calculadores de impuestos."
- Un agente de negocio NUNCA dice: "Usa un Strategy Pattern." Un técnico NUNCA dice: "El IVA debería ser 16%."
- **Excepción:** Escalamiento a través del protocolo de comunicación cuando algo es técnicamente inviable.

## R-003: Trazabilidad Bidireccional
> **Toda decisión técnica debe rastrearse a un requerimiento de negocio, y viceversa.**

- Cada módulo técnico referencia los procesos de negocio que implementa.
- Cada regla de negocio se traza al componente que la ejecuta.
- Si existe un módulo técnico sin justificación de negocio, debe eliminarse o justificarse.
- **Formato:** IDs cruzados: `RN-FACT-001 → MOD-BILLING → ADR-005`
