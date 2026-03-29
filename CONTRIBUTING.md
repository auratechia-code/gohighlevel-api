# Contributing to GHL API Docs

Thank you for helping maintain the high-fidelity documentation for the GoHighLevel API. Follow these guidelines to ensure consistency and quality.

## 🛠️ Standards: The Gold Template
Every endpoint file must contain the following sections in order:

### 1. METADATA
- **Method**: GET/POST/PUT/DELETE
- **URL**: Full endpoint URL
- **Description**: Concise summary
- **Scopes**: Required OAuth scopes
- **Auth**: Token types accepted

### 2. REQUEST
- **Headers**: Mandatory and optional headers
- **Path Parameters**: Table with name, type, required (Y/N), and description
- **Query Parameters**: Table with name, type, required, and description
- **Body Parameters**: Full table for POST/PUT/PATCH requests

### 3. RESPONSE
- **Schema**: Prettified JSON structure
- **Field Table**: Description of every key in the response

### 4. CODE EXAMPLES
Provide functional examples in:
- cURL, Node.js (Axios), Python (Requests), PHP (Guzzle), Java, Go, Ruby, C#, Swift, Dart, PowerShell, Rust.

## 📁 File Naming & Location
- **Path**: `docs/01-api-reference/{category}/{verb}-{resource}.md`
- **Naming**: Use lowercase kebab-case. Remove illegal characters for Windows: `|`, `:`, `*`, `?`, `"`, `<`, `>`, `\`.

## 🚀 Workflow

### Adding a New Endpoint
1. Identify the resource category.
2. Create the Markdown file following the Gold Template.
3. Validate the structure using `python scripts/validate_docs.py`.
4. Commit changes with a descriptive message.

### Updating an Existing Endpoint
1. Locate the file in `docs/01-api-reference/`.
2. Update the specific section (e.g., adding a new query parameter).
3. Ensure the response schema remains up to date.
4. Validate and commit.

## 🧪 Documentation QA
Before submitting, run:
```bash
python scripts/validate_docs.py
```
This script checks for missing sections and malformed tables.
