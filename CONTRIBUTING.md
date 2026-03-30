# Contribuyendo a la Documentación de la API de GHL

Gracias por ayudar a mantener la documentación de alta fidelidad para la API de GoHighLevel. Sigue estas pautas para asegurar la consistencia y calidad en todo el repositorio.

## 🛠️ Estándares: La Plantilla de Oro (Gold Template)
Cada archivo de endpoint debe contener las siguientes secciones en orden:

### 1. METADATA
- **Method**: GET/POST/PUT/DELETE
- **URL**: URL completa del endpoint
- **Description**: Resumen conciso de la funcionalidad
- **Scopes**: Scopes de OAuth requeridos
- **Auth**: Tipos de token aceptados (Location, Agency, etc.)

### 2. REQUEST
- **Headers**: Headers obligatorios y opcionales
- **Path Parameters**: Tabla con nombre, tipo, obligatorio (S/N) y descripción
- **Query Parameters**: Tabla con nombre, tipo, obligatorio y descripción
- **Body Parameters**: Esquema completo para peticiones POST/PUT/PATCH

### 3. RESPONSE
- **Schema**: Estructura JSON formateada y limpia
- **Field Table**: Descripción manual de cada clave en la respuesta JSON

### 4. CODE EXAMPLES
Proporcionar ejemplos funcionales en:
- cURL, Node.js (Axios), Python (Requests), PHP (Guzzle), Java, Go, Ruby, C#, Swift, Dart, PowerShell, Rust.

## 📁 Naming & Ubicación de Archivos
- **Ruta**: `docs/01-referencia-api/{categoría}/{verbo}-{recurso}.md`
- **Nombres**: Usar `kebab-case` en minúsculas. Eliminar caracteres ilegales para Windows: `|`, `:`, `*`, `?`, `"`, `<`, `>`, `\`.

## 🚀 Flujo de Trabajo

### Añadir un Nuevo Endpoint
1. Identifica la categoría del recurso.
2. Crea el archivo Markdown siguiendo la Plantilla de Oro.
3. Valida la estructura ejecutando `python scripts/validate_docs.py`.
4. Realiza el commit con un mensaje descriptivo en español.

### Actualizar un Endpoint Existente
1. Localiza el archivo en `docs/01-referencia-api/`.
2. Actualiza la sección específica (ej. añadiendo un nuevo parámetro de consulta).
3. Asegura que el esquema de respuesta siga siendo preciso.
4. Valida y realiza el commit.

## 🧪 Control de Calidad (QA)
Antes de enviar tus cambios, ejecuta:
```bash
python scripts/validate_docs.py
```
Este script verifica que no falten secciones y que las tablas estén bien formadas.


