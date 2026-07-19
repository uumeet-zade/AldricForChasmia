import re

with open('translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any sequence of newline followed by a bare comma with just a comma
content = re.sub(r',\n\s*,', ',', content)
content = re.sub(r'\"\s*\n\s*,', '",\n', content)
content = re.sub(r'\n,\n', ',\n', content)

# A specific fix for the error:
# "ev-back": "Back to Trail",
# ,
# "nav-name": "Social Democratic Alliance",
content = re.sub(r',\s*\n\s*,', ',\n', content)

with open('translations.js', 'w', encoding='utf-8') as f:
    f.write(content)

