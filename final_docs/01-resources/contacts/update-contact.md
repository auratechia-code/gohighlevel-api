# PUT Update Contact

**Ruta:** `PUT /contacts/{contactId}`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `contacts.write`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Actualiza la información de un contacto existente. Solo se deben enviar los campos que se desean modificar. Los campos no incluidos conservarán su valor original.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |
| Content-Type  | string | ✅        | application/json |

## Path Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `contactId` | string | ✅ | ID único del contacto a actualizar. |

## Query Parameters
*(Ninguno)*

## Request Body
```json
{
  "firstName": "string — Apellido opcional",
  "lastName": "string — Nombre opcional",
  "email": "string — Correo electrónico opcional",
  "phone": "string — Teléfono opcional (E.164)",
  "tags": ["array — Etiquetas a actualizar (sobrescribir/añadir)"],
  "customFields": [
    { "id": "string", "value": "any" }
  ]
}
```

| Campo | Tipo | Requerido | Descripción | Constraints |
|-------|------|-----------|-------------|-------------|
| `firstName` | string | ❌ | Primer nombre. | Opcional (nullable). |
| `email` | string | ❌ | Email del contacto. | Validar formato. |
| `tags` | array | ❌ | Lista de etiquetas. | El comportamiento común es **overwrite**. |

## Response 200
```json
{
  "contact": {
    "id": "abc123456789",
    "firstName": "Juan Actualizado",
    "lastName": "Perez",
    "email": "juan@actualizado.com"
  }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token no válido. | Refrescar token OAuth. |
| 404 | NOT_FOUND | El `contactId` no existe. | Verificar el ID enviado. |
| 422 | UNPROCESSABLE | El nuevo email ya está en uso. | Ver `message[]` para detalle. |

> ⚠️ El campo `message` en errores 422 es un **Array de strings**.

## Ejemplo — Node.js SDK
```typescript
const result = await ghl.contacts.update('abc123456789', {
  firstName: 'Juan Actualizado'
});
```

## Ejemplo — cURL
```bash
curl -X PUT \
  'https://services.leadconnectorhq.com/contacts/abc123456789' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -H 'Content-Type: application/json' \
  -d '{
    "firstName": "Juan Actualizado"
  }'
```

## Notas
> No se requiere `locationId` dentro del cuerpo de la solicitud para el método PUT, ya que se deduce automáticamente de la ruta asignada al `contactId`.
