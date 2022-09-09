from tkinter import *  
from tkinter import messagebox
from turtle import color
from controlador import controladorIndex

ventana = Tk()
ventana.title = "Expresiones regulares"
ventana.geometry("600x300")

def expRegEnterosAFD():
    numEnteros = txt1.get()
    estado = controladorIndex.ValidarEnterosAutomata(numEnteros)
    messagebox.showinfo(message=estado, title="Numeros Enteros AFD")

def expRegRealesAFD():
    numEnteros = txt2.get()
    estado = controladorIndex.validarRealesAutomata(numEnteros)
    messagebox.showinfo(message=estado, title="Numeros Reales AFD")

def expRegEnteros():
    numEnteros = txt1.get()
    estado = controladorIndex.ValidarEnteros(numEnteros)
    if estado:
        messagebox.showinfo(message="La cadena es valida", title="Numeros Enteros")
    else:
        messagebox.showerror(message="La cadena en invalida", title="Numeros Enteros")


def expRegReales():
    numReales = txt2.get()
    estado = controladorIndex.ValidarReales(numReales)
    if estado:
        messagebox.showinfo(message="La cadena es valida", title="Numeros Reales")
    else:
        messagebox.showerror(message="La cadena en invalida", title="Numeros Reales")

def expRegNotacion():
    numNotaciones = txt3.get()
    estado = controladorIndex.ValidarNotacionCientifica(numNotaciones)
    if estado:
        messagebox.showinfo(message="La cadena es valida", title="Notación cientifica")
    else:
        messagebox.showerror(message="La cadena en invalida", title="Notación cientifica")

def expRegEmail():
    cadEmail = txt4.get()
    estado = controladorIndex.ValidarEmail(cadEmail)
    if estado:
        messagebox.showinfo(message="El correo es valido", title="Email")
    else:
        messagebox.showerror(message="El correo es invalido", title="Email")

lbl1 = Label(ventana, text="Numero entero:", font= ('Helvetica 13'), background="#0184ce", fg="white")
lbl1.place(x=10, y=10, width=150, height=30)
txt1 = Entry(ventana, text="")
txt1.place(x=153, y=10, width=100, height=30)
btn1 = Button(ventana, text="Validar", command=expRegEnterosAFD)
btn1.place(x=255, y=10, width=80, height=30)

lbl2 = Label(ventana, text="Numero Real:", font= ('Helvetica 13'), background="#0184ce", fg="white")
lbl2.place(x=10, y=50, width=150, height=30)
txt2 = Entry(ventana, text="")
txt2.place(x=153, y=50, width=100, height=30)
btn2 = Button(ventana, text="Validar", command=expRegRealesAFD)
btn2.place(x=255, y=50, width=80, height=30)

lbl3 = Label(ventana, text="Notación:", font= ('Helvetica 13'), background="#0184ce", fg="white")
lbl3.place(x=10, y=90, width=150, height=30)
txt3 = Entry(ventana, text="")
txt3.place(x=153, y=90, width=100, height=30)
btn3 = Button(ventana, text="Validar", command=expRegNotacion)
btn3.place(x=255, y=90, width=80, height=30)

lbl4 = Label(ventana, text="Email:", font= ('Helvetica 13'), background="#0184ce", fg="white")
lbl4.place(x=10, y=130, width=150, height=30)
txt4 = Entry(ventana, text="")
txt4.place(x=153, y=130, width=100, height=30)
btn4 = Button(ventana, text="Validar", command=expRegEmail)
btn4.place(x=255, y=130, width=80, height=30)
ventana.mainloop()

