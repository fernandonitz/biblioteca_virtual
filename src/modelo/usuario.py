def dni_search(dni):
    return {"dni": dni}

class Usuario:
    def __init__(self, nombre, apellido, dni, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
        self.telefono = telefono

    def to_map(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "dni": self.dni,
            "email": self.email,
            "telefono": self.telefono
        }