---
name: generar-agentes-ia
description: "Genera los archivos .agent.md / .mdc funcionales para cada agente de negocio y técnico, listos para ser consumidos por la herramienta de Vibe Coding."
---

# Skill: generar_agentes_ia

## Propósito
Transforma las definiciones conceptuales de agentes (negocio y técnicos) en archivos de configuración funcionales que la IA de codificación puede consumir directamente.

## Diferencia con `generar_prompts_agentes`
- `generar_prompts_agentes` produce el **texto del prompt** en formato genérico.
- `generar_agentes_ia` produce el **archivo completo** con frontmatter, tools, contexto inyectado y formato nativo de la IA objetivo.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `agentes_negocio` | object[] | Sí | Output de `disenar_agentes_negocio` |
| `agentes_tecnicos` | object[] | Sí | Output de `estructurar_agentes_tecnicos` |
| `reglas_negocio` | object[] | Sí | Output de `formalizar_reglas_negocio` |
| `arquitectura` | object | Sí | Output de `disenar_arquitectura_sistema` |
| `analisis_dominio` | object | Sí | Contexto del negocio |
| `ia_objetivo` | string | Sí | "copilot", "claude", "cursor", "windsurf", "continue" |

## Outputs

```yaml
agentes_ia:
  archivos:
    - ruta: string
      nombre_agente: string
      tipo: enum[negocio, tecnico, orquestador, vibe-coding]
      contenido_completo: string    # Archivo listo para escribir
      herramientas: string[]
      formato: string               # agent.md, .mdc, etc.
      lineas_totales: number        # Para verificar token budget
      token_budget_warning: boolean # true si supera 150 líneas
  orquestador:
    ruta: string
    contenido_completo: string
    tabla_decision: string          # Tabla Markdown: | Activador | Agente | Cuándo NO usar |
  validacion_token_budget:
    total_archivos: number
    archivos_sobre_limite: string[] # Rutas de archivos que superan el budget
    accion_recomendada: string
```

## Proceso de Generación

### Para cada agente, generar:

#### 1. Frontmatter (varía por IA)
```yaml
# Copilot
---
description: "{descripcion_con_contexto_negocio}"
tools: ["read_file", "create_file", ...]
---

# Cursor
---
description: "{descripcion_con_contexto_negocio}"
alwaysApply: false
globs: ""
---

# Windsurf
---
trigger: "model_decision"
description: "{descripcion_con_contexto_negocio}"
---
```

#### 2. Identidad y Contexto (común)
```markdown
# {Nombre del Agente} — {Nombre del Proyecto}

Eres {rol} del proyecto {nombre}. {descripcion_del_proyecto_en_1_parrafo}.

## Contexto de Negocio
{reglas_de_negocio_relevantes_inyectadas}

## Tu Rol Específico
{responsabilidades_del_agente}
```

#### 3. Herramientas y Restricciones (varía por tipo)
```markdown
## Herramientas que Usas
- read_file: Para consultar documentación en docs/
- grep_search: Para buscar referencias en el código
- {herramientas_especificas_del_tipo}

## Restricciones
- {restricciones_de_negocio}
- {restricciones_tecnicas}
- {restricciones_del_rol}
```

#### 4. Patrones de Interacción
```markdown
## Cómo Respondes
Cuando te pidan {tipo_de_tarea}:
1. Paso 1
2. Paso 2
3. ...

## Ejemplo
USER: {ejemplo_de_pregunta_tipica}
TU: {ejemplo_de_respuesta}
```

## Herramientas por Tipo de Agente

### Agentes de Negocio
```yaml
tools:
  - read_file          # Leer documentación
  - grep_search        # Buscar reglas de negocio
  - semantic_search    # Buscar contexto relevante
  - list_dir           # Navegar documentación
```

### Agentes Técnicos
```yaml
tools:
  - read_file
  - create_file
  - replace_string_in_file
  - run_in_terminal
  - grep_search
  - semantic_search
  - list_dir
  - get_errors
```

### Agente Orquestador
```yaml
tools:
  - read_file
  - grep_search
  - semantic_search
  - list_dir
  # NO tiene tools de escritura — solo redirige
```

## Reglas Internas
1. Cada agente IA es autocontenido: funciona sin leer otros agentes.
2. El contexto de negocio se inyecta DENTRO del prompt, no como referencia externa.
3. Los agentes técnicos incluyen las reglas de negocio que les afectan como restricciones hard.
4. El archivo generado es sintácticamente válido para la IA objetivo (frontmatter correcto).
5. Los ejemplos de interacción usan terminología del dominio real del proyecto.
6. Cada agente incluye al inicio de sus respuestas largas: regla/módulo en curso (heartbeat de contexto).
7. Verificar token budget durante generación: agentes > 150 líneas se marcan con `token_budget_warning: true` y se comprimen.
8. La `tabla_decision` del orquestador tiene 3 columnas: Activador | Agente a Llamar | Cuándo NO Usar.
