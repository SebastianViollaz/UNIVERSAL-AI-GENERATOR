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
    restricciones_explicitas: string[]   # Cosas que este agente NO debe hacer
    prompt_base:                         # Estructura mínima obligatoria
      identidad: string                  # "Eres {rol} técnico del proyecto {nombre}. {contexto_tecnico_1_parrafo}"
      contexto_negocio: string           # Por qué existe este rol desde la perspectiva del negocio
      decisiones_que_toma: string[]      # Decisiones técnicas autónomas
      restricciones_tecnicas: string[]   # Estilo de código, patrones prohibidos, tecnologías vetadas
      agente_negocio_contraparte: string # El agente de negocio con quien coordina
stack_consolidado:                       # Objeto único consumido por instrucciones-workspace, rules-ia, skills-ia
  backend:
    tecnologia: string
    version: string
    justificacion: string
  frontend:
    tecnologia: string
    version: string
    justificacion: string
  base_datos_principal:
    tecnologia: string
    justificacion: string
  cache: string
  cola_mensajes: string
  infra: string
  testing:
    unitarios: string
    integracion: string
    e2e: string

## Reglas Internas
1. Mínimo 4 agentes técnicos: arquitecto, backend, frontend, QA/testing.
2. Si hay datos sensibles, agregar un agente de seguridad.
3. Si hay integraciones externas complejas, agregar agente de integraciones.
4. Cada agente técnico tiene al menos un agente de negocio como contraparte.
5. Las justificaciones del stack son técnicas Y de negocio.
6. Producir `stack_consolidado` obligatoriamente — es el único objeto `stack` del sistema; otras skills lo consumen.
