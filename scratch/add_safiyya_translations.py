import re

with open('scripts/manual_translations.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add to French (ga) - fr dictionary
fr_add = """
    "role-gov-safiyya": "Candidate au poste de Gouverneur",
    "const-gov-safiyya": "National",
    "bio-gov-safiyya": "Candidate au poste de Gouverneur représentant les Indépendants, Safiyya est profondément dévouée au peuple de la République et a passé sa vie à se battre pour ses électeurs.",
"""
content = re.sub(r'(fr = \{)', r'\g<1>' + fr_add, content)

# Add to Spanish (ac) - es dictionary
es_add = """
    "role-gov-safiyya": "Candidata a Gobernadora",
    "const-gov-safiyya": "Nacional",
    "bio-gov-safiyya": "Candidata a Gobernadora en representación de los Independientes, Safiyya está profundamente dedicada al pueblo de la República y ha pasado su vida luchando por sus electores.",
"""
content = re.sub(r'(es = \{)', r'\g<1>' + es_add, content)

# Add to Danish (ra) - da dictionary
da_add = """
    "role-gov-safiyya": "Guvernørkandidat",
    "const-gov-safiyya": "National",
    "bio-gov-safiyya": "Guvernørkandidat, der repræsenterer Uafhængig, er Safiyya dybt engageret i Republikkens folk og har brugt sit liv på at kæmpe for sine vælgere.",
"""
content = re.sub(r'(da = \{)', r'\g<1>' + da_add, content)

# Add to Welsh (cy) - cy dictionary
cy_add = """
    "role-gov-safiyya": "Ymgeisydd Llywodraethwr",
    "const-gov-safiyya": "Cenedlaethol",
    "bio-gov-safiyya": "Ymgeisydd Llywodraethwr yn cynrychioli Annibynnol, mae Safiyya yn ymroddedig iawn i bobl y Weriniaeth ac wedi treulio ei bywyd yn ymladd dros ei hetholwyr.",
"""
content = re.sub(r'(cy = \{)', r'\g<1>' + cy_add, content)

# Add to Latvian (lv) - lv dictionary
lv_add = """
    "role-gov-safiyya": "Gubernatora Kandidāts",
    "const-gov-safiyya": "Nacionālais",
    "bio-gov-safiyya": "Gubernatora kandidāte, kura pārstāv Neatkarīgos, Safiyya ir dziļi veltīta Republikas iedzīvotājiem un ir pavadījusi savu dzīvi, cīnoties par saviem vēlētājiem.",
"""
content = re.sub(r'(lv = \{)', r'\g<1>' + lv_add, content)

# Add to German (de) - de dictionary
de_add = """
    "role-gov-safiyya": "Gouverneurskandidatin",
    "const-gov-safiyya": "National",
    "bio-gov-safiyya": "Gouverneurskandidatin für die Unabhängigen, Safiyya ist den Menschen der Republik zutiefst verbunden und hat ihr Leben lang für ihre Wähler gekämpft.",
"""
content = re.sub(r'(de = \{)', r'\g<1>' + de_add, content)

with open('scripts/manual_translations.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Translations for Safiyya added to manual_translations.py")
