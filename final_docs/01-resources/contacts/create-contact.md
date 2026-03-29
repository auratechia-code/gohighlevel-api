# POST Create Contact

**Ruta:** `POST /contacts/`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `contacts.write`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Crea un nuevo registro de contacto en una ubicación (sub-account) específica. Si el email ya existe y la deduplicación está activa, la API puede devolver un error 422 o realizar un merge dependiendo de la configuración del sub-account.

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
  "firstName": "string — Nombre",
  "lastName": "string — Apellido",
  "email": "string — Correo electrónico principal",
  "phone": "string — Teléfono en formato E.164",
  "address1": "string — Dirección",
  "city": "string — Ciudad",
  "state": "string — Estado/Provincia",
  "postalCode": "string — Código postal",
  "website": "string — URL del sitio web",
  "timezone": "string — Zona horaria (ej: America/New_York)",
  "dnd": "boolean — Estado global de No Molestar",
  "tags": ["array — Etiquetas a asignar"],
  "customFields": [
    {
      "id": "string — ID del campo personalizado",
      "value": "any — Valor del campo"
    }
  ],
  "source": "string — Origen del contacto"
}
```

| Campo | Tipo | Requerido | Descripción | Constraints |
|-------|------|-----------|-------------|-------------|
| `locationId` | string | ✅ | ID de la ubicación de destino. | Obligatorio. |
| `email` | string | ❌ | Email del contacto. | Validar formato email. |
| `phone` | string | ❌ | Teléfono del contacto. | Formato E.164. |
| `tags` | array | ❌ | Lista de etiquetas. | Máx 100 caracteres por etiqueta. |

## Response 201
```json
{
  "contact": {
    "id": "abc123456789",
    "locationId": "loc_abc123",
    "email": "juan@ejemplo.com",
    "firstName": "Juan",
    "lastName": "Perez"
  }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 400 | BAD_REQUEST | `locationId` faltante o inválido. | Verificar body params. |
| 401 | UNAUTHORIZED | Token de acceso inválido o expirado. | Refrescar token OAuth. |
| 422 | UNPROCESSABLE | El email ya existe en esta ubicación. | Ver `message[]` para detalle. |
| 429 | RATE_LIMIT | Límite de ráfaga (100/10s) excedido. | Esperar e implementar backoff. |

> ⚠️ El campo `message` en errores 422 es un **Array de strings**, no un string.
> Parsear como `error.message.join(', ')` para evitar crashes.

## Ejemplo — Node.js SDK
```typescript
const result = await ghl.contacts.create({
  locationId: 'loc_abc123',
  firstName: 'Juan',
  lastName: 'Perez',
  email: 'juan@ejemplo.com'
});
```

## Ejemplo — cURL
```bash
curl -X POST \
  'https://services.leadconnectorhq.com/contacts/' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -H 'Content-Type: application/json' \
  -d '{
    "locationId": "loc_abc123",
    "firstName": "Juan",
    "lastName": "Perez",
    "email": "juan@ejemplo.com"
  }'
```

## Notas
> Si se envía un contacto con un email que ya existe en la misma `locationId`, el comportamiento por defecto es rechazar la creación (422) a menos que se use el endpoint de Upsert.
