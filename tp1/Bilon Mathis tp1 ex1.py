Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> nom="Bilon"
>>> prenom="Mathis"
>>> math=17
>>> anglais=16
>>> info=18
>>> promotion=2025
>>> m= (math +  anglais + info ) /3
>>> print m
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print(m)
17.0
>>> type (m)
<class 'float'>
>>> type (nom)
<class 'str'>
>>> type (prenom)
<class 'str'>
>>> type (math)
<class 'int'>
>>> type (anglais)
<class 'int'>
>>> print("l'étudiant", nom, prenom, "de la promotion", promotion, "a une moyenne de", m)
l'étudiant Bilon Mathis de la promotion 2025 a une moyenne de 17.0
