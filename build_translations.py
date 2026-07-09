import json
import re

def update_js(filepath, translations):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for lang_code, new_dict in translations.items():
        # Find the block for the language code
        pattern = r"(" + lang_code + r":\s*\{)(.*?)(^\s*\}(,|;|\n))"
        # We need to insert the new keys before the closing brace.
        
        def replacer(match):
            prefix = match.group(1)
            body = match.group(2)
            suffix = match.group(3)
            
            # Create a string of new keys
            added = ""
            for k, v in new_dict.items():
                # Escape quotes
                v_esc = v.replace('"', '\\"').replace('\n', '\\n')
                added += f'    "{k}": "{v_esc}",\n'
                
            # If body already ends with a comma or whitespace, just append
            if body.rstrip().endswith(','):
                return prefix + body + added + suffix
            else:
                return prefix + body + ",\n" + added + suffix

        content = re.sub(pattern, replacer, content, flags=re.MULTILINE | re.DOTALL)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    with open("new_translations.json", "r", encoding="utf-8") as f:
        translations = json.load(f)
    update_js("translations.js", translations)
