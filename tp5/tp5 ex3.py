chaine = input("Entre un mot ou une phrase : ")
chaine = chaine.lower()
chaine_epuree = ""
for c in chaine:
    if c.isalpha():
        chaine_epuree += c
if chaine_epuree == chaine_epuree[::-1]:
    print("C'est un palndrome !")
else:
    print("Ce n'est pas un palndrome.")
