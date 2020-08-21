"""
SCADE_CENTRALIZATOR

OK - Creem un dictionar din centralizator.cs
OK - Creem un fisier log unde scriem erorile
for item in dictionar din centralizator:
    daca item in dict_fm.py:
        stabileste path
        open fila
        calculeaza (scade centralizator)
        daca rezultatul < > 0:
            scrie material = suma in log
    else:
        scrie material = nu exista in log
"""
import csv
from dict_fm import dictionar

def fa_dictionar_din_centralizator():
    reader = csv.reader(open('centralizator1.csv'))
    dic1 = {}
    for row in reader:
        dic1[row[0]]=row[1]
    #print(dic1)
    return dic1
def creaza_fisier_LOG():
    x = open('LOG.txt', 'w')
    x.close()
def scriem_in_fise_de_magazie(dictio):
    #print(dictio)
    for key, value in dictio.items():
        #print(key, "=", value)
        if key in dictionar:
            #print(key, "in dictionar")
            pass
        else:
            print(key, "not in dictionar")

aa = fa_dictionar_din_centralizator()
creaza_fisier_LOG()
scriem_in_fise_de_magazie(aa)

