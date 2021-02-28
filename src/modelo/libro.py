from .estado_libro import EstadoLibro

class Libro:
    def __init__(self, titulo, autor, categoria, resena):
        self.titulo = titulo
        self.autor = autor	            
        self.categoria = categoria	
        self.resena = resena
        self.status = EstadoLibro.EN_STOCK

    def prestar(self):
        self.status = EstadoLibro.ENTREGADO
    
    def devolver(self):
        self.status = EstadoLibro.EN_STOCK

    def get_status(self):
        return self.status

    def to_map(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "resena": self.resena,
            "status": self.status.value,
        }

if __name__ == "__main__":
    libro = Libro("Juan Pablo II, mi querido predecesor","Joseph Ratzinger","Santos","Un libro para conocer la intimidad de Juan Pablo II desde la optica de su amigo y sucesor Benedicto XVI")
    print(libro.get_status())
    libro.prestar(None)
    print(libro.get_status())
    print("hola")    

    			   