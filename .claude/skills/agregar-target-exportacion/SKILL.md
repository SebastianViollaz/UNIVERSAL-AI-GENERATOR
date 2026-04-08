# Skill: Agregar Target de Exportación

## Descripción
Agregar soporte de una nueva IA de codificación al pipeline de exportación.

## Pasos

1. **Investigar** el formato nativo de la IA:
   - Instrucciones de workspace, reglas, agentes, skills
   - Frontmatter, extensiones, activación

2. **Crear template** `templates/{nombre-ia}/README.md`

3. **Agregar al meta** `meta/export-targets.yml`

4. **Escribir exportador** en `export.py`:
   ```python
   def export_nueva_ia(output_dir: Path):
       # Transformar instructions, rules, agents, skills
   ```

5. **Registrar**:
   - `TARGETS = [..., "nueva-ia"]`
   - `EXPORTERS = {..., "nueva-ia": export_nueva_ia}`

6. **Probar**: `python export.py --target nueva-ia --output ./test`

7. **Actualizar docs**: `README.md`, `docs/08-export-pipeline.md`
