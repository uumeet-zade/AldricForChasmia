import re

with open('scripts/manual_translations.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '"bio-gov-safiyya": "Candidate au poste de Gouverneur représentant les Indépendants, Safiyya est profondément dévouée au peuple de la République et a passé sa vie à se battre pour ses électeurs.",',
    '"bio-gov-safiyya": "Candidate indépendante au poste de Gouverneur, Safiyya est profondément dévouée au peuple de la République et a passé sa vie à se battre pour ses électeurs.",'
)

content = content.replace(
    '"bio-gov-safiyya": "Candidata a Gobernadora en representación de los Independientes, Safiyya está profundamente dedicada al pueblo de la República y ha pasado su vida luchando por sus electores.",',
    '"bio-gov-safiyya": "Candidata independiente a Gobernadora, Safiyya está profundamente dedicada al pueblo de la República y ha pasado su vida luchando por sus electores.",'
)

content = content.replace(
    '"bio-gov-safiyya": "Guvernørkandidat, der repræsenterer Uafhængig, er Safiyya dybt engageret i Republikkens folk og har brugt sit liv på at kæmpe for sine vælgere.",',
    '"bio-gov-safiyya": "Uafhængig guvernørkandidat, Safiyya er dybt engageret i Republikkens folk og har brugt sit liv på at kæmpe for sine vælgere.",'
)

content = content.replace(
    '"bio-gov-safiyya": "Ymgeisydd Llywodraethwr yn cynrychioli Annibynnol, mae Safiyya yn ymroddedig iawn i bobl y Weriniaeth ac wedi treulio ei bywyd yn ymladd dros ei hetholwyr.",',
    '"bio-gov-safiyya": "Fel ymgeisydd annibynnol ar gyfer Llywodraethwr, mae Safiyya yn ymroddedig iawn i bobl y Weriniaeth ac wedi treulio ei bywyd yn ymladd dros ei hetholwyr.",'
)

content = content.replace(
    '"bio-gov-safiyya": "Gubernatora kandidāte, kura pārstāv Neatkarīgos, Safiyya ir dziļi veltīta Republikas iedzīvotājiem un ir pavadījusi savu dzīvi, cīnoties par saviem vēlētājiem.",',
    '"bio-gov-safiyya": "Kā neatkarīga gubernatora kandidāte, Safiyya ir dziļi veltīta Republikas iedzīvotājiem un ir pavadījusi savu dzīvi cīnoties par saviem vēlētājiem.",'
)

content = content.replace(
    '"bio-gov-safiyya": "Gouverneurskandidatin für die Unabhängigen, Safiyya ist den Menschen der Republik zutiefst verbunden und hat ihr Leben lang für ihre Wähler gekämpft.",',
    '"bio-gov-safiyya": "Als unabhängige Gouverneurskandidatin ist Safiyya den Menschen der Republik zutiefst verbunden und hat ihr Leben lang für ihre Wähler gekämpft.",'
)

with open('scripts/manual_translations.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated bio translations for Safiyya.")
