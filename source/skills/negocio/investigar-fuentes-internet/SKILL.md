---
name: investigar-fuentes-internet
description: "Investiga en internet información relevante sobre el dominio del proyecto usando fuentes confiables. Valida datos, regulaciones, benchmarks y tendencias del rubro."
---

# Skill: investigar_fuentes_internet

## Propósito
Investigar en internet información actualizada y verificable sobre el dominio del proyecto. Cada dato obtenido debe incluir la fuente original con URL, permitiendo trazabilidad y validación posterior.

## Cuándo Usar
- Al analizar un dominio de negocio nuevo o desconocido
- Al verificar regulaciones, normativas o estándares del sector
- Al buscar benchmarks, tendencias de mercado o referentes del rubro
- Al validar decisiones técnicas con documentación oficial
- Al investigar integraciones con servicios o APIs externas

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `tema` | string | Sí | Tema principal a investigar |
| `rubro` | string | Sí | Industria o sector del proyecto |
| `pais` | string | No | Jurisdicción para regulaciones locales |
| `profundidad` | enum | No | rapida, estandar, exhaustiva (default: estandar) |
| `tipo_busqueda` | enum | No | regulacion, benchmark, tendencia, tecnologia, competencia |

## Outputs

```yaml
investigacion:
  tema: string
  fecha_consulta: string  # ISO 8601
  hallazgos:
    - titulo: string
      resumen: string
      fuente:
        nombre: string    # Nombre del sitio/organización
        url: string       # URL directa al contenido
        tipo: enum[oficial, academico, industria, periodismo, comunidad]
        confiabilidad: enum[alta, media, baja]
      relevancia: enum[critica, alta, media, baja]
      fecha_publicacion: string  # Si está disponible
  regulaciones_encontradas:
    - nombre: string
      jurisdiccion: string
      url_oficial: string
      impacto_en_proyecto: string
  fuentes_descartadas:
    - url: string
      motivo: string      # Por qué no se consideró confiable
  recomendaciones:
    - accion: string
      basada_en: string   # Referencia al hallazgo
```

## Fuentes Confiables por Categoría

### Regulaciones y Normativas
- Sitios `.gov`, `.gob` del país correspondiente
- EUR-Lex (regulaciones europeas)
- Boletines oficiales del estado
- Organismos reguladores del sector (CNBV, SAT, FDA, HIPAA, GDPR portales oficiales)

### Tecnología y Arquitectura
- Documentación oficial de frameworks y lenguajes (docs.python.org, react.dev, etc.)
- RFC (rfc-editor.org) para estándares de internet
- OWASP (owasp.org) para seguridad
- ThoughtWorks Technology Radar
- Martin Fowler (martinfowler.com) para patrones de arquitectura
- 12factor.net para diseño de aplicaciones

### Negocio e Industria
- Reportes de Gartner, Forrester, McKinsey (resúmenes públicos)
- Statista para estadísticas de mercado
- Crunchbase para datos de competidores y startups
- Informes sectoriales de cámaras de comercio
- Harvard Business Review (artículos públicos)

### Estándares y Mejores Prácticas
- ISO (iso.org) para estándares internacionales
- IEEE para estándares técnicos
- W3C para estándares web y accesibilidad (WCAG)
- NIST para ciberseguridad
- PCI DSS (pcisecuritystandards.org) para pagos

### Académico y Investigación
- Google Scholar (scholar.google.com)
- arXiv para papers de CS/ML
- ACM Digital Library
- ResearchGate (resúmenes públicos)

## Reglas de Investigación

1. **Toda afirmación debe tener fuente.** No incluir datos sin URL verificable.
2. **Priorizar fuentes oficiales** sobre blogs o foros. Orden: oficial > académico > industria > periodismo > comunidad.
3. **Verificar vigencia.** Descartar fuentes con más de 3 años para tecnología, 2 años para regulaciones (salvo leyes vigentes).
4. **Cruzar mínimo 2 fuentes** para datos críticos (regulaciones, cifras de mercado).
5. **Documentar fuentes descartadas** con el motivo de exclusión.
6. **No fabricar URLs.** Solo incluir URLs reales verificadas con `fetch_webpage`.
7. **Señalar incertidumbre.** Si un dato no se pudo verificar, marcarlo como `confiabilidad: baja`.

## Proceso

1. **Identificar temas de búsqueda** — Descomponer el tema en queries específicas
2. **Buscar en fuentes oficiales** — Empezar siempre por documentación oficial y sitios `.gov`
3. **Buscar en fuentes de industria** — Complementar con reportes y benchmarks del sector
4. **Verificar cruzado** — Contrastar datos críticos entre al menos 2 fuentes independientes
5. **Documentar hallazgos** — Registrar cada fuente con URL, tipo y nivel de confiabilidad
6. **Descartar fuentes dudosas** — Documentar por qué se excluyeron
7. **Sintetizar** — Generar resumen accionable con recomendaciones trazables a fuentes

## Ejemplo

**Input:**
```yaml
tema: "regulaciones de facturación electrónica"
rubro: "retail"
pais: "México"
profundidad: estandar
tipo_busqueda: regulacion
```

**Output (fragmento):**
```yaml
investigacion:
  tema: "regulaciones de facturación electrónica en retail México"
  fecha_consulta: "2025-01-15"
  hallazgos:
    - titulo: "CFDI 4.0 — Comprobante Fiscal Digital por Internet"
      resumen: "Desde enero 2023, todo comprobante fiscal debe emitirse en versión 4.0 del CFDI con nombre y domicilio del receptor"
      fuente:
        nombre: SAT — Servicio de Administración Tributaria
        url: "https://www.sat.gob.mx/consultas/43074/actualizacion-factura-electronica"
        tipo: oficial
        confiabilidad: alta
      relevancia: critica
  regulaciones_encontradas:
    - nombre: "CFDI 4.0"
      jurisdiccion: "México federal"
      url_oficial: "https://www.sat.gob.mx/..."
      impacto_en_proyecto: "El módulo de facturación DEBE generar CFDI 4.0 con timbrado PAC"
```
