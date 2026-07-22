import json
import re

# 1. Update data/new_source.json
source_file = '/Users/umidgasimzade/Documents/GitHub/VoteSDA!/data/new_source.json'
with open(source_file, 'r', encoding='utf-8') as f:
    source = json.load(f)

source['modal-refer-publishing'] = "Refer to their respective publishings for campaigning and media events."
source['modal-view-events'] = "View Events"
source['modal-view-media'] = "View Media"

with open(source_file, 'w', encoding='utf-8') as f:
    json.dump(source, f, indent=2, ensure_ascii=False)

# 2. Update scripts/manual_translations.py
manual_file = '/Users/umidgasimzade/Documents/GitHub/VoteSDA!/scripts/manual_translations.py'
with open(manual_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove escaped quotes \" from "auto-candidates-11"
# The line looks like: "auto-candidates-11": "\"No cambies de caballo a mitad del rio!\" Candidata presidencial...",
content = re.sub(r'("auto-candidates-11": ")\\"(.*?)\\"(.*?)"', r'\1\2\3"', content)

# Add new keys before the end of each dictionary block.
# Finding "}" followed by the next section header.

fr_add = '''    "modal-refer-publishing": "Consultez leurs publications respectives pour les événements de campagne et médiatiques.",
    "modal-view-events": "Voir les Événements",
    "modal-view-media": "Voir les Médias",
}'''
content = content.replace("}\n\n# SPANISH", fr_add + "\n\n# SPANISH")

es_add = '''    "modal-refer-publishing": "Consulte sus respectivas publicaciones para eventos de campaña y medios.",
    "modal-view-events": "Ver Eventos",
    "modal-view-media": "Ver Medios",
}'''
content = content.replace("}\n\n# DANISH", es_add + "\n\n# DANISH")

da_add = '''    "modal-refer-publishing": "Se deres respektive udgivelser for kampagne- og mediebegivenheder.",
    "modal-view-events": "Se Begivenheder",
    "modal-view-media": "Se Medier",
}'''
content = content.replace("}\n\n# WELSH", da_add + "\n\n# WELSH")

cy_add = '''    "modal-refer-publishing": "Cyfeiriwch at eu cyhoeddiadau priodol ar gyfer ymgyrchu a digwyddiadau cyfryngau.",
    "modal-view-events": "Gweld Digwyddiadau",
    "modal-view-media": "Gweld y Cyfryngau",
}'''
content = content.replace("}\n\n# LATVIAN", cy_add + "\n\n# LATVIAN")

lv_add = '''    "modal-refer-publishing": "Skatiet to attiecīgās publikācijas par kampaņām un mediju pasākumiem.",
    "modal-view-events": "Skatīt Pasākumus",
    "modal-view-media": "Skatīt Medijus",
}'''
content = content.replace("}\n\n# GERMAN", lv_add + "\n\n# GERMAN")

de_add = '''    "modal-refer-publishing": "Konsultieren Sie die jeweiligen Veröffentlichungen für Wahlkampf- und Medienveranstaltungen.",
    "modal-view-events": "Veranstaltungen Ansehen",
    "modal-view-media": "Medien Ansehen",
}'''
content = content.replace("}\n\n# ===== BUILD FINAL DATA", de_add + "\n\n# ===== BUILD FINAL DATA")

with open(manual_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modal translations added and Mandy quotes removed.")
