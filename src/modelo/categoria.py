class Categoria:
    def __init__(self, name):
        self.name = name
    
    def to_map(self):
        return {
            "name": self.name
        }  