import tkinter as tk
from tkinter import ttk
from ping3 import ping , verbose_ping
import sched, time
import time

starttime=time.time()


class Application(ttk.Frame):
    

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Medidor de lag")
        main_window.geometry("250x80")
        main_window.resizable(False, False)

        self.label = ttk.Label(self, text=executeSomething("Google","www.google.com"),width=40)
        self.label.grid(row=1, column=0)

        self.label2 = ttk.Label(self, text=executeSomething("Lol","4.2.2.2"),width=40)
        self.label2.grid(row=2, column=0)

        self.label3 = ttk.Label(self, text=executeSomething("Discord","162.159.138.23"),width=40)
        self.label3.grid(row=3, column=0)

        self.button = ttk.Button(self, text="Actualizar",width=40,command=self.changeText)
        self.button.grid(row=0, column=0)

        self.pack()

    def changeText(self):
        self.label.configure(text=executeSomething("Google","www.google.com"))  
        self.label2.configure(text=executeSomething("Lol","4.2.2.2"))  
        self.label3.configure(text=executeSomething("Discord","162.159.138.23"))  
        

def executeSomething(Servidor,link):
        return Servidor+": "+str(ping(link, unit='ms')) +"ms."
        

#while True:
#        print ("tick")    
#        time.sleep(10.0 - ((time.time() - starttime) % 10.0))    
        

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()  


