# GoHighLevel API Documentation (Knowledge Base)

Bienvenido a la referencia técnica consolidada de GoHighLevel. Este repositorio contiene una base de conocimientos estructurada, validada y formateada para ser indexada fácilmente por humanos y modelos de IA (RAG-Ready).

## 📂 Estructura de la Documentación
*   [**SUMMARY.md**](SUMMARY.md): El índice maestro categorizado por recursos y servicios.
*   [**endpoints/**](endpoints/): Documentación técnica detallada de los 680 endpoints de la API (Contactos, Calendarios, Oportunidades, etc.).
*   [**webhooks/**](webhooks/): Definiciones de eventos y payloads de ejemplo para integración en tiempo real.
*   [**concepts/**](concepts/): Guías sobre OAuth2, Authorization y políticas del Marketplace.

## 🚀 Contenido de los Archivos
Cada página de documentación (.md) incluye:
*   **YAML Frontmatter:** Metadata para indexación IA.
*   **Información de Endpoint:** Métodos, URLs base y paths específicos.
*   **Esquemas de Parámetros:** Tablas detalladas de Path, Query y Headers.
*   **Ejemplos de Código:** Bloques listos para Python, Node.js y cURL.
*   **Modelos de Respuesta:** Estructuras JSON para diferentes códigos de estado (200, 400, etc.).

## 🛠️ Herramientas (Opcional)
Si necesitás actualizar esta documentación en el futuro, los motores de scraping y formateo están disponibles en la carpeta `/tools`:
*   `tools/ghl_scraper.py`: Motor de extracción asíncrono (Playwright).
*   `tools/ghl_formatter.py`: Conversor de JSON a Markdown.

## 🔒 Seguridad
Este repositorio es 100% estático y no contiene tokens, credenciales o información sensible. Todos los ejemplos utilizan placeholders genéricos.

---
*Generado automáticamente para la comunidad de desarrolladores de GoHighLevel.*
