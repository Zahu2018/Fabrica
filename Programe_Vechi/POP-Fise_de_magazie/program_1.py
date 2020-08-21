from tkinter import *
from tkinter import ttk
import os
class FrameSus:
    def __init__(self, master):
        self.frame_sus = ttk.LabelFrame(master, text = "Intro")
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
    def creaza_fise(self):
        def creaza_fisa():
            pass
            #scrie in fisier antetul / inchide fila
            #refres la lista din stanga (sa apara si noua fila)
            #distruge creaza_fise
        b = Tk()
        label_filename = Label(b, text="Introduceti denumirea materialului")
        label_filename.grid(row=0, column=0)
        entry_filename = Entry(b)
        entry_filename.grid(row=1, column=0)
        buton_filename = ttk.Button(b, text='OK', command=creaza_fisa)
        buton_filename.grid(column=0, row=2)
        #director = preia directorul in care e in variabila: director
        #creaza variabila antet a fisierului
        
            
        b.mainloop

class FrameMijloc:
    def __init__(self, master):
        self.frame_mijloc = ttk.LabelFrame(master, text='Categorii')
        self.frame_mijloc.grid(row=1, column=0, sticky='ew')
        self.frame_mijloc.grid_propagate(True)
        directoare = os.listdir("C:\\Users\\User\\Desktop\\POP-Fise_de_magazie")
        n = 0
        for i, cat in enumerate(directoare):
            bu0 = ttk.Button(self.frame_mijloc, text = cat, command = lambda cat=cat :self.populate)
            bu0.grid(column=i, row=0, sticky = 'w')
    def populate(self):
        pass
class FrameJos:
    def __init__(self, master):
        #==== FRAME JOS : FrameStanga ---- FrameDreapta ===
        self.frame_jos = Frame(master)
        self.frame_jos.grid(row=2, column=0, sticky='w')


        self.frame_jos_stanga = ttk.LabelFrame(self.frame_jos, text = 'Categorii')
        self.frame_jos_stanga.grid(row=0, column=0, sticky='w')
        self.frame_jos_dreapta = ttk.LabelFrame(self.frame_jos, text = 'Working')
        self.frame_jos_dreapta.grid(row=0, column=1, sticky='w')
        

    
        # ====== S T A N G A ========
        self.vsb = ttk.Scrollbar(self.frame_jos_stanga, orient="vertical")
        self.vsb.grid(column=1, row=0, sticky='ns')
        self.canvas = Canvas(self.frame_jos_stanga, borderwidth=0, background="#ffffff", width = 150)
        self.canvas.grid(sticky='nsew', column=0, row=0)
        self.vsb.config(command = self.canvas.yview)
        self.frame = Frame(self.canvas, background="#ffffff")
        self.canvas.create_window((3,3), window=self.frame, anchor="nw", tags="self.frame")
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.frame.bind("<Configure>", self.onFrameConfigure)
    
        # ===== D R E A P T A =========
        # ===== sus === 
        self.vsb1 = ttk.Scrollbar(self.frame_jos_dreapta, orient="vertical")
        self.vsb1.grid(column=1, row=0, sticky='ns')
        self.canvas1 = Canvas(self.frame_jos_dreapta, borderwidth=0, background="#ffffff")
        self.canvas1.grid(sticky='nsew', column=0, row=0)
        self.vsb.config(command = self.canvas1.yview)
        self.frame1 = Frame(self.canvas1, background="#ffffff")
        self.canvas1.create_window((3,3), window=self.frame1, anchor="nw", tags="self.frame1")
        self.canvas1.configure(yscrollcommand=self.vsb1.set)
        self.frame.bind("<Configure>", self.onFrame1Configure)
        # ===== mijloc === 
        # ===== jos === 
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    def onFrame1Configure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all")) 

master = Tk()
master.title("Fise de magazie v1")
master.geometry('800x400')

framesus = FrameSus(master)
framemijloc = FrameMijloc(master)
framejos = FrameJos(master)

master.mainloop()