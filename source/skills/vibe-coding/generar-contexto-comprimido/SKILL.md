---
name: generar-contexto-comprimido
description: "Para IAs con context window limitado (Aider, terminal), comprime el contexto del proyecto manteniendo la semántica clave en el número objetivo de tokens."
---

# Skill: generar_contexto_comprimido

## Propósito
Distinto de `optimizar-prompts-ia` que trabaja a nivel de archivos individuales, esta skill produce una versión ultra-comprimida del contexto completo del proyecto para IAs con memoria de trabajo limitada.

## Diferencia con `optimizar-prompts-ia`
- `optimizar_prompts_ia` afina cada archivo del entorno para su IA objetivo.
- `generar_contexto_comprimido` produce UN solo documento de contexto mínimo para el uso directo en terminales o IAs de línea de comandos.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `instrucciones_workspace` | object | Sí | Output de `generar_instrucciones_workspace` |
| `reglas_negocio` | object[] | Sí | Para priorizar las más críticas |
| `arquitectura` | object | Sí | Para resumir ADRs |
| `stack` | object | Sí | Para incluir stack en el header |
| `target_tokens` | number | No | Límite de tokens objetivo (default: 2000) |

## Outputs

```yaml
contexto_comprimido:
  contenido: string                    # El documento completo, listo para pegar
  tokens_estimados: number
  informacion_incluida: string[]       # Qué se incluyó
  informacion_omitida: string[]        # Qué se dejó fuera y por qué
  donde_encontrar_mas: string[]        # Referencias a docs completos
```

## Estructura del Documento Generado

```markdown
# {NOMBRE_PROYECTO} — Contexto Comprimido

**Stack:** {backend} + {frontend} + {db}
**Dominio:** {rubro} | **Modelo:** {B2B/B2C/etc}

## Reglas Críticas (Top 5)
| ID | Regla | Severidad |
|----|-------|-----------|
{top_5_reglas}

## Arquitectura (Resumen)
- Estilo: {nombre}
- Módulos: {lista_compacta}
- Decisiones clave: {adrs_en_una_linea_cada_uno}

## Convenciones
{convenciones_en_bullets_compactos}

## Glosario (solo términos no-obvios)
{terminos_ambiguos}

---
Contexto completo: ver copilot-instructions.md / CLAUDE.md
```

## Técnica de Compresión
1. Eliminar todos los ejemplos excepto el más representativo por regla
2. Reemplazar listas de reglas por tabla compacta con IDs
3. Comprimir glosario a ≤ 10 términos no-obvios del dominio
4. Resumir cada ADR en una sola línea: "Decisión: X. Por qué: Y."
5. Omitir reiteraciones: si algo ya está en el stack, no repetirlo en convenciones

## Reglas Internas
1. El documento resultante debe tener ≤ `target_tokens` tokens.
2. Prioridad de inclusión: seguridad > reglas legales > reglas de negocio críticas > stack > convenciones.
3. El `donde_encontrar_mas` siempre apunta a los documentos completos.
4. Nunca omitir restricciones de seguridad — aunque se exceda el límite.
5. Las reglas de negocio se comprimen por criticidad: `legal/critico` > `alto` > `medio` > `bajo`.
