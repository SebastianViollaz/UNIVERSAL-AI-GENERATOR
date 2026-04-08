---
name: priorizar-backlog-inicial
description: "Prioriza el backlog de user stories del MVP usando MoSCoW, alineado con el plan de escalabilidad y restricciones de tiempo/presupuesto."
---

# Skill: priorizar_backlog_inicial

## Propósito
Evita el scope creep desde el día uno. Convierte la lista de user stories en un backlog priorizado con sprints estimados, listo para ser consumido por el equipo de desarrollo.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `user_stories` | object[] | Sí | Output de `generar_user_stories` |
| `plan_escalabilidad` | object | Sí | Output de `analizar_escalabilidad_negocio` |
| `restricciones_tiempo` | string | No | Plazo del MVP (ej: "3 meses") |
| `restricciones_presupuesto` | string | No | Rango de presupuesto |
| `velocidad_equipo` | string | No | Story points por sprint estimado |

## Outputs

```yaml
backlog_priorizado:
  mvp:
    duracion_estimada: string
    sprints: number
    historias:
      - story_id: string
        prioridad: enum[must, should, could, wont]
        sprint_estimado: number
        justificacion: string          # Por qué esta prioridad desde el negocio
        dependencias_tecnicas: string[]
    kpis_entregables: string[]         # Qué KPIs de negocio quedan cubiertos al terminar el MVP
  post_mvp:
    - fase: string
      historias: string[]
      trigger_de_inicio: string        # KPI que indica cuando abordar esta fase
  riesgos_scope:
    - historia_id: string
      riesgo: string
      recomendacion: string
  resumen_ejecutivo:
    funcionalidades_mvp: string[]
    funcionalidades_fuera_scope: string[]
    valor_entregado: string            # En términos de negocio
```

## Reglas Internas
1. Los "must" del MVP son solo los necesarios para que el negocio funcione.
2. Las historias con `impacto_si_se_viola: legal` son automáticamente "must".
3. Las dependencias técnicas se respetan incluso si bajan la prioridad de negocio.
4. Incluir al menos 1 historia "quick win" en el sprint 1 para validar el entorno.
5. Las historias "wont" deben documentar por qué — evita repreguntas del cliente.
