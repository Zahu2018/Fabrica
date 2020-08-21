#   FISE DE MAGAZIE v 2
####################################
#    A program written by: Zah    #
###################################
'''
+-----------------------------------------------------------------+
| Open |                                                          |
+------------+-----------+-----------------+----------------------+
| Piele      | Bolero    | Data     ______ | Bolero - inregistrat |
| Captuseala | Dusty     | Document ______ | Softcalf - anulat    |
| Elastic    | Softcalf  | Intrare o       |       ...            |
|   ...      |   ...     | Iesire  o       |       ...            |
|   ...      |   ...     |                 |                      |

+------------+-----------+-----------------+----------------------+

'''
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from os import listdir




class Ate:
    def __init__(self, master):
        self.master = master

        # FRAME MENU - folosim butoane in loc de meniu
        self.framesus = ttk.Frame(self.master)
        self.buton_open = Button(self.framesus, text='Open', command=self.deschide_categorii, relief='flat')
        self.buton_open.grid(column=0, row=0)
        self.framesus.grid(column=0, row=0, columnspan=4, sticky='w')

        # FRAME CATEGORII
        self.frame_categorii = ttk.LabelFrame(self.master, text='Categorii')
        self.frame_categorii.grid(column=0, row=1)

        self.vsb0 = ttk.Scrollbar(self.frame_categorii, orient="vertical",)
        self.vsb0.grid(column = 1, row = 0, sticky = 'ns')

        self.canvas0 = Canvas(self.frame_categorii, borderwidth=0, background="#ffffff", width = 150)
        self.canvas0.grid(column=0, row=0, sticky='nsew')

        self.vsb0.config(command = self.canvas0.yview)
        
        self.scrollwindows = Frame(self.canvas0, background="#ffffff")
        
        self.canvas0.create_window((3,3), window=self.scrollwindows, anchor="nw", tags="self.scrollwindows") # (0,0)
        
        self.canvas0.configure(yscrollcommand=self.vsb0.set)
      
        self.scrollwindows.bind("<Configure>", self.onFrameConfigure0)
        

        # FRAME MATERIALE
        self.materiale = ttk.LabelFrame(self.master, text = "Fise de magazie")
        self.materiale.grid(column = 1, row = 1, sticky = 'w')

        self.vsb = ttk.Scrollbar(self.materiale, orient="vertical")
        self.vsb.grid(column=1, row=0, sticky='ns')

        self.canvas = Canvas(self.materiale, borderwidth=0, background="#ffffff", width = 150)
        self.canvas.grid(sticky='nsew', column=0, row=0)

        self.vsb.config(command = self.canvas.yview)

        self.frame = Frame(self.canvas, background="#ffffff")
        
        self.canvas.create_window((3,3), window=self.frame, anchor="nw", tags="self.frame")

        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.frame.bind("<Configure>", self.onFrameConfigure)
        
        
        # FRAME CALCULARE
        self.framecalculare = ttk.LabelFrame(self.master, text = "Calculare")
        self.datal = ttk.Label(self.framecalculare, text = "Data:")
        self.datal.grid(column = 0, row = 0, sticky = 'w')
        self.data = ttk.Entry(self.framecalculare)
        self.data.grid(column = 1, row = 0, sticky = 'w')
        self.documentl = ttk.Label(self.framecalculare, text = "Document:")
        self.documentl.grid(column = 0, row = 1, sticky = 'w')
        self.document = ttk.Entry(self.framecalculare)
        self.document.grid(column = 1, row = 1, sticky = 'w')
        self.Adauga = StringVar()
        self.adauga = ttk.Radiobutton(self.framecalculare, text = 'Intrare', variable = self.Adauga, value = 1)
        self.adauga.grid(column = 0, row = 2, sticky='w')
        self.scade = ttk.Radiobutton(self.framecalculare, text = 'Iesire', variable = self.Adauga, value = 2)
        self.scade.grid(column = 0, row = 3, sticky ='w')
        self.label1 = Label(self.framecalculare, text = "Fise de magazie")
        self.label1.grid(columnspan=2)
        #self.label = Label(self.framedreapta, text = "Cantitate")
        #self.label.grid()
        self.cantitate = ttk.Entry(self.framecalculare, width=12)
        self.cantitate.grid(columnspan=2)
        #self.cantitate.focus_set() #focalizeaza pe cantitate
        self.but = ttk.Button(self.framecalculare, text = 'Ok', command = self.adauga_ate)
        self.but.grid(columnspan=2)
        self.label_stoc = Label(self.framecalculare, text='stoc')
        self.label_stoc.grid(columnspan=2)
        self.framecalculare.grid(column = 2, row = 1, sticky='nw')



        # FRAME INFORMATII
        self.frame_informatii = ttk.LabelFrame(self.master, text='Informatii')
        Label(self.frame_informatii, text='Informatii').grid()

        self.frame_informatii.grid(column=3, row=1, sticky='nw')

# =======================================================
    def deschide_categorii(self):

        self.filename =  filedialog.askdirectory() # path of the dir Fise de Magazie
        directoare = os.listdir(self.filename)
        
        for cat in directoare:
            
            #button.append(Button(self.framestanga, text = file, command = lambda file = file : self.adauga_ate(file)))
            #button.grid(sticky=W)
            bu0 = Button(self.scrollwindows, text = cat, command = lambda cat=cat :self.populate(cat), background = "white", borderwidth = 0, activeforeground = 'red')
            bu0.grid(sticky = 'w')
        
    def populate(self, cate):   
        for widget in self.frame.winfo_children():
            widget.destroy()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        self.fn = self.filename+"/"+cate
        #print(self.fn)
        
        lista = listdir(self.fn)
        #txt = StringVar()
        #print(lista)
        for file in lista:
            bu = Button(self.frame, text = file, command = lambda file=file :self.deschide_fila(file), background = "white", borderwidth = 0, activeforeground = 'red') # , background = "white", borderwidth = 0, activeforeground = 'red'
            bu.grid(sticky = 'W')
        
        

    def deschide_fila(self, m): #butoanele cu numele fisierelor
    #DESCHIDE FISIERUL PENTRU CITIRE SI ADAUGARE
        n = self.fn+'/'+m
        self.fila_deschisa_citire = open(n, 'r')
        self.fila_deschisa = open(n, 'a')
        self.cantitate.delete(0, 'end') # clear entry
        self.cantitate.focus_set() #focalizeaza pe cantitate
        self.fila = self.fila_deschisa_citire.read()
        self.fila_deschisa_citire.close()
        self.label1.config(text = str(m))
        self.label_stoc.config(text=str(self.fila[-1:-20]))
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
        print(ultima_linie)
        lu = len(ultima_linie)

        unu = str(self.data.get())
        doi = str(self.document.get())
        ad = self.Adauga.get()
        cantitate_introdusa = self.cantitate.get()
        stoc_vechi = float(ultima_linie[lu-2])
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
                var1i = unu+","+doi+","+cant+",,"+stoc_sir+","+"\n"
                var1 = str(var1i)
                self.fila_deschisa.write(var1)
                self.label1.config(text = "")
                
                
                  
            elif ad =="2":
                #SCADEREstoc = float(stoc_vechi)+cant_i
                stoc = stoc_vechi - cant_i
                stoc_sir = str(stoc)
                cant = str(cant_i)
                var2i = unu+","+doi+",,"+cant+","+stoc_sir+","+"\n"
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

    def onFrameConfigure0(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas0.configure(scrollregion=self.canvas0.bbox("all"))
         
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
    root.title("Fise de magazie v2")
    app = Ate(root)
    root.mainloop()

if __name__ == '__main__':
    main()