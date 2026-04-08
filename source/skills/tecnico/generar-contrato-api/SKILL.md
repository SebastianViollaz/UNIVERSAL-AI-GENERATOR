---
name: generar-contrato-api
description: "Genera el contrato OpenAPI 3.0 o GraphQL Schema de cada módulo basado en los bounded contexts, roles de usuario y modelo de seguridad."
---

# Skill: generar_contrato_api

## Propósito
Produce el contrato de API que define la interfaz entre frontend y backend (o entre servicios). Es el artefacto más solicitado por equipos al inicio del desarrollo y actualmente ninguna skill lo genera.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `arquitectura` | object | Sí | Output de `disenar_arquitectura_sistema` (modulos, estrategia_api) |
| `roles_usuario` | object[] | Sí | Para definir autorización por endpoint |
| `modelo_seguridad` | object | Sí | Para autenticación y headers de seguridad |
| `stack` | object | Sí | Para determinar el estilo del contrato (REST vs GraphQL) |
| `reglas_negocio` | object[] | No | Para validaciones en request bodies |

## Outputs

```yaml
contratos_api:
  estilo: enum[REST, GraphQL, gRPC]
  por_modulo:
    - modulo: string
      version: string
      base_path: string                # ej: /api/v1/billing
      endpoints:                       # Para REST
        - metodo: enum[GET, POST, PUT, PATCH, DELETE]
          path: string
          descripcion: string
          autenticacion_requerida: boolean
          roles_autorizados: string[]
          request_body:
            schema: string             # JSON Schema inline
          response_200:
            schema: string
          response_errors:
            - codigo: number
              condicion: string
          reglas_negocio_validadas: string[]  # IDs RN-XXX que este endpoint verifica
      openapi_spec: string             # YAML completo OpenAPI 3.0 para el módulo
  coleccion_postman: string            # JSON listo para importar en Postman
  headers_globales:
    - nombre: string
      descripcion: string
      obligatorio: boolean
```

## Reglas Internas
1. Cada endpoint define explícitamente los roles que pueden accederlo.
2. Los schemas de request body incluyen validaciones que reflejan reglas de negocio.
3. Los endpoints de escritura (POST/PUT/PATCH/DELETE) siempre documentan sus efectos secundarios.
4. Incluir ejemplos concretos en los schemas — la IA los usa para generar código más preciso.
5. La `coleccion_postman` es un artefacto de entrega: el desarrollador la usa el día 1.
6. Versionar desde el inicio: `/api/v1/` — facilita evolución sin breaking changes.
