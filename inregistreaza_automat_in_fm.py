# pivot table, zep, fm, scrie in fise de magazie, automat
# Centralizeaza datele dintr-un zep si le scrie automat in Fisele de Magazie
# 21.06.2019
# Zah Florian

from tkinter import *
from tkinter import filedialog
import os
from decimal import *

PATH = 'D:\\Valenti\\2019\\Fise_Magazie\\'

def deschide_fila_ZEP():
    '''Deschide un zep.csv'''
    global tail, fila1
    fila = filedialog.askopenfilename()
    fila1 = (str(fila)).replace('/', '\\')
    print(fila1)
    head, tail = os.path.split(fila1) # ia numele si extensia fisierului
    #print(tail)
    b = open(fila1, 'r')
    c = b.read()
    b.close
    #print(c)
    fa_dictionar(c)
    

def fa_dictionar(a): # pivot table => dictionar
    # 1. Transforma un text intr-o lista de linii, fiecare linie fiind o lista (o lista de liste)
    global dicti
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

    # 2. Facem o lista de matrice sau o lista de liste de liste
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
    L.append(M)     
    #print(L)

    # 3. Facem un dictionar 
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
                            dicti[item] = suma_i
                        else:
                            dicti[item] = suma_i
                    except:
                        print('nu pot converti in float', item)
    if '' in dicti.keys():
        dicti.pop('')
    #print(dicti, '\n')
    

def scrie_in_fila(k):
    # 1. Deschide fila
    fila = '{}{}.csv'.format(PATH,k)
    if 'SERAFIL' not in str(k):
        if 'FORELL' not in str(k):
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
                    if cantitate != 0:
                        stoc = stoc_vechi + round(cantitate, 2)
                        sir = '{},{},{},,{},\n'.format(d,a,cantitate,stoc)
                        f.write(sir)
                        f.close()
                        print('{}: {} + {} = {} :: Success !'.format(k, stoc_vechi, cantitate, stoc))
                    else:
                        lista_erori.append('{} - cantitate = 0'.format(k))
            except FileNotFoundError:
                lista_erori.append('{} = {}'.format(k, dicti[k]))
                #print('Fisierul {} nu exista'.format(k))
        else:
            lista_erori.append('-')
            pass
    else:
        lista_erori.append('-')
def program():
    global lista_erori
    lista_erori = []
    for k in dicti.keys():
        scrie_in_fila(k)
    print("\n\n\n")
    print("================================================")
    print("=  MATERIALE CARE TREBUIE INREGISTRATE MANUAL  =")
    print("================================================")
    print("\nData-Aviz: {}\n".format(fila1[-17:-4]))
    for h in lista_erori:
        print(h)
    print("-------------------- END -----------------------")
    #print('\n', lista_erori)

def creaza_interfata_grafica():
    global adauga, data, aviz
    app = Tk()
    app.title("Scrie in Fise de Magazie")
    #app.geometry("400x100")
    text_buton = '''Programul acesta creaza un tabel
        pivotant dintr-un singur ZEP si le scrie in Fise de Magazie.
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
    scrie = Button(app, text='Scrie in \nFise de Magazie', command=program)
    scrie.grid(row=1,column=2,rowspan=2)
    
    app.mainloop()
       
creaza_interfata_grafica()   
