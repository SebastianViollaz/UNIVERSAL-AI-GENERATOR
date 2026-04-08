---
name: generar-rules-ia
description: "Genera archivos de reglas de codificación (.instructions.md, .mdc, rules/*.md) específicas del proyecto, basadas en reglas de negocio, seguridad y convenciones técnicas."
---

# Skill: generar_rules_ia

## Propósito
Genera reglas de codificación que las herramientas de Vibe Coding aplican automáticamente al generar código. Cada regla traduce una restricción de negocio, seguridad o arquitectura en una instrucción concreta que la IA debe seguir.

## Diferencia con las reglas del Creador de Entornos
- Las reglas en `source/rules/` gobiernan CÓMO el Creador diseña entornos.
- Las reglas generadas por esta skill gobiernan CÓMO la IA de codificación escribe código en el proyecto final.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `reglas_negocio` | object[] | Sí | Output de `formalizar_reglas_negocio` |
| `modelo_seguridad` | object | Sí | Output de `disenar_seguridad_sistema` |
| `arquitectura` | object | Sí | Output de `disenar_arquitectura_sistema` |
| `estrategia_testing` | object | Sí | Output de `definir_estrategia_testing` |
| `stack` | object | Sí | Output de `stack_consolidado` de `estructurar_agentes_tecnicos` |
| `ia_objetivo` | string | Sí | IA para la que generar |

## Convención de Naming para IDs de Reglas
Todas las reglas generadas siguen el formato `{DOMINIO}-{NNN}` para trazabilidad:
- `SEC-001` — Regla de seguridad
- `ARCH-001` — Regla de arquitectura
- `TEST-001` — Regla de testing
- `{MÓDULO}-001` — Regla de módulo específico (ej: `FACT-001`, `AUTH-001`)

## Outputs

```yaml
rules_ia:
  siempre_activas:
    - ruta: string
      nombre: string
      contenido: string
      aplica_a: string   # "**" para siempre, glob para específico
  por_modulo:
    - ruta: string
      nombre: string
      contenido: string
      aplica_a: string   # ej: "src/modules/billing/**"
  por_tipo_archivo:
    - ruta: string
      nombre: string
      contenido: string
      aplica_a: string   # ej: "**/*.test.ts"
```

## Categorías de Reglas a Generar

### 1. Reglas de Negocio → Reglas de Código
Transformar cada regla de negocio en una restricción de codificación:

```markdown
---
description: "Reglas de negocio del módulo de facturación"
applyTo: "src/modules/billing/**"
---

# Reglas — Facturación

- Los montos SIEMPRE usan Decimal (nunca float). Motivo: RN-FACT-001.
- Una factura emitida NO puede eliminarse, solo cancelarse con nota de crédito. Motivo: Regulación SAT.
- El cálculo de IVA usa TaxCalculatorService, nunca cálculo inline. Motivo: ADR-007.
- Toda operación financiera genera audit log con: usuario, timestamp, monto anterior, monto nuevo.
```

### 2. Reglas de Seguridad → Reglas de Código
```markdown
---
description: "Reglas de seguridad para todo el proyecto"
applyTo: "**"
---

# Reglas de Seguridad

- NUNCA loguear datos sensibles (PII, tokens, passwords). Usar redacción: `[REDACTED]`.
- Todo input de usuario pasa por validación ANTES de llegar al dominio.
- SQL queries SIEMPRE usan prepared statements / ORM. NUNCA concatenación.
- Las API keys van en variables de entorno, NUNCA en código.
- CORS está restringido a los dominios configurados en .env.
```

### 3. Reglas de Arquitectura → Reglas de Código
```markdown
---
description: "Convenciones de arquitectura"
applyTo: "src/**"
---

# Reglas de Arquitectura

- Cada módulo sigue la estructura: domain/ → application/ → infrastructure/ → presentation/.
- El dominio NO importa de infraestructura. NUNCA.
- Los use cases reciben y retornan DTOs, no entidades del dominio.
- Las dependencias se inyectan, no se instancian directamente.
- Un aggregate no puede referenciar otro aggregate directamente, solo por ID.
```

### 4. Reglas de Testing → Reglas de Código
```markdown
---
description: "Convenciones de testing"
applyTo: "**/*.test.*"
---

# Reglas de Testing

- Nomenclatura: `describe('ModuleName')` → `it('should {comportamiento} when {condicion}')`.
- Todo test de negocio debe referenciar la regla que verifica: `// Verifica RN-FACT-001`.
- Mocks solo para dependencias externas. Dominio NUNCA se mockea.
- Cada endpoint público tiene al menos: happy path, validación de input, caso de auth.
- Cobertura mínima en módulos críticos: {gates_de_calidad_de_estrategia_testing}.
```

### 5. Antipatrones con Ejemplos: Contraste Negativo-Positivo
Para cada regla crítica de negocio, incluir contraste visual:
```markdown
❌ INCORRECTO: `const tax = amount * 0.16`
✅ CORRECTO: `const tax = TaxCalculatorService.calculate(amount, TaxType.IVA) // RN-FACT-001`

❌ INCORRECTO: `await db.query('SELECT * FROM users WHERE id = ' + userId)`
✅ CORRECTO: `await db.query('SELECT * FROM users WHERE id = $1', [userId]) // SEC-003`
```

## Formato por IA

| IA | Extensión | Ruta | Frontmatter |
|----|----------|------|-------------|
| Copilot | `.instructions.md` | `.github/instructions/` | `applyTo` |
| Claude | `.md` | `.claude/rules/` | sin frontmatter o `paths` |
| Cursor | `.mdc` | `.cursor/rules/` | `alwaysApply`, `globs` |
| Windsurf | `.md` | `.windsurf/rules/` | `trigger`, `globs` |
| Continue | `.md` | `.continue/rules/` | `alwaysApply`, `globs` |

## Reglas Internas
1. Cada regla cita la fuente: regla de negocio (RN-XXX), ADR, o requisito de seguridad (SEC-XXX).
2. Las reglas son imperativas y concretas, no sugerencias vagas.
3. Las reglas por módulo son más específicas que las globales (override implícito).
4. Máximo 30 reglas globales (más de eso confunde a la IA).
5. Las reglas de testing son obligatoriamente vinculadas a reglas de negocio.
6. Toda regla crítica incluye contraste negativo-positivo con ejemplo de código.
