from datetime import date

class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.entregado = date.today()
        self.devuelto = None

    def devolver_libro(self):
        self.entregado = date.today()

    def to_map(self):
        return {
            "usuario": self.usuario,
            "libro": self.libro,
            "entregado": self.entregado,
            "devuelto": self.devuelto
        }