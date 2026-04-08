# Skill: Agregar Skill al Sistema

## Descripción
Agregar un nuevo skill al sistema BASE-GENERATOR.

## Pasos

1. **Crear directorio** `source/skills/{categoría}/nombre-skill/SKILL.md`
   - Categorías: `negocio`, `tecnico`, `orquestacion`, `vibe-coding`

2. **Estructura del SKILL.md**: Descripción, Inputs, Output, Pasos, Ejemplo

3. **Autodiscovery** — `get_skill_folders()` hace `rglob("SKILL.md")` en `source/skills/`

4. **Probar**: `python export.py --target copilot --output ./test-export`

5. **Actualizar**: `docs/05-skills.md`, `README.md` (conteo), `AGENTS.md` (inventario)
