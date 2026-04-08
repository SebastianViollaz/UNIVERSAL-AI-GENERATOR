---
name: seleccionar-stack-tecnologico
description: "Consolida las preferencias del cliente, restricciones del dominio y recomendaciones técnicas en el objeto stack_consolidado que todas las demás skills consumen."
---

# Skill: seleccionar_stack_tecnologico

## Propósito
Produce el único objeto `stack` del sistema. Ninguna skill debe inventar su propio stack — todas consumen este output. Razona desde el negocio hacia la tecnología, no al revés.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `analisis_dominio` | object | Sí | Output de `analizar_dominio_negocio` |
| `plan_escalabilidad` | object | Sí | Output de `analizar_escalabilidad_negocio` |
| `stack_preferido` | object | No | Tecnologías que el cliente/equipo prefiere |
| `restricciones_equipo` | string[] | No | Lenguajes conocidos, limitaciones de hiring, vendor lock-in |

## Outputs

```yaml
stack_consolidado:
  backend:
    tecnologia: string
    version: string
    justificacion_negocio: string      # Por qué este stack para este negocio
    justificacion_tecnica: string
    alternativas_rechazadas:
      - tecnologia: string
        razon: string
  frontend:
    tecnologia: string
    version: string
    justificacion_negocio: string
    justificacion_tecnica: string
    alternativas_rechazadas:
      - tecnologia: string
        razon: string
  base_datos_principal:
    tecnologia: string
    justificacion: string
    modelo: enum[relacional, documental, grafo, columnar, mixto]
  base_datos_secundaria:              # Cache, búsqueda, etc. — opcional
    tecnologia: string
    proposito: string
  cache:
    tecnologia: string
    proposito: string
  cola_mensajes:                      # Opcional — solo si hay procesos asíncronos
    tecnologia: string
    justificacion: string
  infra:
    proveedor_cloud: string
    contenedores: boolean
    orquestacion: string              # K8s, ECS, Fly.io, etc.
  testing:
    unitarios: string
    integracion: string
    e2e: string
    api: string
  decisiones_clave:
    - decision: string
      justificacion_negocio: string
      referencia_fase_escalabilidad: string
```

## Reglas Internas
1. Siempre justificar desde el negocio (no "es popular" sino "permite iteración rápida para el MVP").
2. Monolito modular > microservicios para proyectos <50k usuarios — justificar si se propone otra cosa.
3. Las restricciones del equipo tienen prioridad sobre las preferencias técnicas.
4. Documentar alternativas rechazadas — el stack elegido cobra sentido en contraste.
5. Este output es la única fuente de verdad del stack para todo el sistema.
