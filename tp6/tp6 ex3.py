def ajouter_elt(lst=[0,1,2], elt=3):
    print("ID de lst :", id(lst))
    lst.append(elt)
    return lst
print(ajouter_elt())
print(ajouter_elt())
print(ajouter_elt())

def ajouter_carac(ch="abc", elt="d"):
    print("ID de ch :", id(ch))
    return ch + elt
print(ajouter_carac())
print(ajouter_carac())
