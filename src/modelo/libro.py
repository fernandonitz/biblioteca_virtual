from .estado_libro import EstadoLibro
from ..servicio.retiro import Retiro

class Libro:
    def __init__(self, titulo, autor, categoria, resena):
        self.titulo = titulo
        self.autor = autor	            
        self.categoria = categoria	
        self.resena = resena
        self.status = EstadoLibro.EN_STOCK
        self.retiro = Retiro()
        print("nuevo libro")

    def __hola(self):
        print("hola")

    def prestar(self):
        self.status = EstadoLibro.ENTREGADO
    
    def get_status(self):
        return self.status

if __name__ == "__main__":
    libro = Libro("Juan Pablo II, mi querido predecesor","Joseph Ratzinger","Santos","Un libro para conocer la intimidad de Juan Pablo II desde la optica de su amigo y sucesor Benedicto XVI")
    print(libro.get_status())
    libro.prestar(None)
    print(libro.get_status())
    print("hola")    

    			   