---
name: generar-arbol-documentacion
description: "Crea el esqueleto completo de archivos .md y .yaml del proyecto con contenido real, adaptado al formato de la IA objetivo."
---

# Skill: generar_arbol_documentacion

## Propósito
Crea el esqueleto completo de archivos que formarán el contexto del entorno de desarrollo. Cada archivo se genera con contenido real (no placeholders vacíos) basado en los outputs de las skills anteriores.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `analisis_dominio` | object | Sí | Output de `analizar_dominio_negocio` |
| `agentes_negocio` | object[] | Sí | Output de `disenar_agentes_negocio` |
| `agentes_tecnicos` | object[] | Sí | Output de `estructurar_agentes_tecnicos` |
| `procesos_detallados` | object[] | Sí | Output de `mapear_procesos_negocio` |
| `arquitectura` | object | Sí | Output de `disenar_arquitectura_sistema` |
| `reglas_negocio` | object[] | Sí | Output de `formalizar_reglas_negocio` |
| `modelo_seguridad` | object | Sí | Output de `disenar_seguridad_sistema` |
| `infraestructura` | object | Sí | Output de `planificar_infraestructura` |
| `nombre_proyecto` | string | Sí | Identificador del proyecto |
| `ia_objetivo` | string | No | "copilot", "claude", "cursor", "windsurf", "aider", "generic" |

## Outputs

```yaml
arbol_documentacion:
  archivos_generados:
    - ruta: string
      tipo: enum[md, yaml, json]
      proposito: string
      contenido: string
      generado_por: string
      dependencias: string[]
  estructura_directorios:
    - ruta: string
      proposito: string
  instrucciones_workspace:
    contenido: string
    referencias_documentacion: string[]
    reglas_codificacion: string[]
  readme:
    contenido: string
  indice_navegacion:
    - seccion: string
      archivos: string[]
      para_que_sirve: string
      leer_cuando: string
```

## Reglas Internas
1. Ningún archivo generado debe estar vacío o tener solo títulos.
2. Cada archivo es autocontenido: comprensible sin leer otros archivos.
3. El índice de navegación es obligatorio para que las IAs sepan dónde buscar.
4. Formato Markdown consistente con headers, listas y tablas.
5. Máximo 500 líneas por archivo.
