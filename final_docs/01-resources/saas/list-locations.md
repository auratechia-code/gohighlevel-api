# GET List SaaS Locations

**Ruta:** `GET /saas/locations`
**Autenticación:** OAuth 2.0 (Agency level scope)
**Scopes requeridos:** `saas.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera una lista paginada de todas las ubicaciones (Sub-Accounts) que tienen habilitado el modo SaaS. Incluye información crítica sobre la suscripción de Stripe, el plan de SaaS asignado y el estado actual de la cuenta. Este endpoint es esencial para agencias que revenden el software.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `companyId` | string | ✅ | ID de la agencia. |
| `limit` | number | ❌ | Cantidad de resultados por página. |
| `page` | number | ❌ | Número de página. |

## Response 200
```json
{
  "locations": [
    {
      "locationId": "loc_123",
      "companyId": "comp_abc",
      "saasMode": "saasV2",
      "subscriptionId": "sub_stripe_123",
      "subscriptionInfo": {
        "saasPlanId": "plan_456",
        "stripeProductId": "prod_789",
        "subscriptionStatus": "active"
      }
    }
  ],
  "pagination": {
    "total": 100,
    "totalPages": 10
  }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token sin permisos de Agencia. | Usar token de nivel Agencia. |
| 404 | NOT_FOUND | Company ID incorrecto. | Validar `companyId`. |

## Ejemplo — Node.js SDK
```typescript
const saasLocations = await ghl.saas.getLocations({ 
  companyId: 'comp_abc',
  limit: 20 
});
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/saas/locations' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'companyId=comp_abc'
```

## Notas
> Este endpoint solo devuelve ubicaciones donde el modo SaaS está explícitamente habilitado. Para obtener todas las ubicaciones (incluyendo las que no son SaaS), use `GET /locations/search`.
