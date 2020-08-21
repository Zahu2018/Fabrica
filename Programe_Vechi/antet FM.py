import os
ANTET = '''Unitatea,,Fisa de Magazie,U.M.,,,
S.C. Valenti, Impex S.R.L.,"Material (produs), sortiment, calitate, marca, profil, dimensiune",,,,
RO5058275,J05/3962/1993,,Nr Mat,,,
Data,Fel,Numar,Intrari,Iesiri,Stoc,Data si semnatura de control (Observatii)'''
def creaza_fila(fila, suma):
    
    fisier = fila + '.csv'
    a = open(fisier, 'w')
    a.write(ANTET)
    a.close()

creaza_fila("fila", 25)