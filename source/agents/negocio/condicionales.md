---
name: agentes-negocio-condicionales
description: "Catálogo de agentes de negocio condicionales que se generan según el rubro del proyecto. Referencia para el Creador de Entornos."
scope: always
---

# Agentes de Negocio Condicionales

Agentes que se instancian solo cuando el rubro del proyecto lo requiere. El Creador de Entornos evalúa las condiciones y genera los que apliquen.

## Especialista Financiero/Contable
- **Se genera cuando:** Facturación, pagos, contabilidad o reporting financiero.
- **Expertise:** Reglas fiscales, conciliación bancaria, auditoría, compliance financiero.
- **Interactúa con:** `agente-estratega-negocio`, `agente-backend`, `agente-operaciones`.

## Especialista en Cadena de Suministro
- **Se genera cuando:** Inventarios, logística, distribución o manufactura.
- **Expertise:** Gestión de inventario, optimización de rutas, planificación de demanda.
- **Interactúa con:** `agente-operaciones`, `agente-backend`, `agente-datos`.

## Especialista en Compliance/Legal
- **Se genera cuando:** Regulaciones complejas (salud, finanzas, educación, gobierno).
- **Expertise:** GDPR, HIPAA, normativas locales, auditoría de compliance.
- **Interactúa con:** `agente-estratega-negocio`, `agente-seguridad`, `agente-arquitecto-principal`.

## Especialista en Recursos Humanos
- **Se genera cuando:** Gestión de personal, nóminas o evaluaciones de desempeño.
- **Expertise:** Legislación laboral, cálculo de nóminas, evaluación de desempeño.
- **Interactúa con:** `agente-operaciones`, `agente-backend`.

## Especialista en Marketing/Ventas
- **Se genera cuando:** CRM, campañas o gestión comercial.
- **Expertise:** Embudos de conversión, segmentación, lead scoring, pipelines de ventas.
- **Interactúa con:** `agente-ux-negocio`, `agente-estratega-negocio`, `agente-frontend`.

## Especialista Sectorial
- **Se genera cuando:** El rubro tiene conocimiento de dominio muy específico.
- **Expertise:** Varía por sector (ej: protocolos médicos, syllabus educativo, routing logístico).
- **Interactúa con:** Todos los agentes de negocio del proyecto.
