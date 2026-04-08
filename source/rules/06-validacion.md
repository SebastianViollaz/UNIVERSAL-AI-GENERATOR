---
name: reglas-validacion
description: "Reglas de calidad mínima y validación que deben cumplirse antes de entregar un entorno. Se aplican siempre."
scope: always
---

# Reglas de Calidad Mínima y Validación

## R-016: Gate de Calidad Pre-Entrega
> **El entorno NO se entrega si la validación puntúa menor a 80/100.**

- Ejecutar `validar_entorno_generado` antes de cualquier exportación.
- Los errores se corrigen automáticamente si es posible.
- Si no es posible, se reportan al programador.

## R-017: Completitud sobre Velocidad
> **Es preferible un entorno completo que tarde más, a uno rápido pero incompleto.**

- No omitir secciones por "brevedad".
- No generar stubs o placeholders vacíos.
- Cada archivo generado tiene contenido accionable.

## R-018: Retrocompatibilidad con IAs
> **La documentación generada debe ser consumible por cualquier IA de codificación moderna.**

- Formato Markdown estándar (compatible con GPT, Claude, Copilot, Cursor, Windsurf, Continue, Aider, etc.).
- No usar extensiones propietarias de Markdown.
- Archivos por debajo de 500 líneas.
- Incluir índice de navegación para que las IAs sepan por dónde empezar.

## Prioridad de Reglas

En caso de conflicto entre reglas, el orden de prioridad es:

1. **R-001** (Primacía del Negocio)
2. **R-005** (Nada Queda Implícito)
3. **R-004** (Profundidad Dual)
4. **R-002** (Separación de Responsabilidades)
5. **R-011** (Protocolo de Conflicto)
6. Todas las demás en orden numérico
