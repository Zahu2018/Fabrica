# calculator, kalkulationen, calculatii, 
# Calculeaza kalkulatii: procente, ruckgabe, ersatz, etc
# 28.05.2019

# FORMULE
# pramie % = ((lederansatz - (lederausgabe - ruckgabe)) * 100)/lederarnsatz
# gevin_verlust = (lederansatz - (lederausgabe - ruckgabe))


import tkinter
from decimal import *

class Kalkulation:
    def __init__(self, master):
        self.master = master
        master.title("CalKal")

        self.frame_sus = tkinter.Frame(master, bd=10)
        self.frame_sus.grid(column=0, row=0)
        self.lederansatz = tkinter.Label(self.frame_sus, text="Lederansatz")
        self.lederansatz.grid(column=0, row=0)
        self.entry_lederansatz = tkinter.Entry(self.frame_sus)
        self.entry_lederansatz.grid(column=1, row=0)
        self.lederausgaben = tkinter.Label(self.frame_sus, text="Lederausgaben")
        self.lederausgaben.grid(column=0, row=1)
        self.entry_lederausgaben = tkinter.Entry(self.frame_sus)
        self.entry_lederausgaben.grid(column=1, row=1)
        self.ruckgabe = tkinter.Label(self.frame_sus, text="Ruckgabe")
        self.ruckgabe.grid(column=0, row=2)
        self.entry_ruckgabe = tkinter.Entry(self.frame_sus)
        self.entry_ruckgabe.grid(column=1, row=2)
        self.gevin_verlust = tkinter.Label(self.frame_sus, text="Gevin / Verslust")
        self.gevin_verlust.grid(column=0, row=3)
        self.entry_gevin_verlust = tkinter.Entry(self.frame_sus)
        self.entry_gevin_verlust.grid(column=1, row=3)
        self.pramie = tkinter.Label(self.frame_sus, text="Pramie")
        self.pramie.grid(column=0, row=4)
        self.entry_pramie = tkinter.Entry(self.frame_sus)
        self.entry_pramie.grid(column=1, row=4)

        self.frame_mijloc = tkinter.Frame(master, bd=10)
        self.frame_mijloc.grid(column=0, row=1)
        self.ok = tkinter.Button(self.frame_mijloc, text='Calculeaza', command=self.ok)
        self.ok.grid(column=0, row=0)
        self.reset = tkinter.Button(self.frame_mijloc, text='Reset', command=self.reset)
        self.reset.grid(column=1, row=0)

        self.frame_jos = tkinter.Frame(master, border=10)
        self.frame_jos.grid(column=0, row=2)
        self.g_v = tkinter.Label(self.frame_jos, text="Gevin / Verlust")
        self.g_v.grid(column=0, row=0)
        self.p = tkinter.Label(self.frame_jos, text="Pramie")
        self.p.grid(column=1, row=0)
        self.r = tkinter.Label(self.frame_jos, text="Ruckgabe")
        self.r.grid(column=2, row=0)
        # afisare
        self.rez_g = tkinter.Label(self.frame_jos, text="", font=(40))
        self.rez_g.grid(column=0, row=1)
        self.rez_p = tkinter.Label(self.frame_jos, text="", font=(40))
        self.rez_p.grid(column=1, row=1)
        self.rez_r = tkinter.Label(self.frame_jos, text="", font=(40))
        self.rez_r.grid(column=2, row=1)

        


      

    def ok(self):
        self.rez_g.config(text='')
        self.rez_p.config(text='')
        self.rez_r.config(text='')

        lederansatz = int(self.entry_lederansatz.get())
        lederausgabe = int(self.entry_lederausgaben.get())
        try:
            # RUCKGABE input
            ruckgabe = int(self.entry_ruckgabe.get())
            #print(ruckgabe)
            verbrauch = lederausgabe - ruckgabe
            gevin__verlust = lederansatz - verbrauch
            pramie = round((gevin__verlust*100)/lederansatz, 2)
            rp = str(pramie)+'%' # rezultat pramie (sa apara si %)
            self.rez_g.config(text=gevin__verlust)
            self.rez_p.config(text=rp)
            self.rez_r.config(text='')
            #print(verbrauch, gevin__verlust, pramie)

        except ValueError:
            #print('ERROR1')
            try:
                # GEV_VER input
                gev_ver = int(self.entry_gevin_verlust.get())
                #print(gev_ver, 'Merge')
                necesar_ruckgabe = gev_ver - lederansatz + lederausgabe
                #print(necesar_ruckgabe)
                


                verbrauch = lederausgabe - necesar_ruckgabe
                gevin__verlust = lederansatz - verbrauch
                pramie = round((gevin__verlust*100)/lederansatz, 2)
                
                rp = str(pramie)+'%' # rezultat pramie (sa apara si %)
                self.rez_p.config(text=rp)
                self.rez_r.config(text=necesar_ruckgabe)
                self.rez_g.config(text='')
                
            except ValueError:
                #print('ERROR2')
                try:
                    # PRAMIE (procentaj)
                    pramie = float(self.entry_pramie.get())
                    print("merge", pramie)
                    necesar_ruckgabe = round((pramie*lederansatz/100) + lederausgabe - lederansatz, 0)
                    verbrauch = lederausgabe - necesar_ruckgabe
                    gevin__verlust = lederansatz - verbrauch
                    self.rez_r.config(text=necesar_ruckgabe)
                    self.rez_p.config(text='')
                    self.rez_g.config(text=gevin__verlust)

                except ValueError:
                    #print('ERROR3')
                    pass

    def reset(self):
        # self.entry.delete(0, 'end')
        self.entry_lederansatz.delete(0, 'end')
        self.entry_lederausgaben.delete(0, 'end')
        self.entry_ruckgabe.delete(0, 'end')
        self.entry_gevin_verlust.delete(0, 'end')
        self.entry_pramie.delete(0, 'end')
        self.rez_g.config(text='')
        self.rez_p.config(text='')
        self.rez_r.config(text='')
        self.entry_lederansatz.focus()

root = tkinter.Tk()
my_gui = Kalkulation(root)
root.mainloop()