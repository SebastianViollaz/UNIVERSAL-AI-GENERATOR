---
name: formalizar-reglas-negocio
description: "Transforma las reglas de negocio implícitas en especificaciones formales, atómicas y testeables para implementación directa."
---

# Skill: formalizar_reglas_negocio

## Propósito
Transforma las reglas de negocio implícitas en especificaciones formales, atómicas y testeables que los agentes técnicos puedan implementar directamente.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `procesos_detallados` | object[] | Sí | Output de `mapear_procesos_negocio` |
| `regulaciones` | object[] | No | Regulaciones aplicables |
| `analisis_dominio` | object | Sí | Output de `analizar_dominio_negocio` |

## Outputs

```yaml
reglas_negocio:
  - id: string
    nombre: string
    categoria: enum[validacion, calculo, restriccion, autorizacion, notificacion, workflow]
    descripcion: string
    condicion: string
    accion: string
    excepcion: string
    impacto_si_se_viola:                 # Clarifica prioridad de implementación
      tipo: enum[legal, financiero, operacional, reputacional]
      severidad: enum[critico, alto, medio, bajo]
      descripcion: string
    procesos_afectados: string[]
    datos_involucrados: string[]
    fuente: string
    prioridad: enum[obligatoria, recomendada, opcional]
    criterio_test:                       # Formato Gherkin para uso directo en tests de aceptación
      dado: string
      cuando: string
      entonces: string
    ejemplos:
      - caso: string
        input: string
        resultado_esperado: string
```

## Reglas Internas
1. Cada regla debe tener al menos un ejemplo concreto.
2. Las reglas deben ser independientes entre sí (atómicas).
3. El `criterio_test` usa formato Gherkin (Dado/Cuando/Entonces) — ejecutable directamente como test de aceptación.
4. Priorizar reglas que provienen de regulaciones legales.
5. El `impacto_si_se_viola` determina el orden de implementación: las de tipo legal/crítico van en el MVP.
