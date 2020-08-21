# stocuri din CFL
# Face storcuri la numele de materiale prezente in CFL
from tkinter import filedialog
import tkinter


PATH_FISE_MAGAZIE = 'D:\\Valenti\\2019\\Fise_Magazie\\'


def scrie_in_fila(tab):
    global nf
    nf = 'stocuri_centralizator.csv'
    with open(nf, 'w') as f:
        for key in tab.keys():
            f.write("%s,%s\n" % (key, tab[key]))


def preia_stocul(fila):
    myfile = fila
    lista_erori = []
    try:
        myvar = open(myfile, 'r', encoding='utf8', errors='ignore')
        lst = myvar.readlines()
        lilen = len(lst)
        myva = lst[lilen-1]  # ultima linie unde e stocul
        a = myva.split(',')
        stoc = a[-2]  # -2 = pe a doua coloana de la dreapta este stocul
        myvar.close()
        # print (myva)
        # print (a)
        # print (stoc)
        return(stoc)
    except:
        lista_erori.append(myfile)
    print(lista_erori)


def preia_din_centralizator_nume(fila):
    global lista_nume
    with open(fila, 'r') as f:
        a = f.readlines()
        lista_nume = []
        for i in a:
            nume = i.split(',')
            lista_nume.append(PATH_FISE_MAGAZIE+nume[0]+'.csv')
        f.close()
    # print(lista_nume)


def selecteaza_centralizator():
    fila = filedialog.askopenfilename()
    preia_din_centralizator_nume(fila)


def interfata():
    app = tkinter.Tk()
    b = tkinter.Button(app, text='Open un centralizator.csv', command=selecteaza_centralizator)
    b.grid()
    app.mainloop()


interfata()
#  selecteaza_centralizator()
#  preia_din_centralizator_nume()
tabel = {}
for item in lista_nume:
    stoc = preia_stocul(item)
    d1 = item.replace('.csv', '')
    d = d1.replace('D:\\Valenti\\2019\\Fise_Magazie\\', '')
    tabel[d] = stoc
    print('*', end='')
print('Final')
# print(tabel)
scrie_in_fila(tabel)
