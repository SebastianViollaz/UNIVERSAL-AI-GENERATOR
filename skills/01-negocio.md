# SKILLS — Dominio de Negocio

Skills orientadas a comprender, modelar y profundizar en la lógica del negocio del proyecto.

---

## Skill: `analizar_dominio_negocio`

### Descripción
Desglosa la descripción de alto nivel del proyecto en sus componentes de negocio fundamentales. Identifica el rubro, los procesos clave, los actores involucrados, las regulaciones aplicables y las oportunidades de mejora. Esta es la primera skill que se ejecuta y alimenta a todas las demás.

### Inputs
| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `descripcion_proyecto` | string | Sí | Descripción libre del proyecto (ej. "ERP para empresa familiar de manufactura") |
| `contexto_adicional` | string | No | Información extra: país, tamaño de empresa, limitaciones conocidas |
| `industria_especifica` | string | No | Si se conoce, el sector exacto (NAICS, ISIC o descripción libre) |

### Outputs
```yaml
analisis_dominio:
  rubro: string                          # Industria identificada
  sub_rubro: string                      # Nicho específico dentro de la industria
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
      dolor_actual: string               # Punto de dolor que el software debe resolver
      mejora_propuesta: string            # Cómo el sistema puede mejorar este proceso
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
      descripcion: string
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
```

### Reglas Internas
1. Nunca asumas procesos genéricos. Investiga las particularidades del rubro.
2. Si la descripción es vaga, genera preguntas de clarificación antes del análisis.
3. Siempre identifica al menos 3 procesos principales y 2 oportunidades de mejora.
4. Los KPIs deben ser medibles y relevantes para el tamaño de empresa descrito.

---

## Skill: `disenar_agentes_negocio`

### Descripción
A partir del análisis del dominio, diseña los agentes de negocio especializados que actuarán como consultores virtuales del dominio. Cada agente es un experto en un área específica del negocio y puede proponer mejoras, validar requerimientos y guiar decisiones.

### Inputs
| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `analisis_dominio` | object | Sí | Output de `analizar_dominio_negocio` |
| `prioridades_cliente` | string[] | No | Áreas que el cliente considera prioritarias |
| `presupuesto_estimado` | string | No | Rango de presupuesto para calibrar la complejidad |

### Outputs
```yaml
agentes_negocio:
  - nombre: string                       # Ej: "Especialista en Cadena de Suministro"
    identificador: string                # Ej: "agente-supply-chain"
    rol: string                          # Descripción de su expertise
    dominio_expertise:
      - area: string
        nivel: enum[experto, avanzado, intermedio]
        conocimientos_especificos: string[]
    responsabilidades: string[]
    capacidades_propositivas:            # Qué mejoras puede proponer al negocio
      - area: string
        tipo_mejora: enum[optimizacion, automatizacion, nueva_funcionalidad, reduccion_riesgo]
        descripcion: string
    decisiones_que_toma: string[]
    decisiones_que_escala: string[]      # Qué decisiones delega a otros agentes
    inputs_que_necesita:
      - fuente: string
        dato: string
        formato: string
    outputs_que_genera:
      - destino: string
        dato: string
        formato: string
    interactua_con: string[]
    criterios_exito: string[]
    preguntas_clave:                     # Preguntas que este agente debe hacer al cliente
      - pregunta: string
        por_que_importa: string
    prompt_base: string                  # Prompt que define la personalidad del agente
```

### Reglas Internas
1. Mínimo 3 agentes de negocio por proyecto, sin importar su tamaño.
2. Siempre incluir un "Agente Estratega de Negocio" que piense en escalabilidad.
3. Cada agente debe tener capacidades propositivas: no solo describen, también mejoran.
4. Los agentes deben cubrir: operaciones, finanzas/métricas, y experiencia de usuario como mínimo.

---

## Skill: `mapear_procesos_negocio`

### Descripción
Toma los procesos identificados en el análisis del dominio y los detalla en flujos completos con estados, decisiones, excepciones y métricas. Produce documentación que sirve como especificación funcional para los agentes técnicos.

### Inputs
| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `procesos_principales` | object[] | Sí | Lista de procesos del análisis del dominio |
| `roles_usuario` | object[] | Sí | Roles de usuario identificados |
| `reglas_negocio` | object[] | No | Reglas de negocio ya formalizadas |

### Outputs
```yaml
procesos_detallados:
  - nombre: string
    identificador: string
    version: string
    estado: enum[borrador, validado, en_revision]
    descripcion: string
    trigger: string                      # Qué inicia el proceso
    precondiciones: string[]
    postcondiciones: string[]
    actores:
      - rol: string
        tipo: enum[primario, secundario, sistema]
    flujo_principal:
      - paso: number
        actor: string
        accion: string
        sistema_responde: string
        datos_involucrados: string[]
    flujos_alternativos:
      - nombre: string
        desde_paso: number
        condicion: string
        pasos: object[]
    excepciones:
      - nombre: string
        condicion: string
        manejo: string
    reglas_negocio_aplicables:
      - regla: string
        descripcion: string
        validacion: string               # Cómo se verifica que se cumple
    metricas:
      - nombre: string
        que_mide: string
        valor_objetivo: string
    dependencias:
      - proceso: string
        tipo: enum[precede, sucede, paralelo]
```

### Reglas Internas
1. Todo proceso debe tener al menos un flujo alternativo y una excepción.
2. Cada paso debe especificar qué datos se crean, leen, actualizan o eliminan.
3. Las reglas de negocio deben ser atómicas y testeables.
4. Incluir métricas que permitan medir la eficiencia del proceso.

---

## Skill: `analizar_escalabilidad_negocio`

### Descripción
Evalúa el potencial de crecimiento del negocio y diseña las fases de evolución que el sistema debe soportar. Piensa más allá del MVP: proyecta cómo el negocio puede evolucionar y qué capacidades técnicas se necesitarán.

### Inputs
| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `analisis_dominio` | object | Sí | Output de `analizar_dominio_negocio` |
| `agentes_negocio` | object[] | Sí | Agentes de negocio diseñados |
| `horizonte_temporal` | string | No | Período de proyección (default: "3 años") |

### Outputs
```yaml
plan_escalabilidad:
  fase_mvp:
    duracion_estimada: string
    funcionalidades_core: string[]
    procesos_cubiertos: string[]
    usuarios_esperados: string
    volumen_datos_estimado: string
  fases_crecimiento:
    - nombre: string
      trigger_de_fase: string            # Qué evento o métrica activa esta fase
      nuevas_funcionalidades: string[]
      nuevos_procesos: string[]
      nuevas_integraciones: string[]
      impacto_arquitectura: string       # Qué cambia a nivel técnico
      agentes_nuevos_requeridos: string[]
      riesgos: string[]
  oportunidades_futuras:
    - oportunidad: string
      viabilidad: enum[alta, media, baja]
      prerequisitos: string[]
      impacto_revenue: enum[alto, medio, bajo]
  decisiones_arquitectura_preventivas:   # Decisiones técnicas a tomar HOY para el futuro
    - decision: string
      justificacion: string
      costo_si_se_pospone: string
```

### Reglas Internas
1. Siempre proyectar mínimo 3 fases de crecimiento.
2. Cada fase debe tener un trigger medible, no basado en tiempo arbitrario.
3. Las decisiones preventivas deben balancear costo actual vs. deuda técnica futura.
4. Considerar pivotes de negocio realistas según el rubro.

---

## Skill: `formalizar_reglas_negocio`

### Descripción
Transforma las reglas de negocio implícitas en especificaciones formales, atómicas y testeables que los agentes técnicos puedan implementar directamente.

### Inputs
| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `procesos_detallados` | object[] | Sí | Output de `mapear_procesos_negocio` |
| `regulaciones` | object[] | No | Regulaciones aplicables |
| `analisis_dominio` | object | Sí | Output de `analizar_dominio_negocio` |

### Outputs
```yaml
reglas_negocio:
  - id: string                           # Ej: "RN-FACT-001"
    nombre: string
    categoria: enum[validacion, calculo, restriccion, autorizacion, notificacion, workflow]
    descripcion: string
    condicion: string                    # Expresión lógica legible
    accion: string                       # Qué ocurre cuando se cumple
    excepcion: string                    # Qué ocurre en caso contrario
    procesos_afectados: string[]
    datos_involucrados: string[]
    fuente: string                       # De dónde viene esta regla (regulación, requisito, etc.)
    prioridad: enum[obligatoria, recomendada, opcional]
    criterio_test: string                # Cómo se prueba que la regla funciona
    ejemplos:
      - caso: string
        input: string
        resultado_esperado: string
```

### Reglas Internas
1. Cada regla debe tener al menos un ejemplo concreto.
2. Las reglas deben ser independientes entre sí (atómicas).
3. El criterio de test debe ser ejecutable, no ambiguo.
4. Priorizar reglas que provienen de regulaciones legales.
