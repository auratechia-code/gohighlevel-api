# GET List Invoices

**Ruta:** `GET /invoices/`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `invoices.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera una lista paginada de facturas (invoices) generadas para una ubicación. Incluye información detallada del contacto, ítems de la factura, impuestos aplicados, configuración de recordatorios automáticos y el estado actual del pago.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `altId` | string | ✅ | ID de la ubicación (`locationId`). |
| `altType` | string | ✅ | Debe ser `location`. |
| `status` | string | ❌ | Filtrar por estado (`draft`, `sent`, `paid`, `void`). |
| `limit` | number | ❌ | Cantidad de resultados (default 20). |
| `offset` | number | ❌ | Desplazamiento para paginación. |

## Response 200
```json
{
  "invoices": [
    {
      "_id": "inv_123",
      "status": "draft",
      "invoiceNumber": "19",
      "currency": "USD",
      "total": 999,
      "amountDue": 999,
      "contactDetails": {
        "id": "con_abc",
        "name": "Alex",
        "email": "alex@example.com"
      },
      "invoiceItems": [
        {
          "name": "Macbook Pro",
          "qty": 1,
          "amount": 999
        }
      ],
      "totalSummary": {
        "subTotal": 999,
        "discount": 0,
        "tax": 0
      }
    }
  ],
  "total": 100
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 400 | BAD_REQUEST | `altId` o `altType` faltante. | Verificar parámetros obligatorios. |
| 401 | UNAUTHORIZED | Scope `invoices.readonly` ausente. | Solicitar permisos correctos. |

## Ejemplo — Node.js SDK
```typescript
const invoices = await ghl.invoices.list({ 
  altId: 'loc_abc', 
  altType: 'location',
  status: 'paid' 
});
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/invoices/' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'altId=loc_abc' \
  -d 'altType=location'
```

## Notas
> Las facturas en estado `draft` no son visibles para el contacto final hasta que se ejecute la acción de "Send". Puede configurar `remindersConfiguration` para automatizar el seguimiento de pagos atrasados.
