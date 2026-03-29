# GET Get Free Slots

**Ruta:** `GET /calendars/{calendarId}/free-slots`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `calendars.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Devuelve todos los horarios disponibles (slots) para un calendario específico dentro de un rango de fechas. Permite filtrar por zona horaria y usuario asignado.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Path Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `calendarId` | string | ✅ | ID único del calendario. |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `startDate` | number | ✅ | Timestamp Unix (milisegundos) de inicio. |
| `endDate` | number | ✅ | Timestamp Unix (milisegundos) de fin. |
| `timezone` | string | ❌ | Zona horaria deseada (ej. `America/New_York`). |
| `userId` | string | ❌ | Filtrar por disponibilidad de un usuario específico. |

## Response 200
```json
{
  "2024-10-28": {
    "slots": [
      "2024-10-28T10:00:00-05:00",
      "2024-10-28T11:00:00-05:00"
    ]
  },
  "2024-10-29": {
    "slots": [
      "2024-10-29T10:00:00-05:00"
    ]
  }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token no válido. | Refrescar acceso. |
| 404 | NOT_FOUND | `calendarId` no existe. | Verificar el ID del calendario. |

## Ejemplo — Node.js SDK
```typescript
const slots = await ghl.calendars.getFreeSlots('cal_abc', {
  startDate: 1711718400000,
  endDate: 1711804800000
});
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/calendars/cal_abc/free-slots' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'startDate=1711718400000' \
  -d 'endDate=1711804800000'
```

## Notas
> La respuesta está agrupada por fecha. Útil para construir interfaces de reserva personalizadas (custom booking widgets).
