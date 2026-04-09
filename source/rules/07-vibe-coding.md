---
name: reglas-vibe-coding
description: "Reglas que gobiernan la generación de archivos de configuración para herramientas de Vibe Coding. Aseguran que el output sea funcional, plug & play y maximice la efectividad de la IA de codificación."
scope: always
---

# Reglas de Vibe Coding

## R-019: Output Ejecutable, No Descriptivo
> **Cada archivo generado para la IA de codificación debe ser funcional, no documentación sobre qué debería existir.**

- INCORRECTO: "El agente backend debería tener acceso a herramientas de lectura de archivos."
- CORRECTO: Un archivo `.agent.md` con `tools: ["read_file", "create_file"]` en el frontmatter.
- Si el output no se puede copiar al workspace y que funcione inmediatamente, NO está listo.
- **Severidad:** Crítica. Un entorno que requiere configuración manual adicional falla el propósito.

## R-020: Contexto de Negocio Inyectado, No Referenciado
> **Los agentes IA generados incluyen el contexto de negocio DENTRO del prompt, no como referencia a documentación externa.**

- INCORRECTO: "Consulta docs/negocio/reglas.md para las reglas de facturación."
- CORRECTO: Inyectar las 5 reglas más críticas de facturación directamente en el prompt del agente backend, con referencia a docs/ solo para el detalle completo.
- Motivo: En Vibe Coding, el programador espera que la IA ya sepa. No quiere navegar documentación.
- **Excepción:** Si una regla tiene >20 líneas de detalle, incluir resumen + referencia.

## R-021: Cada Agente IA es Autónomo
> **Un agente IA generado puede funcionar sin que los otros agentes estén cargados.**

- El agente backend NO depende de que el agente de arquitectura esté activo para saber qué patrones seguir.
- Los patrones y restricciones se inyectan en cada agente que los necesite (duplicación controlada).
- **Razonamiento:** En Vibe Coding, el programador usa UN agente a la vez. Ese agente debe tener contexto completo.

## R-022: Perfiles de Negocio Generan Agentes IA de Negocio
> **Todo perfil de negocio diseñado (estratega, operaciones, UX, condicionales) se materializa como un agente IA funcional.**

- No basta con documentar que "existe un agente estratega de negocio".
- Se genera el archivo `.agent.md` con prompt completo que permite al programador invocar `@estratega-negocio` y obtener análisis estratégico del proyecto.
- El agente de negocio IA tiene tools de lectura pero NO de escritura de código.
- **Severidad:** Alta. Sin agentes de negocio IA, el programador pierde la dimensión estratégica.

## R-023: Perfiles Técnicos Generan Agentes IA de Código
> **Todo perfil técnico diseñado se materializa como un agente IA que puede generar código real.**

- El agente backend IA tiene tools de escritura, terminal y búsqueda.
- El agente frontend IA tiene tools de escritura y puede crear componentes.
- Los agentes técnicos IA incluyen las restricciones de negocio como reglas hard.
- **Cada agente técnico IA sabe:**
  - Qué stack usar (no pregunta)
  - Qué patrones seguir (inyectados como restricciones)
  - Qué reglas de negocio afectan su módulo (inyectadas en el prompt)

## R-024: Token Budget Obligatorio
> **El entorno generado respeta los límites de contexto de la IA objetivo.**

| Archivo | Máximo Recomendado |
|---------|-------------------|
| Instrucciones workspace | 300 líneas |
| Cada agente IA | 150 líneas |
| Cada rule de codificación | 50 líneas |
| Cada skill del proyecto | 100 líneas |
| Total del entorno | < 3000 líneas |

- Si el negocio es complejo (>3000 líneas), priorizar por impacto y mover el detalle a docs/ con referencias.
- **Razonamiento:** Las IAs pierden efectividad cuando el contexto es demasiado largo. Mejor precisión en menos tokens.

## R-025: Quick Start Obligatorio
> **Todo entorno generado incluye un archivo Quick Start que el programador puede seguir en < 5 minutos.**

- Incluye: cómo copiar al workspace, primer prompt sugerido, tabla de agentes disponibles.
- No requiere leer documentación adicional para empezar.
- Los primeros 3 prompts sugeridos usan terminología del dominio real del proyecto.

## R-026: Bidireccionalidad Negocio ↔ Técnica en Agentes IA
> **Los agentes IA de negocio pueden ser consultados por los agentes técnicos, y viceversa.**

- El agente backend puede preguntar: "¿Cuál es la regla de negocio para descuentos por volumen?"
- El agente de estrategia puede preguntar: "¿Es técnicamente viable implementar dynamic pricing?"
- El Quick Start debe incluir ejemplos de esta interacción cruzada.
- **Materialización:** Cada agente IA incluye en su prompt una sección "Cuándo consultar a otros agentes".

## Prioridad de Reglas de Vibe Coding

1. **R-019** (Output Ejecutable) — Si no funciona, nada más importa
2. **R-027** (No Tocar Preexistentes) — Proteger el workspace del usuario
3. **R-020** (Contexto Inyectado) — La IA de codificación necesita saber
4. **R-021** (Agentes Autónomos) — Cada agente funciona solo
5. **R-024** (Token Budget) — Respetar límites
6. R-022, R-023, R-025, R-026 en orden

## R-027: No Modificar Archivos Preexistentes
> **El generador SOLO crea archivos nuevos dentro de `.github/`. NUNCA modifica, mueve, renombra ni elimina archivos que ya existían en el workspace.**

- El workspace del usuario puede tener código, assets, configuraciones. Son intocables.
- Si hay conflicto de nombres, el generador agrega sufijo o pregunta al usuario.
- **Severidad:** Crítica. Borrar o reorganizar el código del usuario destruye confianza.

## R-028: Un Archivo por Agente, Una Carpeta por Skill
> **Cada agente diseñado se materializa como un archivo `.agent.md` individual. Cada skill se materializa como una carpeta con `SKILL.md` individual.**

- NUNCA combinar agentes en un solo archivo catch-all.
- NUNCA combinar skills en un solo archivo.
- Mínimo 5 agentes y 5 skills por entorno generado.
- Si el mínimo no se alcanza, el análisis de dominio fue insuficiente — repetir la fase 1.

## R-029: Meta-herramientas Obligatorias e Intocables
> **Todo entorno generado incluye un agente configurador y 4 meta-skills (crear-agente, crear-skill, modificar-agente, modificar-skill) que permiten evolucionar el entorno después de la generación inicial.**

- El agente `configurador-entorno` y las meta-skills M1-M4 se generan SIEMPRE.
- NUNCA deben ser eliminados por ningún agente, en ninguna circunstancia.
- Si un agente sugiere eliminar skills o agentes "que no se usan", debe excluir explícitamente:
  - `.github/agents/configurador-entorno.agent.md`
  - `.github/skills/crear-agente/`
  - `.github/skills/crear-skill/`
  - `.github/skills/modificar-agente/`
  - `.github/skills/modificar-skill/`
- **Severidad:** Crítica. Sin estas herramientas, el usuario pierde la capacidad de evolucionar su entorno y debe recrear todo desde cero.

## R-030: Investigación con Fuentes Confiables
> **Todo agente IA generado debe tener la capacidad de investigar en internet y DEBE citar fuentes confiables con URL para toda información externa.**

- Los agentes de negocio incluyen `fetch_webpage` en sus tools para investigar regulaciones, mercado y tendencias.
- Los agentes técnicos incluyen `fetch_webpage` en sus tools para consultar documentación oficial y estándares.
- Toda afirmación basada en investigación incluye: nombre de la fuente, URL directa, tipo (oficial/académico/industria).
- Jerarquía de confiabilidad: oficial (.gov, docs oficiales) > académico (scholar, IEEE) > industria (Gartner, Forrester) > periodismo (tech blogs reconocidos) > comunidad (Stack Overflow, foros).
- PROHIBIDO: Citar URLs inventadas o no verificadas. Solo incluir URLs comprobadas con `fetch_webpage`.
- Cada entorno generado incluye una skill `investigar-en-internet` que estandariza el proceso de búsqueda.
- **Severidad:** Alta. Información sin fuente verificable reduce la credibilidad del entorno generado.
