from tkinter import *

# Crea la Ventana
ventana = Tk()

# Define las dimensiones Iniciales de la venta
ventana.geometry("300x300")

# Especifica si puede redimensionarse
ventana.resizable(False, False)

# Asgina el titulo de la ventana
ventana.title("Mi Primera Ventana en Python")

# Crea un Boton
boton = Button(ventana,bg='red',width=5,height=1,text="SALIR",command=ventana.destroy)
boton.pack()

# Crea una Etiqueta
label = Label(ventana, text="Primer Numero", bg="blue")
label.place(x=10,y=10,width=100,height=30)

# Crea una Entrada de texto
texto = Entry(ventana, bg="green")
texto.place(x=120,y=10,width=100,height=30)

# Ejecuta el codigo
ventana.mainloop()

# def suma():
#       num1=txt1.get()
#       num2=txt2.get()
#       s=float(num1)+float(num2)
#       txt3.delete(0,END)
#       txt3.insert(0,s)
