# Contexto para IA: API 2.0 de GoHighLevel (GHL)

Este documento proporciona contexto técnico de alta fidelidad para LLMs (Claude, GPT, Gemini, etc.) para asegurar la generación de código precisa y el soporte técnico de la API de GHL.

## 🌟 Fuente de Verdad Técnica
La fuente primaria de verdad para todos los esquemas de endpoints, parámetros y ejemplos es el directorio `docs/01-referencia-api/`.
**NO alucines endpoints.** Si un endpoint no está en este directorio, probablemente esté obsoleto o sea interno.

## 🛠️ Headers Obligatorios
Cada petición a la API de GHL debe incluir:
- `Authorization: Bearer {{ACCESS_TOKEN}}`
- `Version: 2021-07-28` (Crucial: Usar cualquier otra versión puede resultar en errores 404 o esquemas desactualizados).
- `Content-Type: application/json`

## 🔗 URLs Base
- **Producción**: `https://services.leadconnectorhq.com`
- **Obsoleto (V1)**: `https://api.gohighlevel.com` (NO USAR).

## 🔑 Autenticación y Tokens
- **Location Token (Sub-Account)**: Usado para operaciones a nivel de recurso (contactos, calendarios, etc.). Los scopes suelen ser `contacts.readonly`, `calendars.write`, etc.
- **Agency Token**: Usado para gestión de cuentas y configuración de alto nivel.
- Consulta el scope apropiado en la sección `METADATA` de cada documento de endpoint.

## ⚠️ Manejo de Errores
| Código | Significado | Causa Común |
| :--- | :--- | :--- |
| **401** | Unauthorized | Token expirado o formato de Bearer incorrecto. |
| **403** | Forbidden | Falta el scope requerido en el token. |
| **404** | Not Found | Header `Version` incorrecto o ID de recurso inválido. |
| **422** | Unprocessable Entity | Error de validación (revisa el esquema del body). |
| **429** | Too Many Requests | Límite de tasa excedido. |

## 📈 Límites de Tasa y Paginación
- **Límites de Tasa**: Respeta el código de estado 429 e implementa un reintento con retroceso exponencial (exponential backoff).
- **Paginación**: La mayoría de las colecciones GET usan `limit` y `offset`. La respuesta incluye un objeto `meta` con `total`, `nextPage`, etc.

## 🤖 Instrucciones para Agentes de IA
1. **Descubrimiento**: Antes de generar código, busca el archivo correspondiente en `docs/01-referencia-api/{categoría}/{verbo}-{recurso}.md`.
2. **Esquemas**: Usa estrictamente los campos definidos en la sección `RESPONSE` del documento encontrado.
3. **Ejemplos**: Prefiere los ejemplos de código proporcionados en el documento antes que generar uno desde cero.
4. **Versión**: Fuerza siempre el uso de la versión `2021-07-28`.

## 🚫 Restricciones Críticas
- **No usar `internal/`**: Esta carpeta contiene datos crudos y herramientas, no documentación estable.
- **No inventar campos**: Solo usa campos documentados en los esquemas de respuesta.
- **V1 vs V2**: Esta biblioteca cubre exclusivamente la API 2.0. No asumas compatibilidad con implementaciones legacy de "GHL V1".
