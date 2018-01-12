#   ATE - SERAFIL
#   v_1 - programul de baza, minim functional
#   v_2 - stabila
#   v_2.0 - verifica daca fila exista pentru a nu o rescrie
#   v_2.1 - afiseaza denumirea materialului cu care lucrezi = IMPLEMENTAT
#         - daca la cantitate nu este scris nimic atunci prin apasarea butonului OK se inchide fila fara nici o inregistrare = IMPLEMENTAT
#   v_2.2 - 
####################################
#    A program written by: Zah    #
###################################
from tkinter import *
from tkinter import ttk
from os import listdir
import os.path



class Ate:
    def __init__(self, master):
        self.master = master
        

        #FRAME SUS
        self.framesus = ttk.Frame(self.master)

        self.frameunu = LabelFrame(self.framesus, text = "Data si documentul")
        self.datal = ttk.Label(self.frameunu, text = "Data:")
        self.datal.grid(column = 0, row = 0, sticky = 'W')
        self.data = ttk.Entry(self.frameunu)
        self.data.grid(column = 1, row = 0, sticky = 'W')
        self.documentl = ttk.Label(self.frameunu, text = "Document:")
        self.documentl.grid(column = 0, row = 1, sticky = 'W')
        self.document = ttk.Entry(self.frameunu)
        self.document.grid(column = 1, row = 1, sticky = 'W')
        self.frameunu.grid(column = 0, row = 0, sticky = 'n')

        self.frameradio = LabelFrame(self.framesus, text = "Adauga sau scade")
        self.Adauga = StringVar()
        self.adauga = ttk.Radiobutton(self.frameradio, text = 'Intrare', variable = self.Adauga, value = 1)
        self.adauga.grid(column = 0, row = 0)
        self.scade = ttk.Radiobutton(self.frameradio, text = 'Iesire', variable = self.Adauga, value = 2)
        self.scade.grid(column = 0, row = 1, sticky ='W')
        self.frameradio.grid(column = 1, row = 0, sticky = 'n')

        self.framefila = LabelFrame(self.framesus, text = "Creaza o noua fila")
        self.fila = ttk.Entry(self.framefila)
        self.fila.grid(column = 0, row = 0)
        self.newdoc = ttk.Button(self.framefila, text = "Creaza", command = self.creaza_fila)
        self.newdoc.grid(column = 0, row = 1)
        self.framefila.grid(column = 2, row = 0, sticky = 'n')

        self.framesus.grid(column = 0, row = 0, columnspan = 2)

        #FRAME AFISARE ULTIMELE 3 LINII
        #NOT IMPLEMENTED

        self.frame_afisare = LabelFrame(self.master, text = "Afisare ultimele trei randuri")
        
        #se creaza mai jos la linia 135
        #self.trei_randuri = ttk.Label(self.frame_afisare, text = "...")
        #self.trei_randuri.grid(column = 0, row = 0, sticky = 'W')

        self.frame_afisare.grid(column = 0, row = 1, columnspan = 2, sticky = 'W')


        #FRAME STANGA
        self.framestanga = LabelFrame(self.master, text = "Lista cu fise de magazie")

        self.canvas = Canvas(self.framestanga, borderwidth=0, background="#ffffff", width = 100)
        self.frame = Frame(self.canvas, background="#ffffff")
        self.vsb = Scrollbar(self.framestanga, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(anchor = 'w', side="left", fill="y", expand=True)
        self.canvas.create_window((3,3), window=self.frame, anchor="nw", tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.populate()

        self.framestanga.grid(column = 0, row = 2, sticky = 'w')

        #FRAME DREAPTA
        self.framedreapta = LabelFrame(self.master, text = "Introdu cantitatea")

        self.label1 = Label(self.framedreapta, text = "Fise de magazie")
        self.label1.grid()
        #self.label = Label(self.framedreapta, text = "Cantitate")
        #self.label.grid()
        self.cantitate = ttk.Entry(self.framedreapta)
        self.cantitate.grid()
        #self.cantitate.focus_set() #focalizeaza pe cantitate
        self.but = ttk.Button(self.framedreapta, text = 'Ok', command = self.adauga_ate)
        self.but.grid()

        self.framedreapta.grid(column = 1, row = 2, sticky = "nw")

    def populate(self):

        
        self.lista = listdir()
        #txt = StringVar()
        
        for nr, file in enumerate(self.lista):
            #button.append(Button(self.framestanga, text = file, command = lambda file = file : self.adauga_ate(file)))
            #button.grid(sticky=W)
            bu = Button(self.frame, text = file, command = lambda file=file :self.deschide_fila(file), background = "white", borderwidth = 0, activeforeground = 'red')
            bu.grid(sticky = 'W')
        
        

    def deschide_fila(self, m): #butoanele cu numele fisierelor
    #DESCHIDE FISIERUL PENTRU CITIRE SI ADAUGARE
        self.fila_deschisa_citire = open(m, 'r')
        self.fila_deschisa = open(m, 'a')
        self.cantitate.delete(0, 'end') # clear entry
        self.cantitate.focus_set() #focalizeaza pe cantitate
        self.fila = self.fila_deschisa_citire.read()
        self.fila_deschisa_citire.close()
        self.label1.config(text = str(m))
        #linii pentru afisare 3 la numar
        #l1 = lista[lc-4]
        #l2 = lista[lc-3]
        #l3 = lista[lc-2]
        #self.l1 = ttk.Label(self.frame_afisare, text = l1)
        #self.l1.grid(column = 0, row = 0, sticky = 'W')
        #self.l2 = ttk.Label(self.frame_afisare, text = l2)
        #self.l2.grid(column = 0, row = 1, sticky = 'W')
        #self.l3 = ttk.Label(self.frame_afisare, text = l3)
        #self.l3.grid(column = 0, row = 2, sticky = 'W')
        
              
       

    def adauga_ate(self): # butonul OK care va scrie in fisier si inchide fila
    #CALCULEAZA SCRIE IN FISIER SI INCHIDE
        initial = 0
        nr = self.fila.count('\n')
        lista = []
        for i in range(nr):
            final = self.fila.find('\n', initial)
            lin = self.fila[initial:final]
            #print(lin)
            lin_lista = lin.split(',')
            lista.append(lin_lista)
            initial = final + 1
        lc = len(lista)

        #linia pentru lucru
        ultima_linie = lista[lc-1]
        lu = len(ultima_linie)

        unu = str(self.data.get())
        doi = str(self.document.get())
        ad = self.Adauga.get()
        cantitate_introdusa = self.cantitate.get()
        stoc_vechi = float(ultima_linie[lu-1])
        if cantitate_introdusa == '':
            self.fila_deschisa.close()
            self.label1.config(text = "")
        else:
            cant_i = float(cantitate_introdusa)
            fisier = self.fila_deschisa_citire
            #print(stoc_vechi)

         
        
            if ad == "1":
                #ADAUGARE
                
                stoc = stoc_vechi + cant_i
                stoc_sir = str(stoc)
                cant = str(cant_i)
                var1i = unu+","+doi+","+cant+",,"+stoc_sir+"\n"
                var1 = str(var1i)
                self.fila_deschisa.write(var1)
                self.label1.config(text = "")
                
                
                  
            elif ad =="2":
                #SCADEREstoc = float(stoc_vechi)+cant_i
                stoc = stoc_vechi - cant_i
                stoc_sir = str(stoc)
                cant = str(cant_i)
                var2i = unu+","+doi+",,"+cant+","+stoc_sir+"\n"
                var2 = str(var2i)
                self.fila_deschisa.write(var2) # aici scrie in fila
                self.label1.config(text = "")

            else:
                print("Alege o optiune de mai sus: INTRARE sau IESIRE")
            print(fisier, " = ", cant_i)
            print(stoc_vechi, "-", stoc_sir)    

                

        self.fila_deschisa.close() 

    def creaza_fila(self):
        a = self.fila.get()
        item = a
        m = "%s.csv" %a
        if os.path.isfile(m):
            print("Fisierul exista deja")
        else:
            with open(m, 'w') as b:
                b.write("Denumire produs,%s\nUnitate de masura,\nData,Document,Intrare,Iesire,Stoc\n03.01.2017,Din FM 2016/Inventar,0,0,0\n"%item)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

         
    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Contacte(self.newWindow)

class Contacte: # nu are nici o treaba cu programul. E asa ... in plus
    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(self.master)
        self.quitButton = ttk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton. grid()
        self.frame. grid()

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Contacte(self.newWindow)
            
    def close_windows(self):
        self.master.destroy()

def main():
    root = Tk()
    root.title("Fise de magazie (pt. Serafil)")
    app = Ate(root)
    root.mainloop()

if __name__ == '__main__':
    main()