from DB.crud import BaseRepository

class Servicio:
    def __init__(self, id: int, nombre_servicio: str, descripcion_servicio: str, tipo_cobro_id: int):
        self.id = id
        self.nombre_servicio = nombre_servicio
        self.descripcion_servicio = descripcion_servicio
        self.tipo_cobro_id = tipo_cobro_id

    def create(self):
        BaseRepository.create("servicio", {
            "nombre_servicio": self.nombre_servicio,
            "descripcion_servicio": self.descripcion_servicio,
            "tipo_cobro_id": self.tipo_cobro_id
        })

    def update_values(self):
        BaseRepository.update("servicio", {
            "nombre_servicio": self.nombre_servicio,
            "descripcion_servicio": self.descripcion_servicio,
            "tipo_cobro_id": self.tipo_cobro_id
        }, {
            "id": self.id
        })

    @staticmethod
    def get_all() -> list["Servicio"]:
        resultados = BaseRepository.read_all("servicio")

        return [
            Servicio(
                id=row[0],
                nombre_servicio=row[1],
                descripcion_servicio=row[2],
                tipo_cobro_id=row[3]
            )
            for row in resultados
        ]

# Convierte un SELECT en objeto Servicio
def create_servicio_object(query: tuple) -> Servicio:
    return Servicio(
        id=query[0],
        nombre_servicio=query[1],
        descripcion_servicio=query[2],
        tipo_cobro_id=query[3]
    )
