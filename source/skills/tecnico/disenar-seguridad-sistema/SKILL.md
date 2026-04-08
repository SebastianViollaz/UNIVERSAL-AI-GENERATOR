---
name: disenar-seguridad-sistema
description: "Analiza requerimientos de seguridad desde negocio (datos sensibles, regulaciones) y técnica (auth, OWASP, cifrado, threat modeling)."
---

# Skill: disenar_seguridad_sistema

## Propósito
Analiza requerimientos de seguridad desde perspectiva de negocio y técnica. Produce un modelo de seguridad completo.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `analisis_dominio` | object | Sí | Output de `analizar_dominio_negocio` |
| `arquitectura` | object | Sí | Output de `disenar_arquitectura_sistema` |
| `roles_usuario` | object[] | Sí | Roles y permisos del análisis de dominio |

## Outputs

```yaml
modelo_seguridad:
  clasificacion_datos:
    - tipo_dato: string
      nivel_sensibilidad: enum[publico, interno, confidencial, restringido]
      cifrado_requerido: boolean
      retencion: string
  autenticacion:
    metodo: string
    mfa_requerido: boolean
    politica_passwords: string
    proveedor: string
    politica_rotacion_secretos:          # API keys, tokens, certificados
      frecuencia: string
      proceso: string
      donde_se_almacenan: string         # Vault, env vars, secrets manager
  autorizacion:
    modelo: enum[RBAC, ABAC, mixto]
    roles:
      - rol: string
        permisos: string[]
        restricciones: string[]
  amenazas:
    - amenaza: string
      vector: string
      impacto: enum[critico, alto, medio, bajo]
      mitigacion: string
      owasp_categoria: string
  checklist_owasp:
    - categoria: string
      controles: string[]
  compliance:
    - regulacion: string
      requerimientos: string[]
      como_se_cumple: string[]
  plan_respuesta_incidentes:             # Condicional: obligatorio si hay datos financieros o de salud
    deteccion: string
    contencion: string
    notificacion_usuarios: string
    notificacion_regulatoria: string
    recuperacion: string
    post_mortem: string

## Reglas Internas
1. Si hay datos personales, protección de datos local es obligatoria.
2. Siempre modelar al menos 5 amenazas del OWASP Top 10.
3. El modelo de autorización refleja exactamente los roles de negocio.
4. `plan_respuesta_incidentes` es obligatorio si hay datos financieros o de salud.
5. `politica_rotacion_secretos` es obligatoria para proyectos con >1 integración externa.
