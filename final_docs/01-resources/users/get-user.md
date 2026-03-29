# GET Get User

**Ruta:** `GET /users/{userId}`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `users.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera la información detallada de un usuario, incluyendo sus datos de contacto, permisos granulares (campañas, contactos, workflows, etc.) y los roles asignados a nivel de cuenta o ubicación.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Path Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `userId` | string | ✅ | ID único del usuario. |

## Query Parameters
*(Ninguno)*

## Response 200
```json
{
  "id": "user_123",
  "name": "John Doe",
  "email": "john@doe.com",
  "permissions": {
    "contactsEnabled": true,
    "workflowsEnabled": true,
    "opportunitiesEnabled": true,
    "conversationsEnabled": true
  },
  "roles": {
    "type": "account",
    "role": "admin",
    "locationIds": ["loc_abc"]
  }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token inválido. | Refrescar acceso. |
| 404 | NOT_FOUND | El usuario no existe en la cuenta actual. | Verificar `userId`. |

## Ejemplo — Node.js SDK
```typescript
const user = await ghl.users.get('user_123');
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/users/user_123' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28'
```

## Notas
> El objeto `permissions` es extenso y define qué módulos puede ver o editar el usuario dentro de la plataforma.
