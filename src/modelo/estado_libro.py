from enum import Enum  

class EstadoLibro(Enum):
    EN_STOCK = 1
    AGOTADO = 2
    DIGITAL = 3

if __name__ == "__main__":
    print(EstadoLibro.EN_STOCK.value)