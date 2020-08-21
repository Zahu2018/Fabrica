'''
Programul scrie un zep in fisele de magazie
'''
import dict_fm
from tkinter import *
from tkinter import filedialog
from tkinter import ttk 
import os

class MyFirstGUI:
     

    def __init__(self, master):
        self.master = master
        self.master.title("Fise de Magazie")

        self.button_open = ttk.Button(self.master, text='Open', command=self.open_file)
        self.button_open.grid(row=0, column=0, rowspan=2)
        self.label_data = ttk.Label(master, text="Data: ")
        self.label_data.grid(row=0, column=1)
        self.label_aviz = ttk.Label(master, text="Aviz: ")
        self.label_aviz.grid(row=1, column=1)
        self.data = StringVar()
        self.entry_data = ttk.Entry(master, textvariable=self.data)
        self.entry_data.grid(row=0, column=2)
        self.aviz = StringVar()
        self.entry_aviz = ttk.Entry(master, textvariable=self.aviz)
        self.entry_aviz.grid(row=1, column=2)
        self.button_open = Button(master, text='Inregistreaza\nin\nFise de Magazie', justify='center', command=self.inregistreaza)
        self.button_open.grid(row=0, column=3, rowspan=2)
        self.label_rezultat = Label(self.master, text='Rezultate')
        self.label_rezultat.grid(row=2, column=0, columnspan=4)

    
    def inregistreaza(self):
        data = self.entry_data.get()
        aviz = self.entry_aviz.get()
        
        creaza_lista_de_liste(self.a, data, aviz) 
    #---------------------------------------
    def open_file(self):
        nume_fisier = filedialog.askopenfilename(initialdir="D:\\Valenti\\2018\\ZEP\\",
                           filetypes =(("CSV File", "*.csv"),("All Files","*.*")),
                           title = "Alege un ZEP."
                           )
        fisier = open(nume_fisier, 'r')
        self.a = fisier.read() # a = textul din fisier
        fisier.close()
          
#-------------------------------------
def scrie_in_fila(locul, fila, suma, data, aviz):
    path = os.chdir('D:\\Valenti\\2018\\Fise_Magazie\\'+locul) # Se schimba in functie de computer
    fisier = fila + '.csv'
    a = open(fisier, 'r') #deschisa pt. citire
    c = a.read()
    #print(c)
    b = open(fisier, 'a') #deschisa pt. append
    
    
    nr = c.count('\n')
    #print("%s \nNr randuri = %d" %(c, nr))
    lista = []
    initial = 0
    for i in range(nr): 
        '''Facem o lista cu toate liniile; liniile sunt splitata cu virgula'''
        final = c.find('\n', initial) # gasim primul \n de la inceput
        lin = c[initial:final] #selectam prima linie
        #print(lin)
        lin_lista = lin.split(',')
        lista.append(lin_lista)
        initial = final + 1
    #print(lista)
    lc = len(lista)    #linia pentru lucru    
    ultima_linie = lista[lc-1]  #ultima linie; ne intere pt scadere sau adunare  
    lu = len(ultima_linie)    # lungimea in celule
    stoc_vechi = round((float(ultima_linie[lu-2])), 2)
    #print('ultima linie ', ultima_linie[lu-1])
    #print("Stocul vechi", stoc_vechi)
    
    stoc = stoc_vechi + suma
    stoc_sir = str(stoc)
    cant = str(suma)
    var1i = data+","+aviz+","+cant+",,"+stoc_sir+","+"\n"
    var1 = str(var1i)
    b.write(var1)
    b.close()
    #print(os.getcwd())
    #print("Stocul nou ", stoc)
    
    
def creaza_fila(fila, suma):
    path = os.chdir('D:\\Valenti\\2018\\Fise_Magazie') # asta a folderul cu Foldere Fise de Magazie
    fisier = fila + '.csv'
    a = open(fisier, 'w')
    a.write('''Unitatea,,Fisa de Magazie,U.M.,,,
                S.C. Valenti, Impex S.R.L.,"Material (produs), sortiment, calitate, marca, profil, dimensiune",Furnizor,,,
                RO5058275,J05/3962/1993,,Nr Mat,,,
                Data,Felul si Numarul,Intrari,Iesiri,Stoc,Data si semnatura de control (Observatii)''')

    a.close()
    
    
    
    

def scrie_in_fm(dictionarul_zep, data, aviz): #dictionarul cu materiale-suma / zep
    '''Scrie dictionarul in fise de magazie'''
    
    for key, value in dictionarul_zep.items():
        if key in dict_fm.dictionar.keys():

            scrie_in_fila(dict_fm.dictionar[key], key, dictionarul_zep[key], data, aviz)
            
        else:
            creaza_fila(key, dictionarul_zep[key]) 
            
def dictionar_cu_materiale(L, data, aviz):
    '''Facem dictionar cu key=materiale si value=cantitate'''
    dicti = {}
    for matrice in L:
        for material in matrice[0]:
            if material == '' or material.isnumeric() or material.islower() or 'FORELLG' in material or("/" in material and " " not in material):
                pass
            else:
                indexul_material = matrice[0].index(material)
                adancimea_matricei = len(matrice) #nr de linii
                #print(adancimea_matricei)
                suma_cpb = 0
                for i in range(1, adancimea_matricei):
                    cpb = matrice[i][indexul_material] # valoarea din celule
                    suma_cpb +=  float(cpb)
                    #print(suma_cpb)
                if material in dicti:
                    cant_mat_from_dict = dicti.get(material)
                    suma_cpb += (cant_mat_from_dict)
                    dicti[material] = suma_cpb
                else:
                    dicti[material] = suma_cpb
    #print(dicti)
    pt_afisare = ''
    for chei, valori in sorted(dicti.items()):
    	dd = chei, valori
    	pt_afisare += str(dd) + '\n'
    app.label_rezultat.config(text=pt_afisare)
    scrie_in_fm(dicti, data, aviz)
    
    #x1 = open('dictionar_1.txt', 'a')
    #b1 = x1.write(str(dicti))
    #x1.close

def creaza_matricea(lista, data, aviz):
    '''Cream o lista de matrice'''
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
    M.append(item)  
    L.append(M) 
    dictionar_cu_materiale(L, data, aviz) # L = Matricea principala
    #print(L)

def creaza_lista_de_liste(t, data, aviz): # t = textul din fisier
    '''Transfora textul (var a) in lista de liste de liste'''
    initial = 0
    nr = t.count('\n')
    lista = []
    for i in range(nr):
        final = t.find('\n', initial)
        lin = t[initial:final]
        lin_lista = lin.split(',')
        lista.append(lin_lista)
        initial = final + 1
    creaza_matricea(lista, data, aviz)
    #print(lista) # lista = lista de liste de liste     

root = Tk()
app = MyFirstGUI(root)

root.mainloop()
