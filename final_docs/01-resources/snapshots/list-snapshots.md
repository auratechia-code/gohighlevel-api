# GET List Snapshots

**Ruta:** `GET /snapshots/`
**Autenticación:** OAuth 2.0 (Agency level scope)
**Scopes requeridos:** `snapshots.readonly`
**Rate limit:** Estándar (100 req/10s burst — 200k/día)

## Descripción
Recupera una lista de todos los Snapshots (plantillas de configuración) propios e importados disponibles en la cuenta de agencia. Los Snapshots permiten replicar configuraciones completas de CRM entre diferentes sub-cuentas.

## Headers
| Header        | Tipo   | Requerido | Valor             |
|---------------|--------|-----------|-------------------|
| Authorization | string | ✅        | Bearer {token}    |
| Version       | string | ✅        | 2021-07-28        |

## Query Parameters
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `companyId` | string | ✅ | ID de la agencia. |

## Response 200
```json
{
  "snapshots": [
    {
      "id": "1eM2UgkfaECOYyUdCo9Pa",
      "name": "Martial Arts Snapshot",
      "type": "own"
    },
    {
      "id": "2fN3VhlgbFDPZzVeDp0Qb",
      "name": "Real Estate Starter",
      "type": "imported"
    }
  ]
}
```

## Errores
| Status | Error | Causa frecuente | Solución |
|--------|-------|-----------------|----------|
| 401 | UNAUTHORIZED | Scope incorrecto o token de sub-cuenta. | Asegurar `snapshots.readonly` y nivel agencia. |
| 404 | NOT_FOUND | Agencia no encontrada. | Verificar `companyId`. |

## Ejemplo — Node.js SDK
```typescript
const snapshots = await ghl.snapshots.list('comp_abc');
```

## Ejemplo — cURL
```bash
curl -G \
  'https://services.leadconnectorhq.com/snapshots/' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Version: 2021-07-28' \
  -d 'companyId=comp_abc'
```

## Notas
> Los Snapshots de tipo `own` son aquellos creados por su agencia, mientras que los `imported` son plantillas compartidas a su cuenta por otras agencias o por el sistema.
