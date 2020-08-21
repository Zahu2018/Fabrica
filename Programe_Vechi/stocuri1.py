# 	=S T O C U R I=
# Face un dictionar din numele fisierelor si stocul actual
# Il scrie in fila rezultat_stocuri.csv
import os
import csv

def preia_stocul(fila):
	myfile = fila
	myvar = open(myfile, 'r')
	lst = myvar.readlines()
	ll = len(lst)
	
	myva = lst[ll-1]
	a = myva.split(',')
	stoc = a[-2]
	myvar.close()
	#print (myva)
	#print (a)
	#print (stoc)
	return(stoc)
def fa_lista_din_numele_fisierelor():
	import os
	lista_file = []
	m = (os.listdir())
	for x in m:
		if x[-4] == ".":
			lista_file.append(x)
		else:
			pass
	#print(lista_file)
	return(lista_file)

def scrie_in_fila(tab):
	with open('stocuri.csv', 'wb') as f:
		w = csv.DictWriter(f, tab.keys())
		w.writeheader()
		w.writerow(tab)
		f.close()
	
def main():
	locatie = 'D:\\Valenti\\2018\\Fise_Magazie\\'
	a = input('Introduceti categoria: ')
	locatie_1 = locatie + a + '\\'
	print(locatie_1)
	b = fa_lista_din_numele_fisierelor()
	

	tabel = {}
	for c in b:
		x = preia_stocul(c)
		tabel[c] = x
		
	print(tabel)
	#scrie_in_fila(tabel)
main()
