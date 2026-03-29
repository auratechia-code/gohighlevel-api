# POST Create Appointment

**Ruta:** `POST /calendars/appointments`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `calendars.write`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Crea una nueva cita (appointment) en un calendario específico de la ubicación. Requiere un `contactId` y el ID del calendario.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |
| Content-Type  | string | ✅        | application/json |

## Request Body
```json
{
  "calendarId": "string — ID del calendario (REQUERIDO)",
  "locationId": "string — ID de la ubicación (REQUERIDO)",
  "contactId": "string — ID del contacto (REQUERIDO)",
  "startTime": "string — Fecha inicio (ISO 8601) (REQUERIDO)",
  "endTime": "string — Fecha fin (ISO 8601)",
  "title": "string — Título de la cita",
  "appointmentStatus": "string — (new, confirmed, cancelled, etc.)",
  "address": "string — Ubicación de la reunión"
}
```

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `calendarId` | string | ✅ | ID del calendario destino. |
| `startTime` | string | ✅ | Ejemplo: `2024-03-29T10:00:00Z`. |
| `contactId` | string | ✅ | Triggers de automatización requieren este ID. |

## Response 201
```json
{
  "appointment": {
    "id": "apt_123",
    "calendarId": "cal_456",
    "status": "confirmed",
    "startTime": "2024-03-29T10:00:00Z"
  }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 400 | BAD_REQUEST | Slot de tiempo ya ocupado. | Revisar disponibilidad. |
| 401 | UNAUTHORIZED | Token inválido. | Refrescar acceso. |
| 422 | UNPROCESSABLE | `calendarId` no existe. | Verificar existencia del calendario. |

## Ejemplo — Node.js SDK
```typescript
const result = await ghl.calendars.createAppointment({
  calendarId: 'cal_001',
  locationId: 'loc_abc',
  contactId: 'cnt_789',
  startTime: '2024-04-10T15:00:00Z',
  title: 'Consultoría Especializada'
});
```

## Ejemplo — cURL
```bash
curl -X POST \
  'https://services.leadconnectorhq.com/calendars/appointments' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -H 'Content-Type: application/json' \
  -d '{
    "calendarId": "cal_123",
    "locationId": "loc_456",
    "contactId": "cnt_789",
    "startTime": "2024-04-10T15:00:00Z"
  }'
```

## Notas
> Este endpoint respetará la configuración del calendario (auto-confirmación, buffer, etc.). Si el slot está bloqueado, devolverá un error 400.
