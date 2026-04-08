# Skill: Agregar Agente al Sistema

## Descripción
Agregar un nuevo agente al sistema BASE-GENERATOR.

## Pasos

1. **Crear archivo** en `source/agents/{categoría}/nombre-agente.md`
   - Categorías: `negocio`, `tecnicos`, `vibe-coding`
   - Frontmatter: `name`, `description`, `scope`, `type`
   - `type` determina tools en Copilot export (negocio=lectura, tecnico=escritura+terminal, vibe-coding=lectura+escritura)

2. **Contenido** — Título H1, rol, cuándo actúa, inputs/outputs. < 150 líneas (R-024)

3. **Autodiscovery** — export.py ya itera `source/agents/{negocio,tecnicos,vibe-coding}/`. Archivos `condicionales.md` se excluyen.

4. **Probar**: `python export.py --target copilot --output ./test-export`

5. **Actualizar**: `docs/04-agentes.md`, `README.md` (conteo), `AGENTS.md` (si obligatorio)
