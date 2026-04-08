---
name: verificar-trazabilidad
description: "Construye la matriz de trazabilidad completa: cada requerimiento de negocio debe tener proceso → regla → módulo → agente responsable → test. Detecta huecos."
---

# Skill: verificar_trazabilidad

## Propósito
Complementa `validar-entorno-generado` enfocándose en las relaciones entre capas. Mientras `validar-entorno-generado` verifica completitud, esta skill verifica que los elementos estén correctamente conectados entre sí.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `analisis_dominio` | object | Sí | Para los procesos raíz |
| `procesos_detallados` | object[] | Sí | Output de `mapear_procesos_negocio` |
| `reglas_negocio` | object[] | Sí | Output de `formalizar_reglas_negocio` |
| `arquitectura` | object | Sí | Output de `disenar_arquitectura_sistema` |
| `agentes_negocio` | object[] | Sí | Output de `disenar_agentes_negocio` |
| `agentes_tecnicos` | object[] | Sí | Output de `estructurar_agentes_tecnicos` |
| `estrategia_testing` | object | Sí | Output de `definir_estrategia_testing` |
| `user_stories` | object[] | No | Output de `generar_user_stories` (si existe) |

## Outputs

```yaml
trazabilidad:
  cobertura_total: number              # Porcentaje de requerimientos completamente trazados
  matriz:
    - proceso_id: string
      proceso_nombre: string
      reglas_asociadas: string[]       # IDs RN-XXX
      modulo_arquitectura: string
      agente_negocio: string
      agente_tecnico: string
      user_story_id: string            # Si existe
      test_cubierto: boolean
      estado: enum[completo, parcial, sin_trazar]
  gaps:
    - tipo: enum[proceso_sin_modulo, regla_sin_test, agente_sin_contraparte, modulo_sin_dueño]
      elemento: string
      descripcion: string
      impacto: enum[critico, alto, medio, bajo]
      sugerencia: string
  adrs_sin_regla_origen:               # ADRs que no referencian ningún RN-XXX
    - adr_id: string
      sugerencia: string
  resumen:
    procesos_completamente_trazados: number
    procesos_sin_trazar: number
    reglas_sin_test: number
    recomendacion_prioritaria: string
```

## Reglas Internas
1. Un proceso está "completamente trazado" solo si tiene módulo, agente técnico responsable y al menos un test.
2. Gaps de tipo `critico` bloquean la exportación del entorno.
3. Cada ADR debe referenciar al menos un ID `RN-XXX` que lo justifique.
4. Los agentes de negocio sin contraparte técnica son un gap de tipo `alto`.
5. Ejecutar después de `validar-entorno-generado` — son complementarias, no reemplazables.
