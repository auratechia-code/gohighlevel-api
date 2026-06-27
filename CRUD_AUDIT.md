# Auditoría CRUD — gohighlevel-api (repo de documentación)

> Repo = documentación de la API GHL (588 endpoints en `docs/01-api-reference/` + scrapers Python).
> No hay código que *ejecute* CRUD; "CRUD correcto" se interpreta como: **el método HTTP, URL y metadata de cada doc coinciden con la API real de GHL** (fuente: `internal/raw_data/ghl_kb_output_pro/ghl_kb_pro_v7_final.json`, el scrape oficial).

## ✅ Método HTTP + URL — CORRECTO (487/487)
Comparado el par (URL, método) de cada `.md` contra el set scrapeado de GHL (489 pares / 336 URLs únicas):
- **487 match, 0 mismatch.**
- Los "sospechosos" iniciales NO son bugs — reflejan el diseño real de GHL:
  - `medias/delete-files` → **PUT** (GHL real)
  - `conversations/.../attachments` → **PUT** (GHL real)
  - `contacts/bulk/tags/update` → **POST** (GHL real)
  - `oauth get-access-token` → POST, `social-planner get-posts` → POST (search con body), bulk-* → POST.
- (Un primer chequeo dio 152 "errores" — era falso positivo: GHL reusa la misma URL para GET/PUT/DELETE y el dedup colapsaba métodos. Corregido comparando pares.)

## ⚠️ Gaps de metadata (fixables) — fallo de scraping, no de método
| Issue | Conteo | Causa |
|---|---|---|
| Header `Version` con valor **vacío** | 458 / 588 | El scraper nunca capturó `2021-07-28` (aparece 0 veces en raw). Es constante obligatoria → **hardcodear**. |
| `Scopes Required` vacío o `N/A` | 239 / 588 | No scrapeado para esos endpoints. |

README declara `Version: 2021-07-28` como header OBLIGATORIO, pero la metadata lo muestra vacío/opcional en el 78% de los docs.

## Cobertura CRUD por recurso
`courses` y `lc-email` están **vacíos** (0 docs) — verificar si GHL ofrece esos endpoints. El resto de "faltantes" C/U/D son legítimos (oauth, phone-system, workflows, forms, surveys son read-only en la API).

## Recomendaciones
1. **Fix generación**: inyectar `Version: 2021-07-28` (Required=Yes) en el template para los 458 docs vacíos. `scripts/ghl_formatter_pro.py` / `ghl_bulk_generator.py`.
2. Re-scrapear scopes faltantes (239) — dato sí existe en la API GHL.
3. Completar `courses` y `lc-email` o documentar por qué están vacíos.
4. Métodos/URLs: sin acción, ya son fieles a GHL.
