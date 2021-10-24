from tkinter import * 
from ping3 import ping , verbose_ping
import sched, time, threading
from PIL import Image,ImageTk
import os, sys

def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)

ventana = Tk()
ventana.title("Medidor de lag")
medida = "320x220"
ventana.geometry(medida)
#ventana.resizable(False, False)

Myframe = Frame(ventana)

Myframe.pack(fill="both",expand=True)

def executeSomething(Servidor,link):
        return str(round(ping(link, unit='ms'),2)) +"ms."

def ejecutaScript():
    for i in range(100):
        label.configure(text=executeSomething("Google","www.google.com"))
        label2.configure(text=executeSomething("Lol","4.2.2.2"))  
        label3.configure(text=executeSomething("Discord","162.159.138.23")) 
        time.sleep(1)
    button2.configure(state=ACTIVE)

def changeText():
        label.configure(text=executeSomething("Google","www.google.com"))
        label2.configure(text=executeSomething("Lol","4.2.2.2"))  
        label3.configure(text=executeSomething("Discord","162.159.138.23")) 

def Mostrar():
        button.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        label0.configure(text="Modo: Automatico")
        hilo = threading.Thread(target=ejecutaScript)
        hilo.start()  

        #ejecutaScript()

        button1.grid_forget()
        button2.grid(row=4,column=1)

def MostrarReves():
        button.configure(state=ACTIVE)
        label0.configure(text="Modo: Manual")
        button2.grid_forget()
        button1.grid(row=4,column=1)

label0 = Label(Myframe, text="Modo: Manual")
label0.grid(padx=5,row=0, column=0,columnspan=2)

photo = PhotoImage(file =resolver_ruta('Google.png'))
canvas = Label(Myframe,image=photo)
canvas.grid(row=1, column=0)

label = Label(Myframe, text=executeSomething("Google","www.google.com"))
label.grid(row=1, column=1)

photo2 = PhotoImage(file =resolver_ruta('lol.png'))
canvas2 = Label(Myframe,image=photo2)
canvas2.grid(row=2, column=0)

label2 = Label(Myframe, text=executeSomething("Lol","4.2.2.2"))
label2.grid(row=2, column=1)

photo3 = PhotoImage(file =resolver_ruta('Discord.png'))
canvas3 = Label(Myframe,image=photo3)
canvas3.grid(row=3, column=0)

label3 = Label(Myframe, text=executeSomething("Discord","162.159.138.23"))
label3.grid(row=3, column=1)

button = Button(Myframe, text="Actualizar",width=17,command=changeText)
button.grid(padx=10,row=4,column=0)

button1 = Button(Myframe, text="Cambiar Modo: Automatico",command=Mostrar)
button1.grid(row=4,column=1)

button2 = Button(Myframe, text="Cambiar Modo: Manual",command=MostrarReves)
button2.grid(row=4,column=1)

button2.grid_forget()
       

ventana.mainloop()
