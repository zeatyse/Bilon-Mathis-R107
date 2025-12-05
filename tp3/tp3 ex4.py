n = int(input("Entrez un entier positif n : "))
while n < 0:
    n = int(input("Veuillez entrer un entier positif : "))
choix = input("Choisissez le type de boucle ('for' ou 'while') : ")
while choix not in ['for', 'while']:
    choix = input("Erreur. Reprécisez : 'for' ou 'while' ? ")
fact = 1
if choix == 'for':
    print("\nCalcul de la factorielle de", n, "avec la boucle 'for' :")
    for i in range(1, n+1):
        fact *= i
        print(f"Après multiplication par {i}, factorielle = {fact}")
elif choix == 'while':
    print("\nCalcul de la factorielle de", n, "avec la boucle 'while' :")
    i = 1
    while i <= n:
        fact *= i
        print(f"Après multiplication par {i}, factorielle = {fact}")
        i += 1
print(f"\nLa factorielle de {n} est {fact}")