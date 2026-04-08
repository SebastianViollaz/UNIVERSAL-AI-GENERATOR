# Vibe Coding — Materialización de Agentes IA

## Concepto

Vibe Coding es la capa que transforma agentes **conceptuales** (diseñados en las fases 2-3) en archivos **funcionales** que la IA de codificación consume directamente. El programador copia los archivos al workspace y la IA ya sabe todo del proyecto.

## Antes vs Después del Vibe Coding

| Sin Vibe Coding | Con Vibe Coding |
|-----------------|-----------------|
| Documentación descriptiva que el programador lee | Archivos `.agent.md` que la IA carga automáticamente |
| "El backend debe respetar reglas fiscales" | `@backend` ya tiene las reglas inyectadas en su prompt |
| Manual de 50 páginas que nadie lee | Quick Start en < 5 minutos |
| El programador configura la IA desde cero | La IA arranca pre-configurada con el contexto completo |

## Agentes de Vibe Coding (3)

### Generador de Agentes IA
Transforma cada agente diseñado en un archivo `.agent.md` funcional:
- Frontmatter YAML con metadata (description, tools)
- Contexto de negocio inyectado directamente en el prompt
- Tools asignados según tipo (negocio=lectura, técnico=escritura+terminal, vibe-coding=lectura+escritura)
- < 150 líneas por agente (R-024)

### Configurador de Entorno IA
Genera los archivos de configuración del workspace:
- `copilot-instructions.md` / `CLAUDE.md` con glosario
- Reglas de codificación por módulo
- Convenciones de naming, patrones de diseño, stack tecnológico
- < 300 líneas de instrucciones (R-024)

### Orquestador de Vibe Coding
Coordina todo el flujo de materialización:
- Ejecuta los 5 skills de Vibe Coding en secuencia
- Genera el Quick Start Guide
- Valida que todo sea plug & play
- Optimiza tokens y deduplica contexto

## Skills de Vibe Coding (5)

| Skill | Qué Produce | Regla Asociada |
|-------|-------------|----------------|
| `generar-agentes-ia` | Archivos `.agent.md` por agente | R-019, R-020, R-021 |
| `generar-instrucciones-workspace` | Instrucciones globales con glosario | R-020, R-024 |
| `generar-rules-ia` | Reglas de código por módulo | R-019, R-022 |
| `generar-skills-ia` | Skills del proyecto (ADRs, tests) | R-019, R-023 |
| `optimizar-prompts-ia` | Optimización de tokens por IA | R-024, R-018 |

## Reglas de Vibe Coding (R-019 a R-026)

Las 8 reglas garantizan que la materialización sea:
1. **Ejecutable** — No descriptiva (R-019)
2. **Auto-contenida** — Contexto inyectado, no referenciado (R-020)
3. **Autónoma** — Cada agente funciona solo (R-021)
4. **Completa** — Negocio → agentes negocio IA (R-022), Técnico → agentes código IA (R-023)
5. **Eficiente** — Respeta token budget (R-024)
6. **Rápida** — Quick Start en < 5 min (R-025)
7. **Dual** — Cada agente refleja negocio + técnica (R-026)

## Ejemplo de Archivo Generado

```markdown
---
description: "Agente backend especializado en el ERP de muebles. Conoce las reglas fiscales mexicanas, el modelo de datos de inventario y los patrones del stack Node.js + PostgreSQL."
tools:
  - read_file
  - create_file
  - replace_string_in_file
  - run_in_terminal
  - grep_search
  - semantic_search
  - list_dir
  - get_errors
---

# Agente Backend — ERP Muebles MX

## Contexto del Negocio
Empresa familiar de manufactura de muebles en México con 50 empleados.
Actualmente usan Excel para todo. Se necesita un ERP completo.

## Reglas de Negocio Inyectadas
- RN-FACT-001: Montos monetarios → Decimal(10,2). NUNCA float
- RN-FACT-002: CFDI obligatorio para toda factura > $0 MXN
- RN-INV-001: Stock mínimo = 20% del promedio mensual de venta

## Stack Técnico
- Runtime: Node.js 20 LTS
- Framework: NestJS
- Base de datos: PostgreSQL 16
- ORM: Prisma
...
```
