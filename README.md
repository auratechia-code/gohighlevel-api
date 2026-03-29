# GHL API Documentation Library

Welcome to the comprehensive GoHighLevel (GHL) API Documentation Library. This repository is maintained by **Scalefy System** and serves as the single source of truth for technical integration with the GHL ecosystem.

## 📂 Repository Structure

- `docs/01-api-reference/`: High-fidelity documentation for 588+ API endpoints, including 12-language code examples and response schemas.
- `docs/02-concepts/`: Core concepts of the GHL API (Auth, Sandbox, Rate Limits, etc.).
- `docs/03-guides/`: Module-specific integration guides and tutorials.
- `docs/04-sdk/`: References for official and community SDKs.
- `scripts/`: Internal tools for documentation generation and validation.
- `internal/raw_data/`: Source JSON knowledge bases and raw scraping data.

## 🔍 How to Find an Endpoint

Documentation follows a strict naming convention: `docs/01-api-reference/{resource}/{verb}-{resource}.md`.
Example: To find how to create a contact, look for `docs/01-api-reference/contacts/create-contact.md`.

## 🛠️ Key Conventions

- **Base URL**: `https://services.leadconnectorhq.com`
- **Mandatory Header**: `Version: 2021-07-28`
- **Authentication**: Bearer Token (OAuth Access Token or Private Integration Token).

## 📖 Related Documents

- [Navigation Map](STRUCTURE.md)
- [AI Context for LLMs](docs/AI_CONTEXT.md)
- [Contribution Guidelines](CONTRIBUTING.md)
