# GET Get Sub-account (Location)

**Ruta:** `GET /locations/{locationId}`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `locations.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera los detalles completos de una ubicación (sub-cuenta), incluyendo datos de contacto de la empresa, zona horaria, configuración de duplicados y perfiles de redes sociales asociados.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Path Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `locationId` | string | ✅ | ID único de la ubicación. |

## Query Parameters
*(Ninguno)*

## Response 200
```json
{
  "location": {
    "id": "loc_abc123",
    "companyId": "comp_789",
    "name": "Nombre de la Empresa",
    "timezone": "America/Chicago",
    "address": "Calle Falsa 123",
    "city": "Springfield",
    "email": "contacto@empresa.com",
    "phone": "+1234567890",
    "settings": {
      "allowDuplicateContact": false,
      "allowDuplicateOpportunity": false
    },
    "social": {
      "facebookUrl": "https://facebook.com/empresa",
      "instagram": "https://instagram.com/empresa"
    }
  }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token no válido. | Refrescar acceso. |
| 404 | NOT_FOUND | La ubicación no existe o no tiene acceso. | Verificar `locationId`. |

## Ejemplo — Node.js SDK
```typescript
const location = await ghl.locations.get('loc_abc123');
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/locations/loc_abc123' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28'
```

## Notas
> Este endpoint es vital para aplicaciones que necesitan conocer la zona horaria de la ubicación para programar tareas o mensajes de forma precisa.
