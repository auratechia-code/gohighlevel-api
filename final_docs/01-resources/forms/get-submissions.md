# GET Get Form Submissions

**Ruta:** `GET /forms/submissions`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `forms.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera los datos de los envíos realizados a través de un formulario específico. Incluye no solo los valores de los campos, sino también datos de atribución técnica (fbc, fbp, URLs de origen, etc.) esenciales para el seguimiento publicitario (marketing tracking).

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `locationId` | string | ✅ | ID de la ubicación. |
| `formId` | string | ❌ | Filtrar envíos de un formulario específico. |
| `q` | string | ❌ | Búsqueda por nombre de contacto o email. |
| `limit` | number | ❌ | Cantidad de resultados. |

## Response 200
```json
{
  "submissions": [
    {
      "id": "sub_123",
      "contactId": "con_abc",
      "formId": "form_xyz",
      "email": "test@test.com",
      "others": {
        "eventData": {
          "source": "Direct traffic",
          "page": { "url": "https://example.com" }
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
| 404 | NOT_FOUND | Formulario no encontrado. | Verificar `formId`. |

## Ejemplo — Node.js SDK
```typescript
const submissions = await ghl.forms.getSubmissions({ 
  locationId: 'loc_abc',
  formId: 'form_xyz' 
});
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/forms/submissions' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'locationId=loc_abc' \
  -d 'formId=form_xyz'
```

## Notas
> El objeto `others` contiene información de diagnóstico y seguimiento (eventData) que es crucial para equipos de marketing que optimizan conversiones.
