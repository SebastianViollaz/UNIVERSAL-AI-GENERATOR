# SKILLS — Dominio Técnico

Skills orientadas a diseñar la arquitectura, el stack tecnológico y los agentes técnicos del proyecto.

---

## Skill: `estructurar_agentes_tecnicos`

### Descripción
A partir del análisis del dominio y los agentes de negocio diseñados, define qué roles técnicos (programación, arquitectura, DevOps, QA, seguridad) se necesitan, sus responsabilidades y cómo se coordinan entre sí y con los agentes de negocio.

### Inputs
| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `analisis_dominio` | object | Sí | Output de `analizar_dominio_negocio` |
| `agentes_negocio` | object[] | Sí | Output de `disenar_agentes_negocio` |
| `stack_preferido` | object | No | Tecnologías que el programador prefiere o requiere |
| `restricciones_infra` | string[] | No | Limitaciones de infraestructura (ej. "solo AWS", "on-premise") |

### Outputs
```yaml
agentes_tecnicos:
  - nombre: string                       # Ej: "Arquitecto de Backend"
    identificador: string                # Ej: "agente-backend-arch"
    rol: string
    stack_tecnologico:
      - tecnologia: string
        version: string
        justificacion: string            # Por qué esta tecnología y no otra
    responsabilidades: string[]
    patrones_que_aplica:
      - patron: string
        contexto: string                 # En qué parte del sistema se aplica
        justificacion: string
    estandares_que_sigue:
      - estandar: string
        referencia: string               # Link o documento de referencia
    decisiones_arquitectura:
      - decision: string
        alternativas_consideradas: string[]
        justificacion: string
        consecuencias: string[]
    inputs_que_necesita:
      - fuente: string
        dato: string
    outputs_que_genera:
      - destino: string
        dato: string
    interactua_con:
      - agente: string
        tipo_interaccion: string
        frecuencia: string
    capacidades_tecnicas_profundas:      # Nivel de detalle técnico del agente
      - area: string
        conocimientos: string[]
        puede_decidir: string[]
        debe_consultar: string[]
    prompt_base: string                  # Prompt que define la personalidad del agente
```

### Reglas Internas
1. Mínimo 4 agentes técnicos: arquitecto, backend, frontend, QA/testing.
2. Si el proyecto involucra datos sensibles, agregar un agente de seguridad.
3. Si hay integraciones externas complejas, agregar un agente de integraciones.
4. Cada agente técnico debe tener al menos un agente de negocio como contraparte.
5. Las justificaciones del stack deben ser técnicas Y de negocio.

---

## Skill: `disenar_arquitectura_sistema`

### Descripción
Define la arquitectura del sistema a nivel macro y micro. Produce diagramas conceptuales (en texto), decisiones de arquitectura documentadas (ADRs), y la estructura de módulos/servicios.

### Inputs
| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `analisis_dominio` | object | Sí | Output de `analizar_dominio_negocio` |
| `procesos_detallados` | object[] | Sí | Output de `mapear_procesos_negocio` |
| `agentes_tecnicos` | object[] | Sí | Output de `estructurar_agentes_tecnicos` |
| `plan_escalabilidad` | object | Sí | Output de `analizar_escalabilidad_negocio` |
| `requisitos_no_funcionales` | object | No | Performance, disponibilidad, etc. |

### Outputs
```yaml
arquitectura:
  estilo: string                         # Ej: "Monolito modular", "Microservicios", "Serverless"
  justificacion_estilo: string
  diagrama_alto_nivel: string            # Descripción textual/Mermaid del diagrama
  modulos:
    - nombre: string
      responsabilidad: string
      procesos_negocio_que_cubre: string[]
      bounded_context: string            # En términos de DDD
      entidades_principales: string[]
      servicios_expuestos: string[]
      dependencias: string[]
      agente_negocio_responsable: string
      agente_tecnico_responsable: string
  capas:
    - nombre: string                     # Ej: "Presentación", "Aplicación", "Dominio", "Infraestructura"
      responsabilidad: string
      tecnologias: string[]
      reglas: string[]
  adrs:                                  # Architecture Decision Records
    - id: string                         # Ej: "ADR-001"
      titulo: string
      estado: enum[propuesto, aceptado, rechazado, deprecado]
      contexto: string
      decision: string
      alternativas: string[]
      consecuencias_positivas: string[]
      consecuencias_negativas: string[]
      relacion_negocio: string           # Qué requerimiento de negocio justifica esta decisión
  modelo_datos_conceptual:
    entidades:
      - nombre: string
        atributos_clave: string[]
        relaciones: string[]
        reglas_negocio_asociadas: string[]
    diagrama_er: string                  # Descripción textual/Mermaid
  estrategia_api:
    estilo: enum[REST, GraphQL, gRPC, mixto]
    justificacion: string
    versionado: string
    autenticacion: string
    rate_limiting: string
  requisitos_no_funcionales:
    performance:
      tiempo_respuesta_objetivo: string
      concurrencia_esperada: string
      estrategia: string
    disponibilidad:
      sla_objetivo: string
      estrategia_failover: string
    seguridad:
      modelo_autenticacion: string
      modelo_autorizacion: string
      cifrado: string
      compliance: string[]
```

### Reglas Internas
1. Cada ADR debe estar vinculado a un requerimiento de negocio.
2. La arquitectura debe soportar las fases de escalabilidad definidas.
3. Monolito modular es el default para proyectos pequeños/medianos; justificar si se elige otra cosa.
4. El modelo de datos debe reflejar las entidades del dominio de negocio, no las tablas técnicas.

---

## Skill: `definir_estrategia_testing`

### Descripción
Diseña la estrategia completa de testing del proyecto, alineada con los riesgos del negocio y los procesos críticos identificados.

### Inputs
| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `procesos_detallados` | object[] | Sí | Output de `mapear_procesos_negocio` |
| `reglas_negocio` | object[] | Sí | Output de `formalizar_reglas_negocio` |
| `arquitectura` | object | Sí | Output de `disenar_arquitectura_sistema` |
| `plan_escalabilidad` | object | No | Para tests de carga futuros |

### Outputs
```yaml
estrategia_testing:
  piramide:
    unitarios:
      porcentaje_cobertura_objetivo: string
      enfoque: string
      frameworks: string[]
    integracion:
      porcentaje_cobertura_objetivo: string
      enfoque: string
      frameworks: string[]
    e2e:
      porcentaje_cobertura_objetivo: string
      enfoque: string
      frameworks: string[]
  prioridad_testing:                     # Qué se testea primero basado en riesgo de negocio
    - proceso: string
      riesgo_negocio: enum[critico, alto, medio, bajo]
      tipo_test_requerido: string[]
      escenarios_criticos:
        - escenario: string
          dato_entrada: string
          resultado_esperado: string
          regla_negocio_validada: string
  testing_no_funcional:
    performance:
      herramientas: string[]
      escenarios: string[]
    seguridad:
      herramientas: string[]
      checklist: string[]
    accesibilidad:
      estandar: string
      herramientas: string[]
  estrategia_ci:
    cuando_ejecutar: string
    gates_de_calidad: string[]
    tiempo_maximo_pipeline: string
```

### Reglas Internas
1. Los procesos críticos del negocio deben tener cobertura E2E completa.
2. Cada regla de negocio formalizada debe tener al menos un test asociado.
3. Los tests de seguridad son obligatorios si hay datos personales o financieros.
4. La estrategia debe ser pragmática: priorizar por riesgo de negocio, no por cobertura numérica.

---

## Skill: `disenar_seguridad_sistema`

### Descripción
Analiza los requerimientos de seguridad desde la perspectiva del negocio (datos sensibles, regulaciones, confidencialidad) y la técnica (autenticación, autorización, cifrado, OWASP).

### Inputs
| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `analisis_dominio` | object | Sí | Output de `analizar_dominio_negocio` |
| `arquitectura` | object | Sí | Output de `disenar_arquitectura_sistema` |
| `roles_usuario` | object[] | Sí | Roles y permisos del análisis de dominio |
| `regulaciones` | object[] | No | Regulaciones aplicables |

### Outputs
```yaml
modelo_seguridad:
  clasificacion_datos:
    - tipo_dato: string
      nivel_sensibilidad: enum[publico, interno, confidencial, restringido]
      regulacion_aplicable: string
      cifrado_requerido: boolean
      retencion: string
      procedimiento_eliminacion: string
  autenticacion:
    metodo: string
    mfa_requerido: boolean
    politica_passwords: string
    sesion: string
    proveedor: string
  autorizacion:
    modelo: enum[RBAC, ABAC, mixto]
    roles:
      - rol: string
        permisos: string[]
        restricciones: string[]
    reglas_especiales: string[]
  amenazas:                              # Threat modeling simplificado
    - amenaza: string
      vector: string
      impacto: enum[critico, alto, medio, bajo]
      probabilidad: enum[alta, media, baja]
      mitigacion: string
      owasp_categoria: string
  checklist_owasp:
    - categoria: string
      controles: string[]
      implementacion: string
  compliance:
    - regulacion: string
      requerimientos: string[]
      como_se_cumple: string[]
  plan_respuesta_incidentes:
    pasos: string[]
    responsables: string[]
    comunicacion: string
```

### Reglas Internas
1. Si hay datos personales, GDPR/ley de protección de datos local es obligatoria.
2. Siempre modelar al menos 5 amenazas del OWASP Top 10.
3. El modelo de autorización debe reflejar exactamente los roles de negocio.
4. Definir plan de respuesta a incidentes mínimo si hay datos financieros o de salud.

---

## Skill: `planificar_infraestructura`

### Descripción
Define la estrategia de infraestructura, deployment y operaciones (CI/CD, monitoring, logging) alineada con el plan de escalabilidad del negocio.

### Inputs
| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `arquitectura` | object | Sí | Output de `disenar_arquitectura_sistema` |
| `plan_escalabilidad` | object | Sí | Output de `analizar_escalabilidad_negocio` |
| `restricciones_infra` | string[] | No | Limitaciones del cliente |
| `presupuesto` | string | No | Rango de presupuesto para infra |

### Outputs
```yaml
infraestructura:
  ambiente_desarrollo:
    setup: string[]
    herramientas: string[]
    docker_compose: boolean
  ambiente_staging:
    proveedor: string
    servicios: string[]
    acceso: string
  ambiente_produccion:
    proveedor: string
    servicios: string[]
    alta_disponibilidad: string
    backup: string
    disaster_recovery: string
  ci_cd:
    plataforma: string
    pipeline_stages: string[]
    gates_de_calidad: string[]
    deploy_strategy: enum[blue_green, canary, rolling, recreate]
    tiempo_rollback: string
  monitoring:
    metricas_tecnicas: string[]
    metricas_negocio: string[]           # KPIs del negocio monitoreados en tiempo real
    alertas: string[]
    herramientas: string[]
  logging:
    estrategia: string
    retencion: string
    herramientas: string[]
  costos_estimados:
    mvp: string
    crecimiento_fase_1: string
    crecimiento_fase_2: string
```

### Reglas Internas
1. Siempre incluir métricas de negocio en el monitoring, no solo técnicas.
2. El plan de disaster recovery debe existir si la criticidad del negocio es alta.
3. Los costos deben alinearse con las fases de escalabilidad del negocio.
4. Docker es el default para ambientes de desarrollo; justificar si se omite.
