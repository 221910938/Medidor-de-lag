from tkinter import * 
import tkinter.font as tkFont
from ping3 import ping
import time, threading
import os, sys
import json
from datetime import datetime

def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)

ventana = Tk()
ventana.title("Medidor de lag")
medida = "320x530"
ventana.geometry(medida)
ventana.resizable(False, False)
ventana.wm_attributes("-topmost", 1)

color = "gray10"
color_fuente = "gray99"

Myframe = Frame(ventana,bg=color)
Myframe.pack(fill="both",expand=True)

fileName = "./Resources/Data.json"

def TransformToJson(Aplicacion,Ping):
    now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    jsonObject = {
        "Fecha": now,
        "Aplicacion": Aplicacion,
        "Ping": Ping
    }

    newjson = jsonObject

    print(newjson)

    file = open(fileName, "w")
    json.dump(jsonObject, file)
    file.close()

def executeSomething(link):

        resultado=ping(link, unit='ms')

        if resultado == None:
            entrega = resultado
        
        try:
            text= round(resultado) 
        except:
            text=0

        entrega = str(text)+" ms."



        if link == "www.google.com":
            TransformToJson("Google",text)

        if link == "4.2.2.2":
            TransformToJson("Lol",text)

        if link == "162.159.138.23":
            TransformToJson("Discord",text)



        if text <= 60 :
            color_new = "green2"
            return entrega,color_new
        if text >= 80 :
            color_new = "red2"
            return entrega,color_new
        else :
            color_new = "yellow"
            return entrega,color_new

def ejecutaScript():
    for i in range(120):

        new1=executeSomething("www.google.com")
        texto1=new1[0]
        color1=new1[1]

        new2=executeSomething("4.2.2.2")
        texto2=new2[0]
        color2=new2[1]

        new3=executeSomething("162.159.138.23")

        texto3=new3[0]
        color3=new3[1]

        label.configure(text=texto1,fg=color1)
        label2.configure(text=texto2,fg=color2)  
        label3.configure(text=texto3,fg=color3) 

        time.sleep(1)

    button2.configure(state=ACTIVE)

def changeText():
        new1=executeSomething("www.google.com")
        texto1=new1[0]
        color1=new1[1]

        new2=executeSomething("4.2.2.2")
        texto2=new2[0]
        color2=new2[1]

        new3=executeSomething("162.159.138.23")

        texto3=new3[0]
        color3=new3[1]

        label.configure(text=texto1,fg=color1)
        label2.configure(text=texto2,fg=color2)  
        label3.configure(text=texto3,fg=color3) 

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


label0 = Label(Myframe, text="Modo: Manual",bg=color, font=fontStyle, fg=color_fuente)
label0.grid(padx=5,row=1, column=0,columnspan=2)

photo = PhotoImage(file=resolver_ruta('Google.png'))
canvas = Label(Myframe,image=photo,bg=color)
canvas.grid(row=2, column=0)

var = executeSomething("www.google.com")
texto1=var[0]
color1=var[1]

label = Label(Myframe, text=texto1,bg=color, font=fontStyle, fg=color1)
label.grid(row=2, column=1)

photo2 = PhotoImage(file=resolver_ruta('lol.png'))
canvas2 = Label(Myframe,image=photo2,bg=color)
canvas2.grid(row=3, column=0)

var = executeSomething("4.2.2.2")
texto2=var[0]
color2=var[1]

label2 = Label(Myframe, text=texto2,bg=color, font=fontStyle, fg=color2)
label2.grid(row=3, column=1)

photo3 = PhotoImage(file=resolver_ruta('Discord.png'))
canvas3 = Label(Myframe,image=photo3,bg=color)
canvas3.grid(row=4, column=0)

var = executeSomething("162.159.138.23")
texto3=var[0]
color3=var[1]

label3 = Label(Myframe, text=texto3,bg=color, font=fontStyle, fg=color3)
label3.grid(row=4, column=1)

button = Button(Myframe, text="Actualizar",width=17,command=changeText,bg=color, fg=color_fuente)
button.grid(padx=10,row=5,column=0)

button1 = Button(Myframe, text="Cambiar Modo: Automatico",command=Mostrar,bg=color, fg=color_fuente)
button1.grid(row=5,column=1)

button2 = Button(Myframe, text="Cambiar Modo: Manual",command=MostrarReves,bg=color, fg=color_fuente)
button2.grid(row=5,column=1)

button2.grid_forget()

ventana.mainloop()
