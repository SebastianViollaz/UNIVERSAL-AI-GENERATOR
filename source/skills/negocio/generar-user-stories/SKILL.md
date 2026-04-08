---
name: generar-user-stories
description: "Transforma procesos de negocio mapeados en user stories con criterios de aceptación en formato Gherkin, listas para el backlog."
---

# Skill: generar_user_stories

## Propósito
Produce el puente más directo entre el análisis de negocio y el código. Cada user story es directamente usable como ticket de backlog con criterios de aceptación testeables.

## Diferencia con `mapear-procesos-negocio`
- `mapear_procesos_negocio` describe el FLUJO desde la perspectiva del sistema.
- `generar_user_stories` describe la NECESIDAD desde la perspectiva del usuario, con criterios ejecutables como tests.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `procesos_detallados` | object[] | Sí | Output de `mapear_procesos_negocio` |
| `roles_usuario` | object[] | Sí | Roles de usuario del análisis del dominio |
| `reglas_negocio` | object[] | Sí | Output de `formalizar_reglas_negocio` |

## Outputs

```yaml
user_stories:
  - id: string                         # US-{NNN}
    titulo: string
    rol: string                        # El rol de usuario que la protagoniza
    narrativa:
      como: string                     # "Como {rol}"
      quiero: string                   # "Quiero {accion}"
      para_que: string                 # "Para que {beneficio de negocio}"
    proceso_origen: string             # ID del proceso de negocio del que deriva
    reglas_negocio_aplicadas: string[] # IDs RN-XXX que se deben respetar
    criterios_aceptacion:
      - id: string                     # AC-{NNN}
        gherkin:
          dado: string
          cuando: string
          entonces: string
          y: string[]                  # Condiciones adicionales (opcional)
    definicion_de_listo: string[]      # Checklist técnico para marcar como Done
    prioridad_sugerida: enum[must, should, could, wont]
    dependencias: string[]             # IDs de otras user stories que deben completarse antes
    estimacion_relativa: enum[XS, S, M, L, XL]
```

## Reglas Internas
1. Una user story por flujo principal del proceso; flujos alternativos generan historias adicionales.
2. Los criterios de aceptación usan Gherkin puro — directamente copiables a tests E2E.
3. Cada story referencia las reglas de negocio que valida — trazabilidad completa.
4. La `definicion_de_listo` incluye siempre: tests pasando, reglas de negocio cubiertas, documentación actualizada.
5. Las historias de excepciones (flujos alternativos) tienen menor prioridad que el happy path.
