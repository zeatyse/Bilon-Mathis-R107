import time
n = int(input("Entrez un nombre entier positif : "))
while n < 0:
    n = int(input("Erreur ! Entrez un nombre entier positif : "))
print("\nCompte à rebours avec 'for' :")
for i in range(n, -1, -1):
    print(i)
    time.sleep(1)
print("Fin du compte à rebours !")
import time
n = int(input("Entrez un nombre entier positif : "))
while n < 0:
    n = int(input("Erreur ! Entrez un nombre enier positif : "))
print("\nCompte à rebours avec 'while' :")
i = n
while i >= 0:
    print(i)
    time.sleep(1)
    i -= 1
print("Fin du comte à rebours !")