---
name: validar-entorno-generado
description: "Ejecuta validación completa del entorno generado: consistencia, completitud, trazabilidad y puntuación de calidad antes de entregar."
---

# Skill: validar_entorno_generado

## Propósito
Ejecuta una validación completa del entorno generado para asegurar consistencia, completitud y usabilidad antes de entregarlo al programador.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `arbol_documentacion` | object | Sí | Output de `generar_arbol_documentacion` |
| `prompts_agentes` | object | Sí | Output de `generar_prompts_agentes` |
| `reglas_negocio` | object[] | Sí | Output de `formalizar_reglas_negocio` |
| `arquitectura` | object | Sí | Output de `disenar_arquitectura_sistema` |

## Outputs

```yaml
validacion:
  puntuacion_global: number
  checklist:
    - item: string
      estado: enum[ok, warning, error]
      detalle: string
  cobertura:
    procesos_negocio_cubiertos: string
    reglas_negocio_trazadas: string
    agentes_con_contraparte: string
    adrs_documentados: string
    archivos_con_contenido: string
  errores: string[]
  advertencias: string[]
  sugerencias: string[]
  resumen_ejecutivo: string
```

## Reglas Internas
1. Un entorno con errores NO se entrega. Se corrige primero.
2. La puntuación mínima aceptable es 80/100.
3. Todo proceso de negocio trazado a al menos un módulo técnico.
4. Todo agente de negocio tiene contraparte técnica.
5. Generar resumen ejecutivo en lenguaje no técnico.
