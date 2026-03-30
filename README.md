# Biblioteca de Documentación de la API de GoHighLevel (GHL)

¡Bienvenido! Esta es la fuente de verdad definitiva para integraciones técnicas con el ecosistema de **GoHighLevel (GHL)**. Repositorio mantenido por **Scalefy System**.

Este recurso ha sido diseñado para ser ultra-legible tanto para desarrolladores humanos como para agentes de inteligencia artificial (Claude, GPT, Cursor, etc.).

---

## 📑 Índice de Navegación

1. [Estructura del Repositorio](#-estructura-del-repositorio)
2. [Guía de Inicio Rápido](#-inicio-rápido)
3. [Cómo Buscar un Endpoint](#-cómo-buscar-un-endpoint)
4. [Convenciones Técnicas](#-convenciones-técnicas)
5. [Documentos Relacionados](#-documentos-relacionados)

---

## 📂 Estructura del Repositorio

Para mantener el orden y la escalabilidad, el repositorio se organiza de la siguiente manera:

- `docs/01-referencia-api/`: Documentación de alta fidelidad para **588+ endpoints**, incluyendo ejemplos en 12 lenguajes y esquemas de respuesta.
- `docs/02-conceptos/`: Conceptos fundamentales (Autenticación, Sandbox, Límites de Tasa, etc.).
- `docs/03-guias/`: Guías de integración por módulos y tutoriales paso a paso.
- `docs/04-sdk/`: Referencias para SDKs oficiales y de la comunidad.
- `scripts/`: Herramientas internas para validación y generación de documentos.
- `internal/`: Activos técnicos privados y bases de datos crudas (JSON).

---

## 🚀 Inicio Rápido

Para empezar a trabajar con la API 2.0 de GHL:

1. **Autenticación**: GHL utiliza OAuth 2.0. Necesitarás un `access_token` válido.
2. **Header Obligatorio**: Todas las peticiones **DEBEN** incluir el header `Version: 2021-07-28`.
3. **Base URL**: `https://services.leadconnectorhq.com`

---

## 🔍 Cómo Buscar un Endpoint

Seguimos una convención de nombres estricta para facilitar la búsqueda:
`docs/01-referencia-api/{categoría}/{verbo}-{recurso}.md`

*   **Ejemplo**: Para crear un contacto: `docs/01-referencia-api/contacts/create-contact.md`.
*   **Ejemplo**: Para listar calendarios: `docs/01-referencia-api/calendars/list-calendars.md`.

---

## 🛠️ Convenciones Clave

- **Fidelidad AI**: Cada página incluye esquemas JSON reales para que tu IA no alucine.
- **Ejemplos Multilenguaje**: Disponibles en cURL, Node.js, Python, PHP, Java, Go, Rust, y más.
- **Actualización**: Basado en el último "scrape" oficial de la documentación de GHL.

---

## 📖 Documentos Relacionados

- [Mapa Detallado de Estructura](STRUCTURE.md)
- [Contexto para Agentes de IA](docs/AI_CONTEXT.md)
- [Guía de Contribución](CONTRIBUTING.md)

---
© 2026 Scalefy System. Todos los derechos reservados.
