---
name: generar-protocolo-comunicacion
description: "Define las reglas formales de comunicación entre agentes: formatos de mensajes, escalamiento y resolución de conflictos."
---

# Skill: generar_protocolo_comunicacion

## Propósito
Define las reglas formales de comunicación entre agentes, incluyendo formatos de mensajes, flujos de escalamiento y mecanismos de resolución de conflictos.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `agentes_negocio` | object[] | Sí | Output de `disenar_agentes_negocio` |
| `agentes_tecnicos` | object[] | Sí | Output de `estructurar_agentes_tecnicos` |

## Outputs

```yaml
protocolo_comunicacion:
  formato_mensaje:
    campos_obligatorios: string[]
    campos_opcionales: string[]
    ejemplo: string
  tipos_interaccion:
    - tipo: string
      de: string
      para: string
      formato: string
      ejemplo: string
  flujo_escalamiento:
    - nivel: number
      condicion: string
      accion: string
      responsable: string
  resolucion_conflictos:
    - conflicto_tipo: string
      criterio_resolucion: string
      arbitro: string
  trazabilidad:
    formato_log: string
    que_se_registra: string[]
```

## Reglas Internas
1. Todo mensaje entre agentes es trazable.
2. Los conflictos negocio vs. técnico se resuelven con datos, no con jerarquía.
3. SLA de respuesta para evitar bloqueos.
4. Mecanismo de veto: un agente de negocio puede vetar una decisión técnica si viola reglas del dominio.
