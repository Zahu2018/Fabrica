'''
 PROGRAM CARE EXTRAGE STOCUL DIN FISIERELE XLS
'''

def rezolva(a):
	dictionar_aviz = {}
	for i in a:
		for j in sheet:
			if sheet[8] != 0:
				a = preia numele filei
				b = preia valoarea stocului
				dictionar_aviz[a] = b
			else:
				pass
	return dictionar_aviz

		

def meniu_categorii():
	print('1. Piele')
	print('2. Sintetice')
	print('3. Toate')
	a = input()
	if a == '1':
		lista = ['piele.xls', 'captuseala_piele.xls']
	elif a == '2':
		lista = ['piele_sintetica.xls', 'captuseala_sintetica.xls']
	elif a == '3':
		lista = ['piele.xls', 'captuseala_piele.xls','piele_sintetica.xls', 'captuseala_sintetica.xls']
	else:
		print('Introduceti 1, 2 sau 3')
		meniu_categorii()
	return lista


def main():
	a = meniu_categorii()
	b = rezolva(a) # b = dictionar_aviz
	print('Vrei sa salvezi rezultatul intr-un fisier?')
	print('Apasa D sau d pentru "da" si N sau n pentru "nu"')
	c = input()
	if c == 'd' or c == 'D':
		d = open('rezultat.txt', 'w')
		d.write(b)
		d.close()
		for key, value in b:
			print (key, value)
	elif c == 'n' or c =='N':
		for key, value in b:
			print (key, value)

main()