# GET Get Company

**Ruta:** `GET /companies/{companyId}`
**Autenticación:** OAuth 2.0 (Agency level scope)
**Scopes requeridos:** `companies.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Obtiene los detalles de alto nivel de una Agencia (Company). Incluye configuraciones globales de marca blanca (white-label), dominios, políticas de privacidad, conteo de ubicaciones y configuraciones de SaaS. Este endpoint es fundamental para aplicaciones que operan a nivel de Agencia.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Path Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `companyId` | string | ✅ | ID único de la agencia. |

## Response 200
```json
{
  "company": {
    "id": "comp_123",
    "name": "Tesla Inc",
    "domain": "app.myawesomedomain.com",
    "subdomain": "app.myawesomedomain.com/subdomain",
    "customerType": "agency",
    "status": "active",
    "locationCount": 10,
    "isEnterpriseAccount": true,
    "saasSettings": {
      "agencyDashboardVisibleTo": "admin"
    },
    "twilioTrialMode": false
  }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token sin permisos de Agencia. | Usar un token con scope `companies`. |
| 404 | NOT_FOUND | Company ID inexistente. | Verificar el ID en el panel de Agencia. |

## Ejemplo — Node.js SDK
```typescript
const company = await ghl.companies.get('comp_123');
```

## Ejemplo — cURL
```bash
curl 'https://services.leadconnectorhq.com/companies/comp_123' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28'
```

## Notas
> El `customerType` suele ser `agency`. Muchas de estas configuraciones (como `domain` y `logoUrl`) afectan la apariencia de la plataforma para todos los clientes (Sub-Accounts) de la agencia.
