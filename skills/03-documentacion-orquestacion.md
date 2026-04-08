# SKILLS — Documentación y Orquestación

Skills orientadas a generar la estructura de archivos, documentación y configuración del entorno final.

---

## Skill: `generar_arbol_documentacion`

### Descripción
Crea el esqueleto completo de archivos `.md` y `.yaml` que formarán el contexto del entorno de desarrollo. Cada archivo se genera con contenido real (no placeholders vacíos) basado en los outputs de las skills anteriores.

### Inputs
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
| `estrategia_testing` | object | Sí | Output de `definir_estrategia_testing` |
| `plan_escalabilidad` | object | Sí | Output de `analizar_escalabilidad_negocio` |
| `nombre_proyecto` | string | Sí | Identificador del proyecto |

### Outputs
```yaml
arbol_documentacion:
  archivos_generados:
    - ruta: string                       # Ruta relativa en el proyecto
      tipo: enum[md, yaml, json]
      proposito: string
      contenido: string                  # Contenido completo del archivo
      generado_por: string               # Qué skill/agente lo produjo
      dependencias: string[]             # Qué otros archivos referencia
  estructura_directorios:
    - ruta: string
      proposito: string
  copilot_instructions:                  # Contenido del copilot-instructions.md
    instrucciones_globales: string
    referencias_documentacion: string[]
    reglas_codificacion: string[]
    convenciones_naming: string
    protocolo_agentes: string
  readme:
    contenido: string                    # README.md completo del proyecto
  indice_navegacion:                     # Mapa para que una IA navegue la documentación
    - seccion: string
      archivos: string[]
      para_que_sirve: string
      leer_cuando: string                # En qué situación consultar esta sección
```

### Reglas Internas
1. Ningún archivo generado debe estar vacío o tener solo títulos.
2. Cada archivo debe ser autocontenido: comprensible sin leer otros archivos.
3. El `copilot-instructions.md` debe ser el punto de entrada que guíe a cualquier IA.
4. El índice de navegación es obligatorio para que las IAs sepan dónde buscar qué.
5. Usar formato Markdown consistente con headers, listas y tablas.

---

## Skill: `generar_prompts_agentes`

### Descripción
Genera los prompts completos y listos para usar de cada agente (negocio y técnico). Estos prompts son los que se inyectarán en el entorno para que las IAs asuman sus roles.

### Inputs
| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `agentes_negocio` | object[] | Sí | Output de `disenar_agentes_negocio` |
| `agentes_tecnicos` | object[] | Sí | Output de `estructurar_agentes_tecnicos` |
| `protocolo_comunicacion` | object | Sí | Reglas de comunicación inter-agentes |
| `analisis_dominio` | object | Sí | Para contexto del dominio |

### Outputs
```yaml
prompts_agentes:
  negocio:
    - agente_id: string
      nombre_archivo: string             # Ej: "agente-supply-chain.prompt.md"
      ruta: string
      prompt_completo: string            # Incluyendo identidad, contexto, restricciones
      variables_contexto: string[]       # Qué variables necesita del entorno
      ejemplo_interaccion: string        # Ejemplo de cómo se usa este agente
  tecnicos:
    - agente_id: string
      nombre_archivo: string
      ruta: string
      prompt_completo: string
      variables_contexto: string[]
      ejemplo_interaccion: string
  orquestador:                           # Prompt del agente que coordina a todos
    prompt_completo: string
    ruta: string
    flujo_decisiones: string             # Cómo decide a quién consultar
```

### Reglas Internas
1. Cada prompt debe incluir: identidad, contexto del dominio, responsabilidades, restricciones y formato de respuesta.
2. Los prompts de negocio deben poder funcionar sin conocimiento técnico.
3. Los prompts técnicos deben referenciar las decisiones de negocio como restricciones.
4. Generar un prompt orquestador que sepa cuándo activar cada agente.

---

## Skill: `generar_protocolo_comunicacion`

### Descripción
Define las reglas formales de comunicación entre agentes, incluyendo formatos de mensajes, flujos de escalamiento y mecanismos de resolución de conflictos.

### Inputs
| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `agentes_negocio` | object[] | Sí | Output de `disenar_agentes_negocio` |
| `agentes_tecnicos` | object[] | Sí | Output de `estructurar_agentes_tecnicos` |

### Outputs
```yaml
protocolo_comunicacion:
  formato_mensaje:
    campos_obligatorios: string[]
    campos_opcionales: string[]
    ejemplo: string
  tipos_interaccion:
    - tipo: string                       # Ej: "consulta-negocio-a-tecnico"
      de: string
      para: string
      formato: string
      ejemplo: string
      sla_respuesta: string
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
    donde_se_almacena: string
```

### Reglas Internas
1. Todo mensaje entre agentes debe ser trazable y almacenado.
2. Los conflictos negocio vs. técnico siempre se resuelven con datos, no con jerarquía.
3. El SLA de respuesta debe existir para evitar bloqueos.
4. Incluir mecanismo de veto: un agente de negocio puede vetar una decisión técnica si viola reglas del dominio.

---

## Skill: `validar_entorno_generado`

### Descripción
Ejecuta una validación completa del entorno generado para asegurar consistencia, completitud y usabilidad antes de entregarlo al programador.

### Inputs
| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `arbol_documentacion` | object | Sí | Output de `generar_arbol_documentacion` |
| `prompts_agentes` | object | Sí | Output de `generar_prompts_agentes` |
| `reglas_negocio` | object[] | Sí | Output de `formalizar_reglas_negocio` |
| `arquitectura` | object | Sí | Output de `disenar_arquitectura_sistema` |

### Outputs
```yaml
validacion:
  puntuacion_global: number              # 0-100
  checklist:
    - item: string
      estado: enum[ok, warning, error]
      detalle: string
  cobertura:
    procesos_negocio_cubiertos: string   # Porcentaje
    reglas_negocio_trazadas: string      # Porcentaje con al menos un módulo técnico
    agentes_con_contraparte: string      # Porcentaje negocio <-> técnico
    adrs_documentados: string            # Porcentaje de decisiones técnicas
    archivos_con_contenido: string       # Porcentaje de archivos no vacíos
  errores: string[]                      # Problemas que deben resolverse
  advertencias: string[]                 # Problemas menores
  sugerencias: string[]                  # Mejoras opcionales
  resumen_ejecutivo: string              # Para que el programador entienda el estado
```

### Reglas Internas
1. Un entorno con errores NO se entrega. Se corrige primero.
2. La puntuación mínima aceptable es 80/100.
3. Todo proceso de negocio debe estar trazado a al menos un módulo técnico.
4. Todo agente de negocio debe tener contraparte técnica.
5. Generar resumen ejecutivo en lenguaje no técnico.

---

## Skill: `exportar_entorno`

### Descripción
Empaqueta todo el entorno generado en el formato final que el programador puede inyectar directamente en su workspace.

### Inputs
| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `validacion` | object | Sí | Output de `validar_entorno_generado` (debe estar OK) |
| `arbol_documentacion` | object | Sí | Output de `generar_arbol_documentacion` |
| `prompts_agentes` | object | Sí | Output de `generar_prompts_agentes` |
| `formato_salida` | string | No | "vscode" (default), "cursor", "generic" |

### Outputs
```yaml
entorno_exportado:
  formato: string
  archivos:
    - ruta: string
      contenido: string
      encoding: string
  instrucciones_instalacion: string[]    # Pasos para que el programador active el entorno
  primer_paso_recomendado: string        # Qué hacer primero después de instalar
  notas_importantes: string[]
```

### Reglas Internas
1. Solo exportar si la validación pasó con 80+ puntos.
2. Incluir instrucciones de instalación paso a paso.
3. El primer paso recomendado debe ser el que dé más valor inmediato.
4. Adaptar la estructura de archivos al IDE objetivo.
