#   FNCTIA PIVOT TABLE
###################################
#    A program written by: Zah    #
###################################
# Se introduce un rand suplimentar cu 0
'''tabel = 4,21,9,2018,34027,10,1406,,0,WOVENSTRETCH-S GRAU-HELLGRAU,CARUSO SILBER,CROMATO-S SILBER,CALFLINING KIESEL,AIRTEX KIESEL,HEELGRIP KIESEL,DELIKA KIESEL,JAGER,PU-SCHAUM 6 OFFWHITE,WILHELM SCHAUM 4 OFFWHITE,IBITECH 57 STROBELSTOFF,YL-310 SILBER,10467_90 251_8881,1000-30,411-30,411-60,1358-30,1358-60,414-60,,,,
4,21,9,2018,34027,10,1406,205,120,120,9.02,0.9,7.81,7.08,3.12,,2.06,1.44,0.84,4.2,240,120,1560,1080,510,60,498,132,,,,
4,21,9,2018,34027,10,1406,217,120,120,9.08,0.9,7.82,7.08,3.12,,2.06,1.44,0.84,4.2,240,120,1560,1080,510,60,498,132,,,,
4,21,9,2018,34027,10,1406,229,120,120,9.14,0.9,7.83,7.08,3.12,,2.06,1.44,0.84,4.2,240,120,1560,1080,510,60,498,132,,,,
4,21,9,2018,34027,10,1406,241,120,120,9.31,0.9,7.83,7.08,3.12,,2.06,1.44,0.84,4.2,240,120,1560,1080,510,60,498,132,,,,
4,21,9,2018,34027,10,1406,253,120,120,9.55,0.9,7.71,7.08,3.12,,2.06,1.44,0.84,4.2,240,120,1560,1080,510,60,498,132,,,,
4,21,9,2018,34027,10,1406,265,120,120,9.44,0.9,7.71,7.08,3.12,,2.06,1.44,0.84,4.2,240,120,1560,1080,510,60,498,132,,,,
4,21,9,2018,33354,8,1411,,0,SAMTCHEVRO SASSO,DAYTONACALF WEISS,PREMIERE-METALIC-S SILBER,AIRTEX KIESEL,DELIKA KIESEL,HEELGRIP KIESEL,JAGER,PU-SCHAUM 6 ANTHRAZIT,WILHELM SCHAUM 4 OFFWHITE,IBITECH 57 STROBELSTOFF,Y-012-0_12 SILBER,YL-264 NEW SILBER,RX-73_32 SILBER_CDF_SKY,RX-76_15_100 SASSO,SERAFIL 0321-30,SERAFIL 0321-60,SERAFIL 2000-20,SERAFIL 2000-30,SERAFIL 2000-60,SERAFIL 0412-30,SERAFIL 0412-60,SERAFIL 1358-60,SERAFIL 1000-30
4,21,9,2018,33354,8,1411,157,120,6.66,13.55,3.1,10.38,4.32,3.12,1.92,1.56,0.6,4.2,480,240,50.4,120,540,474,192,660,240,318,228,996,1560
4,21,9,2018,33354,8,1411,169,120,6.67,13.83,3.1,10.38,4.32,3.12,1.92,1.56,0.6,4.2,480,240,50.4,120,540,474,192,660,240,318,228,996,1560
4,21,9,2018,33354,8,1411,181,120,6.69,13.9,3.1,10.38,4.32,3.12,1.92,1.56,0.6,4.2,480,240,50.4,120,540,474,192,660,240,318,228,996,1560
4,21,9,2018,33354,8,1411,193,120,6.63,14.18,3.1,10.38,4.32,3.12,1.92,1.56,0.6,4.2,480,240,50.4,120,540,474,192,660,240,318,228,996,1560
4,21,9,2018,33354,8,1411,205,120,6.48,14.6,3.1,10.38,4.32,3.12,1.92,1.56,0.6,4.2,480,240,50.4,120,540,474,192,660,240,318,228,996,1560
4,21,9,2018,14512,6,1413,,0,WOVENSTRETCH-S ROT,LUCKY-S ROT,PREMIERE-METALLIC-S SILBER,FROTEE OFFWHITE,DELIKA OFFWHITE,HEELGRIP OFFWHITE,CAPAMA,PU-SCHAUM 6 OFFWHITE,WILHELM SCHAUM 4 OFFWHITE,IBITECH 57 STROBELSTOFF,IO 15ML SILBER,YL-310 SILBER,RX-73_32 BLAU_SILBER_ROT,RX-55_15_100 ROT,SERAFIL 0105-30,SERAFIL 0105-60,SERAFIL 0412-30,SERAFIL 0821-30,SERAFIL 2000-60,SERAFIL 1000-30,,,
4,21,9,2018,14512,6,1413,85,120,120,0,2.75,12.48,1.92,2.88,1.69,1.56,0.84,4.2,1920,240,48,120,882,270,180,150,780,1560,,,
3,21,9,2018,41052,57,1455,,0,KROKO-LACK SCHWARZ,DELIKA SCHWARZ,AIRTEX SCHWARZ,HEELGRIP SCHWARZ,SEL LAT 6 ROHWEISS,IBITECH 57 STROBELSTOFF,WULSTEINLAGE CKS 252 ROHWEISS,17437_70 SCHWARZ,4000/10,4000/20,4000/30,4000/60,1000/30,,,,,,,,,,
3,21,9,2018,41052,57,1455,33,120,16.74,11.94,4.44,2.88,0.96,4.2,57.6,16.8,210,126,630,852,1560,,,,,,,,,,
3,21,9,2018,41052,57,1455,45,120,16.65,11.94,4.44,2.88,0.96,4.2,57.6,16.8,210,126,630,852,1560,,,,,,,,,,
3,21,9,2018,41052,57,1455,57,120,17.32,11.94,4.44,2.88,0.96,4.2,57.6,16.8,210,126,630,852,1560,,,,,,,,,'''

from decimal import *
import dict_fm
from tkinter import filedialog

ANTET = '''Unitatea,,Fisa de Magazie,U.M.,,,
S.C. Valenti, Impex S.R.L.,"Material (produs), sortiment, calitate, marca, profil, dimensiune",,,,
RO5058275,J05/3962/1993,,Nr Mat,,,
Data,Fel,Numar,Intrari,Iesiri,Stoc,Data si semnatura de control (Observatii)\n'''

def creaza_fila(fila, pr): # pr = primul rand
    if '/' in fila:
    	pass
    else:
    	fisier = fila + '.csv'
    	a = open(fisier, 'w')
    	a.write(ANTET)
    	a.write(pr)
    	a.close()


def open_file():

    fila = filedialog.askopenfilename()
    fila1 = (str(fila)).replace('/', '\\')
    print(fila1)
    b = open(fila1, 'r')
    c = b.read()
    b.close
    #print(c)
    return c

    
def pivot_table(tabel, coloana, rand):
    """tabel = tabelul de calculat sau matricea
    coloana = a catea colana incepe
    rand = al catelea rand incepe"""

    # 1. LISTA DE LINII 
    inceput = 0
    numar_randuri = tabel.count('\n')
    lista_de_linii = [] #fiecare linie e o lista Ex: [['4', '31', '8'], ['54', '1', '18'], ...]
    for i in range(numar_randuri):
        final = tabel.find('\n', inceput)
        o_linie = tabel[inceput:final]
        lin_lista = o_linie.split(',')
        lista_de_linii.append(lin_lista)
        inceput = final +1
    #print(lista_de_linii)

    # 2. LISTA DE MATRICE
    lista_matrice = [] # lista de matrice
    matrice = []
    for item in lista_de_linii:
        if str(item[coloana]).isupper(): #verifica antetul matricei
            if matrice != []:
                lista_matrice.append(matrice)
            else:
                pass
            matrice = []
            matrice.append(item)
        else:
            matrice.append(item)
    matrice.append(item)
    lista_matrice.append(matrice)
    #print(lista_matrice)
    
    # 3. DICTIONAR CU MATERIALE
    dictionar = {}
    for mat in lista_matrice: # matrice cu header, condum, valori
        for item in mat[0]: # headers pt toate matricele
            if item.isnumeric() == False and item != '' and 'SERAFIL' not in item : # renuntam la cifre, etc si SERAFIL
                ind = mat[0].index(item)
                #print(item, ' = ', ind)
                l = len(mat) # inaltimea matricei in linii
                #print(l)
                for i in range(1, l):
                    suma = 0
                    suma_i = 0
                    m = mat[i][ind]
                    #print(m)
                    try:
                        sm = float(m)
                        suma += sm
                        suma_i += suma
                        
                        if item in dictionar:
                            var = dictionar.get(item)
                            suma_i += var
                            dictionar[item] = suma_i
                        else:
                            dictionar[item] = suma_i
                    except:
                        print('Nu pot converti in float', item)
            else:
                pass
    #print(dictionar)
    return dictionar 
    

def inregistreaza_dict(dictionar, data, aviz):
    a = dict_fm.dictionar_fm
    #print(a.keys())
    for key, value in dictionar.items():
        if key in a.keys():
            #print("+", key)
            path_fara_fila = ('C:\\Users\\User\\Desktop\\test' + '\\' +str(a[key]))
            path = path_fara_fila + '\\' + key + '.csv'
            print(key)
            fisier = open(path, 'r+')
            continut_fisier = fisier.read().splitlines()
            ultima_linie = continut_fisier[-1]
            print(ultima_linie)
            lu = len(ultima_linie)
            lista_ultima_linie = ultima_linie.split(',')
            stoc_vechi = round(Decimal(lista_ultima_linie[-2]), 2)
            #stoc_vechi = round(float(lista_ultima_linie[-2]), 2)
            print(stoc_vechi)
            stoc = stoc_vechi + round(Decimal(value), 2)
            stoc_sir = str(stoc)
            cant = str(value)
            var1i = data+","+aviz+","+cant+",,"+stoc_sir+","+"\n"
            var = str(var1i)
            print(var)
            fisier.write(var)
            fisier.close()
        else:
            
            l = open('log.txt', 'a')
            l1 = str(key) + ' = ' + str(value) + '\n'
            b = l.write(l1)
            l.close()
            cant = str(value)
            primul_rand = str(data+","+aviz+","+cant+",,"+cant+","+"\n")
            creaza_fila(key, primul_rand)
  
# MENIU
data = input("Introduceti data: ")
aviz = input("Introduceti avizul: ")
tabel = open_file()
a = pivot_table(tabel, 9, 0)
inregistreaza_dict(a, data, aviz)
