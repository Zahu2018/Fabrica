# serafil, pivot table, feniplanung
# Face un tabel pivotant cu toate serafil
# Florian Zah
# 24.05.2019
#	SERAFIL PIVOT TABLE FROM Feinplanung.csv
#	v_0: Serafil pivot table
#		v_0.1: Transforma valoarea finala din 'float' in 'integer' (nu ne intereseaza in cm)
#	v_1: Sorteaza alfabetic ===== IN FUTURE
#	v_2: Add GUI (grafic user interface) ====== IN FUTURE



#from tkinter import *

#	Deschidem fisierul in variabila a

with open("Feinplanung.csv", 'r') as f: # se schimba anul
	a = f.read() #citim in variabila "a" fisierul 'Feinplanung.csv'
	f.close

#	Functia calculeaza / realizeaza toate operatiile pentru
# a putea obtine rezultatul dorit
def calculeaza():
	# Transforma un text intr-o lista de linii, fiecare linie fiind o lista (o lista de liste)

	initial = 0
	nr = a.count('\n')
	lista = []
	for i in range(nr):
		final = a.find('\n', initial)
		lin = a[initial:final]
		lin_lista = lin.split(',')
		lista.append(lin_lista)
		initial = final + 1
	#print(lista)

# Facem o lista de matrice sau o lista de liste de liste
	L = [] # lista de matrice
	M = [] # matrice
	for item in lista:
		if str(item[9]).isupper():
			if M != []:
				L.append(M)
			else:
				pass
			M = []
			M.append(item)
		else:
			M.append(item)
	M.append(item)
	L.append(M)
	#print(L)

# Facem un dictionar cu Serafil
	dicti = {}
	for mat in L:
		for item in mat[0]:
			if "/" in item and " " not in item:
				ind = mat[0].index(item) # gasim indexul fiecarui item cu "/" si fara " " (spatiu)
				#print(item, ' = ', ind)
				l = len(mat) # lungimea (inaltimea) matricei in linii
				for i in range(2 , l):
					suma = 0
					suma_i=0
					m = mat[i][ind] #
					try:
						sm = float(m)
						suma += sm
						suma_i += int(suma)
						if item in dicti:
							var = int(dicti.get(item))  # a fost float???
							suma_i += var
							dicti[item] = suma_i
						else:
							dicti[item] = suma_i
					except:
						print('nu pot converti in float', item)



	#print(dicti)
	listare = ''
	for item in dicti:
		lis = ''
		lis = (str(item) + "," + str(dicti.get(item)))
		#print(item, " = ", (dicti.get(item)))
		listare += str(lis) + '\n'
	print(listare)

	var=open("Situatie_Serafil.csv", 'w') #numerele trebuie convertite in siruri inainte de scriere in fisier [str()]
	var.write(listare)
	var.close()





calculeaza()
