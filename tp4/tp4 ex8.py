etudiant1 = {
    "firstname": "Mathis",
    "name": "Bilon",
    "promo": 2025,
    "group": "RT121"
}

print(f"votre nom est '{etudiant1['name']}', prénom est '{etudiant1['firstname']}', vous faites partie de la promo '{etudiant1['promo']}' et votre groupe est '{etudiant1['group']}'\n")

print("Les clés du dictionnaire sont :")
for key in etudiant1.keys():
    print(f"-{key}")

print("\nLes valeurs du dictionnaire sont :")
for value in etudiant1.values():
    print(f"-{value}")

print("\nLes tuplets du dictionnaire sont :")
for item in etudiant1.items():
    print(f"-{item}")

etudiant2 = {
    "firstname": "Nicolas",
    "name": "Kunegel",
    "promo": 2025,
    "group": "RT121"
}

binome = {
    1: etudiant1,
    2: etudiant2
}

print("\nLes étudiants formant le binôme sont :")
for id_etudiant, info in binome.items():
    print(f"- L'étudiant {info['name']} {info['firstname']} du groupe {info['group']}")