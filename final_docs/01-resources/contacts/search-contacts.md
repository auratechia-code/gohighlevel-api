# POST Search Contacts (Advanced)

**Ruta:** `POST /contacts/search`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `contacts.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Permite buscar y filtrar contactos utilizando criterios avanzados como tags, campos personalizados, fechas de creación y más. Este endpoint es preferible sobre el GET tradicional para segmentaciones complejas.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |
| Content-Type  | string | ✅        | application/json |

## Path Parameters
*(Ninguno)*

## Query Parameters
*(Ninguno)*

## Request Body
```json
{
  "locationId": "string — ID de la ubicación (REQUERIDO)",
  "filters": [
    {
      "field": "string — Nombre del campo",
      "operator": "string — Operador (eq, ne, inc, etc.)",
      "value": "any — Valor a filtrar"
    }
  ],
  "sort": "string — Campo de ordenación",
  "limit": "number — Cantidad de resultados",
  "page": "number — Número de página"
}
```

> ⚠️ **PENDIENTE**: Los parámetros detallados del body para filtros avanzados están documentados externamente por GoHighLevel debido a su complejidad.
> **Doc Oficial Adicional:** [ClickUp Documentation Link](https://doc.clickup.com/8631005/d/h/87cpx-158396/6e629989abe7fad)

## Response 200
```json
{
  "contacts": [
    { "id": "abc123", "email": "test@test.com" }
  ],
  "meta": {
    "total": 1250,
    "nextPage": 2
  }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 400 | BAD_REQUEST | Operador de filtro no soportado. | Revisar ClickUp doc. |
| 401 | UNAUTHORIZED | Token inválido. | Refrescar token. |
| 422 | UNPROCESSABLE | `locationId` faltante. | Incluir locationId en body. |

## Ejemplo — Node.js SDK
```typescript
const result = await ghl.contacts.search({
  locationId: 'loc_abc123',
  filters: [{ field: 'email', operator: 'eq', value: 'juan@perez.com' }]
});
```

## Ejemplo — cURL
```bash
curl -X POST \
  'https://services.leadconnectorhq.com/contacts/search' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -H 'Content-Type: application/json' \
  -d '{
    "locationId": "loc_abc123",
    "filters": []
  }'
```

## Notas
> Este endpoint es altamente potente para integraciones de sincronización de bases de datos y creación de audiencias para IAs.
