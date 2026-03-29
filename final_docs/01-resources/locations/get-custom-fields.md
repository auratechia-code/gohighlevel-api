# GET Get Custom Fields

**Ruta:** `GET /locations/{locationId}/customFields`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `locations.custom_fields.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera la lista de todos los campos personalizados (custom fields) definidos para una ubicación. Esto es esencial para mapear formularios externos con los campos de GHL o para agentes inteligentes que necesitan entender qué datos adicionales se rastrean.

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
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `model` | string | ❌ | Filtrar por modelo (`contact`, `opportunity`). |

## Response 200
```json
{
  "customFields": [
    {
      "id": "field_abc123",
      "name": "Fecha de Nacimiento",
      "fieldKey": "contact.date_of_birth",
      "dataType": "DATE",
      "placeholder": "DD/MM/YYYY",
      "picklistOptions": [],
      "model": "contact"
    }
  ]
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token inválido. | Refrescar acceso. |
| 404 | NOT_FOUND | La ubicación no existe. | Verificar `locationId`. |

## Ejemplo — Node.js SDK
```typescript
const fields = await ghl.locations.getCustomFields('loc_abc123');
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/locations/loc_abc123/customFields' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28'
```

## Notas
> El `fieldKey` es el identificador que se utiliza al crear o actualizar contactos u oportunidades (ej. `{{contact.pincode}}`).
