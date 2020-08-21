# antet, fise magazie, fm, inlocuieste
# Inlocuieste antetul din fise de magazie
# 14.06.2019
# Florian Zah

import os

def fa_lista_cu_csvuri():
	'''Citeste dintr-un dir toate filele; returneaza doar csv-uri'''

	lista_fisiere_csv = []
	lista = os.listdir()
	for item in lista:
		if '.csv' in item:
			lista_fisiere_csv.append(item)
			nume = item.replace('.csv', '')
			#print('SUCCESS! - {}'.format(nume))
		else:
			print('\nFAIL! - {}\n'.format(item))
			continue
	#print(lista_fisiere_csv)
	return lista_fisiere_csv

def citeste_fila_in_lista(fila):
	'''Citeste un fisier csv intr-o lista de liste'''
	with open(fila, 'r') as f:
		a = f.readlines()
		f.close()
	#print(a)
	return a

def schimba_antetul_in_lista(lista, nume):
	'''Schimba antetul in lista (cele 4 randuri)'''
	l0 = ',,Fisa de Magazie,,,\n'
	l1 = 'Unitatea,Material:,{},,,\n'.format(nume)
	l2 = '                S.C. Valenti, Impex S.R.L.,   {},,,\n'.format(categorie)
	l3 = '                RO5058275,J05/3962/1993,Nr Mat: ,U.M.: {},,Furnizor: \n'.format(um)
	l4 = '                Data,Felul si Numarul,Intrari,Iesiri,Stoc,Data si semnatura de control (Observatii)\n'
	lista[0] = l0
	lista[1] = l1
	lista[2] = l2
	lista[3] = l3
	lista.insert(4, l4)
	#print(lista)
	return lista
	
def transforma_lista_in_sir(lista):
	'''Transforma o lista in sir pt a putea fi scrisa in fisier'''
	sir = ''.join(lista)
	#print (sir)
	return sir

def rescrie_fila_cu_antetul_nou(fila, sir):
	'''Rescrie fila cu noul antet'''
	with open(fila, 'w') as f:
		f.write(sir)
		f.close()

def start():
	''' Programul '''
	global um, categorie
	um = input('Introduceti unitatea de masura:\n')
	categorie = input('Introduceti categoria materiale:\n')
	aa = fa_lista_cu_csvuri()
	#input('\nARATA FILA INITIALA (LISTA)')
	for item in aa: # aa=fisierele din dosar
		#print(item)
		nume = item.replace('.csv', '')
		print(nume)
		bb = citeste_fila_in_lista(item) # bb=lista din fisier; item=fila
		#input('\nARATA FILA CU ANTETUL SCHIMBAT')
		cc = schimba_antetul_in_lista(bb, nume) # cc=lista cu antet schimbat
		#input('\nARATA SIRUL')
		dd = transforma_lista_in_sir(cc) # dd = sirul de scris 
		#input('\nRESCRIE FILA')
		ee = rescrie_fila_cu_antetul_nou(item, dd) # ee=rescrie fila; item=fila; dd=sirul


start()
print('\nFINAL = SUCCESS !')