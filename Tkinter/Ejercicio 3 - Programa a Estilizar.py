from tkinter import*
from math import exp
import random


ventana = Tk()
ventana.geometry("400x400")
ventana.title("Ejercicios")
  
# VARIABLES
operationData = []
signsList = ['+','-','*','/','Exp','sqrt']
buttonTestColor = "#034748"
buttonCalculatorColor = "#0caadc"
fontMainColor = "#ffffff"
buttonBackColor = "white"
fontButtonBackColor = "black"
labelOperation = "#11b5e4"

# FUNCTIONS
def mathOperation(data):
  number1 = data[1]
  number2 = data[2]
  sign = data[0]
  if sign == signsList[0]:
    return round(number1 + number2,1)
  elif sign == signsList[1]:
    return round(number1 - number2,1)
  elif sign == signsList[2]:
    return round(number1 * number2,1)
  elif sign == signsList[3]:
    return round(number1 / number2,1)
  elif sign == signsList[4]:
    return round(number1 ** number2,1)
  elif sign == signsList[5]:
    return round(number1 ** 0.5,1)            

# CHALLENGES PAGE
def test():

  # CLEAN ALL CONTENT AND COME BACK MAIN MENU
  def cleanData():
    operationScreen.destroy()
    entryResult.destroy()
    buttonNew.destroy()
    buttonVerify.destroy()
    messageOut.destroy()
    outputResult.destroy()
    buttonBack.destroy()
    mainMenu()

  # CLEAN THE RESULT OUTPUT AND THE MESSAGE OUTPUT
  def cleanOuput():
    messageOut.config(text="")
    outputResult.config(text="",bg="#1481ba")

  # COMPARE RESULT-USERINPUT AND SHOW RESULT AND MESSAGE
  def verify(event=None):
    global operationData
    entry = float(entryResult.get())
    result = mathOperation(operationData)
    if entry == result:
      messageOut.config(text='Muy bien Has Acertado 😀',fg='darkgreen')
    else:
      messageOut.config(text='La proxima lo lograras 😉', fg='darkred')
    outputResult.config(text=f'Resultado: {result}', bg="white")

  # SHOW A NEW OPERATION STRING
  def newOperation():
    global operationData
    operation()
    operationString = operationData[3]
    operationScreen.config(text=operationString)
    entryResult.delete(0,END)

  # GENERATE A NEW OPERATION 
  def operation():
    global operationData
    numbers = [random.randint(0,10),random.randint(1,10)]
    number1 = numbers[0]
    number2 = numbers[1]
    sign = signsList[random.randint(0,len(signsList)-1)]
    if sign == signsList[5]:
      operationString = 'sqrt(' + str(number1) + ')'
    else:
      operationString = str(number1) + ' '+ sign + ' ' + str(number2)
    operationData = [sign, number1, number2, operationString]

  # GENERATE A NEW OPERATION AND CLEAN OUTPUTS
  def new(event=None):
    newOperation()
    cleanOuput()
    
  # BUTTONS AND LABELS
  # LABEL FOR SHOW OPERATION TO GUESS
  operationScreen = Label(ventana,font=("Arial",20), bg=labelOperation, fg="black")
  operationScreen.pack(ipady=5,ipadx=50,pady=(50,40))
  # BUTTON FOR THE USER'S INPUT
  entryResult = Entry(ventana,bg="white",justify='center')
  entryResult.pack(ipadx=80,ipady=10)
  # BUTTON FOR VERIFY THE USER'S INPUT
  buttonVerify = Button(ventana, text='Probar', bg=buttonCalculatorColor, fg=fontMainColor, command=verify)
  buttonVerify.place(x=210,y=200,height=30,width=100)
    # IS BIND WITH ENTER KEY
  ventana.bind('<Return>',verify)
  # BUTTON FOR GENERATE A NEW CHALLENGE
  buttonNew = Button(ventana, text='Nuevo', bg=buttonTestColor, fg=fontMainColor, command=lambda:[newOperation(),cleanOuput()])
  buttonNew.place(x=90,y=200,height=30,width=100)
    # IS BIND WITH SPACEBAR KEY
  ventana.bind('<space>',new)
  # LABEL FOR TO SHOW THE MESSAGE ABOUT IF THE USER'S INPUT IS RIGTH OR NOT
  messageOut = Label(ventana, font=('Courier',12,'bold'), bg="#1481ba", fg='black')
  messageOut.place(x=80 ,y=255)
  # LABEL FOR TO SHOW THE CORRECT RESULT
  outputResult =Label(ventana, font=('Courier',15,'bold'), bg="#1481ba", fg='black')
  outputResult.place(x=110,y=300)
  # BUTTON FOR TO COME BACK AT MAIN MENU
  buttonBack = Button(ventana, text="«", font=("Courier",20), bg=buttonBackColor, fg=fontButtonBackColor, command=cleanData)
  buttonBack.pack(ipady=0,side=BOTTOM, fill=X)

  # CALLL AT FIRST OPERATION
  newOperation()


# CALCULATOR PAGE
def calculator():
  entryScreen = Label(ventana, bg='#FFF8F0', fg='black', widt= 30, font=('Arial',15), text='Prueba 2+2')
  entryScreen.pack(pady=(20,5),ipadx=5,ipady=8)
  result = Label(ventana, bg='red', text='Result')
  result.place(x=50,y=50)

# MAIN MENU
def mainMenu():
  def option(x):
    buttonTest.destroy()
    buttonCalculator.destroy()
    if x == 1:
      test()
    else:
      calculator()
      ventana.configure(background="#b3aaa2")
  ventana.configure(background="#1481ba",)
  buttonTest =Button(ventana, text="Prueba Tus Habilidades", bg=buttonTestColor, fg=fontMainColor, command=lambda:option(1))
  buttonTest.pack(ipadx=8,ipady=8,pady=(150,20))
  buttonCalculator = Button(ventana, text="Calculadora", bg=buttonCalculatorColor, fg=fontMainColor, command=lambda:option(2))
  buttonCalculator.pack(ipadx=8,ipady=8)

mainMenu()



ventana.mainloop()


# def borraTexto():
#     entrada1.delete(1.0,END)
#     entrada2.delete(1.0,END)

# def SabeMultiplicar():
#           entrada = int(entrada1.get("1.0", "end"))  
#           if(entrada == 60):
#             salida.insert(END, f'Respuesta Correcta  {entrada} ')
#           else:
#             salida.insert(END, "Respuesta incorecta")

# def Multplicacion():
#           num1 = int(entrada1.get("1.0", "end"))  
#           num2 = int(entrada2.get("1.0", "end"))
#           salida.insert(END, f' {num1} * {num2} = {num1*num2} ')





# l = Label(text = " cuanto es 5 * 12")

# entrada1 = Text(ventana, height = 2,
#                 width = 10,
#                 bg = "light yellow")
# entrada2 = Text(ventana, height = 2,
#                 width = 10,
#                 bg = "light yellow")  

# salida = Text(ventana, height = 2, 
#               width = 30, 
#               bg = "light blue")
  
# boton1 = Button(ventana, height = 2, width = 20, 
#                  text ="Evaluar ",
#                  command = lambda:SabeMultiplicar())


# boton2 = Button(ventana, height = 2, width = 20, 
#                  text ="Multiplicacion ",
#                  command = lambda:Multplicacion())



# boton3 = Button(ventana, text='Borrar Texto de salida ', command=lambda: salida.delete(1.0,END))                
# #boton4 = Button(ventana, text='Borrar Texto de entrada ', command=lambda: entrada1.delete(1.0,END))     
# boton4 = Button(ventana, text='Borrar Texto de entrada ', command=lambda: borraTexto())     


# boton5 = Button(ventana, height = 2, width = 20,
#                 text = "Salir", 
#                 command = ventana.destroy) 


# l.pack()
# entrada1.pack()
# entrada2.pack()
# salida.pack()
# boton1.pack()
# boton2.pack()
# boton3.pack()
# boton4.pack()
# boton5.pack()

# mainloop()
