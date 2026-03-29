# DELETE Delete Contact

**Ruta:** `DELETE /contacts/{contactId}`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `contacts.write`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Elimina permanentemente el registro de un contacto específico de la ubicación. **Esta operación es irreversible**. Elimina también las etiquetas, notas y tareas locales asociadas individualmente al contacto.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Path Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `contactId` | string | ✅ | ID único del contacto a eliminar. |

## Query Parameters
*(Ninguno)*

## Request Body
*(No requerido para DELETE)*

## Response 200
```json
{
  "status": "success",
  "message": "Contact deleted successfully"
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token no válido. | Refrescar token OAuth. |
| 404 | NOT_FOUND | El `contactId` no existe. | Verificar el ID enviado. |
| 429 | RATE_LIMIT | Límite excedido. | Esperar e implementar backoff. |

## Ejemplo — Node.js SDK
```typescript
const result = await ghl.contacts.delete('abc123456789');
```

## Ejemplo — cURL
```bash
curl -X DELETE \
  'https://services.leadconnectorhq.com/contacts/abc123456789' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28'
```

## Notas
> Una vez eliminado, este contacto no aparecerá en las búsquedas ni filtros. Si se vuelve a añadir con el mismo email, se generará un nuevo `contactId`.
