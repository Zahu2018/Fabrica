'''Valenti v1
+---------+
| Fise de |
| magazie |
+---------+---------+
|Saison 2 | Saison 3|
+-------------------+
|
'''

import tkinter
import subprocess


def fise_de_magazie_folder():
	subprocess.Popen('explorer "{0}"'.format('D:\\Valenti\\2018\\Fise_Magazie')) # schimba path of director
def fise_de_magazie():
	subprocess.call(['python','FiseMagazie_v2.pyw'])

def open_stuckliste2():
	subprocess.Popen('explorer "{0}"'.format('D:\\Valenti\\2018\\Stuckliste\\Saison_2.xls')) # schimba path of director
def open_stuckliste3():
	subprocess.Popen('explorer "{0}"'.format('D:\\Valenti\\2018\\Stuckliste\\Saison_3.xls')) # schimba path of director

def feinplanung():
	subprocess.Popen('explorer "{0}"'.format('D:\\Valenti\\2018\\Feinplanung2018.ods')) # schimba path of director


app = tkinter.Tk()
app.title("Valenti v1")
app.geometry("300x300+200+100")
# 1. PRIMUL RAND DE BUTOANE
b00 = tkinter.Button(app, text='Fise de\n magazie\nFOLDER', command=fise_de_magazie_folder)
b00.grid(column=0, row=0)
b01 = tkinter.Button(app, text='Fise de\n magazie\nPROGRAM', command=fise_de_magazie)
b01.grid(column=1, row=0)
# 2. AL DOILEA RAND DE BUTOANE
b10 = tkinter.Button(app, text='Stuckliste\nsaison 2', command=open_stuckliste2)
b10.grid(row=1, column=0)
b11 = tkinter.Button(app, text='Stuckliste\nsaison 3', command=open_stuckliste3)
b11.grid(row=1, column=1)
# 3. AL TREILEA RAND DE BUTOANE
b20 = tkinter.Button(app, text='Feinplanung', command=feinplanung)
b20.grid(row=2, column=0)
app.mainloop()
