Unitatea,,Fisa de Magazie,U.M.,,
                S.C. Valenti, Impex S.R.L.,"Material (produs), sortiment, calitate, marca, profil, dimensiune",Furnizor,,
                RO5058275,J05/3962/1993,,Nr Mat,,
                Data,Felul si Numarul,Intrari,Iesiri,Stoc,Data si semnatura de control (Observatii)
                r())
fi = ''
for file in listdir():
	a = open(file, 'r')
	b = a.readlines()[-2:]
	a.close
	#print(file, b)
	fi += file+"\n"
	for c in b:
		fi += c
	fi += "\n"
#print(fi)
x = open("_check_file_result.txt", 'w')
y = x.write(fi)
x.close()	
	

