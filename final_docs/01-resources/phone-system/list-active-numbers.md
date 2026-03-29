# GET List Active Numbers

**Ruta:** `GET /phone-system/active-numbers`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `phone-system.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera una lista paginada de todos los números de teléfono activos (comprados o portados) en una ubicación específica. Incluye detalles técnicos como SID de Twilio, capacidades (SMS/Voice), configuraciones de reenvío (forwarding) y usuarios vinculados.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `locationId` | string | ✅ | ID de la ubicación. |
| `limit` | number | ❌ | Resultados por página (default 100). |
| `page` | number | ❌ | Número de página. |

## Response 200
```json
{
  "numbers": [
    {
      "phoneNumber": "+14155552671",
      "friendlyName": "Sales Line 1",
      "sid": "PN123...",
      "capabilities": {
        "voice": true,
        "sms": true,
        "mms": true
      },
      "type": "local",
      "forwardingNumber": "+14155552672",
      "dateAdded": "2023-01-15T10:30:00Z"
    }
  ],
  "accountStatus": "active"
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Scope incorrecto. | Asegurar `phone-system.readonly`. |
| 404 | NOT_FOUND | Ubicación no encontrada. | Verificar `locationId`. |

## Ejemplo — Node.js SDK
```typescript
const activeNumbers = await ghl.phoneSystem.listActiveNumbers('loc_abc');
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/phone-system/active-numbers' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'locationId=loc_abc'
```

## Notas
> Si el número está asignado a un "User", las llamadas entrantes sonarán primero para ese usuario específico. El campo `inboundCallService` indica si el número está siendo procesado por una IA de voz.
