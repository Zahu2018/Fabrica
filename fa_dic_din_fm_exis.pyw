#     +------------------------------------------------------------------+
#     | PROGRAMUL CREAZA UN DICTIONAR DIN FISELE DE MAGAZIE DEJA EXISTENTE |
#     | DIN FOLDERE (Capse, Piele, Sireturi, etc)                        |
#     +------------------------------------------------------------------+
#     +------------------------------------------------------------------+
#     |                         Author: Zah                              |
#     +------------------------------------------------------------------+
#     +------------------------------------------------------------------+
#     | versiunea 1  - versiunea de baza                                 |
#     +------------------------------------------------------------------+

import os

# 1 FIND THE PATH OF CURRENT WORKING DIRECTORY
# 1 cwd = os.getcwd() # cwd = current working directory
cwd = "D:\\Valenti\\2018\\Fise_Magazie"
#print(cwd)

# 2 READ IN A LIST ONLY FOLDERS IN CWD
# 1 lista_foldere_FM =  [d for d in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, d))]
lista_foldere_FM =  [d for d in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, d))]
print(lista_foldere_FM)

# 3 MAKE A DICTIONARY OF ALL fm IN ALL FOLDERS: 
# unde fisa de magazie e key si folderul e value
# ex: 'IO 10 ML SILBER':'Capse'
dic_fm = {} # dictionarul cu fise de magazie
for a in lista_foldere_FM:
	if a == '__pycache__':
		pass
	else:
		path = (cwd + '\\' + a)
		b = os.listdir(path)
		print(b)
		for fm in b:
			dic_fm[fm.split('.')[0]] = a

# 4 MAKE A FILE WITH THIS DICTIONARY
e = open('dict_fm.py', 'w')
f = e.write("dictionar_fm = "+str(dic_fm))
e.close
print(dic_fm)

