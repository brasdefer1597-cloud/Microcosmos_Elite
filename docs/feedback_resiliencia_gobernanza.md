# Diseño de loops de retroalimentación, seguridad, resiliencia y gobernanza

## Alcance y supuestos mínimos
- Este documento propone **lineamientos incrementales** sobre componentes ya presentes en el repositorio (telemetría JSONL, scripts operativos, motor de ejecución, dashboard).
- **No se asume** entrenamiento online complejo ni una plataforma MLOps completa; donde falten piezas, se propone una versión mínima y operable.
- Supuestos razonables:
  1. `data/telemetry.jsonl` es la fuente primaria de eventos operativos.
  2. Existen procesos batch (`scripts/*`) y una visualización en frontend (`deploy/src/App.tsx`).
  3. El sistema puede incorporar reglas adaptativas antes de introducir modelos de ML.

---

## 4) Diseño de retroalimentación usuario↔máquina (feedback loops)

### 4.1 Loop canónico recomendado
Se define el ciclo principal:

1. **Usuario → Interacción**
   - Entradas directas: comandos, acciones UI, activación de workflows.
   - Entradas indirectas: tiempo de permanencia, reintentos, abandono, correcciones manuales.

2. **Adquisición (logging / telemetría)**
   - Registrar eventos estructurados en JSONL con `timestamp`, `trace_id`, `user/session_id`, `componente`, `acción`, `resultado`, `latencia_ms`, `error_code`.
   - Redactar datos sensibles (PII/tokens) antes de persistir.

3. **Procesamiento**
   - **Streaming ligero** para alertas rápidas (errores, latencia alta, degradación).
   - **Batch periódico** (cada 15 min / 1h) para agregados: tasa de éxito, calidad, engagement.

4. **Ajuste del sistema**
   - Ajustes automáticos de bajo riesgo:
     - thresholds de timeout,
     - rate limiting dinámico,
     - backoff por proveedor externo,
     - fallback de rutas críticas.
   - Ajustes humanos para cambios de alto impacto:
     - actualización de reglas de negocio,
     - cambios de scoring/calidad,
     - cambios de prompts o parámetros globales.

5. **Retroalimentación al usuario**
   - Mensajes explícitos de estado: `procesando`, `degradado`, `reintento`, `completado con fallback`.
   - Transparencia mínima: razón del fallback y siguiente acción sugerida.

---

### 4.2 Métricas y telemetría a recolectar

#### A) Performance y confiabilidad
- `latency_p50/p95/p99_ms`
- `throughput_rps` (o eventos/min)
- `error_rate_total` y `error_rate_por_componente`
- `timeout_rate`
- `retry_count_promedio`
- `fallback_activation_rate`

#### B) Calidad de salida
- `output_acceptance_rate` (resultado aceptado sin edición)
- `manual_correction_rate`
- `regeneration_rate` (cuántas veces se rehace una salida)
- `quality_score` (heurístico 0-1 o 0-100)

#### C) Satisfacción y engagement
- `thumbs_up/down` o feedback explícito binario
- `session_length`
- `task_completion_rate`
- `return_rate` (usuarios que regresan)

#### D) Gobernanza operativa
- `config_version`, `model_version`, `ruleset_version`
- `schema_version` del evento
- `deployment_id` para correlacionar incidentes con releases

---

### 4.3 Mecanismos automáticos vs. HITL (human-in-the-loop)

#### Automáticos (rápidos, bajo riesgo)
- Autoajuste de timeouts por percentiles de latencia recientes.
- Activación de backoff exponencial con jitter ante 429/5xx.
- Enrutamiento a fallback cuando se supera umbral de error.
- Rate limiting por usuario/session para proteger estabilidad.

#### Humanos (decisiones de alto impacto)
- Revisión de muestras de baja calidad o alto riesgo.
- Aprobación de cambios de reglas antes de promover a producción.
- Curación de dataset para reentrenamientos.
- Postmortem de incidentes (SRE + producto + seguridad).

Regla práctica:
- **Automático** si reversible y acotado.
- **HITL** si cambia comportamiento global, compliance o experiencia crítica.

---

### 4.4 Estrategias de control adaptativo

1. **Bandas de tolerancia**
   - Verde: `error_rate < 1%` y `p95 < objetivo`.
   - Amarillo: `1–3%` o p95 degradado → habilitar medidas conservadoras.
   - Rojo: `>3%` sostenido → degradación controlada + alerta.

2. **Thresholds con histéresis**
   - Entrar a modo degradado en 3%.
   - Salir de modo degradado recién al bajar de 1.5% durante ventana sostenida.
   - Evita “flapping” operativo.

3. **Backoff + retry inteligente**
   - Exponencial + jitter aleatorio.
   - Límite máximo de retries y budget de latencia por request.

4. **Rate limiting dinámico**
   - Límites por IP/API-key/session.
   - Endurecimiento temporal cuando hay saturación o abuso.

5. **Control por presupuesto de error (error budget)**
   - Si se consume rápido el budget mensual, congelar cambios riesgosos y priorizar estabilidad.

---

### 4.5 Pipelines de datos para modelos o reglas

#### Pipeline mínimo recomendado
- **Ingesta**: eventos JSONL (`data/telemetry.jsonl`) + logs auxiliares.
- **ETL batch** (job horario):
  - validación de esquema,
  - limpieza de campos nulos/anómalos,
  - anonimización/redacción,
  - agregados por ventana temporal.
- **Data mart operacional**:
  - tabla `kpi_hourly`,
  - tabla `incidents`,
  - tabla `quality_feedback`.
- **Consumo**:
  - dashboard operativo,
  - reglas adaptativas,
  - datasets curados para reentrenamiento offline.

#### Streaming (cuando aplique)
- Canal de eventos para alertas en casi tiempo real:
  - picos de latencia,
  - aumento de 5xx,
  - caída de aceptación.
- Mantener batch como fuente de verdad para análisis histórico y auditoría.

---

## 5) Seguridad, resiliencia y gobernanza

### 5.1 Riesgos de seguridad clave y mitigaciones

1. **Exposición de secretos**
   - Riesgo: tokens/API keys en scripts o logs.
   - Mitigación:
     - usar variables de entorno/secret manager,
     - escaneo de secretos en CI,
     - redacción automática en logs.

2. **Inyecciones (comandos, payloads, prompts)**
   - Riesgo: entradas no confiables que alteren ejecución.
   - Mitigación:
     - validación estricta de inputs (allowlists),
     - parametrización de comandos/queries,
     - sanitización de campos antes de procesar.

3. **Validaciones insuficientes de datos/eventos**
   - Riesgo: corrupción de métricas y decisiones incorrectas.
   - Mitigación:
     - esquema versionado para telemetría,
     - rechazo/quarantine de eventos inválidos,
     - contratos de datos testeados.

4. **Sobreexposición de observabilidad**
   - Riesgo: dashboard o endpoints de telemetría sin control de acceso.
   - Mitigación:
     - RBAC mínimo,
     - autenticación en endpoints internos,
     - segregación de red y límites de origen.

---

### 5.2 Estrategias de resiliencia

1. **Circuit breakers**
   - Abrir circuito ante fallas repetidas de dependencia externa.
   - Half-open controlado para recuperación gradual.

2. **Retries con jitter**
   - Reintentos solo en errores transitorios.
   - Evitar tormentas de reintento y congestión en cascada.

3. **Fallback handlers**
   - Respuesta degradada pero útil (por ejemplo, resultado parcial/cacheado).
   - Señalización explícita al usuario de modo degradado.

4. **Canary deploys**
   - Liberación progresiva (5% → 25% → 100%).
   - Rollback automático por SLO breach.

5. **Runbooks y health checks**
   - Playbooks para incidentes recurrentes.
   - Probes de salud para detectar degradación temprano.

---

### 5.3 Versionado, migración de esquema y despliegues seguros

1. **Versionado**
   - SemVer para servicios/componentes.
   - Campos obligatorios en telemetría: `schema_version`, `app_version`, `ruleset_version`.

2. **Migraciones de esquema**
   - Compatibilidad hacia atrás por al menos una versión.
   - Migraciones aditivas primero (evitar breaking changes abruptos).
   - Validación dual durante transición (`v1` + `v2`).

3. **Despliegues seguros**
   - Pipeline con gates:
     - pruebas automáticas,
     - validación de seguridad básica,
     - smoke tests post-deploy.
   - Estrategia `blue/green` o canary según criticidad.
   - Rollback documentado y practicado.

---

## Checklist operativo sugerido
- [ ] Definir esquema JSON de telemetría versionado.
- [ ] Instrumentar `trace_id` extremo a extremo.
- [ ] Configurar alertas por p95, error rate y fallback rate.
- [ ] Activar control adaptativo (threshold + histéresis + backoff).
- [ ] Establecer revisión HITL semanal de calidad y seguridad.
- [ ] Documentar runbooks de incidentes y rollback.
