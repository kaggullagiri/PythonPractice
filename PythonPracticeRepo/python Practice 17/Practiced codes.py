
# worked on idle environment

'''s='giri kaggulla'
s.upper()
'GIRI KAGGULLA'
s.lower()
'giri kaggulla'
s.capitalize()
'Giri kaggulla'
s.title()
'Giri Kaggulla'
s.digit()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.digit()
AttributeError: 'str' object has no attribute 'digit'. Did you mean: 'isdigit'?
s.swapcase()
'GIRI KAGGULLA'
b='gIRI Kaggulla 123@56'
b.upper()
'GIRI KAGGULLA 123@56'
b.lower()
'giri kaggulla 123@56'
b.capitalize()
'Giri kaggulla 123@56'
b.swapcase()
'Giri kAGGULLA 123@56'
b[0].upper()
'G'
b[4].upper()
' '
b[0].lower()
'g'
b[0].swapcase()
'G'
b[1:7:1].upper()
'IRI KA'
b[-2:-8:-1].lower()
'5@321 '
b[-6:-12:-1].lower()
'1 allu'
'''
>>> b[::2].swapcase()
'Gr AGLA135'
>>> b.islower()
False
>>> b.isupper()
False
>>> b.istitle()
False
>>> b[0].isupper()
False
>>> b[1].isupper()
True
>>> b[0].islower()
True
>>> b[0:4:1].istitle()
False

>>> b.isaplha()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    b.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
>>> c='GoodMorning'
>>> c.isalpha()
True
>>> c.isnum()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    c.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
>>> c.isalnum()
True
>>> c[0:6:1].isalnum()
True
>>> c[0:4:1].isdigit()
False
>>> c[0:4:2].isspace()
False
>>> d='good morning'
>>> d.isalpha()
False
>>> d.isdigit()
False
>>> d.isalnum()
False
>>> d[4].isspace()
True
'''