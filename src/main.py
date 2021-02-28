from tkinter import *
from .modelo.libro import Libro

def agregarLibro():
    libro = Libro("Juan Pablo II, mi querido predecesor","Joseph Ratzinger","Santos","Un libro para conocer la intimidad de Juan Pablo II desde la optica de su amigo y sucesor Benedicto XVI")

window = Tk()

window.title("Welcome to LikeGeeks app")
lbl = Label(window, text="Hello")

lbl.grid(column=3, row=0)

lbl2 = Label(window, text="Otro")

lbl2.grid(column=2, row=2)

sexo = IntVar()
R1 = Radiobutton(window, text="Masculino", variable=sexo, value=0)
R1.grid(column=2, row=3)

R2 = Radiobutton(window, text="Femenino", variable=sexo, value=1)
R2.grid(column=3, row=3)

B = Button(window, text ="agregar Libro", command = agregarLibro)
B.grid(column=0, row=4)
window.mainloop()