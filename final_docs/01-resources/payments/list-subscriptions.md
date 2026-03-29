# GET List Subscriptions

**Ruta:** `GET /payments/subscriptions`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `payments.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Devuelve una lista paginada de suscripciones recurrentes. Proporciona detalles sobre el proveedor de pagos (Stripe, PayPal), el estado actual de la suscripción y el snapshot técnico del plan contratado.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `locationId` | string | ✅ | ID de la ubicación. |
| `status` | string | ❌ | Estado (`active`, `cancelled`, `past_due`). |
| `contactId` | string | ❌ | Filtrar por un contacto específico. |
| `limit` | number | ❌ | Cantidad de resultados por página. |

## Response 200
```json
{
  "data": [
    {
      "_id": "64bf78af39118e4011926cba",
      "contactId": "XPLSw2SVagl12LMDeTmQ",
      "contactName": "James Bond",
      "amount": "100",
      "currency": "USD",
      "status": "active",
      "paymentProviderType": "stripe",
      "subscriptionId": "I-0UE609H8E43P",
      "createdAt": "2023-11-20T10:23:36.515Z"
    }
  ],
  "totalCount": 1
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 400 | BAD_REQUEST | Parámetros inválidos. | Revisar `locationId`. |
| 401 | UNAUTHORIZED | Token expirado. | Refrescar acceso. |

## Ejemplo — Node.js SDK
```typescript
const subscriptions = await ghl.payments.listSubscriptions({ locationId: 'loc_abc123' });
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/payments/subscriptions' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'locationId=loc_abc123'
```

## Notas
> El campo `subscriptionSnapshot` es un string JSON que contiene la respuesta directa del proveedor de pagos (Stripe/PayPal), útil para auditorías detalladas.
