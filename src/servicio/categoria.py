from ..repositorio.mongoDB import CATEGORIAS_COLLECTION

class ServicioCategoria:
    def __init__(self, db):
        self.db = db

    def crear(self, categoria):
        self.db.insert(CATEGORIAS_COLLECTION, categoria.to_map())

    def delete(self, categoria):
        self.db.delete(CATEGORIAS_COLLECTION, categoria.to_map())

    def get_all(self):
        self.db.get_all(CATEGORIAS_COLLECTION)