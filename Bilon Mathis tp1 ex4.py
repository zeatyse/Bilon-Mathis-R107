Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> x = "Sa"
>>> y = x+"lut"
>>> print y
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print(y)
Salut
>>> y = y+"\n\tCesar"
>>> print(y)
Salut
	Cesar
>>> x+= "lut "+"Jules
SyntaxError: unterminated string literal (detected at line 1)
>>> x+= "lut "+"Jules"
>>> print(x)
Salut Jules
>>> y = len(x)
>>> print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print(x)
Salut Jules
>>> print(y)
11
>>> y = len("BonjourJuju")
>>> print (y)
11
>>> y = "Salut! "*2
>>> print (y)
Salut! Salut! 
>>> x = len(y)
>>> print (y)
Salut! Salut! 
>>> y.strip()
'Salut! Salut!'
>>> y= y.strip()
>>> print (y)
Salut! Salut!
