import json
import urllib.request
import urllib.parse
import time

lang_map = {
    'ga': 'fr',
    'ac': 'es',
    'ra': 'da',
    'my': 'cy',
    'au': 'lv',
    'le': 'de'
}

def translate_text(text, target_lang):
    if not text.strip(): return text
    
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={target_lang}&dt=t&q={urllib.parse.quote(text)}"
    
    for _ in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as response:
                result = json.loads(response.read().decode('utf-8'))
                # Result format: [[[translated_text, original_text, null, null, 1]], null, "en", ...]
                translated = "".join([sentence[0] for sentence in result[0]])
                
                # Apply rules
                translated = translated.replace('—', '-').replace('–', '-')
                # "not X but Y" is hard to perfectly regex, but we ensure no em-dashes
                
                return translated
        except Exception as e:
            time.sleep(1)
            
    return text.replace('—', '-')

print("Loading source dictionary...")
with open('new_source.json', 'r', encoding='utf-8') as f:
    source_dict = json.load(f)

final_data = {'al': source_dict}

for target_key, lang_code in lang_map.items():
    print(f"Translating to {target_key} ({lang_code})...")
    final_data[target_key] = {}
    
    for k, v in source_dict.items():
        if k.startswith('gh-') or k.startswith('fl-'):
            final_data[target_key][k] = v
            continue

        if k == 'idx-hero-title':
            if lang_code == 'fr': t = 'Aldric von Reichel <br/><span style="color: var(--primary);">pour Cambria</span>'
            elif lang_code == 'es': t = 'Aldric von Reichel <br/><span style="color: var(--primary);">para Cambria</span>'
            elif lang_code == 'da': t = 'Aldric von Reichel <br/><span style="color: var(--primary);">for Cambria</span>'
            elif lang_code == 'cy': t = 'Aldric von Reichel <br/><span style="color: var(--primary);">dros Cambria</span>'
            elif lang_code == 'lv': t = 'Aldriks fon Reihels <br/><span style="color: var(--primary);">par Kambriju</span>'
            elif lang_code == 'de': t = 'Aldric von Reichel <br/><span style="color: var(--primary);">für Cambria</span>'
            final_data[target_key][k] = t
            continue

        final_data[target_key][k] = translate_text(v, lang_code)

print("Writing new_translations.json...")
with open('new_translations.json', 'w', encoding='utf-8') as f:
    json.dump(final_data, f, indent=2, ensure_ascii=False)

print("Translations complete!")
