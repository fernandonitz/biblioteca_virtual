import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile 
from .modelo.libro import Libro
from .servicio.libro import ServicioLibro
from .repositorio.googleDrive import GoogleDriveRepo
from .repositorio.mongoDB import MongoDataBase
import json

class Main: 
    def __init__(self):

        self.window = tk.Tk()
        
        self.googleDrive = GoogleDriveRepo()
        self.mongo = MongoDataBase()
        self.servicioLibro = ServicioLibro(self.mongo)

        self.tabControl = ttk.Notebook(self.window) 
  
        self.tab1 = ttk.Frame(self.tabControl) 
        self.tab2 = ttk.Frame(self.tabControl) 
        self.tab3 = ttk.Frame(self.tabControl) 
        self.tab4 = ttk.Frame(self.tabControl) 
        
        self.tabControl.add(self.tab1, text ='Home') 
        self.tabControl.add(self.tab2, text ='Ver Libros') 
        self.tabControl.add(self.tab3, text ='Prestamos') 
        self.tabControl.add(self.tab4, text ='Retirar Libro') 
        self.tabControl.pack(expand = 1, fill ="both") 
        
        self.verLibros()
        self.prestamos()
        self.retirarLibro()
        self.home()

        self.window.mainloop()
         
    def home(self):
        ttk.Label(self.tab1, text ="Welcome to GeeksForGeeks").grid(column = 0, row = 0, padx = 30, pady = 30)  

    def verLibros(self):
        libros = self.servicioLibro.get_all()
        atributos = ["titulo","autor","categoria","resena"]
        titulos = ["Titulo","Autor","Categoria","Reseña"]
        size = [20,20,20,40]
        j = 0
        for titulo in titulos:
            cell = ttk.Label(self.tab2, width=size[j], text=titulo)
            cell.grid(row=1, column=j)
            j = j + 1 
        i = 2
        for libro in libros:
            j = 0
            for attribute, value in libro.items():
                if attribute in atributos:
                    cell = ttk.Label(self.tab2, width=size[j], text=value)
                    cell.grid(row=i, column=j)
                    j = j + 1
            i = i + 1
        btn = ttk.Button(self.tab2, text ='Open', command = lambda:self.open_file()) 
        btn.grid(row=0, column=0) 
        #ttk.Label(self.tab2, text ="Lets dive into the world of computers").grid(column = 0, row = 0, padx = 30, pady = 30) 

    def open_file(self): 
        file_name = askopenfile(filetypes =[('Python Files', '*')]) 
        self.googleDrive.uploadFile(file_name)
  

    def prestamos(self):
        ttk.Label(self.tab3, text ="Lets dive into the world of computers").grid(column = 0, row = 0, padx = 30, pady = 30) 

    def retirarLibro(self):
        ttk.Label(self.tab4, text ="Lets dive into the world of computers").grid(column = 0, row = 0, padx = 30, pady = 30) 

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
