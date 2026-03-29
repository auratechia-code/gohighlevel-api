import json
import os
import sys

# Set encoding to UTF-8 for printing
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

inventory_path = r'C:\Users\luaco\AppData\Local\Temp\full_inventory.json'
if not os.path.exists(inventory_path):
     inventory_path = '/tmp/full_inventory.json'

try:
    with open(inventory_path, 'r', encoding='utf-8') as f:
        inventory = json.load(f)
except:
    with open(inventory_path, 'r', encoding='utf-16le') as f:
        inventory = json.load(f)

groups = {}
for item in inventory:
    p = item['Path'].replace('/', os.sep).replace('\\', os.sep)
    parts = p.split(os.sep)
    
    # Logic to find the first relevant directory after 'gohighlevel-api'
    try:
        base_idx = -1
        for i, part in enumerate(parts):
            if part == 'gohighlevel-api':
                base_idx = i
                break
        
        if base_idx != -1 and base_idx + 1 < len(parts):
            group = parts[base_idx + 1]
        else:
            group = 'Root'
    except:
        group = 'Unknown'
    
    if group not in groups:
        groups[group] = {'count': 0, 'size': 0}
    
    groups[group]['count'] += 1
    groups[group]['size'] += item['SizeKB']

print(f"{'Directory':<25} | {'Files':<8} | {'Size (KB)':<12}")
print("-" * 50)
for g in sorted(groups.keys()):
    data = groups[g]
    print(f"{g:<25} | {data['count']:<8} | {data['size']:<12.2f}")
