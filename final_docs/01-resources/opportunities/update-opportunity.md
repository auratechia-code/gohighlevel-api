# PUT Update Opportunity

**Ruta:** `PUT /opportunities/{opportunityId}`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `opportunities.write`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Actualiza los campos de una oportunidad existente. Comúnmente utilizado para cambiar el estado a `won` o `lost`, mover la oportunidad de etapa (`pipelineStageId`) o actualizar su valor monetario.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |
| Content-Type  | string | ✅        | application/json |

## Path Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `opportunityId` | string | ✅ | ID único de la oportunidad a actualizar. |

## Query Parameters
*(Ninguno)*

## Request Body
```json
{
  "pipelineId": "string — ID del pipeline",
  "name": "string — Nombre actualizado",
  "status": "string — Nuevo estado (open, won, lost, abandoned)",
  "pipelineStageId": "string — Nueva etapa",
  "monetaryValue": "number — Nuevo valor",
  "assignedTo": "string — Nuevo agente",
  "customFields": [
    { "id": "string", "key": "string", "field_value": "any" }
  ]
}
```

## Response 200
```json
{
  "opportunity": {
    "id": "opp_abc123",
    "name": "Updated Opportunity",
    "status": "won",
    "updatedAt": "2024-03-29T13:00:00Z"
  }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Access Token inválido. | Refrescar acceso. |
| 404 | NOT_FOUND | La oportunidad no existe. | Verificar `opportunityId`. |
| 422 | UNPROCESSABLE | Etapa no pertenece al pipeline. | Corregir `pipelineStageId`. |

> ⚠️ El campo `message` en errores 422 es un **Array de strings**.

## Ejemplo — Node.js SDK
```typescript
const result = await ghl.opportunities.update('opp_abc123', {
  status: 'won',
  monetaryValue: 1000
});
```

## Ejemplo — cURL
```bash
curl -X PUT \
  'https://services.leadconnectorhq.com/opportunities/opp_abc123' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -H 'Content-Type: application/json' \
  -d '{
    "status": "won",
    "monetaryValue": 1000
  }'
```

## Notas
> Si cambia el `pipelineId`, asegúrese de proveer también un `pipelineStageId` que sea válido dentro del nuevo pipeline.
