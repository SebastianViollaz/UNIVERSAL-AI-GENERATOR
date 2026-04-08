---
name: reglas-formato
description: "Reglas de formato y estructura de salida para que el output sea inyectable en cualquier entorno de desarrollo. Se aplican siempre."
scope: always
---

# Reglas de Formato y Estructura de Salida

## R-008: Formato Inyectable
> **La salida final debe estar en un formato que el programador pueda inyectar directamente en su entorno de desarrollo.**

- Todos los archivos usan Markdown (.md) o YAML (.yaml) con estructura consistente.
- Las rutas de archivos son válidas en Windows, macOS y Linux.
- Los nombres de archivo usan kebab-case sin caracteres especiales.
- Ningún archivo excede las 500 líneas (dividir si es necesario).

## R-009: Estructura Determinista
> **Dado el mismo input, el agente genera la misma estructura de archivos.**

- La estructura de directorios es fija (definida en el System Prompt).
- El contenido varía según el proyecto, pero la organización no cambia.
- Esto permite que otros agentes y IAs sepan dónde buscar información.

## R-010: Secciones Obligatorias
> **Toda salida del agente debe incluir las 7 secciones definidas en el System Prompt.**

```
1. Análisis del Dominio
2. Agentes de Negocio Diseñados
3. Agentes Técnicos Diseñados
4. Mapa de Comunicación Inter-Agentes
5. Árbol de Documentación Generado
6. Checklist de Validación
7. Próximos Pasos Recomendados
```

- Si una sección no aplica, se indica explícitamente por qué.
- No se agregan secciones adicionales sin completar las obligatorias.
