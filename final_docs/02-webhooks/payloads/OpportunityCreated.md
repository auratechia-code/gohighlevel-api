# Evento: `OpportunityCreated`

**Categoría:** Opportunity
**Trigger:** Se dispara inmediatamente al añadir una nueva oportunidad a una pipeline.
**Criticidad para agentes IA:** ALTA (Acción de prospección inmediata)

## Payload Completo
```json
{
  "type": "OpportunityCreated",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "id": "opp_123 — ID único de la oportunidad",
  "contactId": "mTkSCb1UBjb5tk4OvB69",
  "name": "First New Opportunity",
  "pipelineId": "pip_456",
  "pipelineStageId": "stage_789",
  "status": "open",
  "monetaryValue": 250.00,
  "source": "Google Ads",
  "dateAdded": "2024-03-29T12:00:00Z"
}
```

## Campos Clave
| Campo | Tipo | Descripción | Usar para |
|-------|------|-------------|-----------|
| `pipelineId` | string | ID del embudo. | Clasificación de ventas. |
| `stageId` | string | ID de la etapa actual. | Primer paso de seguimiento. |
| `monetaryValue` | number | Valor estimado del trato. | Lead prioritization. |

## Handler Recomendado (Node.js)
```typescript
case 'OpportunityCreated': {
  const { id, pipelineId, monetaryValue, locationId } = event;
  // logic: Assign tasks to commercial.
  // logic: Send notification.
  break;
}
```

## Notas de Implementación
> Si una oportunidad se crea manualmente en el dashboard o vía API 2.0, este webhook se disparará en tiempo real.
