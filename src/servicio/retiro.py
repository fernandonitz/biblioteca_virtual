from ..repositorio.mongoDB import PRESTAMOS_COLLECTION
from ..modelo.prestamo import Prestamo

class Retiro:
    def __init__(self, db, libro_service):
        self.db = db
        self.libro_service = libro_service

    def retirar_libro(self, usuario, libro):
        libro.prestar()
        prestamo = Prestamo(usuario, libro)
        self.libro_service.update(libro)
        self.update(prestamo)
    
    def devolver_libro(self, usuario, libro):
        libro.devolver()
        prestamo = prestamo.get(usuario,libro)
        self.libro_service.update(libro)
        self.update(prestamo)
    
    def update(self, prestamo):
        self.db.update(PRESTAMOS_COLLECTION, prestamo)

    def insert(self, prestamo):
        self.db.insert(PRESTAMOS_COLLECTION, prestamo)

    def delete(self, prestamo):
        self.db.delete(PRESTAMOS_COLLECTION, prestamo)
    
    def get_all(self):
        self.db.get_all(PRESTAMOS_COLLECTION)

    def get_by_prestamo(self, usuario, libro):
        self.db.get_by_id(PRESTAMOS_COLLECTION, {"usuario":usuario,"libro":libro})