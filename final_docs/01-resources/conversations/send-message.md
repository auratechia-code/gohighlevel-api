# POST Send Message

**Ruta:** `POST /conversations/messages`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `conversations.message.write`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Envía un nuevo mensaje a un contacto específico. Soporta múltiples canales (SMS, Email, WhatsApp, Facebook, etc.) a través del parámetro `type`.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |
| Content-Type  | string | ✅        | application/json |

## Request Body
```json
{
  "type": "string — (SMS, Email, WhatsApp, Facebook, Instagram, Google, InternalComment) (REQUERIDO)",
  "contactId": "string — ID del contacto destinatario (REQUERIDO)",
  "message": "string — Contenido del mensaje",
  "subject": "string — Asunto (Requerido para Email)",
  "emailFrom": "string — Email del remitente",
  "replyTo": "string — Email para respuestas",
  "attachments": ["string — URLs de archivos adjuntos"],
  "scheduledTimestamp": "number — Unix timestamp en segundos para programar envío"
}
```

### Campos Específicos por Tipo
| Tipo | Campos Adicionales Requeridos / Recomendados |
|------|---------------------------------------------|
| **SMS** | `message`, `fromNumber` (opcional si hay uno por defecto). |
| **Email** | `subject`, `message` (o HTML), `emailFrom`. |
| **InternalComment** | `message`, `mentions` (Array de IDs de usuarios). |
| **WhatsApp** | `message`, `templateId` (si se usa plantilla). |

## Response 201
```json
{
  "conversationId": "ABC12h2F6uBrIkfXYazb",
  "messageId": "t22c6DQcTDf3MjRhwf77",
  "msg": "Message queued successfully."
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 400 | BAD_REQUEST | Tipo de mensaje no soportado o `contactId` inválido. | Revisar parámetros obligatorios. |
| 401 | UNAUTHORIZED | Access Token no válido. | Refrescar acceso. |
| 422 | UNPROCESSABLE | No hay saldo de SMS o canal no configurado. | Verificar configuración de ubicación. |

## Ejemplo — Enviar SMS (cURL)
```bash
curl -X POST \
  'https://services.leadconnectorhq.com/conversations/messages' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -H 'Content-Type: application/json' \
  -d '{
    "type": "SMS",
    "contactId": "cnt_abc123",
    "message": "Hola, este es un recordatorio de tu cita."
  }'
```

## Ejemplo — Comentario Interno (Node.js)
```typescript
const result = await ghl.conversations.sendMessage({
  type: 'InternalComment',
  contactId: 'cnt_abc123',
  message: 'El cliente prefiere contacto por la tarde.',
  mentions: ['user_789']
});
```

## Notas
> El envío de mensajes está sujeto a las cuotas de cumplimiento A2P (para SMS) y las políticas de ventana de 24h de WhatsApp/Facebook.
