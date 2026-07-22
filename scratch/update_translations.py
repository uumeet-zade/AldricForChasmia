import re

file_path = "/Users/umidgasimzade/Documents/GitHub/VoteSDA!/scripts/manual_translations.py"
with open(file_path, "r") as f:
    content = f.read()

replacements = [
    (r'"const-gov-safiyya": "National",\s*"bio-gov-safiyya": "Candidate indépendante au poste de Gouverneur, Safiyya est profondément dévouée au peuple de la République et a passé sa vie à se battre pour ses électeurs."',
     '"const-gov-safiyya": "Reno",\n    "bio-gov-safiyya": "Candidate indépendante au poste de Gouverneur de Reno. Elle est la candidate de choix de la SDA."'),
    
    (r'"const-gov-safiyya": "Nacional",\s*"bio-gov-safiyya": "Candidata independiente a Gobernadora, Safiyya está profundamente dedicada al pueblo de la República y ha pasado su vida luchando por sus electores."',
     '"const-gov-safiyya": "Reno",\n    "bio-gov-safiyya": "Candidata Independiente a la Gubernatura de Reno. Ella es la candidata elegida por el SDA."'),

    (r'"const-gov-safiyya": "National",\s*"bio-gov-safiyya": "Uafhængig guvernørkandidat, Safiyya er dybt engageret i Republikkens folk og har brugt sit liv på at kæmpe for sine vælgere."',
     '"const-gov-safiyya": "Reno",\n    "bio-gov-safiyya": "Uafhængig kandidat til guvernørposten i Reno. Hun er SDA\'s foretrukne kandidat."'),
     
    (r'"const-gov-safiyya": "Cenedlaethol",\s*"bio-gov-safiyya": "Fel ymgeisydd annibynnol ar gyfer Llywodraethwr, mae Safiyya yn ymroddedig iawn i bobl y Weriniaeth ac wedi treulio ei bywyd yn ymladd dros ei hetholwyr."',
     '"const-gov-safiyya": "Reno",\n    "bio-gov-safiyya": "Ymgeisydd Annibynnol ar gyfer Llywodraethwr Reno. Hi yw dewis ymgeisydd yr SDA."'),
     
    (r'"const-gov-safiyya": "Nacionālais",\s*"bio-gov-safiyya": "Kā neatkarīga gubernatora kandidāte, Safiyya ir dziļi veltīta Republikas iedzīvotājiem un ir pavadījusi savu dzīvi cīnoties par saviem vēlētājiem."',
     '"const-gov-safiyya": "Reno",\n    "bio-gov-safiyya": "Neatkarīga Reno gubernatora kandidāte. Viņa ir SDA izvēlētā kandidāte."'),
     
    (r'"const-gov-safiyya": "National",\s*"bio-gov-safiyya": "Als unabhängige Gouverneurskandidatin ist Safiyya den Menschen der Republik zutiefst verbunden und hat ihr Leben lang für ihre Wähler gekämpft."',
     '"const-gov-safiyya": "Reno",\n    "bio-gov-safiyya": "Unabhängige Kandidatin für das Gouverneursamt von Reno. Sie ist die Wunschkandidatin der SDA."')
]

for old, new in replacements:
    content = re.sub(old, new, content)

with open(file_path, "w") as f:
    f.write(content)

print("Updated manual_translations.py")
