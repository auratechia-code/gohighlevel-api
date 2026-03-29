# POST Create Opportunity

**Ruta:** `POST /opportunities/`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `opportunities.write`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Crea una nueva oportunidad (deal) en un pipeline y etapa específicos para un contacto determinado. Requiere asignar un estado inicial (ej. `open`).

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
  "pipelineId": "string — ID del pipeline (REQUERIDO)",
  "locationId": "string — ID de la ubicación (REQUERIDO)",
  "name": "string — Nombre de la oportunidad (REQUERIDO)",
  "contactId": "string — ID del contacto relacionado (REQUERIDO)",
  "status": "string — Estado (open, won, lost, abandoned) (REQUERIDO)",
  "pipelineStageId": "string — ID de la etapa",
  "monetaryValue": "number — Valor del trato",
  "assignedTo": "string — Usuario asignado",
  "customFields": [
    { "id": "string", "key": "string", "field_value": "any" }
  ]
}
```

| Campo | Tipo | Requerido | Descripción | Constraints |
|-------|------|-----------|-------------|-------------|
| `pipelineId` | string | ✅ | ID de la tubería de venta. | Obligatorio. |
| `name` | string | ✅ | Título de la oportunidad. | Obligatorio. |
| `status` | string | ✅ | `open`, `won`, `lost`, `abandoned`. | Valor exacto. |
| `contactId` | string | ✅ | ID del contacto. | Debe existir. |

## Response 201
```json
{
  "opportunity": {
    "id": "opp_abc123",
    "pipelineId": "pip_456",
    "name": "Venta de Software",
    "status": "open"
  }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 400 | BAD_REQUEST | `pipelineId` o `name` faltante. | Verificar body params. |
| 401 | UNAUTHORIZED | Token inválido. | Refrescar acceso. |
| 422 | UNPROCESSABLE | El contacto no existe o etapa inválida. | Ver `message[]` detalle. |

> ⚠️ El campo `message` en errores 422 es un **Array de strings**.

## Ejemplo — Node.js SDK
```typescript
const result = await ghl.opportunities.create({
  pipelineId: 'pip_123',
  locationId: 'loc_abc123',
  name: 'Venta Cloud',
  contactId: 'cnt_789',
  status: 'open'
});
```

## Ejemplo — cURL
```bash
curl -X POST \
  'https://services.leadconnectorhq.com/opportunities/' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -H 'Content-Type: application/json' \
  -d '{
    "pipelineId": "pip_123",
    "locationId": "loc_abc123",
    "name": "Cloud Sale",
    "contactId": "cnt_789",
    "status": "open"
  }'
```

## Notas
> Si no se especifica `pipelineStageId`, la oportunidad se creará en la primera etapa definida para ese pipeline.
