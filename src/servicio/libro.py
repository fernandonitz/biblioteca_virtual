from ..repositorio.mongoDB import LIBROS_COLLECTION

class ServicioLibro:
    def __init__(self, db):
        self.db = db

    def crear(self, libro):
        self.db.insert(LIBROS_COLLECTION, libro.to_map())

    def delete(self, libro):
        self.db.delete(LIBROS_COLLECTION, libro.to_map())

    def get_all(self):
        self.db.get_all(LIBROS_COLLECTION)
    
    def get_by_id(self, libro):
        self.db.get_by_id(LIBROS_COLLECTION, libro.get_id())

    def update(self, libro):
        self.db.update(LIBROS_COLLECTION, libro.to_map())