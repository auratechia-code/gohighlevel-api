# GET Get Survey Submissions

**Ruta:** `GET /surveys/submissions`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `surveys.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera los resultados de los envíos realizados a través de encuestas. Al igual que los formularios, incluye datos detallados de atribución publicitaria y el historial de pasos (si aplica).

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `locationId` | string | ✅ | ID de la ubicación. |
| `surveyId` | string | ❌ | Filtrar envíos de una encuesta específica. |
| `q` | string | ❌ | Búsqueda por contacto o email. |
| `limit` | number | ❌ | Cantidad de resultados. |

## Response 200
```json
{
  "submissions": [
    {
      "id": "sub_456",
      "contactId": "con_xyz",
      "surveyId": "survey_123",
      "createAt": "2020-11-01T18:02:21.000Z",
      "others": {
        "eventData": {
          "medium": "survey",
          "source": "Direct traffic"
        }
      }
    }
  ],
  "meta": { "total": 1 }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token inválido. | Refrescar acceso. |
| 404 | NOT_FOUND | Encuesta no encontrada. | Verificar `surveyId`. |

## Ejemplo — Node.js SDK
```typescript
const submissions = await ghl.surveys.getSubmissions({ 
  locationId: 'loc_abc',
  surveyId: 'survey_123' 
});
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/surveys/submissions' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'locationId=loc_abc' \
  -d 'surveyId=survey_123'
```

## Notas
> Las encuestas pueden tener campos personalizados dinámicos. Asegúrese de consultar `GET /locations/{id}/customFields` para interpretar correctamente los IDs de campos devueltos en `others`.
