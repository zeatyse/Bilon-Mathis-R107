nMax= 3
v1= []
v2= []
produit_scalaire=0
n=int(input("entrez la valeur de la taille effective des vecteurs"))
if 1<n<nMax+1:
    print("Saisie du premier vecteur")
    for i in range(n):
        composante=float(input(f"v1[{i}]="))
        v1.append(composante)
    print("Saisie du deuxieme vecteur")
    for i in range(n):
        composante=float(input(f"v2[{i}]="))
        v2.append(composante)
    for i in range(n):
        produit_scalaire +=v1[i] * v2[i]
    print(f"le produit scalaire de v1 par v2 vaut {produit_scalaire}")
else:
    print("entrez a nouveau une valeur")
