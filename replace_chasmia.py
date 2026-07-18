import os
import re

files_to_process = ['new_translations.json', 'translations.js']

for filepath in files_to_process:
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, not found.")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace Chasmia -> Cambria
    content = content.replace('Chasmia', 'Cambria')
    content = content.replace('chasmia', 'cambria')
    content = content.replace('CHASMIA', 'CAMBRIA')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filepath}")
