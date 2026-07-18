import re
data = open('translations.js').read()

data = re.sub(r'^//.*$', '', data, flags=re.MULTILINE)
data = data.replace('const dictionary = {', '{', 1)
data = re.sub(r'document\.addEventListener.*', '', data, flags=re.DOTALL)
data = data.strip().rstrip(';')

data = re.sub(r'^(\s*)([a-zA-Z0-9_]+):\s*\{', r'\1"\2": {', data, flags=re.MULTILINE)
data = re.sub(r',\s*\}', r'}', data)
data = data.replace(r"\'", "'")

import json
try:
    json.loads(data)
    print("VALID JSON after tweaks!")
except json.JSONDecodeError as e:
    print(e)
    lines = data.split('\n')
    line_idx = e.lineno - 1
    print("ERROR AROUND:")
    start = max(0, line_idx - 3)
    end = min(len(lines), line_idx + 4)
    for i in range(start, end):
        prefix = ">> " if i == line_idx else "   "
        print(f"{prefix}{i+1}: {lines[i]}")

