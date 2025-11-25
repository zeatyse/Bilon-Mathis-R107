nombre=float(input("vous cherchez la table dee multiplication de quel nombre ?"))
resultat=[]

for i in range(10):
    note=nombre*i
    resultat.append(note)

for i in range(10):
    print(f"{nombre} * {i} = {resultat[i]}")