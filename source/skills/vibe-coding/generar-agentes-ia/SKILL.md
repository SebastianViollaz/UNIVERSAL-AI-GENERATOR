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

### ITERACIÓN OBLIGATORIA — Un archivo por agente
```
PARA CADA agente en (agentes_negocio + agentes_tecnicos):
  1. Generar frontmatter según ia_objetivo
  2. Generar body con identidad, contexto, herramientas, restricciones
  3. ESCRIBIR archivo individual: .github/agents/{identificador}.agent.md
  4. Verificar que el archivo no supere 150 líneas
FIN PARA

Generar archivo orquestador: .github/agents/orquestador.agent.md
Generar archivo configurador: .github/agents/configurador-entorno.agent.md
```

**PROHIBIDO:** Combinar múltiples agentes en un solo archivo. Cada agente = 1 archivo.
**MÍNIMO:** Si tienes menos de 5 agentes diseñados, el análisis de dominio fue insuficiente — vuelve a `disenar-agentes-negocio`.

### Agente Configurador de Entorno — OBLIGATORIO (siempre se genera)
Este agente permite al usuario crear, modificar y mantener agentes, skills e instrucciones **después** de la generación inicial. Sin él, el usuario pierde la capacidad de evolucionar su entorno.

```markdown
# Configurador de Entorno — {Nombre del Proyecto}

Eres el agente encargado de mantener y evolucionar la configuración de agentes IA, skills e instrucciones de este proyecto.

## Cuándo me invocan
- "Necesito un agente nuevo para X"
- "Quiero agregar una skill para Y"
- "Modifica el agente Z para que también haga W"
- "Actualiza las instrucciones del workspace"

## Lo que hago
1. **Crear agentes** — Uso la skill `crear-agente` para generar `.agent.md` consistentes
2. **Crear skills** — Uso la skill `crear-skill` para generar `SKILL.md` consistentes
3. **Modificar agentes** — Uso la skill `modificar-agente` para evolucionar agentes existentes
4. **Modificar skills** — Uso la skill `modificar-skill` para evolucionar skills existentes
5. **Revisar consistencia** — Verifico que no haya agentes duplicados ni skills huérfanas

## Restricciones
- NUNCA elimino agentes, skills ni instrucciones existentes sin confirmación explícita
- NUNCA modifico archivos fuera de `.github/`
- Mantengo el formato: frontmatter YAML + Markdown
- Respeto el token budget: agentes < 150 líneas, skills < 100 líneas
```

**Tools del configurador:** read_file, create_file, replace_string_in_file, grep_search, semantic_search, list_dir

### Agentes especializados por dominio — NO catálogos genéricos
Los agentes se diseñan a partir del dominio del usuario, no de una lista fija. Ejemplos:
- Videojuego → especialista en el motor (Unity/Godot), diseñador de gameplay, sistema de progresión, monetización, UX de juegos, optimización de rendimiento, audio, QA de juegos
- E-commerce → gestión de catálogo, checkout, logística, marketing, SEO, atención al cliente, analítica
- Salud → compliance regulatorio, historias clínicas, telemedicina, facturación médica, farmacia

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
- fetch_webpage: Para investigar en internet (regulaciones, docs oficiales, estándares)
- {herramientas_especificas_del_tipo}

## Investigación en Internet
Cuando necesites información externa (regulaciones, documentación de APIs, estándares del sector):
1. Usa `fetch_webpage` para consultar fuentes confiables
2. Prioriza: documentación oficial > fuentes académicas > reportes de industria
3. Incluye la URL de cada fuente en tu respuesta
4. No inventes URLs — solo cita las que hayas verificado

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

## Herramientas por Tipo de Agente — USAR EXACTAMENTE ESTAS

### Agentes de Negocio (solo lectura, NO escriben código)
```yaml
tools:
  - read_file          # Leer documentación
  - grep_search        # Buscar reglas de negocio
  - semantic_search    # Buscar contexto relevante
  - list_dir           # Navegar documentación
  - fetch_webpage      # Investigar regulaciones, mercado y tendencias con fuentes confiables
```
**PROHIBIDO en agentes de negocio:** create_file, replace_string_in_file, run_in_terminal. Si un agente de negocio tiene tools de escritura, está MAL configurado.

### Agentes Técnicos (lectura + escritura de código)
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
  - fetch_webpage      # Consultar documentación oficial, estándares y APIs externas
```
**NO agregar** tools de extensiones (pylance, mssql, etc.) ni tools internos de VS Code (vscode/*, browser/*). Solo los 9 tools listados arriba.

### Agente Orquestador
```yaml
tools:
  - read_file
  - grep_search
  - semantic_search
  - list_dir
  - fetch_webpage      # Investigar contexto de dominio cuando se requiera
  # NO tiene tools de escritura — solo redirige
```

## Reglas Internas
1. **Un archivo por agente** — NUNCA combinar agentes en un solo archivo. Cada archivo en `.github/agents/` es un agente independiente.
2. Cada agente IA es autocontenido: funciona sin leer otros agentes.
3. El contexto de negocio se inyecta DENTRO del prompt, no como referencia externa.
4. Los agentes técnicos incluyen las reglas de negocio que les afectan como restricciones hard.
5. El archivo generado es sintácticamente válido para la IA objetivo (frontmatter correcto).
6. Los ejemplos de interacción usan terminología del dominio real del proyecto.
7. **Tools prescritos** — Usar EXACTAMENTE los tools de la sección "Herramientas por Tipo de Agente". No agregar tools de extensiones ni tools internos de VS Code.
8. Verificar token budget durante generación: agentes > 150 líneas se marcan con `token_budget_warning: true` y se comprimen.
9. La `tabla_decision` del orquestador tiene 3 columnas: Activador | Agente a Llamar | Cuándo NO Usar.
10. **NO modificar ni eliminar archivos preexistentes** del workspace. Solo crear archivos nuevos dentro de `.github/`.
