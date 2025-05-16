from db import get_connection
from modelo import Estado

class EstadoDAO:
    def __init__(self,
                 estados: list[Estado] = []):
        self.estados = estados
        self.conn = get_connection()

    def buscar_por_id(self, id: int) -> Estado | None:
        for estado in self.estados:
            if estado.id == id:
                return estado.nome
            else:
                return None

    def salvar(self, estado: Estado):
        self.estados.append(estado)

    def listar_todos(self) -> list[Estado]:
        return self.__str__()
    
    def __str__(self):
        lista_string = []
        for estado in self.estados:
            lista_string.append(estado.nome)
        return lista_string