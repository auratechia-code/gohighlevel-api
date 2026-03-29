import os
from pathlib import Path

def extract_urls(root_dir):
    urls = set()
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                path = Path(root) / file
                content = path.read_text(encoding="utf-8")
                # Intenta encontrar el source_url en el frontmatter o contenido
                # Buscamos patrones como "https://marketplace.gohighlevel.com/docs/..."
                found = re.findall(r'https://marketplace\.gohighlevel\.com/docs/[a-zA-Z0-9\-\/\_]+', content)
                for url in found:
                    urls.add(url.strip().rstrip(")"))
    return sorted(list(urls))

if __name__ == "__main__":
    import re
    base = Path("c:/Users/luaco/OneDrive/Documentos/Dev/gohighlevel-api/endpoints")
    all_urls = extract_urls(base)
    with open("ghl_docs_urls.txt", "w", encoding="utf-8") as f:
        for url in all_urls:
            f.write(url + "\n")
    print(f"Extraídas {len(all_urls)} URLs.")
