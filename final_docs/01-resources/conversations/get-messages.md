# GET Get Messages

**Ruta:** `GET /conversations/{conversationId}/messages`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `conversations.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera el histórico de mensajes de una conversación específica. Devuelve una lista paginada donde cada mensaje incluye su contenido, dirección (`inbound`/`outbound`), estado y metadatos específicos del canal.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Path Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `conversationId` | string | ✅ | ID único de la conversación. |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `lastMessageId` | string | ❌ | Para paginación (ID del último mensaje recibido). |
| `limit` | number | ❌ | Cantidad de mensajes a devolver (Default: 20). |

## Response 200
```json
{
  "messages": {
    "lastMessageId": "msg_789",
    "nextPage": true,
    "messages": [
      {
        "id": "msg_001",
        "type": "SMS",
        "body": "Hola, ¿cómo estás?",
        "direction": "inbound",
        "status": "delivered",
        "dateAdded": "2024-03-29T12:00:00Z",
        "meta": {
          "from": "+14155551234",
          "to": "+14155555678"
        }
      }
    ]
  }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token no válido. | Refrescar acceso. |
| 404 | NOT_FOUND | La conversación no existe. | Verificar `conversationId`. |

## Ejemplo — Node.js SDK
```typescript
const messages = await ghl.conversations.getMessages('abc123456');
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/conversations/abc123456/messages' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28'
```

## Notas
> El objeto `meta` varía significativamente dependiendo de si el mensaje es Email (contiene `subject`, `messageIds`), Call (contiene `duration`, `recordingUrl`) o Redes Sociales.
