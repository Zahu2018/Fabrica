# 	=S T O C U R I=
# Face un dictionar din numele fisierelor si stocul actual
# Il scrie in fila rezultat_stocuri.csv
import os

def preia_stocul(fila):
	myfile = fila
	myvar = open(myfile, 'r')
	lst = myvar.readlines()
	myva = lst[len(lst)-1]
	a = myva.split(',')
	stoc = a[-2]
	myvar.close()
	#print (myva)
	#print (a)
	#print (stoc)
	return(stoc)
def fa_lista_din_numele_fisierelor(loc):
	import os
	lista_file = []
	m = (os.listdir(loc))
	for x in m:
		if x[-4] == ".":
			lista_file.append(x)
	print(lista_file)
	return(lista_file)
	
def main():
	locatie = 'D:\\Valenti\\2018\\Fise_Magazie\\'
	a = input('Introduceti categoria: ')
	locatie_1 = locatie + a
	b = fa_lista_din_numele_fisierelor(locatie_1)
	tabel = {}
	for c in b:
		x = preia_stocul(c)
		tabel[c] = x
		
	print(tabel)
main()
