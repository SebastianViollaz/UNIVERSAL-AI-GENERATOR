---
name: analizar-escalabilidad-negocio
description: "Evalúa el potencial de crecimiento del negocio y diseña las fases de evolución que el sistema debe soportar."
---

# Skill: analizar_escalabilidad_negocio

## Propósito
Evalúa el potencial de crecimiento del negocio y diseña las fases de evolución que el sistema debe soportar. Piensa más allá del MVP: proyecta cómo el negocio puede evolucionar y qué capacidades técnicas se necesitarán.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `analisis_dominio` | object | Sí | Output de `analizar_dominio_negocio` |
| `horizonte_temporal` | string | No | Período de proyección (default: "3 años") |

## Outputs

```yaml
plan_escalabilidad:
  fase_mvp:
    duracion_estimada: string
    funcionalidades_core: string[]
    procesos_cubiertos: string[]
    usuarios_esperados: string
    volumen_datos_estimado: string
  fases_crecimiento:
    - nombre: string
      trigger_de_fase: string
      kpis_que_disparan_fase:            # Métricas medibles que indican que es hora de pasar a esta fase
        - kpi: string
          umbral: string
      nuevas_funcionalidades: string[]
      nuevos_procesos: string[]
      nuevas_integraciones: string[]
      impacto_arquitectura: string
      agentes_nuevos_requeridos: string[]
      riesgos: string[]
  oportunidades_futuras:
    - oportunidad: string
      viabilidad: enum[alta, media, baja]
      prerequisitos: string[]
      impacto_revenue: enum[alto, medio, bajo]
  decisiones_arquitectura_preventivas:
    - decision: string
      justificacion: string
      costo_si_se_pospone: string
```

## Reglas Internas
1. Siempre proyectar mínimo 3 fases de crecimiento.
2. Cada fase tiene un trigger medible con `kpis_que_disparan_fase`, no basado en tiempo arbitrario.
3. Las decisiones preventivas balancean costo actual vs. deuda técnica futura.
4. Considerar pivotes de negocio realistas según el rubro.
5. Puede ejecutarse inmediatamente después de `analizar_dominio_negocio` — no requiere agentes de negocio definidos.
