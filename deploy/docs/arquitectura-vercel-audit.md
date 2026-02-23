# Auditoría técnica táctica — Microcosmos Elite (deploy)

## 1) Limpieza profunda detectada

### Hallazgos principales
- `App.tsx` concentraba responsabilidades de **routing + estado + UI** (acoplamiento alto).
- La carpeta `components/` estaba plana, sin taxonomía por dominio visual.
- Había rastro lógico del enlace removido (heatmap de `Chalamandra Magistral`) aunque el card ya no existía.
- Señales de navegación heredada (`Ajedrez`, `Dado`, `Blog`) no alineadas con los nodos actuales.

### Acciones aplicadas en esta iteración
- Se separó la página principal en `pages/HubPage.tsx`.
- Se movió `SrapBridgePage` a `pages/` para tratarlo como ruta/pantalla.
- Se reorganizaron componentes por categorías:
  - `components/layout`
  - `components/cards`
  - `components/ui`
  - `components/badges`
- Se limpió el heatmap para eliminar referencia a `Chalamandra Magistral`.
- Se actualizó la lógica de tracking contextual para nodos vigentes.

---

## 2) Estructura profesional optimizada (propuesta objetivo)

```txt
src/
  pages/
    HubPage.tsx
    SrapBridgePage.tsx
    routes.ts
  components/
    layout/
      AdminBanner.tsx
      EcosystemHeader.tsx
    cards/
      ProjectCard.tsx
    ui/
      PudinButton.tsx
      PremiumButton.tsx
    badges/
      ProBadge.tsx
  hooks/
    usePudin.ts
    useStats.ts
  data/
    projects.ts
  utils/
    access.ts
  types/
    index.ts
  App.tsx
  main.tsx
```

---

## 3) Riesgos potenciales y plan de endurecimiento

### Rutas
- Hoy hay manejo manual por `window.location.pathname`.
- Recomendación siguiente fase: migrar a `react-router-dom` para rutas declarativas, 404 y lazy-loading.

### Separación UI / lógica
- `HubPage` sigue siendo robusta pero grande.
- Recomendación: extraer hooks por dominio:
  - `useHubStatusPolling`
  - `useHubTelemetry`
  - `useKeyCountdown`

### Tipado y contratos
- Ya hay tipado base correcto en `types/index.ts`.
- Recomendación: tipar payload de `/status.json` con un `zod` schema para validación runtime.

### Arquitectura
- `ProjectCard` combina render + reglas de bloqueo.
- Recomendación: mover reglas a helper puro (`projectAccessPolicy.ts`) para facilitar tests.

---

## 4) Checklist Vercel (listo para despliegue estable)

- `vite build` compila en limpio.
- Estructura de páginas/components alineada para escalar.
- Si se requiere deep-link seguro en SPA, añadir en `vercel.json`:

```json
{
  "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }]
}
```

(Validar si el proyecto ya lo define en raíz o en `deploy/` antes de duplicar reglas.)

---

## 5) Nota de estilo

La identidad “Chalamandra Magistral” se conserva en naming y narrativa visual,
pero la base queda más sobria: menos ruido, más señal, más mantenibilidad.
