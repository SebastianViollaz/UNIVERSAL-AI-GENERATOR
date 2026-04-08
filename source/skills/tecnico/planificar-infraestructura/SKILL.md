---
name: planificar-infraestructura
description: "Define la estrategia de infraestructura, CI/CD, monitoring y operaciones alineada con el plan de escalabilidad del negocio."
---

# Skill: planificar_infraestructura

## Propósito
Define la estrategia de infraestructura, deployment y operaciones alineada con el plan de escalabilidad del negocio.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `arquitectura` | object | Sí | Output de `disenar_arquitectura_sistema` |
| `plan_escalabilidad` | object | Sí | Output de `analizar_escalabilidad_negocio` |
| `restricciones_infra` | string[] | No | Limitaciones del cliente |

## Outputs

```yaml
infraestructura:
  ambiente_desarrollo:
    setup: string[]
    herramientas: string[]
    docker_compose: boolean
  ambiente_produccion:
    proveedor: string
    servicios: string[]
    alta_disponibilidad: string
    backup: string
  ci_cd:
    plataforma: string
    pipeline_stages: string[]
    gates_de_calidad: string[]
    deploy_strategy: enum[blue_green, canary, rolling, recreate]
  monitoring:
    metricas_tecnicas: string[]
    metricas_negocio: string[]
    alertas: string[]
    herramientas: string[]
  costos_estimados:
    mvp: string
    crecimiento_fase_1: string
```

## Reglas Internas
1. Siempre incluir métricas de negocio en monitoring, no solo técnicas.
2. Disaster recovery si la criticidad del negocio es alta.
3. Costos alineados con fases de escalabilidad del negocio.
4. Docker es el default para desarrollo; justificar si se omite.
