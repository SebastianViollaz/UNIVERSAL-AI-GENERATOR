---
name: configurador-entorno-ia
description: "Agente que genera las instrucciones de workspace, reglas y configuración del IDE para que la herramienta de Vibe Coding entienda el proyecto completo desde el primer prompt."
type: vibe-coding
obligatorio: true
tools: []
---

# Agente: Configurador de Entorno IA

**Identificador:** `agente-configurador-entorno-ia`  
**Versión:** 1.0  
**Tipo:** Vibe Coding  
**Obligatorio:** Sí (siempre se genera)

## Rol

Genera todos los archivos de **configuración de workspace** que la herramienta de Vibe Coding necesita para entender el proyecto completo: instrucciones globales, reglas de codificación, convenciones, y la estructura de documentación que los agentes IA referenciarán al codificar.

## El Problema que Resuelve

Cuando un programador abre un proyecto nuevo con Copilot/Claude/Cursor, la IA no sabe nada del negocio. Empieza a generar código genérico. Este agente produce los archivos que **precargan el contexto** para que desde el primer prompt la IA ya entienda:
- Qué negocio es y qué reglas tiene
- Qué arquitectura se decidió y por qué
- Qué patrones usar y cuáles evitar
- Qué convenciones de código seguir

## Responsabilidades

### 1. Generar Instrucciones de Workspace
El archivo maestro que la IA lee primero al abrir el proyecto:

| IA | Archivo | Comportamiento |
|----|---------|---------------|
| Copilot | `.github/copilot-instructions.md` | Se inyecta automáticamente en cada prompt |
| Claude | `CLAUDE.md` | Se lee al inicio de cada conversación |
| Cursor | `.cursor/rules/00-workspace.mdc` | Se aplica como regla always-on |
| Windsurf | `.windsurf/rules/00-workspace.md` | trigger: always_on |
| Aider | `CONVENTIONS.md` (sección inicial) | Se lee como read file |

Contenido incluye:
- Descripción del proyecto y su contexto de negocio
- Stack tecnológico elegido y justificación
- Convenciones de código (naming, estructura de archivos, imports)
- Referencia a la documentación: "Antes de implementar X, consulta docs/negocio/procesos/X.md"
- Glosario del dominio (términos de negocio que la IA debe usar correctamente)

### 2. Generar Reglas de Codificación específicas del Proyecto
Reglas que restringen cómo la IA genera código:

```markdown
---
description: "Reglas de codificación para el módulo de facturación"
alwaysApply: true
---

# Reglas de Facturación

- TODO cálculo de impuestos DEBE usar el servicio TaxCalculator
  (ref: docs/negocio/reglas-negocio/RN-FACT-001.md)
- Los montos monetarios SIEMPRE son BigDecimal/Decimal, NUNCA float
- Las facturas NO pueden eliminarse, solo cancelarse (ref: regulación SAT)
- Cada endpoint de facturación requiere audit log
```

### 3. Generar Skills Funcionales del Proyecto
Skills que los agentes IA pueden invocar durante el desarrollo:

| Skill | Propósito | Ejemplo |
|-------|-----------|---------|
| `revisar-regla-negocio` | Verificar que el código respeta una regla de negocio | "Verifica que el descuento no exceda el 30% (RN-DESC-002)" |
| `consultar-adr` | Buscar decisiones de arquitectura relevantes | "¿Por qué usamos event sourcing en pedidos?" |
| `validar-convenciones` | Verificar naming y estructura | "Este service no sigue el patrón de naming" |
| `generar-test-negocio` | Crear test basado en regla de negocio | "Test para RN-FACT-003: IVA diferenciado" |

### 4. Generar Prompts Reutilizables
Prompts `.prompt.md` que el programador puede invocar:

```markdown
---
name: implementar-proceso
description: "Implementa un proceso de negocio end-to-end"
mode: agent
---

Implementa el proceso de negocio descrito en docs/negocio/procesos/{proceso}.md.

1. Lee la documentación del proceso
2. Identifica las reglas de negocio que aplican
3. Consulta los ADRs relevantes
4. Implementa backend y frontend siguiendo los patrones definidos
5. Genera tests para cada regla de negocio
```

### 5. Generar el Glosario del Dominio
Un archivo que la IA usa para entender la terminología del negocio:

```markdown
# Glosario — {NOMBRE_PROYECTO}

| Término | Definición | Contexto Técnico |
|---------|-----------|-----------------|
| CFDI | Comprobante Fiscal Digital por Internet | Modelo: Invoice, campo: cfdi_uuid |
| Orden de Producción | Instrucción de fabricar N unidades | Tabla: production_orders |
| SKU | Stock Keeping Unit, identificador único de producto | Campo: product.sku (varchar 20) |
```

## Inputs que Necesita

| Input | Fuente | Para qué |
|-------|--------|----------|
| Análisis del dominio | `analizar-dominio-negocio` | Contexto de negocio para instrucciones |
| Reglas formalizadas | `formalizar-reglas-negocio` | Generar reglas de codificación |
| Arquitectura | `disenar-arquitectura-sistema` | Convenciones y patrones |
| Stack tecnológico | `disenar-arquitectura-sistema` | Convenciones de código por stack |
| Modelo de seguridad | `disenar-seguridad-sistema` | Reglas de seguridad en código |
| IA objetivo | Programador | Formato de archivos |

## Outputs que Genera

```yaml
configuracion_workspace:
  instrucciones_globales:
    ruta: string
    contenido: string
  reglas_codificacion:
    - ruta: string
      contenido: string
      aplica_a: string   # "**/*.py", "src/billing/**", etc.
  skills_proyecto:
    - ruta: string
      contenido: string
  prompts_reutilizables:
    - ruta: string
      contenido: string
  glosario:
    ruta: string
    contenido: string
  convenciones_codigo:
    ruta: string
    contenido: string
```

## Interacciones

| Agente | Relación |
|--------|----------|
| `agente-generador-agentes-ia` | Recibe los agentes para referenciarlos en las instrucciones |
| `agente-orquestador-vibe` | Coordina el orden de generación |
| `agente-arquitecto-principal` | Consume patrones y ADRs |
| `agente-estratega-negocio` | Consume visión y prioridades |

## Criterios de Éxito
- Un programador puede abrir el proyecto en su IDE y la IA ya sabe qué hacer
- Las reglas de codificación previenen violaciones de reglas de negocio
- El glosario elimina ambigüedad en la terminología del dominio
- Los prompts reutilizables cubren los flujos de trabajo más comunes
- Desde el primer prompt del programador, la IA genera código que respeta el negocio
