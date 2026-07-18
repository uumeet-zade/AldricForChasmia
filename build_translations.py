import json

def update_js(filepath, translations):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for lang_code, new_dict in translations.items():
        # Find the block for the language code
        block_start_str = f"{lang_code}: {{"
        block_start = content.find(block_start_str)
        if block_start == -1:
            continue
            
        next_block = content.find("\n  },", block_start)
        if next_block == -1:
            next_block = content.find("\n  }\n};", block_start)
        
        if next_block != -1:
            added = ""
            for k, v in new_dict.items():
                v_esc = v.replace('"', '\\"').replace('\n', '\\n')
                added += f'    "{k}": "{v_esc}",\n'
                
            content = content[:next_block] + ",\n" + added + content[next_block:]
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    with open("new_translations.json", "r", encoding="utf-8") as f:
        translations = json.load(f)
    update_js("translations.js", translations)
