import pymongo
DATABASE_NAME = "biblioteca_virtual"
USERIOS_COLLECTION = "usuarios"
LIBROS_COLLECTION = "libros"
CATEGORIAS_COLLECTION = "categorias"
PRESTAMOS_COLLECTION = "prestamos"

class MongoDataBase:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[DATABASE_NAME]
        db_list = self.client.list_database_names()
        if DATABASE_NAME in db_list:
            print("The database exists.")
        else :
            print("The database does not exists.")

    def insert(self, collection, document):
        _collection = self.db[collection]
        x = _collection.insert_one(document)    

    def update(self, collection, document):
        print("TODO")

    def delete(self, collection, document):
        print("TODO")

    def get_all(self, collection):
        _collection = self.db[collection]
        return _collection.find({})
    
    def get_by_id(self, collection, id):
        print("TODO")

if __name__ == "__main__":
    db = MongoDataBase()
    db.insert("usuario", { "name": "John", "address": "Highway 37" })