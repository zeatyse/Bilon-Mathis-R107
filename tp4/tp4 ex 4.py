L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
max = 0
plus_frequent = None

for x in L1:
    occ = L1.count(x)
    if occ > max:
        max = occ
        plus_frequent = x

print(f"Le nombre le plus frequent dans la liste est le : {plus_frequent} ({max} x)")
