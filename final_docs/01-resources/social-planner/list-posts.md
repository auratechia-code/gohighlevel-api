# POST Get Social Planner Posts

**Ruta:** `POST /social-planner/posts`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `social-planner.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera una lista de publicaciones (posts) del planificador social. Aunque utiliza el método `POST`, es una operación de consulta que permite filtrado avanzado por estado (publicado, programado, fallido), fecha y plataforma social.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Body Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `locationId` | string | ✅ | ID de la ubicación. |
| `status` | string | ❌ | Estado del post (`published`, `scheduled`, `failed`). |
| `limit` | number | ❌ | Cantidad de resultados. |

## Response 201
```json
{
  "success": true,
  "statusCode": 201,
  "results": {
    "posts": [
      {
        "_id": "post_123",
        "locationId": "loc_abc",
        "status": "published",
        "content": "Contenido del post",
        "platforms": ["facebook", "instagram"]
      }
    ],
    "count": 1
  }
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token sin permisos de Social Planner. | Revisar scopes. |
| 422 | UNPROCESSABLE | Parámetros de filtrado inválidos. | Validar el esquema del body. |

## Ejemplo — Node.js SDK
```typescript
const posts = await ghl.socialPlanner.getPosts({ 
  locationId: 'loc_abc',
  status: 'published' 
});
```

## Ejemplo — cURL
```bash
curl -X POST \
  'https://services.leadconnectorhq.com/social-planner/posts' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -H 'Content-Type: application/json' \
  -d '{
    "locationId": "loc_abc",
    "status": "published"
  }'
```

## Notas
> El Social Planner admite publicaciones en Facebook, Instagram, LinkedIn, X (Twitter), TikTok y Google Business Profile. Los errores en las publicaciones suelen estar detallados en el campo `published_errors` si el estado es `failed`.
