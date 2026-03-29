# GET List Orders

**Ruta:** `GET /payments/orders`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `payments.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera una lista paginada de pedidos realizados dentro de una ubicación. Permite filtrar por estado del pedido, rango de fechas, contacto y fuente (funnel, website, etc.).

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `locationId` | string | ✅ | ID de la ubicación. |
| `status` | string | ❌ | Estado del pedido (`completed`, `pending`, `cancelled`). |
| `limit` | number | ❌ | Cantidad de resultados por página (default: 20). |
| `offset` | number | ❌ | Desplazamiento para paginación. |

## Response 200
```json
{
  "data": [
    {
      "_id": "653f5e0cde5a1314e62a837c",
      "contactId": "XPLSw2SVagl12LMDeTmQ",
      "contactName": "James Bond",
      "amount": "100",
      "currency": "USD",
      "status": "completed",
      "sourceType": "funnel",
      "couponCode": "100PER",
      "createdAt": "2023-11-20T10:23:36.515Z"
    }
  ],
  "totalCount": 1
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 400 | BAD_REQUEST | Falta `locationId`. | Incluir el ID de la ubicación. |
| 401 | UNAUTHORIZED | Token inválido. | Refrescar acceso. |

## Ejemplo — Node.js SDK
```typescript
const orders = await ghl.payments.listOrders({ locationId: 'loc_abc123', status: 'completed' });
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/payments/orders' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'locationId=loc_abc123' \
  -d 'status=completed'
```

## Notas
> El campo `sourceMeta` (si está presente) contiene detalles técnicos sobre el embudo o página específica donde se originó el pedido.
