import json
import sys
import time
from deep_translator import GoogleTranslator

def uprint(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()

lang_map = {
    'ra': 'da',
    'le': 'de',
}

with open('new_translations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

source = data['al']

for target_key, lang_code in lang_map.items():
    uprint(f"Translating to {target_key} ({lang_code})...")
    translator = GoogleTranslator(source='en', target=lang_code)
    
    data[target_key] = {}
    count = 0
    
    for k, v in source.items():
        if not v.strip():
            data[target_key][k] = ""
            continue
            
        if k == 'hero-title-aldric':
            if lang_code == 'da': t = "Aldric von Reichel <br/>for <span>Cambria</span>"
            elif lang_code == 'de': t = "Aldric von Reichel <br/>für <span>Cambria</span>"
            data[target_key][k] = t
            continue
            
        try:
            time.sleep(0.1)
            translated = translator.translate(v)
            data[target_key][k] = translated
            count += 1
            if count % 10 == 0:
                uprint(f"  Translated {count} strings for {target_key}...")
        except Exception as e:
            uprint(f"Error on {k}: {e}")
            data[target_key][k] = v

with open('new_translations.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

uprint("Phase 2 done.")
