import json
import os
import sys

# Add the tools directory to the path so we can import the generator
sys.path.append(os.path.abspath('tools'))
import ghl_bulk_generator

def test_sample():
    # Load first 5 items from source
    with open('ghl_kb_output_pro/ghl_kb_pro_v7_final.json', 'r', encoding='utf-8') as f:
        full_data = json.load(f)
        data = full_data.get('data', {}).get('endpoint', [])[:5]
    
    # Create temp source for testing
    with open('test_sample.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)
    
    # Update generator constants for test
    ghl_bulk_generator.SOURCE_JSON = 'test_sample.json'
    ghl_bulk_generator.OUTPUT_DIR = 'test_output'
    
    # Run generator
    ghl_bulk_generator.main()
    print("Test generation complete in 'test_output/'")

if __name__ == "__main__":
    # Ensure we are in the right directory
    os.chdir('c:/Users/luaco/OneDrive/Documentos/Dev/gohighlevel-api')
    test_sample()
