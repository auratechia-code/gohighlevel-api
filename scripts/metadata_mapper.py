import json

def extract_scopes(source_json_path):
    with open(source_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    scopes_table = {}
    for entry in data:
        # Looking for the entry that contains "docs/Authorization/Scopes"
        if "docs/Authorization/Scopes" in entry.get('url', ''):
            for table in entry.get('tables', []):
                # The table with "Scope" and "API Endpoints"
                if 'Scope' in table.get('headers', []) and 'API Endpoints' in table.get('headers', []):
                    current_scope = None
                    for row in table.get('rows', []):
                        scope = row.get('Scope', '').replace('Â', '').strip()
                        if scope and scope != '':
                            current_scope = scope
                        
                        endpoint_raw = row.get('API Endpoints', '').strip()
                        if endpoint_raw:
                            # e.g., "GET /businesses"
                            parts = endpoint_raw.split(' ')
                            if len(parts) >= 2:
                                method = parts[0]
                                path = parts[1]
                                key = f"{method} {path}"
                                scopes_table[key] = {
                                    "scope": current_scope,
                                    "auth_type": "OAuth 2.0 / Private Integration", # Standard
                                    "token_type": row.get('Access Type', '').strip()
                                }
    return scopes_table

if __name__ == "__main__":
    scopes = extract_scopes('data-agregated/ALL_DOCS.json')
    with open('data-agregated/SCOPES_MAP.json', 'w') as f:
        json.dump(scopes, f, indent=2)
    print(f"Extracted {len(scopes)} scopes to data-agregated/SCOPES_MAP.json")
