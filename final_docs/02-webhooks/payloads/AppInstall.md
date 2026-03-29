# Evento: `AppInstall`

**Categoría:** App / Marketplace
**Trigger:** Se dispara inmediatamente tras completar el flujo OAuth y autorizar la instalación de la aplicación en la ubicación (sub-account).
**Criticidad para agentes IA:** ALTA (Acción de aprovisionamiento de cuenta inicial)

## Payload Completo
```json
{
  "type": "AppInstall",
  "locationId": "loc_abc123",
  "appId": "ghl_app_789",
  "installId": "inst_456",
  "userId": "user_111 — Instalado por este usuario",
  "installedAt": "2024-03-29T11:00:00.000Z",
  "planId": "plus_plan_101",
  "trialEndsAt": null,
  "status": "Active"
}
```

## Campos Clave
| Campo | Tipo | Descripción | Usar para |
|-------|------|-------------|-----------|
| `locationId` | string | ID de la ubicación de instalación. | Indexación en tu base de datos multi-tenant. |
| `userId` | string | Usuario que autorizó la instalación. | Atribución en tu plataforma. |
| `installedAt` | string | Timestamp de instalación. | Fecha de inicio de servicio. |

## Handler Recomendado (Node.js)
```typescript
case 'AppInstall': {
  const { locationId, userId, appId } = event;
  // logic: Set up database entry for this location.
  // logic: Trigger onboarding email.
  break;
}
```

## Notas de Implementación
> Este evento es el punto de partida esencial para cualquier arquitectura multi-tenant de SaaS construida sobre GoHighLevel App Marketplace.
