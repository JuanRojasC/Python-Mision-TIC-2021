#http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

from tkinter import * 

colorEntry = "#9999a1"
colorLabel = "#66666e"
colorLabelResult = "#ff6f00"

posX = 270 
posY = 10 
width = 50 
height = 50
colorSum = "#ff6f00"
colorSubstraction = "#ff6f00"

def operacion(x):
    
    num1=float(txt1.get())
    num2=float(txt2.get())

    if x == "+":
        s=num1+num2
    elif x == "-":
        s=num1-num2
    elif x == "*":
        s=num1*num2
    elif x == "/":
        s=num1/num2
    elif x == 'c':
        txt1.delete(0,END)
        txt2.delete(0,END)
        txt3.delete(0,END)
        return
        
    txt3.delete(0,END)
    txt3.insert(0,s)



ventana = Tk()
ventana.geometry("400x300")
ventana.title("ejercicio")


# INPUTS
txt1 = Entry(ventana, bg=colorEntry)
txt1.place(x=120,y=10,width=100,height=30)

txt2 = Entry(ventana, bg=colorEntry)
txt2.place(x=120,y=50,width=100,height=30)

txt3 = Entry(ventana, bg=colorEntry)
txt3.place(x=120,y=90,width=100,height=30)


# BUTTONS
btn1 = Button(ventana, text = " Sumar", bg=colorSum,command= lambda: operacion("+"))
btn1.place(x=270,y=10,width=width,height=height)

btn2 = Button(ventana, text = " Restar", bg=colorSum,command= lambda: operacion("-"))
btn2.place(x=posX + width + 5,y=10,width=width,height=height)

btn3 = Button(ventana, text = " Multiplicar", bg=colorSum,command= lambda: operacion("*"))
btn3.place(x=posX,y=10 + height + 5,width=width,height=height)

btn4 = Button(ventana, text = " Dividir", bg=colorSum,command= lambda: operacion("/"))
btn4.place(x=posX + width + 5,y=10 + height + 5,width=width,height=height)

btn5 = Button(ventana, text = " Clean", bg=colorSum,command= lambda: operacion("c"))
btn5.place(x=posX + width + 5,y=10 + height*2 + 5,width=width,height=height)


# LABELS
lab1 = Label(ventana, text = " Primer Numero ",bg=colorLabel)
lab1.place(x=10,y=10,width=100,height=30)

lab2 = Label(ventana, text = " Segundo Numero ",bg=colorLabel)
lab2.place(x=10,y=50,width=100,height=30)

lab3 = Label(ventana, text = " Resultado",bg=colorLabelResult)
lab3.place(x=10,y=90,width=100,height=30)


ventana.mainloop()
