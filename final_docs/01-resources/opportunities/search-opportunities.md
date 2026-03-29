# POST Search Opportunities (Advanced)

**Ruta:** `POST /opportunities/search`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `opportunities.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Permite buscar oportunidades utilizando filtros avanzados. Al igual que el buscador de contactos, este endpoint soporta segmentaciones granulares por pipeline, etapa, usuario asignado y fechas.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |
| Content-Type  | string | ✅        | application/json |

## Path Parameters
*(Ninguno)*

## Query Parameters
*(Ninguno)*

## Request Body
```json
{
  "locationId": "string — ID de la ubicación (REQUERIDO)",
  "pipelineId": "string — Filtrar por pipeline específico",
  "pipelineStageId": "string — Filtrar por etapa",
  "status": "string — Filtrar por estado (open, won, lost, abandoned)",
  "assignedTo": "string — Filtrar por usuario asignado",
  "limit": "number — Resultados por página",
  "page": "number — Página actual"
}
```

> ⚠️ **TIP**: Para filtros más complejos (rangos de fechas, operadores lógicos), consulte la documentación externa especializada.
> **Doc Oficial Adicional:** [ClickUp Documentation Link](https://doc.clickup.com/8631005/d/h/87cpx-424216/7bf11bc9b94f80f)

## Response 200
```json
{
  "opportunities": [
    {
      "id": "opp_123",
      "name": "Opportunity A",
      "status": "open",
      "contact": { "id": "cnt_1", "name": "Doe" }
    }
  ],
  "total": 50,
  "meta": { "nextPage": 2 }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Access Token inválido o expirado. | Refrescar acceso. |
| 422 | UNPROCESSABLE | `locationId` no enviado. | Incluir locationId en body. |

## Ejemplo — Node.js SDK
```typescript
const result = await ghl.opportunities.search({
  locationId: 'loc_abc123',
  status: 'open'
});
```

## Ejemplo — cURL
```bash
curl -X POST \
  'https://services.leadconnectorhq.com/opportunities/search' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -H 'Content-Type: application/json' \
  -d '{
    "locationId": "loc_abc123",
    "status": "open"
  }'
```

## Notas
> Use este endpoint para construir Dashboards personalizados de ventas o motores de reporte de KPI comerciales.
