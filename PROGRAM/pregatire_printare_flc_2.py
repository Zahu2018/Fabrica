# Pregateste pentru printat Fise limita de consum
# Rulezi programul: Ctrl+Shift+Alt+B -> introduci numele fisierului -> Enter
# Creaza un fisier .csv avand ca nume data 
import os

lista = [item for item in os.listdir() if item[-4:] == ".csv"]


def citeste_fila(fila):
    """Deschide fila si o citeste."""
    b = open(fila, 'r', encoding="utf-8")
    c = b.read()
    b.close
    return c
    
def matrice_fila(a):  # a=continut fisier
    """ Transforma un text intr-o lista de linii - MATRICE."""
    initial = 0
    nr = a.count('\n')
    lista = []
    for i in range(nr):
        final = a.find('\n', initial)
        lin = a[initial:final]
        lin_lista = lin.split(',')
        lista.append(lin_lista)
        initial = final + 1
    #return lista
    

# Facem o lista de matrice sau o lista de liste de liste.
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
    return L
    

def creaza_lista_materiale(m): # m = matricea
    lista_materiale = []
    for i in m:
        for j in i[0][6:]:  
            if j == "":
                pass
            elif j not in lista_materiale:
                lista_materiale.append(j)
            else:
                pass
    #print(sorted(lista_materiale))
    return sorted(lista_materiale)
        
        
def transpune_matricea(m, li_mat): # m=matricea; li_mat = lista materiale din matrice
    # versiune 2
    # sa rezulte => [[mat1, cant1, cant2, cant3, ...], [mat2, cant1, ...]]
    matrice_generala = []
    for material in li_mat:
        matrice_linie = []
        matrice_linie.append(material)
        for j in m:
            if material in j[0]:
                pozitia = j[0].index(material)
                for x in range(len(j)-1):
                    cantitate = j[x+1][pozitia]
                    #print(i, " = ", cantitate)
                    matrice_linie.append(cantitate)
                
            
            else:
                
                for x in range(len(j)-1):
                    cantitate = 0
                    #print(i, " = 0")
                    matrice_linie.append(cantitate)
        matrice_generala.append(matrice_linie)
                
    return matrice_generala
    
def scrie_fisa_consum(ma):
    # deprecated since manipulation of all files
    data = fila[:5] + ".2020"
    #nume_fisier = data + ".csv"
    nume_fisier = "rezultat.csv"
    with open(nume_fisier, "a", encoding="utf-8") as f:
        text = "\n\n,,,,,FISE LIMITA DE CONSUM\n,,,,,{},\n\n".format(data)
        for s in ma:
            linie = ','.join([str(elem) for elem in s]) 
            text = text + linie + "\n"
        text += "\nSemnatura magazioner,,,,Semnatura maistru croit,,,,,,,,Semnatura maistii cusut\n"
        text += "\nPop,,,,Szilagyi,,,,,Lacatus,,,Pop,,,Pop\n"
        text += "Stefan,,,,Attila,,,,,Florina,,,Anamaria,,,Mariana"
        f.write(text)
        print(text)
         
# Deprecated sice we process all files  
# fila = input("Introduceti numele fisierului:\n")
for fila in lista:
    a = citeste_fila(fila)
    b = matrice_fila(a)  # b = matricea
    c = creaza_lista_materiale(b)
    d = transpune_matricea(b, c)  # b = matricea; c = lista materiale
    scrie_fisa_consum(d)
    
 
