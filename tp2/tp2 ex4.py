BASE=4
fromage=800.0
eau=2
ail=2
pain=400
nbconvives=int(input("Entrez le nombre de personne (s) conviées à la fondue :"))
nouvelleQuantite_fromage=fromage*nbconvives / BASE
nouvelleQuantite_eau=eau*nbconvives / BASE
nouvelleQuantite_ail=ail*nbconvives / BASE
nouvelleQuantite_pain=pain*nbconvives / BASE
print("pour faire une fondue fribourgeoise pour 3 personnes, il vous faut:")
print("-",nouvelleQuantite_fromage,"gr de fromage")
print("-",nouvelleQuantite_eau,"dl d'eau")
print("-",nouvelleQuantite_ail,"gousse(s) d'ail")
print("-",nouvelleQuantite_pain,"gr de pain")