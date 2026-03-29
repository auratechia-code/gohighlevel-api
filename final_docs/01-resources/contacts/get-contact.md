# GET Get Contact

**Ruta:** `GET /contacts/{contactId}`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `contacts.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera la información completa de un contacto específico utilizando su identificador único (`contactId`). Devuelve campos básicos, campos personalizados y etiquetas.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Path Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `contactId` | string | ✅ | ID único del contacto a recuperar. |

## Query Parameters
*(Ninguno)*

## Request Body
*(No requerido para GET)*

## Response 200
```json
{
  "contact": {
    "id": "abc123456789",
    "firstName": "Juan",
    "lastName": "Perez",
    "email": "juan@ejemplo.com",
    "phone": "+1234567890",
    "tags": ["cliente", "vip"],
    "customFields": [
      { "id": "field_id_123", "value": "mi-valor-personalizado" }
    ],
    "locationId": "loc_abc123"
  }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token faltante o expirado. | Refrescar token OAuth. |
| 404 | NOT_FOUND | El `contactId` no existe. | Verificar el ID enviado. |
| 429 | RATE_LIMIT | Límite excedido. | Esperar e implementar backoff. |

## Ejemplo — Node.js SDK
```typescript
const result = await ghl.contacts.get('abc123456789');
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/contacts/abc123456789' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28'
```

## Notas
> No se requiere `locationId` como parámetro de búsqueda si ya se cuenta con el `contactId`, ya que este último es globalmente único para la ubicación asociada.
