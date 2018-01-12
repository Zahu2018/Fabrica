#	SERAFIL SITUATION FROM FEINPLANUNG.CSV
#	DESCRIERE:
'''

'''
#	v_0: 
#	v_1: Am adaugat interfata grafica la program
#	v_2: Am adaugat posibilitatea de a apasa Enter in loc de click pe buttonul "Calculeaza"
###################################
#    A program written by: Zah    #
###################################

from tkinter import *

#	Deschidem fisierul in variabila a

with open("D:\\Valenti\\2017\\Feinplanung.csv", 'r') as f: # se schimba anul
	a = f.read()
	f.close

#	Creaza GUI, main windows pt. aplicatie
root = Tk()
root.title("SERAFIL SITUATION")
root.geometry("250x300")
#root.overrideredirect(0)



#	Functia calculeaza / realizeaza toate operatiile pentru
# a putea obtine rezultatul dorit
def calculeaza():
	search = entry.get()

	


# Transforma un text intr-o lista de linii, fiecare linie fiind o lista
	
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
		if str(item[8]).isupper():
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

# Idendificam indexul SEARCH:_ in linie si adunam
	suma = 0
	pozitii = 0
	for mat in L: #pentru matrice in Lista de matrice
		if search in mat[0]:
			ind = mat[0].index(search) # indexul
			l = len(mat) # lungimea matricei, nr. de elemente
			for i in range(2, l):
				pozitie = 0 # incepe numararea de blocuri; pozitie = block
				pozitie += l-2 # pozitie = block
							
				m = mat[i][ind] #i=linia din matrice, ind=index SEARCH
				suma += float(m)
				#print(m, '===', suma) # arata fiecare pozitie in parte

		else:
			continue
		pozitii += pozitie	# pozitii = nr. de blockuri
	r = 	(search, "=", suma, "m", "in", pozitii, 'blockuri')	# rezultatul printat in GUI
	#print ('\n\n', search, ' = ', suma, 'm in', pozitii, 'blocks') # rezultatul printat in cmd
	rez.set(r)
	
	#rez = StringVar()
	#label_e = Label(root, textvariable = rez)
	#label_e.pack()



root.bind("<Return>", calculeaza)
# GUI
label = Label(root, text = 'Introduceti serafil (culoare/grosime)')
label.pack()
entry = Entry(root)
entry.pack()
buton = Button(root, text = 'Calculeaza', command = lambda: calculeaza())
buton.pack()

label_d = Label(root, text = "Rezultate: ")
label_d.pack()

rez = StringVar()
Label(root, textvariable = rez).pack()
root.bind("<Return>", lambda event: calculeaza())


entry.focus()

root.mainloop()