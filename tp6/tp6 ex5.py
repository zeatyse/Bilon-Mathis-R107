
def supprimer_accents(texte):
    remplacements = {
        "à": "a", "â": "a", "ä": "a", "á": "a",
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "î": "i", "ï": "i", "ì": "i", "í": "i",
        "ô": "o", "ö": "o", "ò": "o", "ó": "o",
        "ù": "u", "û": "u", "ü": "u", "ú": "u",
        "ç": "c",
        "À": "a", "Â": "a", "Ä": "a", "Á": "a",
        "É": "e", "È": "e", "Ê": "e", "Ë": "e",
        "Î": "i", "Ï": "i",
        "Ô": "o", "Ö": "o",
        "Ù": "u", "Û": "u", "Ü": "u",
        "Ç": "c"
    }

    texte_sans_accents = ""
    for c in texte:
        if c in remplacements:
            texte_sans_accents += remplacements[c]
        else:
            texte_sans_accents += c

    return texte_sans_accents

def nettoyer(texte):
    texte = texte.lower()
    texte = supprimer_accents(texte)

    chaine_epuree = ""
    for c in texte:
        if c.isalpha():    # garde seulement les lettres (a-z)
            chaine_epuree += c

    return chaine_epuree

def est_palindrome(texte):
    propre = nettoyer(texte)
    return propre == propre[::-1]

chaine = input("Entrez un mot ou une phrase : ")

if est_palindrome(chaine):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")