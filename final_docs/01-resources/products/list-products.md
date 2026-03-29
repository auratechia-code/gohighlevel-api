# GET List Products

**Ruta:** `GET /products/`
**Autenticación:** OAuth 2.0 / Private Integration Token
**Scopes requeridos:** `payments.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera una lista paginada de productos configurados en una ubicación. Soporta productos físicos y digitales, variantes (ej. tallas, colores), configuración de impuestos y metadatos de visibilidad en la tienda.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `locationId` | string | ✅ | ID de la ubicación. |
| `limit` | number | ❌ | Máximo de resultados (default 20). |
| `offset` | number | ❌ | Desplazamiento para paginación. |
| `search` | string | ❌ | Filtrar por nombre de producto. |

## Response 200
```json
{
  "products": [
    {
      "_id": "655b33a82209e60b6adb87a5",
      "name": "Awesome Product",
      "description": "Descripción del producto",
      "productType": "PHYSICAL",
      "availableInStore": true,
      "variants": [
        {
          "id": "var_123",
          "name": "Size",
          "options": [{ "id": "opt_1", "name": "XL" }]
        }
      ],
      "image": "https://url-de-la-imagen.png",
      "isTaxesEnabled": true,
      "slug": "awesome-product"
    }
  ],
  "total": [{ "total": 1 }]
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Token sin permisos de `payments`. | Revisar scopes. |
| 404 | NOT_FOUND | Ubicación no existe. | Verificar `locationId`. |

## Ejemplo — Node.js SDK
```typescript
const products = await ghl.products.list({ locationId: 'loc_abc', search: 'Washing' });
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/products/' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'locationId=loc_abc' \
  -d 'limit=10'
```

## Notas
> El `productType` puede ser `PHYSICAL` o `DIGITAL`. Para obtener los precios específicos de un producto, utilice el endpoint de `GET /products/{productId}/prices`.
