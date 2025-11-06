nombre=int(input("entrez un nombre entier:"))
if  nombre==0:

        print("le nombre est 0 ")
if nombre >0:
    nombre=nombre%2
    if nombre==0:
        print("le nombre est positif et paire")
    else:
        print("le nombre est positif et impaire")
if nombre <0:
    nombre = nombre%2
    if nombre==0:
        print("le nombre est negatif et paire")
    else:
        print("le nombre est negatif et impaire")
