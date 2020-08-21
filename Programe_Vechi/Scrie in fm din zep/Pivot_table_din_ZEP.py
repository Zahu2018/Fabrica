#   SERAFIL PIVOT TABLE FROM ZEP
###################################
#    A program written by: Zah    #
###################################
# functia care realizeaza pivot table
# S-ar putea ca sa fie nevoie sa introducem un ultim
# rand cu 0
from tkinter import *
from tkinter import filedialog

def open_file():

    fila = filedialog.askopenfilename()
    fila1 = (str(fila)).replace('/', '\\')
    #print(fila1) # printeaza numele fisierul si Path
    b = open(fila1, 'r')
    c = b.read()
    b.close
    #print(c) # printeaza continutul fisierului text

    calculeaza(c)
#   Functia calculeaza / realizeaza toate operatiile pentru
# a putea obtine rezultatul dorit
def calculeaza(a): # Rezultatul va fi: [['4', '31', '8'], ['54', '1', '18'], ...]
    # Transforma un text intr-o lista de linii, 
    # fiecare linie fiind o lista ce contine valoarea din
    # fiecare celula a liniei
    # a = textul_pt_lucru
    ccci = 9 # cu_care_coloana_incepem - 1

    initial = 0
    nr = a.count('\n')
    lista = []
    for i in range(nr):
        final = a.find('\n', initial)
        lin = a[initial:final]
        lin_lista = lin.split(',')
        lista.append(lin_lista)
        initial = final + 1
    #print(lista) # lista de linii

# Facem o lista de matrice sau o lista de liste de liste
''' Rezultatul va fi:
[[['a', 'b', 'c'],
  ['1', '2', '3'],
  ['3', '8', '0']],
  [['x', 'b', 'z'],
  ['1', '2', '3'],
  ['3', '8', '0']]]
'''
    L = [] # lista de matrice
    M = [] # matrice
    for item in lista:
        if str(item[ccci]).isupper(): # verifica antetul matricei
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
                            dicti[item] = suma_i
                        else:
                            dicti[item] = suma_i
                    except:
                        print('nu pot converti in float', item)



    #print(dicti)
    listare = ''
    for item in dicti:
        lis = ''
        lis = (str(item) + "," + str(round(dicti.get(item), 2)))
        #print(item, " = ", (dicti.get(item)))
        listare += str(lis) +'\n'
    print(listare)

    var=open("Centralizator.csv", 'w') #numerele trebuie convertite in siruri inainte de scriere in fisier [str()]
    var.write(listare) 
    var.close()
    



app = Tk()
app.title("Pivot Table din ZEP - single file")
app.geometry("200x100")
label = Label(app, text = 'Programul acesta creaza un tabel\npivotant dintr-un singur ZEP.')
label.grid(row=0)
bu = Button(app, text='Open', command=open_file)
bu.grid(row=1)
app.mainloop()

