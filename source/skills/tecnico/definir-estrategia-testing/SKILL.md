---
name: definir-estrategia-testing
description: "Diseña la estrategia completa de testing: pirámide, priorización por riesgo de negocio, testing no funcional y CI gates."
---

# Skill: definir_estrategia_testing

## Propósito
Diseña la estrategia completa de testing del proyecto, alineada con los riesgos del negocio y los procesos críticos identificados.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `procesos_detallados` | object[] | Sí | Output de `mapear_procesos_negocio` |
| `reglas_negocio` | object[] | Sí | Output de `formalizar_reglas_negocio` |
| `arquitectura` | object | Sí | Output de `disenar_arquitectura_sistema` |

## Outputs

```yaml
estrategia_testing:
  piramide:
    unitarios:
      porcentaje_cobertura_objetivo: string
      enfoque: string
      frameworks: string[]
    integracion:
      porcentaje_cobertura_objetivo: string
      enfoque: string
      frameworks: string[]
    e2e:
      porcentaje_cobertura_objetivo: string
      enfoque: string
      frameworks: string[]
  prioridad_testing:
    - proceso: string
      riesgo_negocio: enum[critico, alto, medio, bajo]
      tipo_test_requerido: string[]
      escenarios_criticos:
        - escenario: string
          regla_negocio_validada: string
          gherkin:                       # Directamente usable en tests de aceptación
            dado: string
            cuando: string
            entonces: string
            y: string[]                  # Condiciones adicionales (opcional)
  testing_no_funcional:
    performance:
      herramientas: string[]
      escenarios: string[]
    seguridad:
      herramientas: string[]
      checklist: string[]
    accesibilidad:
      estandar: string
      herramientas: string[]
  estrategia_ci:
    cuando_ejecutar: string
    gates_de_calidad: string[]
    tiempo_maximo_pipeline: string
  test_data_management:
    estrategia: enum[fixtures, factories, seeders, mocks]
    datos_sensibles: string             # Cómo manejar PII en tests (anonimizar, sintetizar)
    consistencia: string                # Cómo garantizar que los datos respetan reglas de negocio
    herramientas: string[]

## Reglas Internas
1. Los procesos críticos del negocio tienen cobertura E2E completa.
2. Cada regla de negocio formalizada tiene al menos un test asociado con formato Gherkin.
3. Tests de seguridad obligatorios si hay datos personales o financieros.
4. Priorizar por riesgo de negocio, no por cobertura numérica.
5. La estrategia de `test_data_management` es obligatoria si hay reglas de negocio sobre integridad de datos.
