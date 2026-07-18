import json

source = json.load(open('new_source.json', 'r'))

keys_to_translate = [k for k in source.keys() if not (k.startswith('gh-') or k.startswith('fl-'))]
# Let's print the keys we actually need to translate
print("Keys to translate:", keys_to_translate)
print("Count:", len(keys_to_translate))
