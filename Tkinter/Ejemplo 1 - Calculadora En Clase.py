#http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

from tkinter import * 
from math import *

ventana = Tk()
ventana.geometry("400x600")
ventana.resizable(False,False)  
ventana.configure(background="azure2") 
ventana.title(" Calculadora  Python 4.0 ")
colorbtn="cyan"
anchbtn=10
altobtn=3

ope=""
textoDisplay=StringVar()

def limPanta():
    global ope
    ope=""
    textoDisplay.set("")

def clickBtn(btn):
    global ope
    ope=ope+str(btn)
    print(ope)
    textoDisplay.set(ope)

def resultado():
    global ope
    try:
        r=str(eval(ope))
    except:
        r = "E  R  R  O  R"
    textoDisplay.set(r)    

#primera fila
btn0=Button(ventana,text="0",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn(0)).grid(row=1,column=0,pady=12)
btn1=Button(ventana,text="1",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn(1)).grid(row=1,column=1,pady=12)
btn2=Button(ventana,text="2",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn(2)).grid(row=1,column=2,pady=12)
btn3=Button(ventana,text="3",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn(3)).grid(row=1,column=3,pady=12)
#segunda fila
btn4=Button(ventana,text="4",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn(4)).grid(row=2,column=0,pady=12)
btn5=Button(ventana,text="5",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn(5)).grid(row=2,column=1,pady=12)
btn6=Button(ventana,text="6",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn(6)).grid(row=2,column=2,pady=12)
btn7=Button(ventana,text="7",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn(7)).grid(row=2,column=3,pady=12)
#tercera fila
btn8=Button(ventana,text="8",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn(8)).grid(row=3,column=0,pady=12)
btn9=Button(ventana,text="9",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn(9)).grid(row=3,column=1,pady=12)
btnpi=Button(ventana,text="π",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn("pi")).grid(row=3,column=2,pady=12)
btnpu=Button(ventana,text=".",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn(".")).grid(row=3,column=3,pady=12)
#cuarta fila
btns=Button(ventana,text="+",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn("+")).grid(row=4,column=0,pady=12)
btnr=Button(ventana,text="-",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn("-")).grid(row=4,column=1,pady=12)
btnm=Button(ventana,text="*",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn("*")).grid(row=4,column=2,pady=12)
btndi=Button(ventana,text="/",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn("/")).grid(row=4,column=3,pady=12)
#
btnrai=Button(ventana,text="√",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn("sqrt")).grid(row=5,column=0,pady=12)
btncle=Button(ventana,text="C",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:limPanta()).grid(row=5,column=1,pady=12)
btnexp=Button(ventana,text="Exp",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn("exp")).grid(row=5,column=2,pady=12)
btnigu=Button(ventana,text="=",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:resultado()).grid(row=5,column=3,pady=12)

btnpai=Button(ventana,text="(",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn("(")).grid(row=6,column=0,pady=12)
btnpad=Button(ventana,text=")",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn(")")).grid(row=6,column=1,pady=12)
btnmod=Button(ventana,text="%",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn("%")).grid(row=6,column=2,pady=12)
btnlog=Button(ventana,text="log",bg=colorbtn,width=anchbtn,height=altobtn,command=lambda:clickBtn("log")).grid(row=6,column=3,pady=12)

Display = Entry(ventana,font=("arial", 20, "bold"),width=24, borderwidth=1,background="light cyan",textvariable=textoDisplay) 
Display.grid(row=0,column=0,columnspan=4,padx=22,pady=10)

ventana.mainloop()

