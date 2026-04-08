---
name: disenar-arquitectura-sistema
description: "Define la arquitectura del sistema: estilo, módulos, ADRs, modelo de datos conceptual, estrategia de API y requisitos no funcionales."
---

# Skill: disenar_arquitectura_sistema

## Propósito
Define la arquitectura del sistema a nivel macro y micro. Produce ADRs, estructura de módulos/servicios y modelo conceptual de datos.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `analisis_dominio` | object | Sí | Output de `analizar_dominio_negocio` |
| `procesos_detallados` | object[] | Sí | Output de `mapear_procesos_negocio` |
| `agentes_tecnicos` | object[] | Sí | Output de `estructurar_agentes_tecnicos` |
| `plan_escalabilidad` | object | Sí | Output de `analizar_escalabilidad_negocio` |
| `requisitos_no_funcionales` | object | No | Performance, disponibilidad, etc. |

## Outputs

```yaml
arquitectura:
  estilo: string
  justificacion_estilo: string
  diagrama_alto_nivel: string          # Formato Mermaid obligatorio: C4Context o graph TD
  diagrama_modulos: string             # Mermaid flowchart con dependencias entre módulos
  modulos:
    - nombre: string
      responsabilidad: string
      procesos_negocio_que_cubre: string[]
      bounded_context: string
      entidades_principales: string[]
      servicios_expuestos: string[]
      dependencias: string[]
      agente_negocio_responsable: string
      agente_tecnico_responsable: string
  capas:
    - nombre: string
      responsabilidad: string
      tecnologias: string[]
      reglas: string[]
  adrs:
    - id: string
      titulo: string
      estado: enum[propuesto, aceptado, rechazado, deprecado]
      contexto: string
      decision: string
      alternativas: string[]
      consecuencias_positivas: string[]
      consecuencias_negativas: string[]
      relacion_negocio: string
      reglas_negocio_referenciadas: string[]  # IDs RN-XXX que justifican este ADR
  modelo_datos_conceptual:
    entidades:
      - nombre: string
        atributos_clave: string[]
        relaciones: string[]
        reglas_negocio_asociadas: string[]
  estrategia_api:
    estilo: enum[REST, GraphQL, gRPC, mixto]
    justificacion: string
    versionado: string
    autenticacion: string
  requisitos_no_funcionales:
    performance:
      tiempo_respuesta_objetivo: string
      concurrencia_esperada: string
    disponibilidad:
      sla_objetivo: string
    seguridad:
      modelo_autenticacion: string
      modelo_autorizacion: string
      compliance: string[]
```

## Reglas Internas
1. Cada ADR vinculado a un requerimiento de negocio y al menos un ID `RN-XXX`.
2. La arquitectura debe soportar las fases de escalabilidad definidas.
3. Monolito modular es el default para proyectos pequeños/medianos.
4. El modelo de datos refleja entidades del dominio de negocio, no tablas técnicas.
5. Los diagramas usan Mermaid exclusivamente — son renderizables en docs y agentes IA.
