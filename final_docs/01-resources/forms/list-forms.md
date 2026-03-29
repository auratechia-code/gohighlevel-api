# GET List Forms

**Ruta:** `GET /forms/`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `forms.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera una lista de todos los formularios creados dentro de una ubicación específica. Permite obtener los IDs necesarios para consultar envíos (submissions) o para integrar formularios en sitios externos.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `locationId` | string | ✅ | ID de la ubicación. |
| `limit` | number | ❌ | Cantidad de resultados. |
| `skip` | number | ❌ | Desplazamiento para paginación. |

## Response 200
```json
{
  "forms": [
    {
      "id": "form_abc",
      "name": "Formulario de Contacto",
      "locationId": "loc_123"
    }
  ],
  "total": 1
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token inválido. | Refrescar acceso. |
| 404 | NOT_FOUND | Ubicación no encontrada. | Verificar `locationId`. |

## Ejemplo — Node.js SDK
```typescript
const forms = await ghl.forms.list({ locationId: 'loc_abc' });
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/forms/' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'locationId=loc_abc'
```

## Notas
> Este endpoint solo devuelve los formularios estáticos (Form Builder). No incluye encuestas (Surveys), que tienen su propia sección en la API.
