import os
import re
import shutil
from pathlib import Path
from datetime import datetime

class DocumentationReorganizer:
    def __init__(self, root_dir: str):
        self.root = Path(root_dir)
        self.endpoints_dir = self.root / "endpoints"
        self.general_dir = self.endpoints_dir / "general"
        self.concepts_dir = self.root / "concept_pages"
        self.summary_file = self.root / "SUMMARY.md"

        # Regex to extract category from source URL
        # Example: https://marketplace.gohighlevel.com/docs/ghl/contacts/get-contacts
        # Result: contacts
        self.source_regex = re.compile(r'source: "https://marketplace\.gohighlevel\.com/docs/ghl/([^/]+)/?.*"')

    def reorganize_endpoints(self):
        print("Reorganizing endpoints...")
        if not self.general_dir.exists():
            print(f"Directory {self.general_dir} not found. Skipping.")
            return

        files_moved = 0
        for md_file in self.general_dir.glob("*.md"):
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            match = self.source_regex.search(content)
            if match:
                category = match.group(1)
                # Ensure category is clean (no -hash if present, though scraper should have handled it)
                category = re.sub(r'-[a-z0-9]{3}$', '', category)
                
                target_dir = self.endpoints_dir / category
                target_dir.mkdir(parents=True, exist_ok=True)
                
                new_path = target_dir / md_file.name
                shutil.move(str(md_file), str(new_path))
                files_moved += 1
            else:
                # Default fallback if no match
                pass
        
        print(f"Moved {files_moved} endpoint files.")

    def reorganize_concepts(self):
        print("Reorganizing concepts...")
        if not self.concepts_dir.exists():
            return

        # Simple grouping for concepts
        groups = {
            "oauth": ["oauth", "access-token", "authorization", "scopes", "token"],
            "guides": ["guide", "tutorial", "started", "step-", "setup"],
            "policies": ["policy", "sandbox", "marketplace"],
            "webhooks": ["webhook"]
        }

        files_moved = 0
        for md_file in self.concepts_dir.glob("*.md"):
            found_group = "general"
            filename_lower = md_file.name.lower()
            
            for group, keywords in groups.items():
                if any(k in filename_lower for k in keywords):
                    found_group = group
                    break
            
            target_dir = self.root / "concepts" / found_group
            target_dir.mkdir(parents=True, exist_ok=True)
            
            new_path = target_dir / md_file.name
            shutil.move(str(md_file), str(new_path))
            files_moved += 1
        
        print(f"Moved {files_moved} concept files.")
        
        # Remove old empty directory if possible
        try:
            if self.concepts_dir.exists() and not any(self.concepts_dir.iterdir()):
                self.concepts_dir.rmdir()
        except Exception:
            pass

    def generate_summary(self):
        print("Generating new SUMMARY.md...")
        summary_content = [
            "# GoHighLevel Documentation Index",
            f"\nGenerated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        ]

        # Process Endpoints
        summary_content.append("## Endpoints")
        sorted_resource_dirs = sorted([d for d in self.endpoints_dir.iterdir() if d.is_dir()])
        
        for res_dir in sorted_resource_dirs:
            # Skip empty general after move
            if res_dir.name == "general" and not any(res_dir.iterdir()):
                continue
                
            summary_content.append(f"### {res_dir.name.replace('-', ' ').title()}")
            files = sorted(res_dir.glob("*.md"))
            for f in files:
                title = self._get_title(f)
                rel_path = f.relative_to(self.root).as_posix()
                summary_content.append(f"* [{title}]({rel_path})")
            summary_content.append("")

        # Process Concepts
        concepts_root = self.root / "concepts"
        if concepts_root.exists():
            summary_content.append("## Concepts")
            for sub_dir in sorted([d for d in concepts_root.iterdir() if d.is_dir()]):
                summary_content.append(f"### {sub_dir.name.title()}")
                files = sorted(sub_dir.glob("*.md"))
                for f in files:
                    title = self._get_title(f)
                    rel_path = f.relative_to(self.root).as_posix()
                    summary_content.append(f"* [{title}]({rel_path})")
                summary_content.append("")

        # Process SDKs, Modules, Policies
        for cat in ["sdks", "modules", "policys"]:
            cat_dir = self.root / cat
            if cat_dir.exists():
                summary_content.append(f"## {cat.title()}")
                files = sorted(cat_dir.glob("*.md"))
                for f in files:
                    title = self._get_title(f)
                    rel_path = f.relative_to(self.root).as_posix()
                    summary_content.append(f"* [{title}]({rel_path})")
                summary_content.append("")

        with open(self.summary_file, "w", encoding="utf-8") as f:
            f.write("\n".join(summary_content))
        print("SUMMARY.md generated successfully.")

    def _get_title(self, file_path: Path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            match = re.search(r'title: "(.*?)"', content)
            if match:
                return match.group(1)
            # Fallback to H1
            match = re.search(r'^# (.*)', content, re.MULTILINE)
            if match:
                return match.group(1).strip()
        except Exception:
            pass
        return file_path.stem.replace("-", " ").title()

if __name__ == "__main__":
    reorganizer = DocumentationReorganizer(".")
    reorganizer.reorganize_endpoints()
    reorganizer.reorganize_concepts()
    reorganizer.generate_summary()
