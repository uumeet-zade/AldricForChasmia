import json
import sys
from deep_translator import GoogleTranslator

lang_map = {
    'ga': 'fr',
    'ac': 'es',
    'ra': 'da',
    'my': 'cy',
    'au': 'lv',
    'le': 'de'
}

with open('new_translations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

source = data['al']

for target_key, lang_code in lang_map.items():
    print(f"Translating to {target_key} ({lang_code})...")
    translator = GoogleTranslator(source='en', target=lang_code)
    
    data[target_key] = {}
    
    for k, v in source.items():
        if not v.strip():
            data[target_key][k] = ""
            continue
            
        if k == 'hero-title-aldric':
            if lang_code == 'fr': t = "Aldric von Reichel <br/>pour <span>Cambria</span>"
            elif lang_code == 'es': t = "Aldric von Reichel <br/>para <span>Cambria</span>"
            elif lang_code == 'da': t = "Aldric von Reichel <br/>for <span>Cambria</span>"
            elif lang_code == 'cy': t = "Aldric von Reichel <br/>dros <span>Cambria</span>"
            elif lang_code == 'lv': t = "Aldriks fon Reihels <br/>par <span>Kambriju</span>"
            elif lang_code == 'de': t = "Aldric von Reichel <br/>für <span>Cambria</span>"
            data[target_key][k] = t
            continue
            
        # Temporarily hide quotes to prevent weird formatting if needed, but googletrans handles them fine.
        try:
            translated = translator.translate(v)
            data[target_key][k] = translated
        except Exception as e:
            print(f"Error on {k}: {e}")
            data[target_key][k] = v # fallback

with open('new_translations.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Done translating JSON. Rebuilding JS...")
