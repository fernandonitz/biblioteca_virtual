from enum import Enum  

class EstadoLibro(Enum):
    EN_STOCK = 1
    ENTREGADO = 2

if __name__ == "__main__":
    print(EstadoLibro.EN_STOCK.value)