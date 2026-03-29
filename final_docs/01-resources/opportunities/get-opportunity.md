# GET Get Opportunity

**Ruta:** `GET /opportunities/{opportunityId}`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `opportunities.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera los detalles completos de una oportunidad, incluyendo su estado actual, valor monetario, pipeline, etapa y los datos básicos del contacto asociado.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Path Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `opportunityId` | string | ✅ | ID único de la oportunidad a recuperar. |

## Query Parameters
*(Ninguno)*

## Request Body
*(No requerido para GET)*

## Response 200
```json
{
  "opportunity": {
    "id": "opp_123",
    "name": "Testing Opportunity",
    "monetaryValue": 500,
    "pipelineId": "pip_456",
    "pipelineStageId": "stage_789",
    "status": "open",
    "contactId": "cnt_001",
    "locationId": "loc_abc",
    "contact": {
      "id": "cnt_001",
      "name": "John Doe",
      "email": "john@doe.com",
      "phone": "+12025550107"
    },
    "customFields": [
      { "id": "field_1", "fieldValue": "value_1" }
    ],
    "createdAt": "2024-03-29T12:00:00Z",
    "updatedAt": "2024-03-29T13:00:00Z"
  }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Access Token inválido. | Refrescar token. |
| 404 | NOT_FOUND | La oportunidad no existe. | Verificar `opportunityId`. |
| 429 | RATE_LIMIT | Límite de ráfaga excedido. | Esperar 10 segundos. |

## Ejemplo — Node.js SDK
```typescript
const result = await ghl.opportunities.get('opp_123');
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/opportunities/opp_123' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28'
```

## Notas
> Devuelve un objeto anidado `contact` con los datos esenciales. Para la información extendida del contacto, utilice el endpoint de Contactos.
