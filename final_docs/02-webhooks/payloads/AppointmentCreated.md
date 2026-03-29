# Evento: `AppointmentCreated`

**Categoría:** Calendar
**Trigger:** Se dispara cuando se crea una nueva cita (appointment) en cualquier calendario de la ubicación.
**Criticidad para agentes IA:** ALTA (Acción de confirmación inmediata o automatización de recordatorios)

## Payload Completo
```json
{
  "type": "AppointmentCreated",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "appointment": {
    "id": "apt_123",
    "address": "123 Main St",
    "title": "Strategy Session",
    "calendarId": "cal_456",
    "contactId": "cnt_789",
    "startTime": "2024-04-01T10:00:00.000Z",
    "endTime": "2024-04-01T11:00:00.000Z",
    "status": "confirmed"
  }
}
```

## Campos Clave
| Campo | Tipo | Descripción | Usar para |
|-------|------|-------------|-----------|
| `appointment.id` | string | ID único de la cita. | Registro en calendario externo. |
| `calendarId` | string | ID del calendario. | Clasificación de tipo de cita. |
| `startTime` | string | Fecha y hora de inicio. | Sincronización de agenda. |

## Handler Recomendado (Node.js)
```typescript
case 'AppointmentCreated': {
  const { id, appointment, locationId } = event;
  const { startTime, title } = appointment;
  // logic: Add to local DB or external Calendar.
  // logic: Trigger SMS reminder workflow.
  break;
}
```

## Notas de Implementación
> Este evento es ideal para sistemas de sincronización de calendarios bidireccionales y flujos de precalentamiento antes de las reuniones.
