liste = [5, 2, 4, 8, 1, 3]
print(liste)
n = 0
for x in liste:
    n += 1
i = 0
while i < n:
    min_index = i
    j = i + 1
    while j < n:
        if liste[j] < liste[min_index]:
            min_index = j
        j += 1
    liste[i], liste[min_index] = liste[min_index], liste[i]
    print(liste)
    i += 1
