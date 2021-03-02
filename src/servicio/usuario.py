from ..repositorio.mongoDB import USERIOS_COLLECTION, dni_search

class ServicioUsuario:
    def __init__(self, db):
        self.db = db
    
    def crear(self, usuario):
        self.db.insert(USERIOS_COLLECTION, usuario.to_map())

    def delete(self, usuario):
        self.db.delete(USERIOS_COLLECTION, usuario.to_map())

    def get_all(self):
        self.db.get_all(USERIOS_COLLECTION)
    
    def get_by_dni(self, dni):
        self.db.get_by_id(USERIOS_COLLECTION, dni_search(dni))