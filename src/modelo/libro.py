from .estado_libro import EstadoLibro

class Libro:
    def __init__(self, titulo, autor, categoria, resena, es_digital=False):
        self.titulo = titulo
        self.autor = autor	            
        self.categoria = categoria	
        self.resena = resena
        self.cantidad = 0
        self.es_digital = es_digital
        if (es_digital):
            self.status = EstadoLibro.DIGITAL
        else:
            self.status = EstadoLibro.EN_STOCK
            self.cantidad = 1

    def agregar(self):
        self.cantidad = self.cantidad + 1
        self.status = EstadoLibro.EN_STOCK

    def agregar_digital(self):
        self.es_digital = True

    def prestar(self):
        self.cantidad = self.cantidad - 1
        if self.cantidad == 0:
            self.status = EstadoLibro.AGOTADO
    
    def devolver(self):
        self.cantidad = self.cantidad + 1
        self.status = EstadoLibro.EN_STOCK

    def hay_stock(self):
        return self.cantidad > 0

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

    			   