from tkinter import *

ventana = Tk()
ventana.geometry("300x300")
ventana.title(" Ejercicios ................... ")
  
  
def borraTexto():
    entrada1.delete(1.0,END)
    entrada2.delete(1.0,END)

def SabeMultiplicar():
          entrada = int(entrada1.get("1.0", "end"))  
          if(entrada == 60):
            salida.insert(END, f'Respuesta Correcta  {entrada} ')
          else:
            salida.insert(END, "Respuesta incorecta")

def Multplicacion():
          num1 = int(entrada1.get("1.0", "end"))  
          num2 = int(entrada2.get("1.0", "end"))
          salida.insert(END, f' {num1} * {num2} = {num1*num2} ')





l = Label(text = " cuanto es 5 * 12")

entrada1 = Text(ventana, height = 2,
                width = 10,
                bg = "light yellow")
entrada2 = Text(ventana, height = 2,
                width = 10,
                bg = "light yellow")  

salida = Text(ventana, height = 2, 
              width = 30, 
              bg = "light blue")
  
boton1 = Button(ventana, height = 2, width = 20, 
                 text ="Evaluar ",
                 command = lambda:SabeMultiplicar())


boton2 = Button(ventana, height = 2, width = 20, 
                 text ="Multiplicacion ",
                 command = lambda:Multplicacion())



boton3 = Button(ventana, text='Borrar Texto de salida ', command=lambda: salida.delete(1.0,END))                
#boton4 = Button(ventana, text='Borrar Texto de entrada ', command=lambda: entrada1.delete(1.0,END))     
boton4 = Button(ventana, text='Borrar Texto de entrada ', command=lambda: borraTexto())     


boton5 = Button(ventana, height = 2, width = 20,
                text = "Salir", 
                command = ventana.destroy) 


l.pack()
entrada1.pack()
entrada2.pack()
salida.pack()
boton1.pack()
boton2.pack()
boton3.pack()
boton4.pack()
boton5.pack()

mainloop()
