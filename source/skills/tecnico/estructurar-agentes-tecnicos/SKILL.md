---
name: estructurar-agentes-tecnicos
description: "Define los roles técnicos necesarios (arquitectura, backend, frontend, QA, DevOps, seguridad), sus responsabilidades y coordinación con agentes de negocio."
---

# Skill: estructurar_agentes_tecnicos

## Propósito
A partir del análisis del dominio y los agentes de negocio, define qué roles técnicos se necesitan, sus responsabilidades y cómo se coordinan entre sí y con los agentes de negocio.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `analisis_dominio` | object | Sí | Output de `analizar_dominio_negocio` |
| `agentes_negocio` | object[] | Sí | Output de `disenar_agentes_negocio` |
| `stack_preferido` | object | No | Tecnologías que el programador prefiere |
| `restricciones_infra` | string[] | No | Limitaciones de infraestructura |

## Outputs

```yaml
agentes_tecnicos:
  - nombre: string
    identificador: string
    rol: string
    stack_tecnologico:
      - tecnologia: string
        version: string
        justificacion: string
    responsabilidades: string[]
    patrones_que_aplica:
      - patron: string
        contexto: string
        justificacion: string
    estandares_que_sigue:
      - estandar: string
        referencia: string
    decisiones_arquitectura:
      - decision: string
        alternativas_consideradas: string[]
        justificacion: string
        consecuencias: string[]
    capacidades_tecnicas_profundas:
      - area: string
        conocimientos: string[]
        puede_decidir: string[]
        debe_consultar: string[]
    interactua_con:
      - agente: string
        tipo_interaccion: string
        frecuencia: string
    prompt_base: string
```

## Reglas Internas
1. Mínimo 4 agentes técnicos: arquitecto, backend, frontend, QA/testing.
2. Si hay datos sensibles, agregar un agente de seguridad.
3. Si hay integraciones externas complejas, agregar agente de integraciones.
4. Cada agente técnico tiene al menos un agente de negocio como contraparte.
5. Las justificaciones del stack son técnicas Y de negocio.
