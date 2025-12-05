import random
def generer(nbr, vmin, vmax):
    table = []
    for _ in range(nbr):
        table.append(random.randint(vmin, vmax))
    return table

def combienInferieur(table, vseuil):
    compteur = 0
    for val in table:
        if val < vseuil:
            compteur += 1
    return compteur
nb = int(input("Combien de valeurs voulez-vous générer ? "))
vmin = int(input("Valeur minimale (vmin) : "))
vmax = int(input("Valeur maximale (vmax) : "))
rep = input("Vous voulez préciser le seuil ? (Oui/O ou Non/N) : ")
if rep.upper() in ("OUI", "O"):
    vseuil = int(input("Quel seuil souhaitez-vous utiliser ? "))
else:
    vseuil = 30
    print("Seuil par défaut 30 appliqué.")
print(f"\nGénération de {nb} valeurs entre {vmin} et {vmax}...")
tab = generer(nb, vmin, vmax)
tab.sort()
print("Tableau généré et trié :")
print(tab)
total = combienInferieur(tab, vseuil)
print(f"\nIl y en a {total} inférieurs à {vseuil}.")