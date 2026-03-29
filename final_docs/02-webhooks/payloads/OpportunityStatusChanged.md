# Evento: `OpportunityStatusChanged`

**Categoría:** Opportunity
**Trigger:** Se dispara cuando el campo `status` de una oportunidad cambia (de `open` a `won`, `lost`, `abandoned`).
**Categoría:** Opportunity
**Criticidad para agentes IA:** ALTA (Acción de éxito de ventas o recuperación de clientes perdidos)

## Payload Completo
```json
{
  "type": "OpportunityStatusChanged",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "id": "opp_123 — ID único de la oportunidad",
  "assignedTo": "user_789 — ID del propietario actual",
  "contactId": "mTkSCb1UBjb5tk4OvB69",
  "monetaryValue": 250,
  "name": "Updated Deal",
  "pipelineId": "pip_456",
  "pipelineStageId": "stage_789",
  "source": "Referral",
  "status": "won",
  "dateAdded": "2024-03-29T12:00:00.000Z"
}
```

## Campos Clave
| Campo | Tipo | Descripción | Usar para |
|-------|------|-------------|-----------|
| `status` | string | Nuevo estado (p. ej. `won`). | Acción de contrato o feedback. |
| `monetaryValue` | number | Valor final del trato. | Reporte de ingresos. |
| `assignedTo` | string | Agente asignado. | Comisiones y atribución. |

## Handler Recomendado (Node.js)
```typescript
case 'OpportunityStatusChanged': {
  const { id, status, monetaryValue, locationId } = event;
  if (status === 'won') {
    // success logic
  } else {
    // lost logic
  }
  break;
}
```

## Notas de Implementación
> Este evento es fundamental para monitorear el desempeño de los agentes comerciales en tiempo real.
