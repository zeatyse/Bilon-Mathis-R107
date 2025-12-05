import os.path
from datetime import datetime
fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du second fichier : ")
date1 = date2 = None
if os.path.isfile(fichier1):
    taille1 = os.path.getsize(fichier1)
    date1 = os.path.getmtime(fichier1)
    print(f"\nLe fichier {fichier1} existe.")
    print(f"  → Taille : {taille1} octets")
    print(f"  → Dernière modification : {datetime.fromtimestamp(date1)}")
else:
    print(f"\nLe fichier {fichier1} n'existe pas.")
if os.path.isfile(fichier2):
    taille2 = os.path.getsize(fichier2)
    date2 = os.path.getmtime(fichier2)
    print(f"\nLe fichier {fichier2} existe.")
    print(f"  → Taille : {taille2} octets")
    print(f"  → Dernière modification : {datetime.fromtimestamp(date2)}")
else:
    print(f"\nLe fichier {fichier2} n'existe pas.")
if date1 is not None and date2 is not None:
    if date1 > date2:
        print(f"\nLe fichier le plus récent est {fichier1}, modifié le {datetime.fromtimestamp(date1)}")
    elif date2 > date1:
        print(f"\nLe fichier le plu récent est {fichier2}, modifié le {datetime.fromtimestamp(date2)}")
    else:
        print(f"\nLes dux fichiers ont été modifiés à la même date : {datetime.fromtimestamp(date1)}")