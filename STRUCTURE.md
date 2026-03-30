# Mapa de Estructura del Repositorio

Este documento proporciona una guía de navegación detallada para el repositorio de documentación de la API de GHL, optimizada tanto para desarrolladores como para agentes de IA.

## 📁 Árbol de Directorios

- `/docs`: Carpeta raíz de toda la documentación.
    - `/01-api-reference`: Más de 588 documentos de endpoints de alta fidelidad.
        - `/{categoría}/`: Endpoints agrupados por recursos de GHL (ej. calendars, contacts, payments).
    - `/02-concepts`: Conceptos fundamentales para la integración (Límites, Sandbox, Errores).
    - `/03-guides`: Tutoriales basados en escenarios reales de integración.
    - `/04-sdk`: Información sobre SDKs disponibles y bibliotecas de la comunidad.
- `/scripts`: Herramientas de automatización y validación.
    - `ghl_bulk_generator.py`: Motor de generación masiva.
    - `validate_docs.py`: Script de QA para verificar la integridad de la documentación.
- `/internal`: Activos técnicos privados (no recomendados para uso externo).
    - `/raw_data`: Bases de datos JSON y resultados de scraping.

## 📝 Convenciones de Documentos

### Estructura de Documentación de Endpoints
Cada archivo en `docs/01-api-reference/` sigue una estructura estricta (el "Gold Template"):
1. **METADATA**: Método HTTP, URL, Scopes necesarios y requisitos de Auth.
2. **REQUEST**: Tablas detalladas de Headers, Path Parameters, Query Parameters y Body.
3. **RESPONSE**: Esquema JSON formateado y tabla descriptiva de cada campo.
4. **CODE EXAMPLES**: 12 ejemplos funcionales en distintos lenguajes.
5. **NOTES**: Detalles específicos de implementación y "gotchas".

### Convención de Nombres
Los archivos deben nombrarse siguiendo el patrón:
`{verbo}-{recurso-singular}.md` en letras minúsculas y usando `kebab-case`.
*   Correcto: `create-contact.md`, `get-calendar-slot.md`.
*   Incorrecto: `CreateContact.md`, `get_contact.md`.

## 🔍 Guía de Navegación

### Para Desarrolladores Humanos 👨‍💻
- Usa este **STRUCTURE.md** para entender la ubicación de los recursos.
- Utiliza la función de búsqueda de tu editor para localizar endpoints por su nombre de archivo descriptivo.

### Para Agentes de IA (Claude, GPT, etc.) 🤖
- Trata `docs/01-referencia-api/` como la fuente primaria de verdad para esquemas técnicos.
- Consulta `docs/AI_CONTEXT.md` para reglas predefinidas sobre versiones y autenticación.
- Sigue las rutas definidas en este mapa para evitar alucinaciones de archivos inexistentes.


