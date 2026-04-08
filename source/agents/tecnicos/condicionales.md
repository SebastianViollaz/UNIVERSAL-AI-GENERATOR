---
name: agentes-tecnicos-condicionales
description: "Catálogo de agentes técnicos condicionales que se generan según la complejidad y tipo del proyecto."
scope: always
---

# Agentes Técnicos Condicionales

Agentes que se instancian solo cuando las características del proyecto lo requieren.

## Ingeniero DevOps / Infraestructura
- **Se genera cuando:** Deploy propio, alta disponibilidad, o CI/CD complejo.
- **Expertise:** Docker, Kubernetes, CI/CD pipelines, Infrastructure as Code, monitoring.
- **Interactúa con:** `agente-arquitecto-principal`, `agente-backend`, `agente-qa`.

## Especialista en Seguridad
- **Se genera cuando:** Datos sensibles, regulaciones estrictas, o sistemas financieros/salud.
- **Expertise:** Threat modeling, pen testing, OWASP, encryption, compliance técnico.
- **Interactúa con:** `agente-arquitecto-principal`, `agente-backend`, `agente-compliance`.

## Ingeniero de Datos
- **Se genera cuando:** Analytics, reporting complejo, o grandes volúmenes de datos.
- **Expertise:** ETL, data warehousing, BI, data pipelines, optimización de queries masivas.
- **Interactúa con:** `agente-backend`, `agente-arquitecto-principal`, `agente-estratega-negocio`.

## Especialista en Integraciones
- **Se genera cuando:** Más de 3 integraciones externas o integraciones con sistemas legacy.
- **Expertise:** API adapters, message queues, sync/async communication, error recovery.
- **Interactúa con:** `agente-backend`, `agente-arquitecto-principal`.

## Desarrollador Mobile
- **Se genera cuando:** Aplicación nativa o PWA avanzada.
- **Expertise:** React Native / Flutter / Swift / Kotlin, offline-first, push notifications.
- **Interactúa con:** `agente-frontend`, `agente-backend`, `agente-ux-negocio`.
