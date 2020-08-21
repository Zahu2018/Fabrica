# fise de magazie,
# Administreaza fise de magazie
# Florian Zah
# 03.06.2019
'''
+-----------------------------------------------------------------+
| Open | Creaza noua fila                                         |
+------------+-----------+-----------------+----------------------+
| Piele      | Bolero    | Data     ______ | Bolero - inregistrat |
| Captuseala | Dusty     | Document ______ | Softcalf - anulat    |
| Elastic    | Softcalf  | Intrare o       |       ...            |
|   ...      |   ...     | Iesire  o       |       ...            |
|   ...      |   ...     |                 |                      |
+------------+-----------+-----------------+----------------------+
|   ULTIMELE LINII DIN FILA                                       |
|                                                                 |
+-----------------------------------------------------------------+
'''
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from os import listdir
from decimal import *
import shutil


class CreazaONouaFiseDeMagazie:
    def __init__(self, master):
        self.master = master
        label_data = Label


class Ate:
    def __init__(self, master):
        self.master = master

        # FRAME MENU - folosim butoane in loc de meniu
        self.framesus = ttk.Frame(self.master)
        self.buton_open = Button(self.framesus, text='Open', command=self.deschide_categorii, relief='flat')
        self.buton_open.grid(column=0, row=0)
        self.buton_creaza_fm = Button(self.framesus, text='Creaza fise magazie', command=self.creaza_fm, relief='flat')
        self.buton_creaza_fm.grid(column=1, row=0)
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

        self.canvas = Canvas(self.materiale, borderwidth=0, background="#ffffff", width = 250)
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
        self.adauga = StringVar()
        self.aduna = ttk.Radiobutton(self.framecalculare, text = 'Intrare', variable = self.adauga, value = 1)
        self.aduna.grid(column = 0, row = 2, sticky='w')
        self.scade = ttk.Radiobutton(self.framecalculare, text = 'Iesire', variable = self.adauga, value = 2)
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
        
        self.framecalculare.grid(column = 2, row = 1, sticky='nw')



        # FRAME INFORMATII
        self.frame_informatii = ttk.LabelFrame(self.master, text='Informatii')
        Label(self.frame_informatii, text='Informatii').grid()

        self.frame_informatii.grid(column=3, row=1, sticky='nw')

        #FRAME ULTIMELE LINII
        #Titluri
        
        self.frame_ultimele_linii = Frame(self.master)

        self.titlu_fise_de_magazie = Label(self.frame_ultimele_linii, text='FISA DE MAGAZIE',  fg='midnight blue', font=("Times New Roman", 14, "bold"))
        self.titlu_fise_de_magazie.grid(row=0, column=0, columnspan=5)

        self.titlu_data = Label(self.frame_ultimele_linii, text='Data',  fg='blue', width=11)
        self.titlu_data.grid(row=1, column=0)
        self.titlu_document = Label(self.frame_ultimele_linii, text='Felul si Nr. Document',  fg='blue', width=20)
        self.titlu_document.grid(row=1, column=1)
        self.titlu_intrari = Label(self.frame_ultimele_linii, text='Intrari',  fg='blue', width=10)
        self.titlu_intrari.grid(row=1, column=2)
        self.titlu_iesiri = Label(self.frame_ultimele_linii, text='Iesiri',  fg='blue', width=10)
        self.titlu_iesiri.grid(row=1, column=3)
        self.titlu_stoc = Label(self.frame_ultimele_linii, text='Stoc', fg='blue', width=10)
        self.titlu_stoc.grid(row=1, column=4)
        #Penultimul rand
        self.titlu_pdata = Label(self.frame_ultimele_linii, text='', width=11)
        self.titlu_pdata.grid(row=2, column=0)
        self.titlu_pdocument = Label(self.frame_ultimele_linii, text='', width=20)
        self.titlu_pdocument.grid(row=2, column=1)
        self.titlu_pintrari = Label(self.frame_ultimele_linii, text='', width=10)
        self.titlu_pintrari.grid(row=2, column=2)
        self.titlu_piesiri = Label(self.frame_ultimele_linii, text='', width=10)
        self.titlu_piesiri.grid(row=2, column=3)
        self.titlu_pstoc = Label(self.frame_ultimele_linii, text='', width=10, justify=LEFT)
        self.titlu_pstoc.grid(row=2, column=4, sticky='W')
        #Ultimul rand
        self.titlu_udata = Label(self.frame_ultimele_linii, text='', width=11)
        self.titlu_udata.grid(row=3, column=0)
        self.titlu_udocument = Label(self.frame_ultimele_linii, text='', width=20)
        self.titlu_udocument.grid(row=3, column=1)
        self.titlu_uintrari = Label(self.frame_ultimele_linii, text='', width=10)
        self.titlu_uintrari.grid(row=3, column=2)
        self.titlu_uiesiri = Label(self.frame_ultimele_linii, text='', width=10)
        self.titlu_uiesiri.grid(row=3, column=3)
        self.titlu_ustoc = Label(self.frame_ultimele_linii, text='', width=10, justify=LEFT)
        self.titlu_ustoc.grid(row=3, column=4, sticky='w')
        #Randul recent
        self.titlu_rdata = Label(self.frame_ultimele_linii, text='', fg='red', width=11)
        self.titlu_rdata.grid(row=4, column=0)
        self.titlu_rdocument = Label(self.frame_ultimele_linii, text='',  fg='red', width=20)
        self.titlu_rdocument.grid(row=4, column=1)
        self.titlu_rintrari = Label(self.frame_ultimele_linii, text='',  fg='red', width=10)
        self.titlu_rintrari.grid(row=4, column=2)
        self.titlu_riesiri = Label(self.frame_ultimele_linii, text='',  fg='red', width=10)
        self.titlu_riesiri.grid(row=4, column=3)
        self.titlu_rstoc = Label(self.frame_ultimele_linii, text='', fg='red', width=10, justify=LEFT)
        self.titlu_rstoc.grid(row=4, column=4, sticky='w')


        '''
        self.penultima_linie = Label(self.frame_ultimele_linii, text='penultima linie')
        self.penultima_linie.grid(row=0, sticky='nw')
        self.ultima_linie = Label(self.frame_ultimele_linii, text='ultima linie')
        self.ultima_linie.grid(row=1, sticky='nw')
        self.linia_recenta = Label(self.frame_ultimele_linii, text='linia recenta')
        self.linia_recenta.grid(row=2, sticky='nw')
        '''
        
        self.frame_ultimele_linii.grid(row=2, column=0, columnspan=4, sticky='nw')

# =======================================================
    def creaza_fm_actiune_buton(self):
        # VERIFICA DACA EXISTA FILA CA SA NU FIE RESCRISA
        x = self.ef.get()  
        cat = self.ca.get()
        canti = self.ec.get()
        d = self.data.get()
        do = self.document.get()
        sl = r'\\'
        np = str(self.fn).replace('/', sl) # np = new path inlocuim / cu \\     
        newfile = np+str(sl)+str(x)+'.csv'
        sursa = 'D:\\Valenti\\2019\\Fise_Magazie\\Adezivi\\0STAS.csv'
        shutil.copy2(sursa, newfile)
        primul_rand = d+","+do+","+canti+",,"+canti+","+"\n"
        with open (newfile, 'a') as spr:
            spr.write(primul_rand)
        self.cfm.destroy()

    def creaza_fm(self):
        # creaza o noua fise de magazie in categoria selectata
        self.cfm =  Tk()
        #cfm.title("Creaza noi fise de magazie")
        
        lf = ttk.Label(self.cfm, text='Nume fise magazie')
        lf.grid(column=0, row=0)
        lca = ttk.Label(self.cfm, text='Categorie')
        lca.grid(column=0, row=1)
        lc = ttk.Label(self.cfm, text='Cantitate')
        lc.grid(column=0, row=2)
        self.ef = ttk.Entry(self.cfm)
        self.ef.grid(column=1, row=0)
        self.eca = ttk.Entry(self.cfm)
        self.eca.grid(column=1, row=1)
        self.ef.focus_set()
        self.ec = ttk.Entry(self.cfm)
        self.ec.grid(column=1, row=2)
        bf = ttk.Button(self.cfm, text="Creaza", command = self.creaza_fm_actiune_buton)
        bf.grid(row=2, columnspan=2, sticky='we')
        self.cfm.mainloop()

    

    def deschide_categorii(self): #actiunea butonului OPEN -> butoane categorii


        self.filename =  filedialog.askdirectory() # path of the dir Fise de Magazie
        directoare = os.listdir(self.filename)
        
        for cat in directoare:
            
            #button.append(Button(self.framestanga, text = file, command = lambda file = file : self.adauga_ate(file)))
            #button.grid(sticky=W)
            bu0 = Button(self.scrollwindows, text = cat, command = lambda cat=cat :self.populate(cat), background = "white", borderwidth = 0, activeforeground = 'red')
            bu0.grid(sticky = 'w')
        
    def populate(self, cate):   #actiunea butonului categorii -> butoane materiale
        for widget in self.frame.winfo_children():
            widget.destroy()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        self.fn = self.filename+"/"+cate # e si pentru functia creaza_fm_actiune_buton
        #print(self.fn)

       
        
        lista = listdir(self.fn)
        #txt = StringVar()
        #print(lista)
        for file in lista:
            bu = Button(self.frame, text = file, command = lambda file=file :self.deschide_fila(file), background = "white", borderwidth = 0, activeforeground = 'red') # , background = "white", borderwidth = 0, activeforeground = 'red'
            bu.grid(sticky = 'W')
        
        

    def deschide_fila(self, m): #actiunea butonului categorii si citire fila
    #DESCHIDE FISIERUL PENTRU CITIRE
    #1. Deschide fila
    #2. Facem matricea


        n = self.fn+'/'+m
        self.nn = n
        self.fila_deschisa_citire = open(n, 'r')
        self.fila = self.fila_deschisa_citire.read()
        self.fila_deschisa_citire.close()

        self.cantitate.delete(0, 'end') # clear entry
        self.cantitate.focus_set() #focalizeaza pe cantitate
        
        self.label1.config(text = str(m))
        
           
        initial = 0
        nr = self.fila.count('\n')
        lista = []
        for i in range(nr):
            final = self.fila.find('\n', initial)
            lin = self.fila[initial:final]
            #print(lin) #printeaza liniile fisierului
            lin_lista = lin.split(',')
            lista.append(lin_lista)
            initial = final + 1
        lc = len(lista)

        #linia pentru lucru
        ultima_linie = lista[lc-1]
        #print(ultima_linie)
        self.titlu_fise_de_magazie.config(text=m)
        #Penultimul rand
        self.titlu_pdata.config(text=lista[lc-2][0])
        self.titlu_pdocument.config(text=lista[lc-2][1])
        self.titlu_pintrari.config(text=lista[lc-2][2])
        self.titlu_piesiri.config(text=lista[lc-2][3])
        self.titlu_pstoc.config(text=lista[lc-2][4])
        #Ultimul rand
        self.titlu_udata.config(text=lista[lc-1][0])
        self.titlu_udocument.config(text=lista[lc-1][1])
        self.titlu_uintrari.config(text=lista[lc-1][2])
        self.titlu_uiesiri.config(text=lista[lc-1][3])
        self.titlu_ustoc.config(text=lista[lc-1][4])
        #Randul recent - in rosu
        self.titlu_rintrari.config(text='')
        self.titlu_riesiri.config(text='')
        self.titlu_rstoc.config(text='')

        lu = len(ultima_linie)

        #self.stoc_vechi = float(ultima_linie[lu-2]) # asta a fost initial
        self.stoc_vechi = round(Decimal(ultima_linie[lu-2]), 2)  


    def adauga_ate(self): # butonul OK care va scrie in fisier si inchide fila
    #CALCULEAZA SCRIE IN FISIER SI INCHIDE
        self.unu = str(self.data.get())
        self.doi = str(self.document.get())  
        self.ad = self.adauga.get()
        self.cantitate_introdusa = self.cantitate.get()
        self.fila_deschisa = open(self.nn, 'a')

        if self.cantitate_introdusa == '':
            self.fila_deschisa.close()
            self.label1.config(text = "")
            
        else:
            #cant_i = float(self.cantitate_introdusa) # asta a fost initial
            cant_i = round(Decimal(self.cantitate_introdusa), 2)
            fisier = self.fila
            #print(stoc_vechi) 

        
            if self.ad == "1":
                #ADAUGARE
                
                stoc = self.stoc_vechi + cant_i
                stoc_sir = str(stoc)
                cant = str(cant_i)
                var1i = self.unu+","+self.doi+","+cant+",,"+stoc_sir+","+"\n"
                var1 = str(var1i)
                self.fila_deschisa.write(var1)
                self.label1.config(text = "")
                #self.linia_recenta.config(text=var1i)
                #Randul recent
                self.titlu_rdata.config(text=self.unu)
                self.titlu_rdocument.config(text=self.doi)
                self.titlu_rintrari.config(text=cant)
                self.titlu_riesiri.config(text='')
                self.titlu_rstoc.config(text=stoc_sir)
                
                  
            elif self.ad =="2":
                #SCADERE
                stoc = self.stoc_vechi - cant_i
                stoc_sir = str(stoc)
                cant = str(cant_i)
                var2i = self.unu+","+self.doi+",,"+cant+","+stoc_sir+","+"\n"
                var2 = str(var2i)
                self.fila_deschisa.write(var2) # aici scrie in fila
                self.label1.config(text = "")
                #self.linia_recenta.config(text=var2i)

                self.titlu_rdata.config(text=self.unu)
                self.titlu_rdocument.config(text=self.doi)
                self.titlu_rintrari.config(text='')
                self.titlu_riesiri.config(text=cant)
                self.titlu_rstoc.config(text=stoc_sir)

            else:
                print("Alege o optiune de mai sus: INTRARE sau IESIRE")
            

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
     

def main():
    root = Tk()
    root.title("Fise de magazie v2")
    app = Ate(root)
    root.mainloop()

if __name__ == '__main__':
    main()