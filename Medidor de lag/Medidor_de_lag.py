from tkinter import * 
import tkinter.font as tkFont
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
medida = "360x280"
ventana.geometry(medida)
#ventana.resizable(False, False)

ventana.overrideredirect(True)

color = "gray10"

color_fuente = "gray99"

Myframe = Frame(ventana,bg=color)

Myframe.pack(fill="both",expand=True)

def move(event):
    ventana.geometry('+{0}+{1}'.format(event.x_root,event.y_root))

def executeSomething(link):
        resultado=ping(link, unit='ms')
        print(resultado)

        if resultado == None:
            text = resultado
        else :
            text= str(int(resultado)) +"ms."

        return text

def ejecutaScript():
    for i in range(120):
        label.configure(text=executeSomething("www.google.com"))
        
        label2.configure(text=executeSomething("4.2.2.2"))  
        
        label3.configure(text=executeSomething("162.159.138.23")) 
        time.sleep(1)
    button2.configure(state=ACTIVE)

def changeText():
        label.configure(text=executeSomething("www.google.com"))
        label2.configure(text=executeSomething("4.2.2.2"))  
        label3.configure(text=executeSomething("162.159.138.23")) 

def Mostrar():
        button.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        label0.configure(text="Modo: Automatico")

        hilo = threading.Thread(target=ejecutaScript)
        hilo.start()  

        #ejecutaScript()

        button1.grid_forget()
        button2.grid(row=5,column=1)

def MostrarReves():
        button.configure(state=ACTIVE)
        label0.configure(text="Modo: Manual")
        button2.grid_forget()
        button1.grid(row=5,column=1)

fontStyle = tkFont.Font(family="Lucida Grande", size=20)

title = Label(Myframe,text="Medidor de Lag",bg=color,fg="lime", font=fontStyle)
title.grid(row=0, column=0,columnspan=2)
Myframe.bind("<B1-Motion>",move)

close_button = Button(Myframe,text="   x   ",command=ventana.destroy,bg=color, fg=color_fuente)
close_button.grid(row=0, column=2)

label0 = Label(Myframe, text="Modo: Manual",bg=color, font=fontStyle, fg=color_fuente)
label0.grid(padx=5,row=1, column=0,columnspan=2)

photo = PhotoImage(file =resolver_ruta('Google.png'))
canvas = Label(Myframe,image=photo,bg=color)
canvas.grid(row=2, column=0)

label = Label(Myframe, text=executeSomething("www.google.com"),bg=color, font=fontStyle, fg=color_fuente)
label.grid(row=2, column=1)

photo2 = PhotoImage(file =resolver_ruta('lol.png'))
canvas2 = Label(Myframe,image=photo2,bg=color)
canvas2.grid(row=3, column=0)

label2 = Label(Myframe, text=executeSomething("4.2.2.2"),bg=color, font=fontStyle, fg=color_fuente)
label2.grid(row=3, column=1)

photo3 = PhotoImage(file =resolver_ruta('Discord.png'))
canvas3 = Label(Myframe,image=photo3,bg=color)
canvas3.grid(row=4, column=0)

label3 = Label(Myframe, text=executeSomething("162.159.138.23"),bg=color, font=fontStyle, fg=color_fuente)
label3.grid(row=4, column=1)

button = Button(Myframe, text="Actualizar",width=17,command=changeText,bg=color, fg=color_fuente)
button.grid(padx=10,row=5,column=0)

button1 = Button(Myframe, text="Cambiar Modo: Automatico",command=Mostrar,bg=color, fg=color_fuente)
button1.grid(row=5,column=1)

button2 = Button(Myframe, text="Cambiar Modo: Manual",command=MostrarReves,bg=color, fg=color_fuente)
button2.grid(row=5,column=1)

button2.grid_forget()
       

ventana.mainloop()
