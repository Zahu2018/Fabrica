# centralizator, zepuri dintr-o luna
# Centralizeaza toate zepurile dintr-o luna
# 01.07.2019
# Florian Zah

"""Selectezei dosarul cu zepuri."""

from tkinter import filedialog
import tkinter
import os


def deschide_dosarul():
    director = filedialog.askdirectory()
    fa_lista_cu_file(director)


def fa_lista_cu_file(director):
    global folder_OK
    folder_nume = os.listdir(director)
    folder_OK = []
    path = director
    for f in folder_nume:
        folder_OK.append(path + '/' + f)
    # print(folder_OK)


def deschide_fila(fila):
    b = open(fila, 'r')
    c = b.read()
    b.close
    calculeaza_fila(c, fila)


def calculeaza_fila(a, filax):
    """ Transforma un text intr-o lista de linii, fiecare linie fiind o lista (o lista de liste)."""
    initial = 0
    nr = a.count('\n')
    lista = []
    for i in range(nr):
        final = a.find('\n', initial)
        lin = a[initial:final]
        lin_lista = lin.split(',')
        lista.append(lin_lista)
        initial = final + 1
    # print(lista)

# Facem o lista de matrice sau o lista de liste de liste
    L = []  # lista de matrice
    M = []  # matrice
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
    # print(L)

# Facem un dictionar cu Serafil
    dicti = {}
    for mat in L:
        for item in mat[0]:
            if item.isnumeric() is False:
                ind = mat[0].index(item)  # gasim indexul fiecarui item cu "/" si fara " " (spatiu)
                # print(item, ' = ', ind)
                l = len(mat)  # lungimea (inaltimea) matricei in linii
                for i in range(1, l):  #
                    suma = 0
                    suma_i = 0
                    m = mat[i][ind]
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
                        print('nu pot converti in float', item, filax)


    # print(dicti)
    listare = ''
    for item in dicti:
        lis = ''
        lis = (str(item) + "," + str(round(dicti.get(item), 2)))
        # print(item, " = ", (dicti.get(item)))
        listare += str(lis) + '\n'
    print(listare)
    print(filax)
    scrie_fila(listare)


def scrie_fila(listare):
    var = open("Centralizator.csv", 'a')  # numerele trebuie convertite in siruri inainte de scriere in fisier [str()]
    var.write(listare)
    var.close()


def program():
    app = tkinter.Tk()
    app.title("CFL din zepuri de pe o luna")
    app.geometry("250x100")
    label = tkinter.Label(app, text='Programul acesta creaza un CFL\ndin ZEP-urile dintr-o luna\nsi face un csv.')
    label.grid(row=0)
    bu = tkinter.Button(app, text='Open', command=deschide_dosarul)
    bu.grid(row=1)
    print("Lucrez ...")
    app.mainloop()


program()
# deschide_dosarul()
# fa_lista_cu_file()
for file in folder_OK:
    deschide_fila(file)
    # calculeaza_fila()
    # scrie_fila()'''
    print("END")
