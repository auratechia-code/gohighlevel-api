# DELETE Delete Opportunity

**Ruta:** `DELETE /opportunities/{opportunityId}`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `opportunities.write`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Elimina de forma permanente una oportunidad específica. **Esta operación es irreversible**. No elimina al contacto asociado, solo la instancia de la oportunidad en el pipeline.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Path Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `opportunityId` | string | ✅ | ID único de la oportunidad a eliminar. |

## Query Parameters
*(Ninguno)*

## Request Body
*(No requerido para DELETE)*

## Response 200
```json
{
  "status": "success",
  "message": "Opportunity deleted successfully"
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Access Token inválido. | Refrescar acceso. |
| 404 | NOT_FOUND | La oportunidad no existe. | Verificar `opportunityId`. |
| 429 | RATE_LIMIT | Límite de ráfaga excedido. | Esperar 10 segundos. |

## Ejemplo — Node.js SDK
```typescript
const result = await ghl.opportunities.delete('opp_abc123');
```

## Ejemplo — cURL
```bash
curl -X DELETE \
  'https://services.leadconnectorhq.com/opportunities/opp_abc123' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28'
```

## Notas
> Si utiliza este método, se disparará el webhook `OpportunityDeleted` (si está configurado).
