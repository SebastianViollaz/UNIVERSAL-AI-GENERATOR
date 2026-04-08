---
name: generar-quick-start-guide
description: "Produce el documento que el desarrollador lee en menos de 5 minutos para empezar: estructura del entorno, cómo activar agentes, comandos de setup y primer flujo de trabajo."
---

# Skill: generar_quick_start_guide

## Propósito
Es el primer documento que lee el programador y el más importante para la adopción del entorno. Sin él, el desarrollador recibe 30+ archivos sin saber por dónde empezar. Diseñado para ser completado en menos de 5 minutos.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `arbol_documentacion` | object | Sí | Output de `generar_arbol_documentacion` |
| `agentes_ia` | object | Sí | Output de `generar_agentes_ia` |
| `skills_ia` | object[] | Sí | Output de `generar_skills_ia` |
| `infraestructura` | object | Sí | Output de `planificar_infraestructura` |
| `stack` | object | Sí | Output de `stack_consolidado` |
| `ia_objetivo` | string | Sí | Para instrucciones específicas de la herramienta |

## Outputs

```yaml
quick_start_guide:
  contenido: string                    # El documento completo
  tiempo_estimado_setup: string        # "~5 minutos"
  primer_prompt_recomendado: string    # Para validar que la IA cargó el contexto
  comandos_setup: string[]             # En orden: clonar, instalar, configurar, ejecutar
```

## Estructura del Documento Generado

```markdown
# {NOMBRE_PROYECTO} — Quick Start Guide

> Tendrás el entorno listo en ~{tiempo_estimado_setup}.

## 1. Setup (2 min)
```bash
{comandos_setup}
```

## 2. Estructura del Entorno IA ({tiempo} min)

### Agentes disponibles
| Agente | Para qué usarlo | Cómo invocarlo |
|--------|----------------|---------------|
{tabla_agentes}

### Skills disponibles
| Skill | Cuándo usarla |
|-------|--------------|
{tabla_skills}

### Documentación clave
| Archivo | Leerlo cuando... |
|---------|-----------------|
{tabla_docs}

## 3. Primer Flujo de Trabajo Recomendado
1. {paso_1}
2. {paso_2}
3. {paso_3}

## 4. Valida que Todo Funciona
Envía este mensaje a tu IA:
> "{primer_prompt_recomendado}"

Respuesta esperada: La IA debe mencionar el nombre del proyecto, el stack y al menos una regla de negocio.

## Dónde Pedir Ayuda
- Reglas de negocio: `docs/negocio/reglas-negocio/`
- Decisiones de arquitectura: `docs/tecnico/arquitectura/adr/`
- Convenciones de código: instrucciones del workspace
```

## Reglas Internas
1. El Quick Start Guide no supera 2 páginas (< 80 líneas). Si es más largo, está mal.
2. Los comandos son copiables directamente — sin explicaciones largas en medio.
3. El `primer_prompt_recomendado` debe ser específico del dominio del proyecto, no genérico.
4. Las tablas de agentes, skills y docs son la referencia rápida — no repetir el contenido completo.
5. Asumir que el desarrollador llega sin saber nada del entorno generado.
