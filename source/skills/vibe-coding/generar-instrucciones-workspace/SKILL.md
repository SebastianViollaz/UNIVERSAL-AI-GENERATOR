---
name: generar-instrucciones-workspace
description: "Genera el archivo de instrucciones del workspace (copilot-instructions.md, CLAUDE.md, etc.) con el contexto completo del negocio, stack, convenciones y glosario."
---

# Skill: generar_instrucciones_workspace

## Propósito
Genera el archivo maestro de instrucciones que la IA de codificación lee automáticamente al abrir el proyecto. Este archivo precarga el contexto de negocio, las convenciones técnicas y el glosario del dominio para que la IA genere código correcto desde el primer prompt.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `analisis_dominio` | object | Sí | Output de `analizar_dominio_negocio` |
| `arquitectura` | object | Sí | Output de `disenar_arquitectura_sistema` |
| `reglas_negocio` | object[] | Sí | Reglas formalizadas |
| `modelo_seguridad` | object | Sí | Restricciones de seguridad |
| `nombre_proyecto` | string | Sí | Nombre del proyecto |
| `stack` | object | Sí | Stack tecnológico elegido |
| `ia_objetivo` | string | Sí | IA para la que generar |

## Outputs

```yaml
instrucciones_workspace:
  archivo_principal:
    ruta: string       # .github/copilot-instructions.md, CLAUDE.md, etc.
    contenido: string
  glosario:
    ruta: string       # docs/glosario.md o inline
    contenido: string
    terminos: object[] # Lista de términos del dominio
```

## Estructura del Archivo Generado

```markdown
# {NOMBRE_PROYECTO} — Instrucciones para IA

## Sobre Este Proyecto
{descripcion_del_negocio_en_2_parrafos}

Rubro: {rubro}
Usuarios principales: {roles_usuario}
Problema que resuelve: {dolor_principal}

## Stack Tecnológico
- Backend: {backend} — elegido porque {justificacion}
- Frontend: {frontend} — elegido porque {justificacion}
- Base de datos: {db} — elegido porque {justificacion}
- Infraestructura: {infra}

## Convenciones de Código
### Naming
- Archivos: {convencion_archivos}
- Funciones: {convencion_funciones}
- Variables: {convencion_variables}
- Tablas BD: {convencion_tablas}

### Estructura del Proyecto
```
src/
├── modules/          # Un módulo por bounded context
│   ├── {modulo1}/
│   │   ├── domain/       # Entidades, value objects, reglas
│   │   ├── application/  # Use cases, services
│   │   ├── infrastructure/ # Repos, adapters
│   │   └── presentation/ # Controllers, DTOs
│   └── {modulo2}/
├── shared/           # Código compartido
└── config/           # Configuración
```

### Patrones a Seguir
- {patron_1}: usar para {caso_de_uso}
- {patron_2}: usar para {caso_de_uso}

### Patrones a EVITAR
- {antipatron_1}: porque {razon}
- {antipatron_2}: porque {razon}

## Glosario del Dominio
| Término | Significado | Dónde se usa en código |
|---------|------------|----------------------|
| {termino_1} | {definicion} | {modelo/tabla/variable} |
| {termino_2} | {definicion} | {modelo/tabla/variable} |

## Reglas de Negocio Críticas
Antes de implementar cualquier funcionalidad, verifica:
1. {regla_mas_importante}
2. {regla_segunda}
3. {regla_tercera}

Referencia completa: docs/negocio/reglas-negocio/

## Documentación Clave
- docs/negocio/procesos/ — Flujos de trabajo del negocio
- docs/negocio/reglas-negocio/ — Reglas formalizadas
- docs/tecnico/arquitectura/adr/ — Decisiones de arquitectura
- docs/tecnico/api/contratos.md — Contratos de API

## Agentes Disponibles
{lista_de_agentes_con_cuando_usarlos}
```

## Adaptaciones por IA

### GitHub Copilot
- Ruta: `.github/copilot-instructions.md`
- Sin frontmatter (Copilot no lo usa en instrucciones globales)
- Incluir referencia a los agentes como `@nombre-agente`

### Claude Code
- Ruta: `CLAUDE.md`
- Incluir `@import` virtual a `.claude/rules/` para referencia
- Formato conciso (Claude tiene límite de contexto por instrucciones)

### Cursor
- Ruta: `.cursor/rules/00-workspace.mdc`
- Frontmatter: `alwaysApply: true`
- Puede ser más extenso (Cursor inyecta reglas always-on eficientemente)

### Windsurf
- Ruta: `.windsurf/rules/00-workspace.md`
- Frontmatter: `trigger: always_on`

## Reglas Internas
1. El archivo debe ser comprensible por sí solo sin leer documentación adicional.
2. El glosario incluye SOLO términos que la IA podría confundir o usar incorrectamente.
3. Las convenciones de código son específicas al stack elegido, no genéricas.
4. Las reglas de negocio críticas se resumen en máximo 10 líneas — el detalle está en docs/.
5. Máximo 300 líneas para instrucciones de workspace (las IAs pierden contexto con textos largos).
