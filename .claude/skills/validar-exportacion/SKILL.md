# Skill: Validar Exportación

## Descripción
Verificar que el pipeline de exportación funciona correctamente.

## Pasos

1. **Ejecutar**: `python export.py --target all --output ./test-export-validacion`

2. **Verificar cada target**:
   - **Copilot**: `.github/{copilot-instructions.md, instructions/, agents/, skills/, prompts/}`
   - **Claude**: `CLAUDE.md`, `.claude/{settings.json, rules/, agents/, skills/}`
   - **Cursor**: `AGENTS.md`, `.cursor/rules/*.mdc`
   - **Windsurf**: `AGENTS.md`, `.windsurf/{rules/, skills/}`
   - **Aider**: `CONVENTIONS.md`, `.aider.conf.yml`
   - **Continue**: `.continue/{config.yaml, rules/}`

3. **Checklist**:
   - [ ] 6 targets generan sin errores
   - [ ] Frontmatter correcto para cada IA
   - [ ] `condicionales.md` NO exportados como agentes
   - [ ] Skills con estructura carpeta/SKILL.md
   - [ ] 10 agentes, 7 rules, 20 skills en el output
   - [ ] Tools de Copilot respetan tipo (negocio/tecnico/vibe-coding)

4. **Limpiar**: borrar `./test-export-validacion`
