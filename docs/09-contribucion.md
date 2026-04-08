# Guía de Contribución

## Cómo agregar un nuevo agente

1. Crear archivo en `source/agents/{categoría}/nombre-agente.md`
2. Incluir frontmatter universal:
   ```yaml
   ---
   name: "nombre-agente"
   description: "Descripción breve para discovery por la IA"
   scope: "manual"
   type: "negocio"    # negocio | tecnico | vibe-coding
   ---
   ```
3. Escribir el contenido del agente (< 150 líneas por R-024)
4. Si es condicional, agregarlo al catálogo `condicionales.md` correspondiente
5. Verificar con `python export.py --target copilot --output ./test-export`

**El export.py ya itera automáticamente** los subdirectorios `agents/negocio`, `agents/tecnicos` y `agents/vibe-coding`, así que un nuevo archivo en esos directorios se exporta sin modificar el script.

## Cómo agregar un nuevo skill

1. Crear directorio `source/skills/{categoría}/nombre-skill/`
2. Crear `SKILL.md` dentro con la especificación completa
3. El skill debe incluir: descripción, inputs, outputs, pasos, ejemplos
4. Verificar con `python export.py --target copilot --output ./test-export`

**Los skills se descubren automáticamente** por `get_skill_folders()` que hace `rglob("SKILL.md")`.

## Cómo agregar una nueva regla

1. Decidir la categoría (o crear un nuevo archivo `{NN}-nombre.md`)
2. Agregar al archivo correspondiente en `source/rules/`
3. Asignar ID secuencial (R-NNN)
4. Mantener < 50 líneas por archivo de regla (R-024)

## Cómo agregar un nuevo target de exportación

1. **Investigar el formato nativo** de la IA:
   - ¿Dónde pone instrucciones de workspace?
   - ¿Tiene reglas? ¿Cómo se activan? ¿Qué frontmatter usa?
   - ¿Tiene agentes nativos? ¿Con tools?
   - ¿Tiene skills? ¿Prompts?

2. **Crear template** en `templates/{nombre-ia}/README.md` documentando la estructura

3. **Agregar al meta** en `meta/export-targets.yml` con los mappings de frontmatter

4. **Escribir el exportador** en `export.py`:
   ```python
   def export_nueva_ia(output_dir: Path):
       print("  Exportando para NuevaIA...")
       # Workspace instructions
       ws = read_file(SOURCE_DIR / "instructions" / "workspace.md")
       write_file(output_dir / "TARGET_FILE", strip_frontmatter(ws))
       # Rules, agents, skills...
   ```

5. **Registrar en EXPORTERS**:
   ```python
   EXPORTERS = {
       ...
       "nueva-ia": export_nueva_ia,
   }
   ```

6. **Agregar a TARGETS**:
   ```python
   TARGETS = [..., "nueva-ia"]
   ```

7. **Verificar**: `python export.py --target nueva-ia --output ./test`

## Convenciones

### Nombres de archivos
- Kebab-case: `analizar-dominio-negocio`, no `analizarDominioNegocio`
- Sin números de orden en agents y skills (el orden no importa)
- Números de orden en rules (01- a NN-)

### Frontmatter
- Siempre incluir `name` y `description`
- `scope` solo en rules e instructions
- `type` solo en agents
- `file_patterns` solo si `scope: file_pattern`

### Contenido
- Markdown estándar, sin HTML
- Encabezados empezando en `#` (H1) para el título principal
- `##` para secciones principales
- Listas con `-` (no `*`)
- Token budget: agentes < 150 líneas, instrucciones < 300, rules < 50
