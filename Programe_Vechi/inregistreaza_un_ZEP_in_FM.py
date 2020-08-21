#	SCRIE UN ZEP IN FISE DE MAGAZIE
###################################
#    A program written by: Zah    #
###################################


from tkinter import *
from tkinter import filedialog



#	Deschidem fisierul ::: def open_file():
#	Facem table pivotant ::: def calculeaza(a)



def open_file():

	fila = filedialog.askopenfilename()
	fila1 = (str(fila)).replace('/', '\\')
	#print(fila1)
	b = open(fila1, 'r')
	c = b.read()
	b.close
	#print(c)

	calculeaza(c)
#	Functia calculeaza / realizeaza toate operatiile pentru
# a putea obtine rezultatul dorit
def calculeaza(a):
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
			if item.isnumeric() == False:
				ind = mat[0].index(item) # gasim indexul fiecarui item cu "/" si fara " " (spatiu)
				#print(item, ' = ', ind)
				l = len(mat) # lungimea (inaltimea) matricei in linii
				for i in range(1 , l):  #
					suma = 0
					suma_i=0
					m = mat[i][ind] #
					try:
						sm = float(m)
						suma += sm
						suma_i += suma
						if item in dicti:
							var = round(float(dicti.get(item)), 2)
							suma_i += var
							dicti[item] = round(suma_i, 2)
						else:
							dicti[item] = round(suma_i, 2)
					except:
						print('nu pot converti in float', item)



	print(dicti)
# Verificam daca exista creata fisa de magazie
# Creem LOG
# Daca da SCRIEM
# Daca nu Scriem in LOG
# Daca e minus Scriem in LOG
# Daca e plus la materiale EXCEPT: ate,  scriem in log




	



app = Tk()
app.title("Pivot Table din ZEP - single file")
app.geometry("200x100")
label = Label(app, text = 'Programul inregistreaza un ZEP\nin fisele de magazie.')
label.grid(row=0)
bu = Button(app, text='Alege un ZEP', command=open_file)
bu.grid(row=1)
app.mainloop()

