import random
x = random.randint(0, 100)
print("J'ai choisi un nombre entre 0 et 100. À vus de deiner !")
trouve = False
compteur = 0
while not trouve:
    essai = int(input("Votre proposition : "))
    compteur += 1
    if essai < x:
        print("C'est plus grand.")
    elif essai > x:
        print("C'est plus petit.")
    else:
        print(f"Bravo ! Vous avez trouvé le nombre mystère ({x}) en {compteur} tentatives.")
        trouve = True