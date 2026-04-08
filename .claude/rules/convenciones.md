# Convenciones del Repositorio BASE-GENERATOR

## Python (export.py)
- Solo stdlib: argparse, pathlib, re, shutil, sys, os
- Sin pip install, sin dependencias externas
- Type hints en firmas de funciones

## Markdown (source/)
- Frontmatter YAML entre `---` obligatorio
- Campos mínimos: `name`, `description`
- Agentes incluyen `type:` (negocio/tecnico/vibe-coding)
- Listas con `-` (no `*`)

## Nombres de archivos
- kebab-case: `analizar-dominio-negocio.md`
- Skills: carpeta/SKILL.md
- Rules: `{NN}-nombre.md`

## Token Budget (R-024)
- Instrucciones: < 300 líneas
- Agentes: < 150 líneas
- Reglas: < 50 líneas por archivo
