def est_bissextile(a):
    return (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)
def verification_date(date):
    i = 0
    for x in date:
        i += 1
        if x < '0' or x > '9':
            print("Format incorrect, utilisz 8 chiffres jjmmaaaa.")
            return
    if i != 8:
        print("Format incorrect, utilisez 8 chiffres jjmmaaaa.")
        return
    jj = int(date[0] + date[1])
    mm = int(date[2] + date[3])
    aaaa = int(date[4] + date[5] + date[6] + date[7])

    if mm < 1 or mm > 12:
        print("Mois incorrect.")
        return
    if mm == 2:
        jour_max = 29 if est_bissextile(aaaa) else 28
    elif mm in [4, 6, 9, 11]:
        jour_max = 30
    else:
        jour_max = 31

    if jj < 1 or jj > jour_max:
        print("Jour incorrect.")
        return
    print(f"La date {date} est corecte.")

date_input = input("Veuillez sisir une date au format jjmmaaaa : ")
verification_date(date_input)
