
while True:
  N = int(input("écrit N un enter naturel"))
  if N == 100:
    print("Fin du programme")
    break
  somme = 0
  for i in range(0,N+1):
   somme += i
   print("La somme des entiers de 0 à", N, "est :", somme)

valeurs = []
i = 0
while i < 10:
    v = float(input(f"Entrez une valeur réelle comprise entre 0 et 20 ({i+1}/10): "))
    if 0 <= v <= 20:
        valeurs.append(v)
        i += 1
    else:
        print("La valeur doit être comprise entre 0 et 20. Réessayez.")
nb_inf_10 = 0
nb_10_15 = 0
nb_sup_ou_eq_15 = 0
for v in valeurs:
 if v < 10:
  nb_inf_10 += 1

  nb_10_15 += 1

  nb_sup_ou_eq_15 += 1
print("Nombre de valeurs inférieures strictement à 10:", nb_inf_10)
print("Nombre de valeurs supérieures ou égales à 10 et inférieures strictement à 15:", nb_10_15)
print("Nombre de valeurs supérieures ou égales à 15:", nb_sup_ou_eq_15)
X = float(input("Entrer un nombre X supérieur à 1 : "))
while X <= 1:
    X = float(input("Erreur, entrer un nombre X supéreur à 1 : "))
N = 0
somme = 0
while somme + (N + 1) <= X:
    N += 1
    somme += N
print("Le plus grand N est :", N)
print("La somme est :", somme)

