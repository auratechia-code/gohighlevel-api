import os
import re

OUTPUT_DIR = 'final_docs/01-resources'

def validate_docs():
    total_files = 0
    errors = []
    
    required_sections = [
        '## 1. METADATA',
        '## 2. REQUEST',
        '## 3. RESPONSE',
        '## 4. CODE EXAMPLES',
        'Version: 2021-07-28'
    ]
    
    for root, dirs, files in os.walk(OUTPUT_DIR):
        for file in files:
            if file.endswith('.md'):
                total_files += 1
                full_path = os.path.join(root, file)
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    missing = [sec for sec in required_sections if sec not in content]
                    if missing:
                        errors.append(f"{file}: Missing {', '.join(missing)}")
                    
                    if 'N/A' in content and '## 2. REQUEST' in content:
                        # Check if it's too skeletal
                        pass

    print(f"Validation Summary:")
    print(f"Total Files Found: {total_files}")
    print(f"Files with Errors: {len(errors)}")
    
    if errors:
        print("\nTop 10 Errors:")
        for err in errors[:10]:
            print(f"- {err}")

if __name__ == "__main__":
    validate_docs()
