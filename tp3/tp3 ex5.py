def demander_heure(message):
    heure_str = input(message)
    est_num = True
    vide = True
    i = 0
    for i in heure_str:
        vide = False
        if not (i >= '0' and i <= '9'):
            est_num = False
    if not est_num or vide:
        print("Les heures doivent être comprises entre 0 et 24 !")
        return -1
    heure = int(heure_str)
    return heure

def calculer_tarif(heure_debut, heure_fin):
    heures_tarif1 = 0
    heures_tarif2 = 0
    for h in range(heure_debut, heure_fin):
        if (0 <= h < 7) or (17 <= h < 24):
            heures_tarif1 += 1
        elif 7 <= h < 17:
            heures_tarif2 += 1
    return heures_tarif1, heures_tarif2
while True:
    debut = demander_heure("Donnez l’heure de début de la location (un entier) : ")
    if debut == -1:
        continue
    fin = demander_heure("Donnez l’heure de fin de la loction (un entier) : ")
    if fin == -1:
        continue

    if not (0 <= debut <= 24) or not (0 <= fin <= 24):
        print("Les heures doivent être comrises entre 0 et 24 !")
        continue
    if debut == fin:
        print("Attention ! l’heure de fin est identique à l’heure de début.")
        continue
    if debut > fin:
        print("Attention ! le début de la location est après la fin ...")
        continue
    heures_tarif1, heures_tarif2 = calculer_tarif(debut, fin)
    print("Vous avez loué votre vélo pendant")
    if heures_tarif1 != 0:
        print(f"{heures_tarif1} heure(s au tarif horaire de 1.0 euro(s)")
    if heures_tarif2 != 0:
        print(f"{heures_tarif2} heure(s) au tarif horaire de 2.0 euro(s)")
    montant = heures_tarif1 * 1.0 + heures_tarif2 * 2.0
    print(f"Le montant total à payer st de {montant:.1f} euro(s).")
    break