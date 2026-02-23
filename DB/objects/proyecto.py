from DB.crud import BaseRepository
from typing import Any

class Proyecto:
    def __init__(self, id: int, nombre: str, fecha_inicio: Any, fecha_fin: Any, costo: float,
                 descripcion: str, cliente_id: int, servicio_id: int, proyecto_estado: int,
                 imputable: bool):
        self.id = id
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.costo = costo
        self.descripcion = descripcion
        self.cliente_id = cliente_id
        self.servicio_id = servicio_id
        self.proyecto_estado = proyecto_estado
        self.imputable = imputable

    def create_proyecto(self):
        BaseRepository.create("proyecto", {
            "nombre": self.nombre,
            "fecha_inicio": self.fecha_inicio,
            "fecha_fin": self.fecha_fin,
            "costo": self.costo,
            "descripcion": self.descripcion,
            "cliente_id": self.cliente_id,
            "servicio_id": self.servicio_id,
            "proyecto_estado": self.proyecto_estado,
            "imputable": self.imputable
        })

    def update_values(self):
        BaseRepository.update("proyecto", {
            "nombre": self.nombre,
            "fecha_inicio": self.fecha_inicio,
            "fecha_fin": self.fecha_fin,
            "costo": self.costo,
            "descripcion": self.descripcion,
            "cliente_id": self.cliente_id,
            "servicio_id": self.servicio_id,
            "proyecto_estado": self.proyecto_estado,
            "imputable": self.imputable
        }, {"id": self.id})

    def delete(self):
        BaseRepository.delete("proyecto", {"id": self.id})
        
    @staticmethod
    def get_all() -> list["Proyecto"]:
        resultados = BaseRepository.read_all("proyecto")

        return [
            Proyecto(
                id=row[0],
                nombre=row[1],
                fecha_inicio=row[2],
                fecha_fin=row[3],
                costo=row[4],
                descripcion=row[5],
                cliente_id=row[6],
                servicio_id=row[7],
                proyecto_estado=row[8],
                imputable=row[9]
            )
            for row in resultados
        ]


def create_proyecto_object(query: tuple) -> Proyecto:
    return Proyecto(*query)

def get_all_proyecto() -> list[Proyecto]:
    resultados = BaseRepository.read_all("proyecto")
    return [create_proyecto_object(row) for row in resultados]
