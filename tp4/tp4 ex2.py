
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
note = []
somme=0
temp=0
if 0<nombreEtudiants :
    for i in range(nombreEtudiants):
        temp=float(input(f"quel est la note de l étudiant {i}"))
        if 0<temp<20:
            note.append(temp)
            somme += temp
        else:
            print("entrez une note valable")
else:
    print("entre un nombre d'étudiant valable")
moyenne= somme/nombreEtudiants
print("moyenne de classe=", moyenne)
print("numero de l'étudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart= note[i]-moyenne
    print(f"{i} | {note[i]} |{ecart} ")