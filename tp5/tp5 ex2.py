notes = []
coeffs = []
print("Saisie des notes et coefficients ")
for i in range(1, 6):
    entree = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")
    valeur = entree.split(" ")
    note = float(valeur[0])
    coeff = int(valeur[1])
    notes.append(note)
    coeffs.append(coeff)
somme_ponderee = 0
somme_coeffs = sum(coeffs)
for i in range(5):
    somme_ponderee += notes[i] * coeffs[i]
moyenne = somme_ponderee / somme_coeffs
admis = moyenne > 10 or min(notes) >= 8
print("\n=== Résultats ===")
print(f"Moyenne générale : {moyenne:.2f}")
if admis:
    print("L'étudiant est ADMIS.")
else:
    print("L'étudiant n'est PAS admis.")