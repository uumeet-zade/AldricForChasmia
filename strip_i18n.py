import os
import re

allowed_keys = {
    'marquee',
    'footer-name',
    'footer-motto',
    'footer-copy',
    'floating-cta'
}

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    def repl(match):
        key = match.group(1)
        if key in allowed_keys:
            return match.group(0) # Keep it
        return '' # Remove it

    new_content = re.sub(r'\s*data-i18n="([^"]+)"', repl, content)

    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")

