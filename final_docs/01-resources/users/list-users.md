# GET List Users

**Ruta:** `GET /users/`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `users.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Devuelve una lista de usuarios asociados a una ubicación específica o a la cuenta global. Es útil para asignar tareas o leads de forma dinámica basándose en la lista de agentes disponibles.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `locationId` | string | ✅ | Filtrar usuarios que pertenecen a esta ubicación. |

## Response 200
```json
{
  "users": [
    {
      "id": "user_123",
      "name": "John Doe",
      "email": "john@doe.com",
      "roles": {
        "type": "account",
        "role": "admin"
      }
    }
  ]
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 400 | BAD_REQUEST | Falta `locationId`. | Incluir `locationId` en la query. |
| 401 | UNAUTHORIZED | Token inválido. | Refrescar acceso. |

## Ejemplo — Node.js SDK
```typescript
const users = await ghl.users.list({ locationId: 'loc_abc123' });
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/users/' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'locationId=loc_abc123'
```

## Notas
> Si el usuario tiene acceso a múltiples ubicaciones, aparecerá en los resultados de cada una de ellas si se filtra individualmente.
