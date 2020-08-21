inlocuitor='''Unitatea,,Fisa de Magazie,U.M.,,
                S.C. Valenti, Impex S.R.L.,"Material (produs), sortiment, calitate, marca, profil, dimensiune",Furnizor,,
                RO5058275,J05/3962/1993,,Nr Mat,,
                Data,Felul si Numarul,Intrari,Iesiri,Stoc,Data si semnatura de control (Observatii)'''

def inlocuieste(fila):
	a = open(fila, 'r')
	b = a.read()
	a.close()

	rf = b.replace(b[0:82], inlocuitor)

	c = open(fila, 'w')
	d = c.write(rf)
	c.close
lista = os.listdir()
#print(lista)
for item in lista:
	inlocuieste(item)
