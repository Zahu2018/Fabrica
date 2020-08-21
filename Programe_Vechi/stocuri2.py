# stoc, stocuri, dictionar, fise magazie 
# Face un dictionar din numele fisierelor si stocul actual
# 15.06.2019
# Florian Zah

# Il scrie in fila rezultat_stocuri.csv
import os
import csv

def preia_stocul(fila):
    myfile = fila
    myvar = open(myfile, 'r')
    lst = myvar.readlines()
    ll = len(lst)
    
    myva = lst[ll-1] # ultima linie unde e stocul
    a = myva.split(',')
    stoc = a[-2] # -2 = pe a doua coloana de la dreapta este stocul
    myvar.close()
    #print (myva)
    #print (a)
    #print (stoc)
    return(stoc)
def fa_lista_din_numele_fisierelor():
    import os
    lista_file = []
    m = (os.listdir())
    for x in m:
        if x[-4] == ".":
            lista_file.append(x)
    #print(lista_file)
    return(lista_file)

def scrie_in_fila(tab):
    global nf
    nf = '000___stocuri.csv'
    with open(nf, 'w') as f:
        for key in tab.keys():
            f.write("%s,%s\n"%(key,tab[key]))
    
def main():
    #locatie = 'D:\\Valenti\\2018\\Fise_Magazie\\'
    #a = input('Introduceti categoria: ')
    #locatie_1 = locatie + a 
    
    b = fa_lista_din_numele_fisierelor()
    

    tabel = {}
    for c in b:
        x = preia_stocul(c)
        d = c.replace('.csv', '')
        tabel[d] = x
        
    #print(tabel)
    scrie_in_fila(tabel)
main()
print('\nFINAL - SUCCESS !')
print('A fost creat fisierul {}'.format(nf))
