# program valenti, main, principal
#
# 22.06.2019
# Florian Zah

from tkinter import Tk, PhotoImage, Button
from tkinter.ttk import LabelFrame, Frame
import subprocess

class PROGRAM:
	'''Programul principal - Valenti'''
	def __init__(self):
		
		program = Tk()
		program.title('Valenti - command center')

		foto = PhotoImage(file='D:\\Valenti\\PROGRAME\\PROGRAM\\fundal.png')
		
		lab_meniu = Frame(program)
		lab_meniu.grid(row=0, column=0, columnspan=2, sticky='nwse')
		lab_fm = LabelFrame(program, text='Fise de magazie')
		lab_fm.grid(row=1, column=0, sticky='n')
		lab_fp = LabelFrame(program, text='Planuri si stuckliste')
		lab_fp.grid(row=1, column=1, sticky='n')

		bm1 = Button(lab_meniu, text='Help', command=self.help, relief='flat')
		bm1.grid(row=0, column=1, sticky='nw')

		b01 = Button(lab_fm, text="Inregistreaza \nautomat un ZEP", command=self.inregistreaza_automat_un_zep, image=foto, compound='center', relief='flat')
		b01.grid(row=0, column=0)
		b02 = Button(lab_fm, text="Inregistreaza/Scade \nmanual un ZEP/CFL", command=self.inregistreaza_manual_un_zep,  image=foto, compound='center', relief='flat')
		b02.grid(row=0, column=1)
		b03 = Button(lab_fm, text="Fise de magazie", command=self.fise_de_magazie, image=foto, compound='center', relief='flat')
		b03.grid(row=1, column=0)
		b04 = Button(lab_fm, text="Scade automat \nun CFL", command=self.scade_cfl, image=foto, compound='center', relief='flat')
		b04.grid(row=1, column=1)

		b11 = Button(lab_fp, text="Feinplanung", command=self.feinplanung, image=foto, compound='center', relief='flat')
		b11.grid(row=0, column=0)
		b12 = Button(lab_fp, text="Stuckliste", command=self.stuckliste, image=foto, compound='center', relief='flat')
		b12.grid(row=0, column=1)

		program.mainloop()

	def help(self):
		pass
	def inregistreaza_automat_un_zep(self):
		subprocess.call(['python','D:\\Valenti\\PROGRAME\\PROGRAM\\scrie_automat_in_fm.py'])
	def inregistreaza_manual_un_zep(self):
		subprocess.call(['python','D:\\Valenti\\PROGRAME\\PROGRAM\\scrie_manual_in_fm.pyw'])
	def fise_de_magazie(self):
		subprocess.Popen('explorer "{0}"'.format('D:\\Valenti\\2019\\Fise_Magazie')) # schimba path of director
	def feinplanung(self):
		subprocess.call(['C:\\Program Files\\LibreOffice\\program\\soffice.exe', 'D:\\Valenti\\2019\\Feinplanung.xlsx']) 
	def stuckliste(self):
		subprocess.Popen('explorer "{0}"'.format('D:\\Valenti\\2019\\Stuckliste')) # schimba path of director
	def scade_cfl(self):
		subprocess.call(['python','D:\\Valenti\\PROGRAME\\PROGRAM\\scade_automat_un_cfl.py'])

PROGRAM()