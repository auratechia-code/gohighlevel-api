# GET List Surveys

**Ruta:** `GET /surveys/`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `surveys.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera la lista de todas las encuestas (surveys) configuradas en una ubicación. A diferencia de los formularios simples, las encuestas son flujos multi-paso con lógica condicional.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `locationId` | string | ✅ | ID de la ubicación. |
| `limit` | number | ❌ | Cantidad máxima de resultados. |
| `skip` | number | ❌ | Desplazamiento para paginación. |

## Response 200
```json
{
  "surveys": [
    {
      "id": "survey_abc",
      "name": "Encuesta de Satisfacción",
      "locationId": "loc_123"
    }
  ],
  "total": 1
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token sin permisos de surveys. | Verificar scopes del token. |
| 404 | NOT_FOUND | Ubicación no disponible. | Revisar `locationId`. |

## Ejemplo — Node.js SDK
```typescript
const surveys = await ghl.surveys.list({ locationId: 'loc_abc' });
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/surveys/' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'locationId=loc_abc'
```

## Notas
> Las encuestas suelen capturar perfiles de contacto más profundos. Los IDs devueltos aquí se utilizan para filtrar los envíos en el endpoint de `submissions`.
