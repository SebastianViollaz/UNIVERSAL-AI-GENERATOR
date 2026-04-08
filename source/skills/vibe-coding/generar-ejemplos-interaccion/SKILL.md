---
name: generar-ejemplos-interaccion
description: "Genera conversaciones ejemplo entre el desarrollador y cada agente IA: el primer mensaje, cómo hacer preguntas de arquitectura, cómo pedir código respetando las reglas."
---

# Skill: generar_ejemplos_interaccion

## Propósito
Sin ejemplos de interacción, el desarrollador no sabe cómo hablar con los agentes generados. Esta skill produce conversaciones reales del dominio que demuestran la forma correcta de usar cada agente.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `agentes_ia` | object | Sí | Output de `generar_agentes_ia` |
| `procesos_detallados` | object[] | Sí | Para generar ejemplos del dominio real |
| `reglas_negocio` | object[] | Sí | Para mostrar cómo el agente las aplica |
| `arquitectura` | object | No | Para ejemplos de consultas técnicas |

## Outputs

```yaml
ejemplos_interaccion:
  por_agente:
    - agente_id: string
      agente_nombre: string
      conversaciones:
        - titulo: string               # "Consulta de regla de negocio"
          tipo: enum[consulta_simple, decision_arquitectura, generacion_codigo, resolucion_conflicto, context_reload]
          prompt_usuario: string       # Exacto — copiable directamente
          respuesta_esperada_resumen: string
          por_que_funciona: string     # Qué hace que este prompt sea efectivo
          errores_comunes:             # Cómo NO usar este agente
            - prompt_incorrecto: string
              problema: string
              version_correcta: string
  context_reload:                      # Instrucciones para cuando la IA "olvida" el contexto
    sintoma: string
    prompt_de_recuperacion: string     # Prompt estándar para recargar contexto
    archivos_a_mencionar: string[]
```

## Reglas Internas
1. Cada agente tiene mínimo 3 conversaciones: consulta simple, escenario complejo, y context reload.
2. Los prompts de ejemplo usan terminología real del dominio — no ejemplos genéricos.
3. El `context_reload` es obligatorio en todos los agentes — es la solución a la deriva de contexto.
4. Los `errores_comunes` muestran qué pasa cuando se usa el agente incorrectamente.
5. Las conversaciones demuestran específicamente las `restricciones_explicitas` del agente.
