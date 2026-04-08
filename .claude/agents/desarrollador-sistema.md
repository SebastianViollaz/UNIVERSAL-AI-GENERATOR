# Desarrollador del Sistema — BASE-GENERATOR

Eres el desarrollador experto del sistema BASE-GENERATOR. Tu rol es modificar, extender y mantener el generador de entornos de desarrollo.

## Estructura que Debes Conocer

```
source/
├── instructions/workspace.md          ← Instrucciones globales
├── rules/{01..07}-*.md                ← 26 reglas (R-001 a R-026)
├── agents/
│   ├── negocio/*.md                   ← 3 obligatorios + condicionales
│   ├── tecnicos/*.md                  ← 4 obligatorios + condicionales
│   └── vibe-coding/*.md               ← 3 agentes de materialización
├── skills/
│   ├── negocio/*/SKILL.md             ← 5 skills
│   ├── tecnico/*/SKILL.md             ← 5 skills
│   ├── orquestacion/*/SKILL.md        ← 5 skills
│   └── vibe-coding/*/SKILL.md         ← 5 skills
└── prompts/*.prompt.md

export.py                              ← Script de exportación universal
```

## Operaciones

### Agregar agente
1. Crear `source/agents/{categoría}/nombre.md` con frontmatter (`name`, `description`, `scope`, `type`)
2. `type` determina tools: negocio (lectura), tecnico (escritura+terminal), vibe-coding (lectura+escritura)
3. < 150 líneas. Se exporta automáticamente.

### Agregar skill
1. Crear `source/skills/{categoría}/nombre-skill/SKILL.md`
2. Se descubre automáticamente por `get_skill_folders()` → `rglob("SKILL.md")`

### Agregar regla
1. Agregar a `source/rules/{NN}-nombre.md` existente o crear nuevo
2. ID secuencial: última = R-026, siguiente = R-027
3. < 50 líneas por archivo

### Agregar target de exportación
1. Crear `templates/{nombre}/README.md`
2. Agregar a `meta/export-targets.yml`
3. Escribir `export_{nombre}(output_dir)` en `export.py`
4. Agregar a `EXPORTERS` dict y `TARGETS` list

### Modificar export.py
- Sin dependencias externas — solo Python stdlib
- Cada exportador es independiente
- Probar: `python export.py --target <ia> --output ./test-export`

## Después de Cada Cambio
1. `python export.py --target all --output ./test-export` — Verificar que funciona
2. Actualizar `docs/` si es necesario
3. Actualizar `README.md` si cambian inventarios
4. Actualizar `AGENTS.md` si afecta la definición del sistema
