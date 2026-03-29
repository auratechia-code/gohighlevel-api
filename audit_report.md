# Informe de Auditoría — Repositorio GHL API Docs

Este informe detalla el estado actual del repositorio `gohighlevel-api` y propone una reorganización estratégica para optimizar su uso por parte de humanos y sistemas de IA.

---

## 📂 FASE 1 — INVENTARIO

| Directorio | Archivos | Tamaño (Total) | Descripción |
| :--- | :--- | :--- | :--- |
| `final_docs/01-resources/` | 588 | 6.2 MB | **Versión Actual (Gold Standard)**. Documentación completa en Markdown generada recientemente. |
| `ghl_docs_pro/` | 646 | 8.6 MB | Versión legacy de documentación. Contiene duplicados de los mismos endpoints pero con estructura previa. |
| `endpoints/` | 649 | 3.2 MB | Otra versión legacy. Archivos más pequeños y menos detallados que la versión Gold. |
| `data-agregated/` | 1 | 7.4 MB | `ALL_DOCS.json`: El knowledge base unificado utilizado para la generación masiva. |
| `ghl_kb_output_pro/` | 2 | 11.0 MB | JSONs de origen adicionales (v7 final). Datos brutos del scraping. |
| `concepts/` | 2 | 28 KB | Páginas de conceptos generales (Sandbox, etc.). |
| `modules/` | 11 | 85 KB | Documentación específica por módulos de GHL. |
| `tools/` | 14 | 117 KB | Scripts de automatización (bulk generator, validator). |
| `scraped_v2/` | 14 | 27 KB | Datos crudos de scraping antiguos. |
| `sdks/` | 4 | 15 KB | Referencias parciales sobre SDKs. |

---

## 🔍 FASE 2 — DIAGNÓSTICO

1.  **Relevancia**:
    *   **Alta**: `final_docs/01-resources/` es el activo más valioso. Es la única fuente que cumple con el estándar de 12 ejemplos de código y esquemas de respuesta completos.
    *   **Media**: `concepts/` y `modules/` contienen información contextual útil que no está en los endpoints individuales.
    *   **Baja**: `ghl_docs_pro/` y `endpoints/` son versiones obsoletas que ensucian el contexto de búsqueda para la IA.

2.  **Duplicación**:
    *   Existe una redundancia del **300%** en la documentación de endpoints (`final_docs` vs `ghl_docs_pro` vs `endpoints`). Esto causa alucinaciones en LLMs al encontrar múltiples versiones del mismo endpoint.

3.  **Completitud**:
    *   `final_docs` cubre 588 endpoints. Se estima que faltan ~46 endpoints menores o deprecated que están en los JSONs pero no se generaron.

4.  **Calidad**:
    *   `final_docs`: Excelente (Markdown estructurado, tablas, código).
    *   `modules/`: Media (texto plano o Markdown simple).

5.  **Categoría**: 
    *   El repositorio es mayoritariamente **API Reference** orientado a **CRM** y **SaaS (Marketplace)**.

---

## 📋 FASE 3 — RECOMENDACIONES

| Archivo / Directorio Actual | Acción Recomendada | Motivo |
| :--- | :--- | :--- |
| `final_docs/01-resources/` | **MANTENER & PROMOVER** | Es la versión final curada. Debe ser la raíz de la nueva estructura. |
| `ghl_docs_pro/` | **ELIMINAR** | Información duplicada y obsoleta que confunde a la IA. |
| `endpoints/` | **ELIMINAR** | Totalmente redundante con `final_docs`. |
| `data-agregated/` | **ARCHIVAR** | Mover a una carpeta `/raw_data` o `/source` para referencia técnica. |
| `concepts/` | **FUSIONAR** | Integrar en una sección `docs/guides` o `docs/concepts`. |
| `tools/` | **RENOMBRAR** | Cambiar a `/scripts` para separar la lógica de los documentos. |

---

## 🏗️ FASE 4 — ESTRUCTURA PROPUESTA

Diseñada para acceso rápido (humano) y rastro de contexto coherente (IA).

```text
/
├── docs/                       # Toda la documentación de usuario/dev
│   ├── 01-api-reference/       # (Ex final_docs) Endpoints por categoría
│   ├── 02-concepts/            # Conceptos core (Sandbox, Auth, Rate Limits)
│   ├── 03-guides/              # Guías por módulos y tutoriales
│   └── 04-sdk/                 # Referencias de SDKs (si existen)
├── scripts/                    # (Ex tools) Herramientas de generación
├── internal/                   # JSONs de origen y logs de scraping
│   ├── raw_data/               # ALL_DOCS.json, etc.
│   └── logs/                   # Historial de procesos
├── .cursorrules                # Instrucciones específicas para IA
├── README.md                   # Portal de entrada
└── STRUCTURE.md                # Mapa del tesoro para humanos e IA
```

---

## 📝 FASE 5 — NUEVOS ARCHIVOS DE INSTRUCCIONES

1.  **README.md**:
    *   Propósito: Puerta de entrada al repo.
    *   Contenido: Qué es el repo, cómo navegar la estructura `docs/`, versiones de API soportadas.
2.  **STRUCTURE.md**:
    *   Propósito: Guía de navegación para humanos e IA.
    *   Contenido: Mapa detallado de carpetas y qué esperar en cada nivel.
3.  **AI_CONTEXT.md**:
    *   Propósito: "Pre-prompt" para LLMs (Claude/GPT).
    *   Contenido: Reglas de la API (v2021-07-28), cómo interpretar los scopes, advertencias sobre endpoints comunes.
4.  **CONTRIBUTING.md**:
    *   Propósito: Estandarizar cómo agregar nuevos endpoints.
    *   Contenido: Uso del script en `scripts/` para mantener el template Gold Standard.

---

## 📊 ESTIMACIÓN FINAL

*   **Archivos a eliminar**: ~1,300 (carpetas `ghl_docs_pro` y `endpoints`).
*   **Archivos a fusionar/reubicar**: ~20 (concepts, modules, sdks).
*   **Archivos Gold Standard que quedan**: 588.
*   **Versión Limpia**: ~610 archivos organizados lógicamente.
