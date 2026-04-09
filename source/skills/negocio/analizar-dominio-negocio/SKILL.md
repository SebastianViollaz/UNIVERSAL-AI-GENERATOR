---
name: analizar-dominio-negocio
description: "Desglosa la descripción de alto nivel del proyecto en componentes de negocio: rubro, procesos, roles, regulaciones, KPIs y oportunidades de mejora."
---

# Skill: analizar_dominio_negocio

## Propósito
Desglosa la descripción de alto nivel del proyecto en sus componentes de negocio fundamentales. Identifica el rubro, los procesos clave, los actores involucrados, las regulaciones aplicables y las oportunidades de mejora. Es la primera skill que se ejecuta y alimenta a todas las demás.

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `descripcion_proyecto` | string | Sí | Descripción libre del proyecto |
| `contexto_adicional` | string | No | País, tamaño de empresa, limitaciones |
| `industria_especifica` | string | No | Sector exacto si se conoce |

## Outputs

```yaml
analisis_dominio:
  rubro: string
  sub_rubro: string
  modelo_negocio:
    tipo: enum[B2B, B2C, B2B2C, marketplace, SaaS, interno]
    descripcion: string
    fuentes_ingreso: string[]
  procesos_principales:
    - nombre: string
      descripcion: string
      actores: string[]
      frecuencia: enum[continuo, diario, semanal, mensual, eventual]
      criticidad: enum[critica, alta, media, baja]
      dolor_actual: string
      mejora_propuesta: string
  roles_usuario:
    - nombre: string
      descripcion: string
      permisos_clave: string[]
      flujos_principales: string[]
  regulaciones_aplicables:
    - nombre: string
      jurisdiccion: string
      impacto_en_sistema: string
  integraciones_externas:
    - sistema: string
      tipo: enum[API, archivo, manual, webhook]
      criticidad: enum[critica, alta, media, baja]
  kpis_negocio:
    - nombre: string
      formula: string
      frecuencia_medicion: string
      objetivo: string
  riesgos_negocio:
    - riesgo: string
      probabilidad: enum[alta, media, baja]
      impacto: enum[alto, medio, bajo]
      mitigacion: string
  referentes_mercado:
    - nombre: string
      tipo: enum[competidor_directo, referente_industria, producto_alternativo]
      diferenciador_vs_este_proyecto: string
  oportunidades_quick_wins:
    - oportunidad: string
      impacto_estimado: enum[alto, medio, bajo]
      esfuerzo_estimado: enum[alto, medio, bajo]
      proceso_relacionado: string
  preguntas_clarificacion:
    - pregunta: string
      campo_afectado: string
      urgencia: enum[bloquea_analisis, mejora_calidad, opcional]
  fuentes_consultadas:
    - nombre: string
      url: string
      tipo: enum[oficial, academico, industria, periodismo, comunidad]
      dato_obtenido: string
```

## Reglas Internas
1. Nunca asumir procesos genéricos. Investigar particularidades del rubro usando `fetch_webpage` en fuentes confiables (sitios .gov, cámaras de comercio, reguladores sectoriales).
2. Si la descripción tiene menos de 100 palabras o faltan campos críticos, poblar `preguntas_clarificacion` antes de continuar con el análisis.
3. Siempre identificar al menos 3 procesos principales y elevar las mejoras a `oportunidades_quick_wins`.
4. Los KPIs deben ser medibles y relevantes para el tamaño de empresa descrito.
5. Incluir mínimo 2 referentes de mercado para guiar decisiones de UX y features.
6. Las regulaciones deben verificarse en fuentes oficiales (.gov/.gob, portales de reguladores). Incluir URL de la fuente.
7. Los referentes de mercado deben investigarse en fuentes de industria (Crunchbase, Statista, reportes sectoriales). Incluir URL.
8. Toda afirmación sobre el sector, cifra o regulación citada debe tener fuente verificable con URL.
