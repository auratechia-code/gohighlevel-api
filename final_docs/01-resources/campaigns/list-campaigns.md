# GET List Campaigns

**Ruta:** `GET /campaigns/`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `campaigns.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera una lista de las campañas heredadas (Legacy Campaigns) configuradas en una ubicación. Nota importante: GoHighLevel ha migrado la mayoría de sus funcionalidades de automatización hacia los "Workflows". Este endpoint es útil para recuperar nombres y estados de campañas antiguas.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `locationId` | string | ✅ | ID de la ubicación. |
| `status` | string | ❌ | Filtrar por estado (`published`, `draft`). |

## Response 200
```json
{
  "campaigns": [
    {
      "id": "camp_123",
      "name": "Nurture Campaign",
      "status": "published",
      "createdAt": "2025-12-12T08:24:46.700Z",
      "updatedAt": "2026-01-23T05:58:48.453Z"
    }
  ],
  "total": 1
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token sin permisos de campañas. | Revisar scopes. |
| 404 | NOT_FOUND | Ubicación no encontrada. | Verificar `locationId`. |

## Ejemplo — Node.js SDK
```typescript
const campaigns = await ghl.campaigns.list({ locationId: 'loc_abc' });
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/campaigns/' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'locationId=loc_abc'
```

## Notas
> Se recomienda encarecidamente utilizar el endpoint de `workflows` para nuevas implementaciones, ya que las campañas son una funcionalidad en proceso de depreciación.
