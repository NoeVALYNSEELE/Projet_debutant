Python 2.7.18 (default, Oct 15 2023, 16:43:11) 
[GCC 11.4.0] on linux2
Type "help", "copyright", "credits" or "license()" for more information.
>>> raw_input()
J'écris une phrase dans pithon!!!
"J'\xc3\xa9cris une phrase dans pithon!!!"
>>> raw_input()
J'écris une phrase dans pithon!!!

''
>>> raw_input()
J'écris une phrase dans pithon!!!

''
>>> 
>>> raw_input()
J'écris une phrase dans pithon

''
>>> raw_input()
J'écris une phrase dans pithon
"J'\xc3\xa9cris une phrase dans pithon"
>>> 
>>> raw_input(Donne-moi un nombre)
SyntaxError: invalid syntax
>>> raw_input("Donne-moi un nombre:")
Donne-moi un nombre: 26
' 26'
>>> raw_input("Propose un nombre : ")
Propose un nombre : 17
'17'
>>> raw_input(mon_invite)

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    raw_input(mon_invite)
NameError: name 'mon_invite' is not defined
>>> mon_invite = "Donne-moi un nombre")
SyntaxError: invalid syntax
>>> mon_invite = "Donne-moi un nombre"
>>> nbr_du__joueur = raw_input(mon_invite)
Donne-moi un nombre26
>>> raw_input(mon_invite)
Donne-moi un nombre26
'26'
>>> mon_invite = "Donne-moi un nombre : ")
SyntaxError: invalid syntax
>>> mon_invite = "Donne-moi un nombre : "
>>> nbr_du_joueur

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    nbr_du_joueur
NameError: name 'nbr_du_joueur' is not defined
>>> nbr_du__joueur
'26'
>>> nbr_du_joueur = raw_input(mon_invite)
Donne-moi un nombre : 26
>>> nbr_du_joueur
'26'
>>> a = 1
>>> a == 1
True
>>> a == 32
False
>>> a=2
>>> a == 1
False
>>> a==2
True
>>> 1==1
True
>>> 2==1
False
>>> 1 = 2
SyntaxError: can't assign to literal
>>> 3/2
1
>>> -3/2
-2
>>> 3/2.0
1.5
>>> a = 2
>>> 3/a
1
>>> 3/float(a)
1.5
>>> a= 1
>>> a+1
2
>>> nbr_du_joueur = raw_input (mon_invite)
Donne-moi un nombre : 26
>>> nbr_du_joueur+1

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    nbr_du_joueur+1
TypeError: cannot concatenate 'str' and 'int' objects
>>> nbr_du_joueur
'26'
>>> nbr_secret = 26
>>> nbr_secret == nbr_du_joueur
False
>>> nbr_secret == int(nbr_du_joueur)
True
>>> int('1.0')

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    int('1.0')
ValueError: invalid literal for int() with base 10: '1.0'
>>> int('1 jour parfais')

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    int('1 jour parfais')
ValueError: invalid literal for int() with base 10: '1 jour parfais'
>>> int('       26       ')
26
>>> if nbr_secret == int(nbr_du_joueur)
SyntaxError: invalid syntax
>>> if nbr_secret == int(nbr_du_joueur):
	print(C'est bien ça!!!!)
	      
SyntaxError: EOL while scanning string literal
>>> if nbr_secret == int(nbr_du_joueur):
	print("C'est bien ça!!!!")

	
C'est bien ça!!!!
>>> 
>>> if 1 == 2:
	print(Correct!)
	
SyntaxError: invalid syntax
>>> if 1 == 2:
	print("Correct!")

	
>>> if 1 == 1:
	print("Correct!")

	
Correct!
>>> if nbr_secret == int(nbr_du_joueur)+1:
	print("Correct!!!")
else:
	print(Faux! Recommence!!!)
	
SyntaxError: invalid syntax
>>> if nbr_secret == int(nbr_du_joueur)+1:
	print("Correct!!!")
else:
	print("Faux! Recommence!!!")

	
Faux! Recommence!!!
>>> if nbr_secret == int(nbr_du_joueur):
	print("
KeyboardInterrupt
>>> if nbr_secret == int(nbr_du_joueur):
	print("Correct!!!")
elif nbr_secret > int(nbr_du_joueur):
	print("Ton nombre est trop petit")
else:
	print("Ton nombre est trop grand")

	
Correct!!!
>>> if nbr_secret == int(nbr_du_joueur)-1:
	print("Correct!!!")
elif nbr_secret > int(nbr_du_joueur):
	print("Ton nombre est trop petit")
else:
	print("Ton nombre est trop grand")

	
Ton nombre est trop grand
>>> if nbr_secret == int(nbr_du_joueur)+1:
	print("Correct!!!")
elif nbr_secret > int(nbr_du_joueur):
	print("Ton nombre est trop petit")
else:
	print("Ton nombre est trop grand")

	
Ton nombre est trop grand
>>> if nbr_secret == int(nbr_du_joueur)-1:
	print("Correct!!!")
elif nbr_secret > int(nbr_du_joueur)-1:
	print("Ton nombre est trop petit")
else:
	print("Ton nombre est trop grand")

	
Ton nombre est trop petit
>>>  a == 3
 
  File "<pyshell#82>", line 1
    a == 3
    ^
IndentationError: unexpected indent
>>> a =
SyntaxError: invalid syntax
>>> a = 3
>>> if a == 1:
	print("a vaut 1!")
elif a == 2 :
	print("a vaut 2!")
elif a == 3:
	print("a vaut 3!")
else:
	print("Je ne sais pas!!!")

	
a vaut 3!
>>> if nbr_secret == int(nbr_du_joueur):
	print("Correct!!!")
elif nbr_secret > int(nbr_du_joueur):
	print("Ton nombre est trop petit")
else:
	print("Ton nombre est trop grand")

	
Correct!!!
>>> nbr_secret = 25
>>> nbr_du_joueur = 26
>>> if nbr_secret == int(nbr_du_joueur):
	print("Correct!!!")
elif nbr_secret > int(nbr_du_joueur):
	print("Ton nombre est trop petit")
else:
	print("Ton nombre est trop grand")

	
Ton nombre est trop grand
>>> nbr_secret = 27
>>> if nbr_secret == int(nbr_du_joueur):
	print("Correct!!!")
elif nbr_secret > int(nbr_du_joueur):
	print("Ton nombre est trop petit")
else:
	print("Ton nombre est trop grand")

	
Ton nombre est trop petit
>>> nbr_secret=26
>>> if nbr_secret == int(nbr_du_joueur):
	print("Correct!!!")
elif nbr_secret > int(nbr_du_joueur):
	print("Ton nombre est trop petit")
else:
	print("Ton nombre est trop grand")

	
Correct!!!
>>> nbr_secret = 30
>>> invite = "Donne-moi un nombre"
>>> while True:
	nbr_du_joueur = raw_input(invite)
if nbr_secret = int(nbr_du_joueur):
	
SyntaxError: invalid syntax
>>> nbr_secret = 30invite = "Donne-moi un nombre"
SyntaxError: invalid syntax
>>> nbr_secret = 30
>>> invite = "Donne-moi un nombre"
>>> while True:
	nbr_du_joueur = raw_input(invite)
        if nbr_secret = int(nbr_du_joueur):
		
SyntaxError: invalid syntax
>>> nbr_secret = 30
>>> invite = "Donne-moi un nombre"
>>> while True:
	nbr_du_joueur = raw_input(invite)
        if nbr_secret == int(nbr_du_joueur):
		print("Correct!!!")
		break
	elif nbr_secret > int(nbr_du_joueur):
		print(Ton nombre est trop petit)
		
SyntaxError: invalid syntax
>>> nbr_secret = 30invite = "Donne-moi un nombre"while True:
	nbr_du_joueur = raw_input(invite)
        if nbr_secret == int(nbr_du_joueur):
		print("Correct!!!")
		break
	elif nbr_secret > int(nbr_du_joueur):
		print("Ton nombre est trop petit")
		
SyntaxError: invalid syntax
>>> nbr_secret = 30
>>> invite = "Donne-moi un nombre"
>>> while True:
	nbr_du_joueur = raw_input(invite)
        if nbr_secret == int(nbr_du_joueur):
		print("Correct!!!")
		break
	elif nbr_secret > int(nbr_du_joueur):
		print("Ton nombre est trop petit")
	else:
		print("Ton nombre est trop grand")

		
Donne-moi un nombre25
Ton nombre est trop petit
Donne-moi un nombre52
Ton nombre est trop grand
Donne-moi un nombre5
Ton nombre est trop petit
Donne-moi un nombre25
Ton nombre est trop petit
Donne-moi un nombre28
Ton nombre est trop petit
Donne-moi un nombre30
Correct!!!
>>> nbr_secret = 30
>>> invite = "Donne-moi un nombre : "
>>> while True:
	nbr_du_joueur = raw_input(invite)
        if nbr_secret == int(nbr_du_joueur):
		print("Correct!!!")
		break
	elif nbr_secret > int(nbr_du_joueur):
		print("Trop petit")
	else:
		print("Trop grand")

		
Donne-moi un nombre : 2
Trop petit
Donne-moi un nombre : 15
Trop petit
Donne-moi un nombre : 20
Trop petit
Donne-moi un nombre : 30
Correct!!!
>>> 
>>> break
SyntaxError: 'break' outside loop
>>> for i in range(3):
	for j in range (3):
		print(str(i)+", "+str(j))
	if i == 1:
		break

	
0, 0
0, 1
0, 2
1, 0
1, 1
1, 2
>>> for i in range(3):
	for j in range (3):
		print(str(i)+", "+str(j))
	if i == 1:
	    break

	
0, 0
0, 1
0, 2
1, 0
1, 1
1, 2
>>> for i in range(3):
	for j in range (3):
		print(str(i)+", "+str(j))
	        if i == 1:
	            break

	        
0, 0
0, 1
0, 2
1, 0
2, 0
2, 1
2, 2
>>> for i in range(3):   #1ère boucle (3 fois)
	for j in range (3):   #2ème boucle  (3 fois dans la boucle 1 (9fois sn break))
		print(str(i)+", "+str(j))  #2ème boucle
	        if i == 1:   #2ème boucle
	            break   #2ème boucle (sort immédiatement de la 2ème boucle/reviens à la 1ère)

	        
0, 0
0, 1
0, 2
1, 0
2, 0
2, 1
2, 2
>>> for i in range(3):  #1ère boucle (3 fois)
	for j in range (3): # 2ème boucle DANS la boucle 1 (3 fois par boucle 1)
		print(str(i)+", "+str(j)) #Idem
	if i == 1: #Fais partie de la boucle 1 mais s'exécute après la boucle 2
	    break  #Idem == cela arrête donc le programme car on sort de la boucle principal (n°1)

	
0, 0
0, 1
0, 2
1, 0
1, 1
1, 2
>>> 
>>> 
>>> import random
>>> random.randint(1,100)
2
>>> help(random.randint)
Help on method randint in module random:

randint(self, a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

>>> random.randint(1,100)
39
>>> 
>>> random.randint(1,100)
27
>>> random.randint(1,100)
59
>>> random.randint(1,100)
65
>>> 
>>> 
>>> random.randint(1,100)
21
>>> random.randint(1,100)
92
>>> 
>>> 
>>> import antigravity
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import random
>>> 
>>> nbr_secret = random.radint(1,100)

Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    nbr_secret = random.radint(1,100)
AttributeError: 'module' object has no attribute 'radint'
>>> nbr_secret = random.randint(1,100)
>>> invite = "Donne-moi un nombre"
>>> while True:
	nbr_du_joueur = raw_input(invite)invite = "Donne-moi un nombre"
	
SyntaxError: invalid syntax
>>> import random
>>> nbr_secret = random.radint(1,100)

Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    nbr_secret = random.radint(1,100)
AttributeError: 'module' object has no attribute 'radint'
>>> import random
>>> nbr_secret = random.randint(1,100)
>>> invite = "Donne-moi un nombre"
>>> while True:
	nbr_du_joueur = raw_input(invite)
	if nbr_secret = nbr_du_joueur:
		
SyntaxError: invalid syntax
>>> pwhile True:
	nbr_du_joueur = raw_input(invite)
	if nbr_secret == nbr_du_joueur:
		
SyntaxError: invalid syntax
>>> while True:
	nbr_du_joueur = raw_input(invite)
	if nbr_secret == nbr_du_joueur:
		print("Bravo c'est ça!!!!")
		break
	elif nbr_secret > nbr_du_joueur:
		print("Plus GRAND!!!")
	else:
		print("Plus petit!!!")

		
Donne-moi un nombre50
Plus petit!!!
Donne-moi un nombre40
Plus petit!!!
Donne-moi un nombre30
Plus petit!!!
Donne-moi un nombre20
Plus petit!!!
Donne-moi un nombre10
Plus petit!!!
Donne-moi un nombre5
Plus petit!!!
Donne-moi un nombre4
Plus petit!!!
Donne-moi un nombre3
Plus petit!!!
Donne-moi un nombre2
Plus petit!!!
Donne-moi un nombre1
Plus petit!!!
Donne-moi un nombre80
Plus petit!!!
Donne-moi un nombre90
Plus petit!!!
Donne-moi un nombre100
Plus petit!!!
Donne-moi un nombre

Traceback (most recent call last):
  File "<pyshell#199>", line 2, in <module>
    nbr_du_joueur = raw_input(invite)
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 1398, in readline
    line = self._line_buffer or self.shell.readline()
KeyboardInterrupt
>>> import random
>>> nbr_secret = random.randint(1,100)
>>> invite = "Donne-moi un nombre : "
>>> while True:
	nbr_du_joueur = raw_input(invite)
	if nbr_secret == nbr_du_joueur:
		print("Bravo c'est ça!!!!")
		break
	elif nbr_secret > nbr_du_joueur:
		print("Plus GRAND!!!")
	else:
		print("Plus petit!!!")

		
Donne-moi un nombre : 50
Plus petit!!!
Donne-moi un nombre : 40
Plus petit!!!
Donne-moi un nombre : 30
Plus petit!!!
Donne-moi un nombre : 0
Plus petit!!!
Donne-moi un nombre : -50
Plus petit!!!
Donne-moi un nombre : -10000000000
Plus petit!!!
Donne-moi un nombre : 

Traceback (most recent call last):
  File "<pyshell#204>", line 2, in <module>
    nbr_du_joueur = raw_input(invite)
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 1398, in readline
    line = self._line_buffer or self.shell.readline()
KeyboardInterrupt
>>> nbr_secret
87
>>> while True:
	nbr_du_joueur = raw_input(invite)
	if nbr_secret == nbr_du_joueur:
		print("Bravo c'est ça!!!!")
		break
	elif nbr_secret > int(nbr_du_joueur):
		print("Plus GRAND!!!")
	else:
		print("Plus petit!!!")

		
Donne-moi un nombre : 50
Plus GRAND!!!
Donne-moi un nombre : 60
Plus GRAND!!!
Donne-moi un nombre : 70
Plus GRAND!!!
Donne-moi un nombre : 80
Plus GRAND!!!
Donne-moi un nombre : 90
Plus petit!!!
Donne-moi un nombre : 85
Plus GRAND!!!
Donne-moi un nombre : 87
Plus petit!!!
Donne-moi un nombre : 86
Plus GRAND!!!
Donne-moi un nombre : 88
Plus petit!!!
Donne-moi un nombre : 87
Plus petit!!!
Donne-moi un nombre : 86
Plus GRAND!!!
Donne-moi un nombre : 86.5

Traceback (most recent call last):
  File "<pyshell#207>", line 6, in <module>
    elif nbr_secret > int(nbr_du_joueur):
ValueError: invalid literal for int() with base 10: '86.5'
>>> nbr_secret
87
>>> while True:
	nbr_du_joueur = raw_input(invite)
	if nbr_secret == int(nbr_du_joueur):
		print("Bravo c'est ça!!!!")
		break
	elif nbr_secret > int(nbr_du_joueur):
		print("Plus GRAND!!!")
	else:
		print("Plus petit!!!")

		
Donne-moi un nombre : 50
Plus GRAND!!!
Donne-moi un nombre : 75
Plus GRAND!!!
Donne-moi un nombre : 80
Plus GRAND!!!
Donne-moi un nombre : 95
Plus petit!!!
Donne-moi un nombre : 90
Plus petit!!!
Donne-moi un nombre : 85
Plus GRAND!!!
Donne-moi un nombre : 87
Bravo c'est ça!!!!
>>> nbr de tentative = 0
SyntaxError: invalid syntax
>>> nbr_de_tentative = 0
>>> while True:
	nbr_du_joueur = raw_input(invite)
	if nbr_secret == int(nbr_du_joueur):
		print("Bravo c'est ça!!!!")
		nbr_de_tentative + 1
		print(nbr_de_tentative)
		break
	elif nbr_secret > int(nbr_du_joueur):
		print("Plus GRAND!!!")
		nbr_de_tentative + 1
	else:
		print("Plus petit!!!")
		nbr_de_tentative +1

		
Donne-moi un nombre : 50
Plus GRAND!!!
1
Donne-moi un nombre : 75
Plus GRAND!!!
1
Donne-moi un nombre : 85
Plus GRAND!!!
1
Donne-moi un nombre : 90
Plus petit!!!
1
Donne-moi un nombre : 88
Plus petit!!!
1
Donne-moi un nombre : 87
Bravo c'est ça!!!!
1
0
>>> while True:
	nbr_du_joueur = raw_input(invite)
	if nbr_secret == int(nbr_du_joueur):
		print("Bravo c'est ça!!!!")
		int(nbr_de_tentative)+ 1
		print(nbr_de_tentative)
		break
	elif nbr_secret > int(nbr_du_joueur):
		print("Plus GRAND!!!")
		int(nbr_de_tentative)+ 1
	else:
		print("Plus petit!!!")
		int(nbr_de_tentative) +1

		
Donne-moi un nombre : 50
Plus GRAND!!!
1
Donne-moi un nombre : 75
Plus GRAND!!!
1
Donne-moi un nombre : 

Traceback (most recent call last):
  File "<pyshell#218>", line 3, in <module>
    if nbr_secret == int(nbr_du_joueur):
ValueError: invalid literal for int() with base 10: ''
>>> 
>>> 
>>> 
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
>>> 
>>> 
