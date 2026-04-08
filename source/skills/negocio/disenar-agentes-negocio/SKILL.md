---
name: disenar-agentes-negocio
description: "Diseña los agentes de negocio especializados que actuarán como consultores virtuales del dominio, con capacidad propositiva de mejoras."
---

# Skill: disenar_agentes_negocio

## Propósito
A partir del análisis del dominio, diseña los agentes de negocio especializados que actuarán como consultores virtuales. Cada agente es un experto en un área específica del negocio y puede proponer mejoras, validar requerimientos y guiar decisiones.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `analisis_dominio` | object | Sí | Output de `analizar_dominio_negocio` |
| `prioridades_cliente` | string[] | No | Áreas prioritarias para el cliente |
| `presupuesto_estimado` | string | No | Rango de presupuesto |

## Outputs

```yaml
agentes_negocio:
  - nombre: string
    identificador: string
    rol: string
    dominio_expertise:
      - area: string
        nivel: enum[experto, avanzado, intermedio]
        conocimientos_especificos: string[]
    responsabilidades: string[]
    capacidades_propositivas:
      - area: string
        tipo_mejora: enum[optimizacion, automatizacion, nueva_funcionalidad, reduccion_riesgo]
        descripcion: string
    decisiones_que_toma: string[]
    decisiones_que_escala: string[]
    inputs_que_necesita:
      - fuente: string
        dato: string
        formato: string
    outputs_que_genera:
      - destino: string
        dato: string
        formato: string
    interactua_con: string[]
    criterios_exito: string[]
    preguntas_clave:
      - pregunta: string
        por_que_importa: string
    restricciones_explicitas: string[]   # Cosas que este agente NO debe hacer
    prompt_base:                         # Estructura mínima obligatoria
      identidad: string                  # "Eres {rol} del proyecto {nombre}. {contexto_1_parrafo}"
      contexto_dominio: string           # Las 3 reglas de negocio más relevantes para este agente
      decisiones_que_toma: string[]      # Lista concreta de decisiones autónomas
      restricciones_hard: string[]       # Líneas que nunca cruza
      formato_respuesta: string          # Cómo estructura sus outputs
agentes_condicionales_recomendados:
  - nombre: string
    justificacion: string
    trigger: string                      # Qué característica del dominio justifica este agente
```

## Reglas Internas
1. Mínimo 3 agentes de negocio por proyecto.
2. Siempre incluir un "Agente Estratega de Negocio" que piense en escalabilidad.
3. Cada agente debe tener capacidades propositivas: no solo describen, también mejoran.
4. Cubrir como mínimo: operaciones, finanzas/métricas, y experiencia de usuario.
5. El `prompt_base` sigue la estructura mínima definida: identidad, contexto, decisiones, restricciones, formato.
6. Siempre evaluar y recomendar agentes condicionales del catálogo en AGENTS.md.
