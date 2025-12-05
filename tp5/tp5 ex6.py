def taille_chaine(T):
    c = 0
    for _ in T:
        c += 1
    return c
def pourcentage_voyelles(T):
    voyelles = "aeiouyAEIOUY"
    nb_voyelles = 0
    taille = 0
    for c in T:
        taille += 1
        if c in voyelles:
            nb_voyelles += 1

    if taille == 0:
        return 0
    return (nb_voyelles / taille) * 100
def trouver_wagon(T):
    motif = "wagon"
    n = taille_chaine(T)
    m = taille_chaine(motif)
    for i in range(n - m + 1):
        j = 0
        while j < m and T[i + j] == motif[j]:
            j += 1
        if j == m:
            return i
    return -1
def nb_occurrences_wagon(T):
    motif = "wagon"
    n = taille_chaine(T)
    m = taille_chaine(motif)
    compte = 0
    for i in range(n - m + 1):
        j = 0
        while j < m and T[i + j] == motif[j]:
            j += 1
        if j == m:
            compte += 1
    return compte
phrases = [
    "Le wagon bleu est rapide.",
    "Un petit wagon roule vite.",
    "Le ciel est bleu, comme un wagon.",
    "Wagon après wagon, le train avance.",
    "Il y a cinq wagons dans le train.",
    "La locomotive tire les wagons.",
    "Wagon, wagon, wagon, ciel bleu.",
    "Le train avance avec ses wagons.",
    "Un wagon rouge file à toute vitesse.",
    "Le wagon jaune transporte des marchandises."
]
for phrase in phrases:
    print("Phrase :", phrase)
    print("Taille :", taille_chaine(phrase))
    print("Pourcentage de voyelles : {:.2f}%".format(pourcentage_voyelles(phrase)))
    pos = trouver_wagon(phrase.lower())
    print("Première ccurrence de 'wagon' :", pos if pos != -1 else "Aucune")
    nb = nb_occurrences_wagon(phrase.lower())
    print("Nombre d'occurrences : ", nb)
    print("-" * 50)