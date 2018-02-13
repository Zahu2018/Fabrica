from tkinter import filedialog
import tkinter

def deschide_fila():
	fila = filedialog.askopenfilename()
	fila1 = (str(fila)).replace('/', '\\')
	print(fila1)
	b = open(fila1, 'r')
	c = b.read()
	b.close
	print(c)


app = tkinter.Tk()
a = tkinter.Button(app, text='Open', command=deschide_fila)
a.grid()
app.mainloop()