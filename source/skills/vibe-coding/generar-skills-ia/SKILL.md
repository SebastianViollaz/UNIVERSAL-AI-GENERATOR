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

Las siguientes son skills base que aplican a la mayoría de proyectos. Además de estas, **genera skills específicas del dominio** (ver sección siguiente).

### ITERACIÓN OBLIGATORIA — Una carpeta por skill
```
PARA CADA skill diseñada:
  1. Crear carpeta: .github/skills/{nombre-skill}/
  2. Crear archivo: .github/skills/{nombre-skill}/SKILL.md
  3. Contenido sigue el Template Mínimo Obligatorio
FIN PARA
```

**PROHIBIDO:** Combinar múltiples skills en un solo archivo. Cada skill = 1 carpeta con 1 SKILL.md.
**MÍNIMO:** 5 skills. Si tienes menos, el análisis de dominio fue insuficiente.

### Skills específicas del dominio — OBLIGATORIAS
Además de las skills estándar, diseña skills que sean únicas para el dominio del usuario. Ejemplos:
- Videojuego: `configurar-mecanica-juego`, `balancear-dificultad`, `optimizar-rendimiento-escena`, `crear-enemigo-tipo`, `disenar-sistema-progresion`, `crear-ui-juego`
- E-commerce: `crear-flujo-checkout`, `configurar-pasarela-pago`, `crear-regla-descuento`, `generar-reporte-ventas`
- Salud: `validar-compliance-hipaa`, `crear-formulario-clinico`, `generar-prescripcion`

### Meta-skills de mantenimiento — OBLIGATORIAS (siempre se generan)
Estas skills permiten al usuario crear y modificar agentes, skills y reglas después de la generación inicial. **NUNCA deben omitirse ni borrarse.**

#### M1. crear-agente
```markdown
---
name: crear-agente
description: "Crea un nuevo agente .agent.md siguiendo las convenciones del proyecto. Usa cuando necesites un experto nuevo que no existe."
---

# Skill: Crear Agente Nuevo

## Contexto
Este proyecto usa agentes IA especializados en `.github/agents/`. Cada agente es un archivo `.agent.md` con frontmatter y prompt.

## Proceso
1. Recibe: nombre del agente, área de expertise, tipo (negocio/técnico)
2. Lee `.github/agents/` para ver los agentes existentes y mantener consistencia
3. Genera el archivo `.github/agents/{nombre}.agent.md` con:
   - Frontmatter: description + tools (solo lectura para negocio, lectura+escritura para técnico)
   - Identidad y contexto del proyecto inyectado
   - Responsabilidades y restricciones
   - Sección "Cuándo consultar a otros agentes"
4. Tools para negocio: read_file, grep_search, semantic_search, list_dir, fetch_webpage
5. Tools para técnico: read_file, create_file, replace_string_in_file, run_in_terminal, grep_search, semantic_search, list_dir, get_errors, fetch_webpage
6. Verifica: < 150 líneas, frontmatter válido, no duplica agente existente

## Ejemplo
Input: "Necesito un agente especialista en shaders para Unity"
Output: `.github/agents/especialista-shaders.agent.md` con contexto del proyecto, conocimiento de URP/HDRP, y restricciones de rendimiento.
```

#### M2. crear-skill
```markdown
---
name: crear-skill
description: "Crea una nueva skill SKILL.md siguiendo las convenciones del proyecto. Usa cuando necesites automatizar una tarea recurrente."
---

# Skill: Crear Skill Nueva

## Contexto
Este proyecto usa skills en `.github/skills/{nombre}/SKILL.md`. Cada skill es un flujo invocable por agentes.

## Proceso
1. Recibe: nombre de la skill, propósito, agentes que la usarán
2. Lee `.github/skills/` para ver las skills existentes y mantener consistencia
3. Crea carpeta `.github/skills/{nombre}/`
4. Genera `SKILL.md` con el template:
   - Frontmatter: name + description
   - Sección "Contexto de Negocio" con reglas relevantes
   - Sección "Proceso" con pasos numerados
   - Sección "Ejemplo" con input/output real del dominio
5. Verifica: < 100 líneas, frontmatter válido, no duplica skill existente

## Ejemplo
Input: "Skill para optimizar texturas en Unity"
Output: `.github/skills/optimizar-texturas/SKILL.md` con proceso de análisis de resolución, compresión y atlas.
```

#### M3. modificar-agente
```markdown
---
name: modificar-agente
description: "Modifica un agente existente: agrega responsabilidades, ajusta restricciones o actualiza contexto. Usa cuando un agente necesita evolucionar."
---

# Skill: Modificar Agente Existente

## Proceso
1. Recibe: nombre del agente a modificar + cambios deseados
2. Lee `.github/agents/{nombre}.agent.md` actual
3. Aplica los cambios manteniendo la estructura: frontmatter, identidad, contexto, herramientas, restricciones
4. Verifica: < 150 líneas, frontmatter sigue válido, tools correctos para el tipo
5. NO elimina secciones existentes a menos que se pida explícitamente
```

#### M4. modificar-skill
```markdown
---
name: modificar-skill
description: "Modifica una skill existente: actualiza el proceso, agrega pasos o ajusta ejemplos. Usa cuando una skill necesita evolucionar."
---

# Skill: Modificar Skill Existente

## Proceso
1. Recibe: nombre de la skill a modificar + cambios deseados
2. Lee `.github/skills/{nombre}/SKILL.md` actual
3. Aplica los cambios manteniendo la estructura: frontmatter, contexto, proceso, ejemplo
4. Verifica: < 100 líneas, frontmatter sigue válido
5. NO elimina secciones existentes a menos que se pida explícitamente
```

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

### 7. investigar-en-internet
```markdown
---
name: investigar-en-internet
description: "Investiga en internet información relevante sobre el dominio del proyecto usando fuentes confiables. Toda información externa debe incluir URL de la fuente."
---

# Skill: Investigar en Internet

## Contexto de Negocio
Cuando un agente necesita información que no está en la documentación del proyecto (regulaciones actualizadas, documentación de APIs externas, estándares del sector, benchmarks de mercado), debe investigar en internet con fuentes verificables.

## Fuentes Confiables (orden de prioridad)
1. **Oficiales:** Sitios .gov/.gob, documentación oficial de frameworks, RFCs
2. **Académicas:** Google Scholar, IEEE, ACM, arXiv
3. **Industria:** Gartner, Forrester, ThoughtWorks, McKinsey (resúmenes públicos)
4. **Estándares:** ISO, OWASP, W3C, NIST, PCI DSS
5. **Periodismo tech:** Publicaciones reconocidas del sector

## Proceso
1. Recibe: tema a investigar + contexto del proyecto
2. Usa `fetch_webpage` para consultar fuentes confiables
3. Verifica: mínimo 2 fuentes independientes para datos críticos
4. Descarta fuentes sin autoría clara o con más de 3 años (tecnología) / 2 años (regulaciones)
5. Retorna: hallazgos con URL verificada, tipo de fuente y nivel de confiabilidad

## Ejemplo
Input: "¿Qué estándares de accesibilidad aplican para una app de salud en la UE?"
Output:
- EN 301 549 (estándar europeo de accesibilidad ICT) — fuente: etsi.org — confiabilidad: alta
- WCAG 2.1 AA (requisito base para EN 301 549) — fuente: w3.org/WAI — confiabilidad: alta
- European Accessibility Act (EAA, aplica desde junio 2025) — fuente: ec.europa.eu — confiabilidad: alta
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
1. **Una carpeta por skill** — NUNCA combinar skills en un solo archivo. Cada carpeta en `.github/skills/` contiene exactamente un `SKILL.md`.
2. Cada skill tiene un ejemplo concreto del dominio del proyecto, no genérico.
3. Las skills referencian archivos reales del proyecto (no rutas hipotéticas).
4. El output de cada skill es accionable: código, checklist o diagnóstico.
5. Las skills de negocio NO generan código; las técnicas SÍ.
6. Toda skill de testing vincula a la regla de negocio que verifica.
7. Todas las skills generadas siguen el template mínimo: frontmatter + Contexto de Negocio + Proceso + Ejemplo.
8. La sección "Contexto de Negocio" inyecta los IDs de reglas relevantes directamente en la skill.
9. **Generar skills del dominio** además de las estándar. Si el proyecto es de videojuegos, las skills deben reflejar tareas de desarrollo de videojuegos. Si es de salud, tareas de compliance médico. Etc.
10. **NO modificar ni eliminar archivos preexistentes** del workspace. Solo crear archivos nuevos.
