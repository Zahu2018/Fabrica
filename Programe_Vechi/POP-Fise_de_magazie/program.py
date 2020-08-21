# Fise de magazie versiunea 1

import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from os import listdir

class GUI:
    def __init__(self, master):
        self.master = master
        self.partea_de_sus()
        self.partea_de_mijloc()
        self.partea_de_jos()
        

    def partea_de_sus(self):
        self.frame_sus = Frame(self.master)
        self.frame_sus.grid(row=0, column=0, sticky='w')
        l1 = Label(self.frame_sus, text = 'Data:')
        l1.grid(column=0, row=0, sticky='w')
        l2 = Label(self.frame_sus, text = 'Aviz:')
        l2.grid(column=0, row=1, sticky='w')
        e1 = Entry(self.frame_sus)
        e1.grid(column=1, row=0, sticky='w')
        e2 = Entry(self.frame_sus)
        e2.grid(column=1, row=1, sticky='w')
        b = ttk.Button(self.frame_sus, text = 'Creaza o noua fise', command = self.creaza_fise)
        b.grid(column=3, row=0, sticky='e')
    def partea_de_mijloc(self):   
        self.frame_mijloc = ttk.LabelFrame(self.master, text='Categorii')
        self.frame_mijloc.grid(row=1, column=0, sticky='ew')
        self.frame_mijloc.grid_propagate(True)
        self.variable = StringVar
        directoare = os.listdir("C:\\Users\\User\\Desktop\\POP-Fise_de_magazie")
        n = 0
        for i, cat in enumerate(directoare):
            bu0 = Radiobutton(self.frame_mijloc, text = cat, command = lambda cat=cat :self.populate, variable = self.variable(), value=i, activeforeground = 'red', )
            bu0.grid(column=i, row=0, sticky = 'w')

    def partea_de_jos(self):
        self.frame_jos = Frame(self.master)
        self.frame_jos.grid(row=2, column=0, sticky='ew')
        # ====== S T A N G A ========
        self.materiale = ttk.LabelFrame(self.frame_jos, text = "Fisele de magazie")
        self.materiale.grid(column = 0, row = 0, sticky = 'w')

        self.vsb = ttk.Scrollbar(self.materiale, orient="vertical")
        self.vsb.grid(column=1, row=0, sticky='ns')
        self.canvas = Canvas(self.materiale, borderwidth=0, background="#ffffff", width = 150)
        self.canvas.grid(sticky='nsew', column=0, row=0)
        self.vsb.config(command = self.canvas.yview)
        self.frame = Frame(self.canvas, background="#ffffff")
        self.canvas.create_window((3,3), window=self.frame, anchor="nw", tags="self.frame")
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.frame.bind("<Configure>", self.onFrameConfigure)

        # ===== D R E A P T A =========
        self.lucru = ttk.LabelFrame(self.frame_jos, text = "WorkZone")
        self.lucru.grid(column = 1, row = 0, sticky = 'ew')
        self.label_material = Label(self.lucru, text = 'Denumire Material')
        self.label_material.grid(column=0, row=0, sticky='wn')

        self.vsb1 = ttk.Scrollbar(self.lucru, orient="vertical")
        self.vsb1.grid(column=1, row=0, sticky='ns')
        self.canvas1 = Canvas(self.lucru, borderwidth=0, background="#ffffff")
        self.canvas1.grid(sticky='nsew', column=0, row=0)
        self.vsb.config(command = self.canvas1.yview)
        self.frame1 = Frame(self.canvas1, background="#ffffff")
        self.canvas1.create_window((3,3), window=self.frame1, anchor="nw", tags="self.frame1")
        self.canvas1.configure(yscrollcommand=self.vsb1.set)
        self.frame.bind("<Configure>", self.onFrame1Configure)
        #----------------------------------
        
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    def onFrame1Configure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))    
    def creaza_fise(self):
        pass
    def populate(self):
        pass
    
class Rezolva:
    pass




def main():
    root = Tk()
    root.title("Fise de magazie v1")
    root.geometry('800x400')
    app = GUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()