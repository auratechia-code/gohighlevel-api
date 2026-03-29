# Evento: `AppUninstall`

**Categoría:** App / Marketplace
**Trigger:** Se dispara cuando el usuario remueve tu aplicación desde los ajustes integrados de GoHighLevel.
**Criticidad para agentes IA:** ALTA (Acción de limpieza de datos o cancelación de cuenta externa)

## Payload Completo
```json
{
  "type": "AppUninstall",
  "locationId": "loc_abc123",
  "appId": "ghl_app_789",
  "uninstalledAt": "2024-03-29T12:00:00.000Z",
  "uninstalledBy": "user_222"
}
```

## Campos Clave
| Campo | Tipo | Descripción | Usar para |
|-------|------|-------------|-----------|
| `locationId` | string | Ubicación removida. | Eliminación/Desactivación del tenant local. |
| `uninstalledBy` | string | Usuario que lo realizó. | Seguimiento de auditoría. |
| `uninstalledAt` | string | Timestamp de remoción. | Fecha de fin de servicio. |

## Handler Recomendado (Node.js)
```typescript
case 'AppUninstall': {
  const { locationId, uninstalledBy } = event;
  // logic: Mark tenant as inactive in local DB.
  // logic: Trigger offboarding email or survey.
  break;
}
```

## Notas de Implementación
> Una vez uninstalada, tus Access Tokens para esa `locationId` dejarán de ser válidos de inmediato.
