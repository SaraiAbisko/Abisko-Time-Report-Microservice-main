from DB.crud import BaseRepository
from typing import Any

class Estados:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

    def create_estados(self):
        BaseRepository.create("estados", {
            "nombre": self.nombre
        })

    def update_values(self):
        BaseRepository.update("estados", {
            "nombre": self.nombre
        }, {"id": self.id})

    def delete(self):
        BaseRepository.delete("estados", {"id": self.id})
        
    @staticmethod
    def get_all() -> list["Estados"]:
        resultados = BaseRepository.read_all("estados")

        return [
            Estados(
                id=row[0],
                nombre=row[1]
            )
            for row in resultados
        ]


def create_estados_object(query: tuple) -> Estados:
    return Estados(*query)

def get_all_estados() -> list[Estados]:
    resultados = BaseRepository.read_all("estados")
    return [create_estados_object(row) for row in resultados]
