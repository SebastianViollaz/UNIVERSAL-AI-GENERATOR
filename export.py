"""
export.py — Exportador Universal del Creador de Entornos Iniciales

Transforma los archivos fuente canónicos (source/) al formato nativo
de la IA objetivo: Copilot, Claude, Cursor, Windsurf, Aider o Continue.

Uso:
    python export.py --target copilot --output ./mi-proyecto
    python export.py --target claude --output ./mi-proyecto
    python export.py --target cursor --output ./mi-proyecto
    python export.py --target windsurf --output ./mi-proyecto
    python export.py --target aider --output ./mi-proyecto
    python export.py --target continue --output ./mi-proyecto
    python export.py --target all --output ./exports
"""

import argparse
import os
import re
import shutil
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent.resolve()
SOURCE_DIR = SCRIPT_DIR / "source"
TEMPLATES_DIR = SCRIPT_DIR / "templates"

TARGETS = ["copilot", "claude", "cursor", "windsurf", "aider", "continue"]


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def strip_frontmatter(content: str) -> str:
    """Remove YAML frontmatter from markdown content."""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            return content[end + 3:].lstrip("\n")
    return content


def extract_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter as a simple dict (no PyYAML dependency)."""
    fm = {}
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            block = content[3:end].strip()
            for line in block.split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    val = val.strip().strip('"').strip("'")
                    # Handle inline YAML lists: [item1, item2]
                    if val.startswith("[") and val.endswith("]"):
                        items = val[1:-1].split(",")
                        val = [i.strip().strip('"').strip("'") for i in items if i.strip()]
                    fm[key.strip()] = val
    return fm


def build_frontmatter(fields: dict) -> str:
    """Build YAML frontmatter string from dict."""
    if not fields:
        return ""
    lines = ["---"]
    for key, val in fields.items():
        if isinstance(val, list):
            lines.append(f"{key}:")
            for item in val:
                lines.append(f"  - {item}")
        elif isinstance(val, bool):
            lines.append(f"{key}: {'true' if val else 'false'}")
        else:
            lines.append(f'{key}: "{val}"')
    lines.append("---\n")
    return "\n".join(lines)


def get_source_files(subdir: str, extension: str = ".md") -> list[Path]:
    """Get all source files from a subdirectory."""
    source_path = SOURCE_DIR / subdir
    if not source_path.exists():
        return []
    return sorted(source_path.rglob(f"*{extension}"))


def get_skill_folders() -> list[Path]:
    """Get all skill SKILL.md files."""
    skills_dir = SOURCE_DIR / "skills"
    if not skills_dir.exists():
        return []
    return sorted(skills_dir.rglob("SKILL.md"))


# ─────────────────────────────────────────────
# Export: GitHub Copilot
# ─────────────────────────────────────────────

def export_copilot(output_dir: Path):
    print("  Exportando para GitHub Copilot...")

    # Workspace instructions
    ws = read_file(SOURCE_DIR / "instructions" / "workspace.md")
    write_file(output_dir / ".github" / "copilot-instructions.md", strip_frontmatter(ws))

    # Rules -> .github/instructions/*.instructions.md
    for rule_file in get_source_files("rules"):
        content = read_file(rule_file)
        fm = extract_frontmatter(content)
        body = strip_frontmatter(content)
        new_fm = build_frontmatter({
            "description": fm.get("description", ""),
            "applyTo": "**",
        })
        name = rule_file.stem
        write_file(
            output_dir / ".github" / "instructions" / f"{name}.instructions.md",
            new_fm + body,
        )

    # Agents -> .github/agents/*.agent.md
    for agent_dir in ["agents/negocio", "agents/tecnicos", "agents/vibe-coding"]:
        for agent_file in get_source_files(agent_dir):
            if agent_file.stem == "condicionales":
                continue  # Skip catalog files
            content = read_file(agent_file)
            fm = extract_frontmatter(content)
            body = strip_frontmatter(content)
            agent_type = fm.get("type", "")
            source_tools = fm.get("tools", [])
            if agent_type == "tecnico":
                tools = ["read_file", "create_file", "replace_string_in_file", "run_in_terminal", "grep_search", "semantic_search", "list_dir", "get_errors"]
            elif agent_type == "vibe-coding":
                tools = ["read_file", "create_file", "replace_string_in_file", "grep_search", "semantic_search", "list_dir"]
            else:
                tools = ["read_file", "grep_search", "semantic_search", "list_dir"]
            # Merge source-declared tools (e.g. fetch_webpage) without duplicates
            for t in source_tools:
                if t and t not in tools:
                    tools.append(t)
            new_fm = build_frontmatter({
                "description": fm.get("description", ""),
                "tools": tools,
            })
            write_file(
                output_dir / ".github" / "agents" / f"{agent_file.stem}.agent.md",
                new_fm + body,
            )

    # Skills -> .github/skills/*/SKILL.md
    for skill_md in get_skill_folders():
        skill_name = skill_md.parent.name
        content = read_file(skill_md)
        write_file(
            output_dir / ".github" / "skills" / skill_name / "SKILL.md",
            content,
        )

    # Prompts
    for prompt_file in get_source_files("prompts"):
        content = read_file(prompt_file)
        write_file(output_dir / ".github" / "prompts" / prompt_file.name, content)

    # Copy template README
    template_readme = TEMPLATES_DIR / "copilot" / "README.md"
    if template_readme.exists():
        write_file(output_dir / ".github" / "EXPORT-INFO.md", read_file(template_readme))


# ─────────────────────────────────────────────
# Export: Claude Code
# ─────────────────────────────────────────────

def export_claude(output_dir: Path):
    print("  Exportando para Claude Code...")

    # CLAUDE.md (workspace instructions with @imports)
    ws = read_file(SOURCE_DIR / "instructions" / "workspace.md")
    body = strip_frontmatter(ws)
    imports = "\n## Documentación Referenciada\n\n"
    imports += "Los agentes y reglas están en `.claude/rules/` y `.claude/agents/`.\n"
    imports += "La documentación del proyecto está en `docs/`.\n"
    write_file(output_dir / "CLAUDE.md", body + "\n" + imports)

    # Rules -> .claude/rules/*.md
    for rule_file in get_source_files("rules"):
        content = read_file(rule_file)
        fm = extract_frontmatter(content)
        body = strip_frontmatter(content)
        # Claude uses 'paths' instead of 'applyTo'
        new_fm = ""  # No paths = always active
        write_file(
            output_dir / ".claude" / "rules" / rule_file.name,
            (new_fm + body) if new_fm else body,
        )

    # Agents -> .claude/agents/*.md
    for agent_dir in ["agents/negocio", "agents/tecnicos", "agents/vibe-coding"]:
        for agent_file in get_source_files(agent_dir):
            if agent_file.stem == "condicionales":
                continue
            content = read_file(agent_file)
            fm = extract_frontmatter(content)
            body = strip_frontmatter(content)
            new_fm = build_frontmatter({"description": fm.get("description", "")})
            write_file(
                output_dir / ".claude" / "agents" / agent_file.name,
                new_fm + body,
            )

    # Skills -> .claude/skills/*/SKILL.md
    for skill_md in get_skill_folders():
        skill_name = skill_md.parent.name
        content = read_file(skill_md)
        write_file(
            output_dir / ".claude" / "skills" / skill_name / "SKILL.md",
            content,
        )

    # Settings
    settings = '{\n  "permissions": {\n    "allow": ["read_file", "list_dir", "grep_search"],\n    "ask": ["write_file", "run_command"],\n    "deny": []\n  }\n}\n'
    write_file(output_dir / ".claude" / "settings.json", settings)


# ─────────────────────────────────────────────
# Export: Cursor
# ─────────────────────────────────────────────

def export_cursor(output_dir: Path):
    print("  Exportando para Cursor...")

    # AGENTS.md (workspace instructions)
    ws = read_file(SOURCE_DIR / "instructions" / "workspace.md")
    write_file(output_dir / "AGENTS.md", strip_frontmatter(ws))

    # Rules -> .cursor/rules/*.mdc (always-on)
    for rule_file in get_source_files("rules"):
        content = read_file(rule_file)
        fm = extract_frontmatter(content)
        body = strip_frontmatter(content)
        new_fm = build_frontmatter({
            "description": fm.get("description", ""),
            "alwaysApply": True,
        })
        name = rule_file.stem
        write_file(
            output_dir / ".cursor" / "rules" / f"{name}.mdc",
            new_fm + body,
        )

    # Agents -> .cursor/rules/*.mdc (model_decision)
    for agent_dir in ["agents/negocio", "agents/tecnicos", "agents/vibe-coding"]:
        for agent_file in get_source_files(agent_dir):
            if agent_file.stem == "condicionales":
                continue
            content = read_file(agent_file)
            fm = extract_frontmatter(content)
            body = strip_frontmatter(content)
            new_fm = build_frontmatter({
                "description": fm.get("description", ""),
                "alwaysApply": False,
            })
            write_file(
                output_dir / ".cursor" / "rules" / f"agente-{agent_file.stem}.mdc",
                new_fm + body,
            )


# ─────────────────────────────────────────────
# Export: Windsurf
# ─────────────────────────────────────────────

def export_windsurf(output_dir: Path):
    print("  Exportando para Windsurf...")

    # AGENTS.md
    ws = read_file(SOURCE_DIR / "instructions" / "workspace.md")
    write_file(output_dir / "AGENTS.md", strip_frontmatter(ws))

    # Rules -> .windsurf/rules/*.md (always_on)
    for rule_file in get_source_files("rules"):
        content = read_file(rule_file)
        fm = extract_frontmatter(content)
        body = strip_frontmatter(content)
        new_fm = build_frontmatter({
            "trigger": "always_on",
            "description": fm.get("description", ""),
        })
        write_file(
            output_dir / ".windsurf" / "rules" / rule_file.name,
            new_fm + body,
        )

    # Agents -> .windsurf/rules/*.md (model_decision)
    for agent_dir in ["agents/negocio", "agents/tecnicos", "agents/vibe-coding"]:
        for agent_file in get_source_files(agent_dir):
            if agent_file.stem == "condicionales":
                continue
            content = read_file(agent_file)
            fm = extract_frontmatter(content)
            body = strip_frontmatter(content)
            new_fm = build_frontmatter({
                "trigger": "model_decision",
                "description": fm.get("description", ""),
            })
            write_file(
                output_dir / ".windsurf" / "rules" / f"agente-{agent_file.stem}.md",
                new_fm + body,
            )

    # Skills -> .windsurf/skills/*/SKILL.md
    for skill_md in get_skill_folders():
        skill_name = skill_md.parent.name
        content = read_file(skill_md)
        write_file(
            output_dir / ".windsurf" / "skills" / skill_name / "SKILL.md",
            content,
        )


# ─────────────────────────────────────────────
# Export: Aider
# ─────────────────────────────────────────────

def export_aider(output_dir: Path):
    print("  Exportando para Aider...")

    # Aider has a limited context window: order by descending priority so the
    # most actionable content appears first in CONVENTIONS.md.
    # Priority: stack/conventions > security/quality > execution rules >
    #           vibe-coding agents > other agents > skills

    sections = []

    # 1. Workspace instructions (identity + flujo de trabajo obligatorio)
    ws = read_file(SOURCE_DIR / "instructions" / "workspace.md")
    sections.append(strip_frontmatter(ws))

    # 2. Rules — ordered by priority (vibe-coding → quality → security → others)
    RULE_PRIORITY = ["07-vibe-coding", "02-calidad", "06-validacion", "01-separacion",
                     "05-escalabilidad", "04-comunicacion", "03-formato"]
    rule_files_by_stem: dict[str, Path] = {
        f.stem: f for f in get_source_files("rules")
    }
    ordered_rules: list[Path] = (
        [rule_files_by_stem[s] for s in RULE_PRIORITY if s in rule_files_by_stem]
        + [f for f in get_source_files("rules") if f.stem not in RULE_PRIORITY]
    )
    sections.append("\n---\n\n# Reglas de Ejecución\n")
    for rule_file in ordered_rules:
        sections.append(strip_frontmatter(read_file(rule_file)))

    # 3. Agents — vibe-coding first (most relevant for coding sessions), then others
    sections.append("\n---\n\n# Agentes del Sistema\n")
    for agent_dir in ["agents/vibe-coding", "agents/negocio", "agents/tecnicos"]:
        for agent_file in get_source_files(agent_dir):
            if agent_file.stem == "condicionales":
                continue
            sections.append(strip_frontmatter(read_file(agent_file)))

    # 4. Skills — summarized as a single table of contents to preserve token budget
    sections.append("\n---\n\n# Skills Disponibles\n")
    for skill_md in get_skill_folders():
        content = read_file(skill_md)
        fm = extract_frontmatter(content)
        skill_name = skill_md.parent.name
        desc = fm.get("description", "")
        sections.append(f"- **{skill_name}** — {desc}")

    write_file(output_dir / "CONVENTIONS.md", "\n\n".join(sections))

    # .aider.conf.yml
    config = "read:\n  - CONVENTIONS.md\n"
    write_file(output_dir / ".aider.conf.yml", config)


# ─────────────────────────────────────────────
# Export: Continue.dev
# ─────────────────────────────────────────────

def export_continue(output_dir: Path):
    print("  Exportando para Continue.dev...")

    # Workspace instructions as rule 01
    ws = read_file(SOURCE_DIR / "instructions" / "workspace.md")
    fm = extract_frontmatter(ws)
    body = strip_frontmatter(ws)
    new_fm = build_frontmatter({
        "name": "workspace-instructions",
        "description": fm.get("description", ""),
        "alwaysApply": True,
    })
    write_file(output_dir / ".continue" / "rules" / "01-workspace.md", new_fm + body)

    # Rules -> .continue/rules/*.md
    idx = 2
    for rule_file in get_source_files("rules"):
        content = read_file(rule_file)
        fm = extract_frontmatter(content)
        body = strip_frontmatter(content)
        new_fm = build_frontmatter({
            "name": fm.get("name", rule_file.stem),
            "description": fm.get("description", ""),
            "alwaysApply": True,
        })
        write_file(
            output_dir / ".continue" / "rules" / f"{idx:02d}-{rule_file.stem}.md",
            new_fm + body,
        )
        idx += 1

    # Agents -> .continue/rules/*.md
    for agent_dir in ["agents/negocio", "agents/tecnicos", "agents/vibe-coding"]:
        for agent_file in get_source_files(agent_dir):
            if agent_file.stem == "condicionales":
                continue
            content = read_file(agent_file)
            fm = extract_frontmatter(content)
            body = strip_frontmatter(content)
            new_fm = build_frontmatter({
                "name": fm.get("name", agent_file.stem),
                "description": fm.get("description", ""),
                "alwaysApply": False,
            })
            write_file(
                output_dir / ".continue" / "rules" / f"agente-{agent_file.stem}.md",
                new_fm + body,
            )

    # config.yaml
    config = "# Continue.dev configuration\n# Adjust models per your preference\nmodels:\n  - name: default\n    provider: anthropic\n"
    write_file(output_dir / ".continue" / "config.yaml", config)


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────

EXPORTERS = {
    "copilot": export_copilot,
    "claude": export_claude,
    "cursor": export_cursor,
    "windsurf": export_windsurf,
    "aider": export_aider,
    "continue": export_continue,
}


def main():
    parser = argparse.ArgumentParser(
        description="Exportar el Creador de Entornos Iniciales al formato de una IA específica."
    )
    parser.add_argument(
        "--target",
        choices=TARGETS + ["all"],
        required=True,
        help="IA objetivo: copilot, claude, cursor, windsurf, aider, continue, all",
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Directorio de salida donde se generarán los archivos",
    )

    args = parser.parse_args()
    output_base = Path(args.output).resolve()

    # Guard: prevent exporting into the BASE-GENERATOR repo itself.
    # Exporting to SCRIPT_DIR or any subdirectory would overwrite .github/ and .claude/
    # files used by the AI (Copilot/Claude) to develop this project.
    try:
        output_base.relative_to(SCRIPT_DIR)
        print(
            f"\nERROR: El directorio de salida '{output_base}' está dentro del repositorio BASE-GENERATOR.\n"
            f"Exportar aquí sobreescribiría los archivos .github/ y .claude/ usados para desarrollar este proyecto.\n"
            f"Usa un directorio externo al repo. Ejemplo:\n"
            f"  python export.py --target {args.target} --output ../mi-proyecto\n"
        )
        sys.exit(1)
    except ValueError:
        pass  # output_base is outside SCRIPT_DIR — safe to proceed

    if args.target == "all":
        for target in TARGETS:
            out = output_base / target
            print(f"\n{'='*50}")
            print(f"  Target: {target}")
            print(f"  Output: {out}")
            print(f"{'='*50}")
            EXPORTERS[target](out)
        print(f"\nExportación completa. {len(TARGETS)} targets generados en {output_base}")
    else:
        print(f"\n{'='*50}")
        print(f"  Target: {args.target}")
        print(f"  Output: {output_base}")
        print(f"{'='*50}")
        EXPORTERS[args.target](output_base)
        print(f"\nExportación completa en {output_base}")


if __name__ == "__main__":
    main()
