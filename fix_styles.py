import os

files = [
    'index.html',
    'platform.html',
    'events.html',
    'event-guildhall.html',
    'event-field.html',
    'event-littlewood.html'
]

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Logo swap - Nav
    content = content.replace(
        '<img class="nav-logo"\n        src="SDAlogo.svg"\n        alt="Social Democratic Alliance Logo" />',
        '<img class="nav-logo logo-light" src="SDAlogo.svg" alt="Social Democratic Alliance Logo" />\n      <img class="nav-logo logo-dark" src="SDAlogo-dark.svg" alt="Social Democratic Alliance Logo" />'
    )
    
    # Logo swap - Footer
    content = content.replace(
        '<img\n          src="SDAlogo.svg"\n          alt="Social Democratic Alliance" />',
        '<img class="logo-light" src="SDAlogo.svg" alt="Social Democratic Alliance" />\n        <img class="logo-dark" src="SDAlogo-dark.svg" alt="Social Democratic Alliance" />'
    )

    # Inline styles strip
    content = content.replace('color: white;', '')
    content = content.replace('color: rgba(255,255,255,0.9);', 'opacity: 0.9;')
    content = content.replace('background: rgba(255, 255, 255, 0.03);', 'background: var(--glass-bg);')
    content = content.replace('background: linear-gradient(135deg, rgba(217,4,41,0.1) 0%, rgba(0,0,0,0) 100%);', 'background: var(--bento-gradient);')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
print("Done inline replacements!")
