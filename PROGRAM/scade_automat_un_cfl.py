# pivot table, cfl, fm, scrie in fise de magazie, automat, scade un cfl
# Centralizeaza datele dintr-un cfl si le scrie automat in Fisele de Magazie
# 27.06.2019
# Zah Florian

from tkinter import *
from tkinter import filedialog
import os
from decimal import *

PATH = 'D:\\Valenti\\2019\\Fise_Magazie\\'
#PATH = 'C:\\Users\\User\\Desktop\\fm\\New folder\\'

def fa_dictionar_din_csv(csv):
	'''Face un dictionar dintr-un csv, pe doua coloane'''
	global dicti # dictionar
	dicti = {}
	#print (csv)
	with open(csv) as f:
		lista = f.readlines()
		for i in lista:
			m = i.strip('\n').split(',')
			dicti[m[0]] = eval(m[1])
		print(dicti)

def deschide_fila_ZEP():
    '''Deschide un zep.csv'''
    global tail
    fila = filedialog.askopenfilename()
    fila1 = (str(fila)).replace('/', '\\')
    #print(fila1)
    head, tail = os.path.split(fila1) # ia numele si extensia fisierului
    #print(tail)
    b = open(fila1, 'r')
    c = b.read()
    b.close
    #print(c)
    fa_dictionar_din_csv(fila)

def scrie_in_fila(k):
    # 1. Deschide fila; k = denumire material/fila
    fila = '{}{}.csv'.format(PATH,k)
    try:
        with open(fila, 'r+') as f:
            a = f.readlines()
    # 2. Ia stocul
            ultima_linie = a[-1].split(',')
            stoc_vechi = round(float(ultima_linie[-2]), 2)
            #print(stoc_vechi)
            d = data.get()
            a = aviz.get()
            #ie = adauga.get() # radio buton neimplementat
            cantitate = dicti[k]
            stoc = stoc_vechi - round(cantitate, 2)
            if stoc >= 0:
            	sir = '{},{},,{},{},\n'.format(d,a,cantitate,stoc)
            	f.write(sir)
            	f.close()
            	print('{}: {} - {} = {} :: Success !'.format(k, stoc_vechi, cantitate, stoc))
            else:
            	lista_erori.append('{} = {}'.format(k, dicti[k]))
    except FileNotFoundError:
        lista_erori.append('{} = {}'.format(k, dicti[k]))
        #print('Fisierul {} nu exista'.format(k))

def program():
    global lista_erori
    lista_erori = []
    for k in dicti.keys():
        scrie_in_fila(k)
    print('\n', lista_erori)

def creaza_interfata_grafica():
    global adauga, data, aviz
    app = Tk()
    app.title("Scade automat un CFL")
    #app.geometry("400x100")
    text_buton = '''Programul acesta scade un CFL din Fise de Magazie.
        Apasa aici pentru a deschide - OPEN'''
    bu = Button(app, text=text_buton, command=deschide_fila_ZEP)
    bu.grid(row=0, columnspan=3)

    ld = Label(app, text='Data')
    ld.grid(row=1, column=0)
    la = Label(app, text='Aviz')
    la.grid(row=2, column=0)
    data = Entry(app)
    data.grid(row=1, column=1, sticky='w')
    aviz = Entry(app)
    aviz.grid(row=2, column=1, sticky='w')
    scrie = Button(app, text='Scade din \nFise de Magazie\nun CFL', command=program)
    scrie.grid(row=1,column=2,rowspan=2)

    app.mainloop()

creaza_interfata_grafica()
