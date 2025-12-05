nom1 = input("Entrez le nom de la première personne : ")
prenom1 = input("Entrez le prénom de la première personne : ")
nom2 = input("Entrez le nom de la deuxième personne : ")
prenom2 = input("Entrez le prénom de la deuxième personne : ")
pers1 = (nom1.upper(), prenom1.capitalize())
pers2 = (nom2.upper(), prenom2.capitalize())
if pers2 < pers1:
    pers1, pers2 = pers2, pers1
print(pers1[1], pers1[0])
print(pers2[1], pers2[0])