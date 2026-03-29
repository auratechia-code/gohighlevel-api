import os
import re
import json

class SupplementalParser:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.body_params = {} # Map (method, path) -> list of params
        self.errors = {}      # Map code -> schema

    def parse_all(self):
        self._parse_body_params()
        self._parse_errors()
        return {
            "body_params": self.body_params,
            "errors": self.errors
        }

    def _parse_body_params(self):
        bp_dir = os.path.join(self.base_dir, 'body-params')
        if not os.path.exists(bp_dir): return

        for filename in os.listdir(bp_dir):
            if not filename.endswith('.md'): continue
            path = os.path.join(bp_dir, filename)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find patterns like "## Create Appointment (POST /path/)"
            sections = re.split(r'##\s+', content)
            for section in sections:
                header_match = re.search(r'([A-Za-z\s]+)\s*\(`(GET|POST|PUT|PATCH|DELETE)\s+([^`\s\)]+)`\)', section)
                if header_match:
                    method = header_match.group(2).upper()
                    ep_path = header_match.group(3).strip().rstrip('/')
                    
                    # Extract table
                    table_match = re.search(r'\|.*\|(\n\|.*\|)+', section)
                    if table_match:
                        table_text = table_match.group(0)
                        params = self._parse_table(table_text)
                        self.body_params[(method, ep_path)] = params

    def _parse_errors(self):
        error_file = os.path.join(self.base_dir, 'errors', 'base_schemas.md')
        if not os.path.exists(error_file): return
        
        with open(error_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find ### 400 Bad Request ... ```json ... ```
        error_sections = re.split(r'###\s+', content)
        for section in error_sections:
            match = re.search(r'(\d{3})\s+.*\n.*\n```json\n(.*?)\n```', section, re.DOTALL)
            if match:
                code = match.group(1)
                schema = json.loads(match.group(2))
                self.errors[code] = schema

    def _parse_table(self, table_text):
        lines = [l.strip() for l in table_text.split('\n') if l.strip()]
        if len(lines) < 2: return []
        
        headers = [h.strip() for h in lines[0].split('|')[1:-1]]
        params = []
        for line in lines[2:]:
            cols = [c.strip() for c in line.split('|')[1:-1]]
            if len(cols) >= len(headers):
                row = {headers[i]: cols[i] for i in range(len(headers))}
                # Standardize to generator's expected format
                params.append({
                    "name": row.get('Field', '').replace('`', ''),
                    "type": row.get('Type', ''),
                    "required": "YES" in row.get('Required', '').upper(),
                    "description": row.get('Description', '')
                })
        return params

if __name__ == "__main__":
    parser = SupplementalParser('scraped_v2')
    res = parser.parse_all()
    # Save for generator to use
    with open('data-agregated/SUPPLEMENTAL_DATA.json', 'w', encoding='utf-8') as f:
        # Convert tuple keys to string for JSON
        serializable = {
            "body_params": {f"{k[0]} {k[1]}": v for k, v in res['body_params'].items()},
            "errors": res['errors']
        }
        json.dump(serializable, f, indent=2)
    print("Supplemental data parsed successfully.")
