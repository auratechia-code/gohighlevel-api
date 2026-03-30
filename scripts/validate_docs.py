import os
from pathlib import Path

BASE_DIR = Path("c:/Users/luaco/OneDrive/Documentos/Dev/gohighlevel-api")
OUTPUT_DIR = BASE_DIR / "docs" / "01-referencia-api"

def validate_docs():
    total_files = 0
    errors = []
    
    # New pattern for checking essential blocks
    required_patterns = [
        "---", # Metadata start
        "### Estructura del Endpoint",
        "### Ejemplos de Implementación",
        "````carousel", # Our special code examples block
        "### Respuestas",
        "© 2026 Scalefy System"
    ]
    
    for root, dirs, files in os.walk(OUTPUT_DIR):
        for file in files:
            if file.endswith('.md'):
                total_files += 1
                full_path = os.path.join(root, file)
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    missing = [sec for sec in required_patterns if sec not in content]
                    if missing:
                        errors.append(f"{file}: Faltan {', '.join(missing)}")

    print(f"Resumen de Validación (Nuevo Formato):")
    print(f"Total de archivos encontrados: {total_files}")
    print(f"Archivos con errores: {len(errors)}")
    
    if errors:
        print("\nPrimeros 10 errores:")
        for err in errors[:10]:
            print(f"- {err}")
    else:
        print("\n✨ ¡Todos los archivos cumplen con el estándar AuraTechia!")

if __name__ == "__main__":
    validate_docs()
