# GET List Funnels

**Ruta:** `GET /funnels/`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `funnels.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera una lista paginada de todos los embudos de venta (funnels) configurados en una ubicación. Incluye información de los pasos (steps), URLs, dominios asociados y metadatos de rastreo (tracking).

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `locationId` | string | ✅ | ID de la ubicación. |
| `name` | string | ❌ | Filtrar por nombre del funnel. |
| `offset` | number | ❌ | Desplazamiento para paginación. |
| `limit` | number | ❌ | Máximo de resultados (default 20). |

## Response 200
```json
{
  "funnels": [
    {
      "_id": "funnel_123",
      "name": "Ebook Funnel",
      "locationId": "loc_abc",
      "url": "/ebook-download",
      "steps": [
        {
          "id": "step_1",
          "name": "Optin Page",
          "type": "optin_funnel_page",
          "url": "/optin"
        }
      ],
      "dateAdded": "2024-04-29T15:00:05.681Z"
    }
  ],
  "count": 1
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token sin permisos de funnels. | Revisar scopes del token. |
| 404 | NOT_FOUND | Ubicación no encontrada. | Verificar `locationId`. |

## Ejemplo — Node.js SDK
```typescript
const funnels = await ghl.funnels.list({ locationId: 'loc_abc' });
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/funnels/' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'locationId=loc_abc'
```

## Notas
> Un funnel suele tener múltiples "steps". Para obtener los detalles específicos de las páginas dentro de cada paso, consulte el objeto `steps` devuelto en este endpoint.
