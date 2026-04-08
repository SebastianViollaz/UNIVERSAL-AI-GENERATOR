# Skill: Agregar Regla de Ejecución

## Descripción
Agregar nuevas reglas de ejecución al sistema.

## Pasos

1. **Determinar categoría** — 7 archivos existentes:
   - `01-separacion.md` (R-001–R-003), `02-calidad.md` (R-004–R-007)
   - `03-formato.md` (R-008–R-010), `04-comunicacion.md` (R-011–R-013)
   - `05-escalabilidad.md` (R-014–R-015), `06-validacion.md` (R-016–R-018)
   - `07-vibe-coding.md` (R-019–R-026)

2. **Asignar ID** — Última: R-026, siguiente: R-027+

3. **Formato**: título `### R-NNN: Nombre`, descripción, ejemplo de cumplimiento/violación

4. **Restricción**: < 50 líneas por archivo (R-024)

5. **Probar**: `python export.py --target copilot --output ./test-export`

6. **Actualizar**: `docs/06-reglas.md`, `README.md` (conteo), `AGENTS.md` (si aplica)
