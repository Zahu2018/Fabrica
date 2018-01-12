#Verifica ultima linie din FM ate
import os
from os import listdir


#print(listdir())
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
	

