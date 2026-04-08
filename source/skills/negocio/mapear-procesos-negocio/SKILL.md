---
name: mapear-procesos-negocio
description: "Detalla los procesos de negocio en flujos completos con estados, decisiones, excepciones y métricas medibles."
---

# Skill: mapear_procesos_negocio

## Propósito
Toma los procesos identificados en el análisis del dominio y los detalla en flujos completos con estados, decisiones, excepciones y métricas. Produce documentación que sirve como especificación funcional para los agentes técnicos.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `procesos_principales` | object[] | Sí | Lista de procesos del análisis del dominio |
| `roles_usuario` | object[] | Sí | Roles de usuario identificados |
| `reglas_negocio` | object[] | No | Reglas de negocio ya formalizadas |

## Outputs

```yaml
procesos_detallados:
  - nombre: string
    identificador: string
    version: string
    trigger: string
    precondiciones: string[]
    postcondiciones: string[]
    actores:
      - rol: string
        tipo: enum[primario, secundario, sistema]
    flujo_principal:
      - paso: number
        actor: string
        accion: string
        sistema_responde: string
        datos_involucrados: string[]
    flujos_alternativos:
      - nombre: string
        desde_paso: number
        condicion: string
        pasos: object[]
    excepciones:
      - nombre: string
        condicion: string
        manejo: string
    reglas_negocio_aplicables:
      - regla: string
        descripcion: string
        validacion: string
    metricas:
      - nombre: string
        que_mide: string
        valor_objetivo: string
    dependencias:
      - proceso: string
        tipo: enum[precede, sucede, paralelo]
```

## Reglas Internas
1. Todo proceso debe tener al menos un flujo alternativo y una excepción.
2. Cada paso especifica qué datos se crean, leen, actualizan o eliminan.
3. Las reglas de negocio deben ser atómicas y testeables.
4. Incluir métricas que permitan medir la eficiencia del proceso.
