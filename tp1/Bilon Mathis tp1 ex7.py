print("Donner les trois nombres entiers x1, x2 et x3 : ")
x1 = int(input("valeur de x1"))
x2 = int(input("valeur de x2"))
x3 = int(input("valeur de x3"))
condition = (x1 > x2) or (x3 < x1)
if(condition) :
    print(str(condition)+" = VRAI")
else :
    print(str(condition)+" = FAUX")
