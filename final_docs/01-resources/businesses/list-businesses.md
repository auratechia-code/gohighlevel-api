# GET List Businesses

**Ruta:** `GET /businesses/`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `businesses.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera la lista de perfiles de negocio (Business Profiles) asociados a una ubicación. Estos perfiles contienen información firmográfica como dirección, sitio web, industria y datos de contacto oficiales del negocio.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `locationId` | string | ✅ | ID de la ubicación. |

## Response 200
```json
{
  "businesses": [
    {
      "id": "bus_123",
      "name": "Microsoft",
      "phone": "+123456789",
      "email": "abc@microsoft.com",
      "website": "microsoft.com",
      "address": "One Microsoft Way",
      "city": "Redmond",
      "state": "WA",
      "country": "united states",
      "locationId": "loc_abc",
      "createdAt": "2024-07-29T15:51:28.071Z"
    }
  ]
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token inválido. | Refrescar acceso. |
| 404 | NOT_FOUND | Ubicación no encontrada. | Verificar `locationId`. |

## Ejemplo — Node.js SDK
```typescript
const businesses = await ghl.businesses.listByLocation('loc_abc');
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/businesses/' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'locationId=loc_abc'
```

## Notas
> Un contacto (Contact) puede estar asociado a uno o más negocios (Businesses) a través del sistema de asociaciones. Este perfil es central para el manejo de cuentas B2B.
