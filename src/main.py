from tkinter import *
from .modelo.libro import Libro

class Main: 
    def __init__(self):
        self.window = Tk()
        self.createMainPage();
        self.window.mainloop()
        
    def initWindow(self):
        self.window.geometry("400x200")
        self.window.title("Welcome to LikeGeeks app")
    
    def createMainPage(self):
        self.initWindow()
        lbl = Label(self.window, text="Titulo")
        lbl.grid(column=1, row=0)
        B = Button(self.window, text ="Ver Libros", command = self.verLibros)
        B.grid(column=1, row=1)     
        B = Button(self.window, text ="Prestamos", command = self.prestamos)
        B.grid(column=1, row=2)     
        B = Button(self.window, text ="Retirar Libro", command = self.retirar)
        B.grid(column=1, row=3)     
        lbl = Label(self.window, text="Buscar libro o Usuario: ")
        lbl.grid(column=0, row=4)
        entry = Entry(self.window,width=30)
        entry.grid(column=1, row=4)
        B = Button(self.window, text ="Buscar", command = self.buscar)
        B.grid(column=2, row=4)         
    def verLibros(self):
        print("TODO")
    def prestamos(self):
        print("TODO")
    def retirar(self):
        print("TODO")
    def buscar(self):
        print("TODO")
main = Main()
#lbl = Label(window, text="Hello")
#lbl.grid(column=3, row=0)
#lbl2 = Label(window, text="Otro")
#lbl2.grid(column=2, row=2)
#sexo = IntVar()
#R1 = Radiobutton(window, text="Masculino", variable=sexo, value=0)
#R1.grid(column=2, row=3)
#R2 = Radiobutton(window, text="Femenino", variable=sexo, value=1)
#R2.grid(column=3, row=3)
#B = Button(window, text ="agregar Libro", command = agregarLibro)
#B.grid(column=0, row=4)
