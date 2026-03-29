# GET List Pipelines

**Ruta:** `GET /opportunities/pipelines`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `opportunities.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera todos los embudos de ventas (pipelines) configurados en una ubicación, incluyendo sus etapas (stages). Este endpoint es crítico para saber en qué etapa colocar una oportunidad al crearla o actualizarla.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `locationId` | string | ✅ | ID de la ubicación. |

## Response 200
```json
{
  "pipelines": [
    {
      "id": "pipe_123",
      "name": "Ventas Inmobiliarias",
      "stages": [
        { "id": "stage_1", "name": "Lead Nuevo" },
        { "id": "stage_2", "name": "Cita Programada" }
      ],
      "showInFunnel": true,
      "showInPieChart": true
    }
  ]
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token inválido. | Refrescar acceso. |
| 404 | NOT_FOUND | Ubicación no encontrada. | Verificar `locationId`. |

## Ejemplo — Node.js SDK
```typescript
const pipelines = await ghl.opportunities.listPipelines('loc_abc');
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/opportunities/pipelines' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'locationId=loc_abc'
```

## Notas
> Al trabajar con oportunidades, siempre es mejor obtener primero la lista de pipelines para asegurar que se están utilizando IDs de etapa válidos.
