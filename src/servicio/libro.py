from ..repositorio.mongoDB import LIBROS_COLLECTION
from ..modelo.libro import Libro
from ..repositorio.mongoDB import MongoDataBase

class ServicioLibro:
    def __init__(self, db):
        self.db = db

    def crear(self, libro):
        self.db.insert(LIBROS_COLLECTION, libro.to_map())

    def delete(self, libro):
        self.db.delete(LIBROS_COLLECTION, libro.to_map())

    def get_all(self):
        return self.db.get_all(LIBROS_COLLECTION)
    
    def get_by_id(self, libro):
        self.db.get_by_id(LIBROS_COLLECTION, libro.get_id())

    def update(self, libro):
        self.db.update(LIBROS_COLLECTION, libro.to_map())

if __name__ == "__main__":
    libro1 = Libro("Juan Pablo II, mi querido predecesor","Joseph Ratzinger","Santos","Un libro para conocer la intimidad de Juan Pablo II desde la optica de su amigo y sucesor Benedicto XVI")
    libro2 = Libro("Práctica de amor a Jesucristo", "San Alfonso María de Ligorio","Espiritualidad","Es una meditación del himno a la caridad que escribiera San Pablo y que se ocupa de centrar al cristianismo en lo más importante, lo que no pasará nunca: el amor.")
    
    servicio = ServicioLibro(MongoDataBase())
    servicio.crear(libro1)
    servicio.crear(libro2)