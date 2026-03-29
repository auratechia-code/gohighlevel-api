# Repository Structure Map

This document provides a detailed navigation guide for the GHL API documentation repository, optimized for both developers and AI agents.

## 📁 Directory Tree

- `/docs`: Root documentation folder.
    - `/01-api-reference`: 588+ high-fidelity endpoint docs.
        - `/{category}/`: Endpoints grouped by GHL resource (e.g., calendars, contacts, payments).
    - `/02-concepts`: Fundamental concepts for API integration.
    - `/03-guides`: Scenario-based integration walkthroughs.
    - `/04-sdk`: Information on available SDKs and libraries.
- `/scripts`: Automation and validation tools.
    - `ghl_bulk_generator.py`: The bulk generation engine.
    - `validate_docs.py`: QA script to verify documentation integrity.
- `/internal`: Private technical assets.
    - `/raw_data`: Source JSON knowledge bases and scraping results.

## 📝 Document Conventions

### Endpoint Documentation Structure
Every file in `docs/01-api-reference/` follows a consistent structure:
1. **METADATA**: HTTP Method, Scopes, and Auth requirements.
2. **REQUEST**: Header, Path, Query, and Body parameter tables.
3. **RESPONSE**: Prettified JSON schema and field-level description table.
4. **CODE EXAMPLES**: 12 functional examples in various programming languages.
5. **NOTES**: Implementation-specific details.

### Concept Documentation Table
| File | Topic |
| :--- | :--- |
| `02-concepts/sandbox.md` | Testing in the GHL Sandbox environment. |
| ... | (Refer to the individual files in the folder for more depth). |

## 🔍 Navigation Guide

### For Human Developers
- Use this **STRUCTURE.md** to understand where resources are located.
- Search for specific resources by following the `{verb}-{resource}.md` pattern.

### For AI Agents (Claude, Cursor, etc.)
- Treat `docs/01-api-reference/` as the primary source of truth for technical schemas.
- Refer to `docs/AI_CONTEXT.md` for pre-defined rules regarding versioning and authentication.
