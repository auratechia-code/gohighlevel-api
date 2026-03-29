# GET List Workflows

**Ruta:** `GET /workflows/`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `workflows.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera la lista de flujos de trabajo (workflows) disponibles en una ubicación. Permite conocer el estado (borrador o publicado) y la versión de cada flujo.

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
  "workflows": [
    {
      "id": "wf_123",
      "name": "Seguimiento de Leads",
      "status": "published",
      "version": 2,
      "createdAt": "2021-05-26T11:33:49.000Z",
      "updatedAt": "2021-05-26T11:33:49.000Z"
    }
  ]
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token inválido. | Refrescar acceso. |
| 403 | FORBIDDEN | Sin permisos para workflows. | Verificar scopes del token. |

## Ejemplo — Node.js SDK
```typescript
const workflows = await ghl.workflows.list({ locationId: 'loc_abc' });
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/workflows/' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'locationId=loc_abc'
```

## Notas
> Este endpoint solo lista los metadatos de los workflows. No devuelve la lógica interna de los pasos ni las condiciones del trigger.
