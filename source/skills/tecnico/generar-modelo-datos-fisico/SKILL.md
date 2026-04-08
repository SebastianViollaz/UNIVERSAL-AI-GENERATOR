---
name: generar-modelo-datos-fisico
description: "Transforma el modelo conceptual de la arquitectura en esquema físico: SQL con tipos, índices, constraints y migraciones, o schema NoSQL equivalente."
---

# Skill: generar_modelo_datos_fisico

## Propósito
El modelo conceptual de `disenar-arquitectura-sistema` define entidades y relaciones en lenguaje de negocio. Esta skill lo convierte en el esquema físico real que el desarrollador puede ejecutar directamente.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `arquitectura` | object | Sí | Output de `disenar_arquitectura_sistema` (modelo_datos_conceptual) |
| `reglas_negocio` | object[] | Sí | Para traducir restricciones a constraints de BD |
| `stack` | object | Sí | Output de `stack_consolidado` (tipo de BD) |
| `modelo_seguridad` | object | Sí | Para campos de auditoría y cifrado |

## Outputs

```yaml
modelo_datos_fisico:
  tipo: enum[sql, nosql_documental, nosql_grafo, nosql_columnar]
  esquema:
    tablas:                            # Para SQL
      - nombre: string
        propósito: string
        columnas:
          - nombre: string
            tipo: string
            nullable: boolean
            default: string
            descripcion: string
        primary_key: string[]
        foreign_keys:
          - columna: string
            tabla_ref: string
            columna_ref: string
            on_delete: enum[CASCADE, SET_NULL, RESTRICT, NO_ACTION]
        indices:
          - nombre: string
            columnas: string[]
            tipo: enum[unique, btree, hash, fulltext]
            justificacion: string
        constraints:
          - nombre: string
            tipo: enum[check, unique, not_null]
            expresion: string
            regla_negocio_origen: string  # ID RN-XXX
        campos_auditoria:              # Siempre: created_at, updated_at, deleted_at, created_by
          - nombre: string
            tipo: string
  migraciones:
    - nombre: string                   # ej: 001_create_users_table.sql
      orden: number
      contenido: string                # SQL/script ejecutable
  seed_data:
    - tabla: string
      proposito: string                # "Datos de catálogo", "Usuario admin inicial", etc.
      contenido: string
  diagrama_er: string                  # Mermaid erDiagram
```

## Reglas Internas
1. Toda tabla tiene campos de auditoría: `created_at`, `updated_at`, `deleted_at` (soft delete), `created_by`.
2. Los constraints de BD reflejan las reglas de negocio obligatorias — no solo los triggers de aplicación.
3. Los índices se justifican con el volumen de transacciones del proceso que los usa.
4. El `diagrama_er` en Mermaid es obligatorio — directamente renderizable en docs.
5. Nunca usar `float` para montos monetarios — usar `decimal(19,4)` o equivalente en el stack elegido.
6. Las migraciones son reversibles (incluir comentario con el DOWN correspondiente).
