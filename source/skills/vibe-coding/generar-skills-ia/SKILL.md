---
name: generar-skills-ia
description: "Genera archivos SKILL.md funcionales del proyecto que los agentes IA pueden invocar para tareas recurrentes: revisar reglas de negocio, consultar ADRs, generar tests por regla, etc."
---

# Skill: generar_skills_ia

## Propósito
Genera skills invocables por los agentes IA dentro del proyecto. Estas skills NO son las del Creador de Entornos — son las que los agentes de negocio y técnicos usarán día a día durante el desarrollo.

## Diferencia con las skills del Creador
- Skills del Creador (source/skills/): se usan para DISEÑAR el entorno.
- Skills generadas por esta skill: se usan para DESARROLLAR el proyecto con Vibe Coding.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `reglas_negocio` | object[] | Sí | Reglas formalizadas |
| `procesos_negocio` | object[] | Sí | Procesos mapeados |
| `arquitectura` | object | Sí | Decisiones de arquitectura |
| `modelo_seguridad` | object | Sí | Modelo de amenazas |
| `stack` | object | Sí | Output de `stack_consolidado` de `estructurar_agentes_tecnicos` |
| `ia_objetivo` | string | Sí | IA para la que generar |

## Template Mínimo Obligatorio para Toda Skill Generada
```markdown
---
name: {nombre-skill}
description: "{descripción precisa}"
---

# Skill: {Nombre Legible}

## Contexto de Negocio
{Por qué existe esta skill desde la perspectiva del negocio}
Reglas relacionadas: {IDs RN-XXX aplicables}

## Proceso
1. Recibe: {input}
2. Hace: {acción concreta}
3. Retorna: {output accionable}

## Ejemplo
Input: "{ejemplo_real_del_dominio}"
Output: {resultado_esperado}
```

## Outputs

```yaml
skills_proyecto:
  archivos:
    - ruta: string                # ej: .github/skills/revisar-regla-negocio/SKILL.md
      nombre: string
      descripcion: string
      contenido_completo: string
      invocable_por: string[]     # Qué agentes lo usan
```

## Skills Estándar a Generar

### 1. revisar-regla-negocio
```markdown
---
name: revisar-regla-negocio
description: "Busca y muestra la regla de negocio que aplica a un módulo o funcionalidad específica."
---

# Skill: Revisar Regla de Negocio

Cuando un agente necesita verificar una regla antes de implementar:

## Proceso
1. Recibe: nombre del módulo o funcionalidad
2. Busca en docs/negocio/reglas-negocio/ las reglas con tag del módulo
3. Retorna: lista de reglas aplicables con su ID, descripción y restricciones

## Ejemplo
Input: "facturación"
Output: RN-FACT-001 (IVA diferenciado), RN-FACT-002 (cancelación), RN-FACT-003 (timbrado)
```

### 2. consultar-adr
```markdown
---
name: consultar-adr
description: "Busca decisiones de arquitectura (ADRs) relevantes para el módulo o patrón en cuestión."
---

# Skill: Consultar ADR

## Proceso
1. Recibe: módulo, patrón o tecnología en cuestión
2. Busca en docs/tecnico/arquitectura/adr/ los ADRs relacionados
3. Retorna: ADR con decisión, contexto, alternativas consideradas y consecuencias
```

### 3. generar-test-regla-negocio
```markdown
---
name: generar-test-regla-negocio
description: "Genera un test que verifica una regla de negocio específica, usando el framework de testing del proyecto."
---

# Skill: Generar Test de Regla de Negocio

## Proceso
1. Recibe: ID de regla de negocio (ej: RN-FACT-001)
2. Lee la regla y sus condiciones / excepciones
3. Genera: test con happy path + edge cases + la referencia a la regla en comentario

## Template de Output
```{lenguaje}
describe('{Módulo}', () => {{
  // Verifica: {ID_REGLA} — {descripcion_regla}
  it('should {comportamiento} when {condicion}', () => {{
    // Arrange: {setup}
    // Act: {accion}
    // Assert: {verificacion}
  }});
}});
```
```

### 4. validar-proceso-negocio
```markdown
---
name: validar-proceso-negocio
description: "Verifica que una implementación cubre todos los pasos del proceso de negocio documentado."
---

# Skill: Validar Proceso de Negocio

## Proceso
1. Recibe: nombre del proceso
2. Lee docs/negocio/procesos/{proceso}.md
3. Extrae: pasos, excepciones, validaciones y puntos de decisión
4. Compara contra la implementación actual
5. Retorna: pasos cubiertos, pasos faltantes, excepciones no manejadas
```

### 5. auditar-seguridad-modulo
```markdown
---
name: auditar-seguridad-modulo
description: "Revisa un módulo contra el modelo de amenazas y las reglas de seguridad del proyecto."
---

# Skill: Auditar Seguridad de Módulo

## Proceso
1. Recibe: ruta del módulo
2. Lee el modelo de amenazas en docs/tecnico/seguridad/
3. Verifica: autenticación, autorización, validación de input, manejo de datos sensibles
4. Retorna: hallazgos con severidad y remediación sugerida
```

### 6. crear-modulo-nuevo
```markdown
---
name: crear-modulo-nuevo
description: "Scaffolding de un nuevo módulo siguiendo la arquitectura y convenciones del proyecto."
---

# Skill: Crear Módulo Nuevo

## Proceso
1. Recibe: nombre del módulo y bounded context
2. Lee las convenciones de arquitectura
3. Genera la estructura de carpetas: domain/, application/, infrastructure/, presentation/
4. Crea archivos base: entidad, repository interface, use case, controller, tests
5. Actualiza el índice de módulos
```

## Skills Condicionales (según el proyecto)

| Condición | Skill Adicional |
|-----------|----------------|
| Tiene facturación | `calcular-impuestos` — Verifica cálculos fiscales |
| Tiene workflows | `validar-estado-transicion` — Verifica máquina de estados |
| Tiene reportes | `generar-query-reporte` — SQL optimizado para BI |
| Multi-tenant | `verificar-aislamiento-tenant` — Asegura data isolation |
| Tiene integraciones | `simular-api-externa` — Mock de APIs de terceros |

## Reglas Internas
1. Cada skill tiene un ejemplo concreto del dominio del proyecto, no genérico.
2. Las skills referencian archivos reales del proyecto (no rutas hipotéticas).
3. El output de cada skill es accionable: código, checklist o diagnóstico.
4. Las skills de negocio NO generan código; las técnicas SÍ.
5. Toda skill de testing vincula a la regla de negocio que verifica.
6. Todas las skills generadas siguen el template mínimo: frontmatter + Contexto de Negocio + Proceso + Ejemplo.
7. La sección "Contexto de Negocio" inyecta los IDs de reglas relevantes directamente en la skill.
