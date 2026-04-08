---
name: optimizar-prompts-ia
description: "Afina y optimiza los prompts de los agentes IA generados para maximizar la efectividad con la herramienta de Vibe Coding específica, aplicando técnicas de prompt engineering avanzado."
---

# Skill: optimizar_prompts_ia

## Propósito
Toma los agentes IA, instrucciones y rules generados y los optimiza para máxima efectividad con la IA de codificación específica. Cada herramienta tiene particularidades que afectan cómo procesa prompts — esta skill conoce esas diferencias y optimiza en consecuencia.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `agentes_ia` | object[] | Sí | Output de `generar_agentes_ia` |
| `instrucciones_workspace` | object | Sí | Output de `generar_instrucciones_workspace` |
| `rules_ia` | object[] | Sí | Output de `generar_rules_ia` |
| `skills_ia` | object[] | Sí | Output de `generar_skills_ia` |
| `ia_objetivo` | string | Sí | IA para la que optimizar |

## Outputs

```yaml
entorno_optimizado:
  archivos_optimizados:
    - ruta: string
      contenido_original: string
      contenido_optimizado: string
      optimizaciones_aplicadas: string[]
  metricas:
    cuantitativas:
      tokens_totales: number
      archivos_totales: number
      reglas_totales: number
      agentes_totales: number
    cualitativas:
      especificidad_prompts: enum[alta, media, baja]   # ¿Son concretos o abstractos?
      cobertura_casos_borde: enum[alta, media, baja]   # ¿Cubren excepciones del negocio?
      claridad_restricciones: enum[alta, media, baja]  # ¿Los "no hagas" son inequívocos?
  recomendaciones: string[]
```

## Optimizaciones por IA

### GitHub Copilot (VS Code)
- **Context window:** Los `.instructions.md` con `applyTo` se inyectan automáticamente. No duplicar contenido entre instructions y agent prompts.
- **Tools:** Copilot soporta tools declarados en frontmatter. Declarar SOLO los tools que el agente realmente necesita (menos tools = menos confusión).
- **Agentes:** Se invocan con `@nombre`. El nombre debe ser corto y memorable.
- **Optimización clave:** Las instrucciones globales deben ser concisas (<200 líneas). El detalle va en agents y skills.

### Claude Code
- **CLAUDE.md:** Se lee completo al inicio. Mantener <300 líneas. Usar `@import` para delegar a archivos en .claude/rules/.
- **Agents:** Claude procesa bien instrucciones largas pero pierde contexto con interrupciones. Cada agente debe ser autocontenido.
- **Optimización clave:** Incluir los "no hagas" explícitamente. Claude tiende a ser proactivo — las restricciones deben ser claras.

### Cursor
- **Rules .mdc:** Las reglas `alwaysApply: true` se inyectan en CADA prompt. Minimizar el tamaño de las always-on.
- **Model context:** Cursor usa el modelo que el usuario elige. Escribir prompts que funcionen tanto con Claude como con GPT.
- **Optimización clave:** Las reglas por `globs` son más eficientes que las always-on. Usar scoping agresivo.

### Windsurf
- **Cascade:** Windsurf usa Cascade como su agente. Las rules always_on alimentan a Cascade.
- **Model decision:** Los agentes como `trigger: model_decision` se activan automáticamente cuando Cascade cree que son relevantes. La descripción debe ser muy precisa.
- **Optimización clave:** Las descriptions de agentes deben incluir keywords del dominio para mejorar el matching automático.

### Aider
- **CONVENTIONS.md:** Todo se concatena en un solo archivo. Hay que ser agresivo con la brevedad.
- **Read files:** Aider puede leer archivos adicionales con `read:`. No todo debe estar en CONVENTIONS.
- **Optimización clave:** Priorizar las reglas más importantes al inicio del archivo. Aider da más peso al inicio.

### Continue.dev
- **Rules:** Similar a Cursor con `alwaysApply` y `globs`.
- **Config:** Soporta modelos múltiples. Las rules deben ser model-agnostic.
- **Optimización clave:** Mantener rules independientes entre sí (Continue puede cargar subsets).

## Técnicas de Optimización Transversales

### 1. Deduplicación de Contexto
Si una regla de negocio aparece en las instrucciones de workspace Y en un agente, dejar solo una referencia en el agente: "Consulta las instrucciones del workspace para reglas de negocio generales."

### 2. Compresión Semántica
Reducir verbosidad sin perder información:
- ANTES: "Cuando implementes funcionalidad relacionada con la facturación, asegúrate de que todo cálculo monetario utilice el tipo de dato Decimal en lugar de float para evitar errores de precisión."
- DESPUÉS: "Módulo facturación: montos → Decimal, NUNCA float. (RN-FACT-001)"

### 3. Ordenamiento por Prioridad
Las reglas más violadas o más críticas van primero. Las IAs dan más peso al inicio del contexto.

### 4. Ejemplos Concretos > Reglas Abstractas
- ANTES: "Sigue el principio de separación de responsabilidades."
- DESPUÉS: "domain/ no importa de infrastructure/. Si necesitas un repo, define la interface en domain/ e inyecta la implementación."

### 5. Tokens Budget
Monitorear el consumo total de tokens del entorno:
- Instrucciones workspace: máx 200-300 líneas
- Cada agente: máx 150 líneas
- Cada rule: máx 50 líneas
- Cada skill: máx 100 líneas

### 6. Context Compression para IAs con Ventana Limitada
Para Aider y Continue (context window reducido), aplicar:
1. Eliminar ejemplos verbosos — mantener solo el más representativo por regla
2. Reemplazar listas de reglas por tabla compacta con IDs
3. Comprimir glosario a solo términos no-obvios (≤ 10 términos)
4. Consolidar ADRs en resumen ejecutivo de una línea por decisión
5. Resultado objetivo: contexto ≤40 líneas que la IA puede mantener en memoria de trabajo

## Reglas Internas
1. La optimización NO cambia el contenido semántico, solo lo hace más efectivo.
2. Cada optimización se registra para trazabilidad.
3. El token budget se respeta: si se excede, comprimir las secciones menos críticas.
4. Los prompts optimizados se testean mentalmente con un ejemplo del dominio.
5. Si una regla es crítica pero larga, se parte en una rule always-on (resumen) + referencia a docs (detalle).
