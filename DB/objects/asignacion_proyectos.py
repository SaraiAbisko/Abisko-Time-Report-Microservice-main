from DB.crud import BaseRepository

class Asignacion_proyecto:
    def __init__(self, id: int, proyecto_id: int, consultor_id: int, activo: bool):
        self.id = id
        self.proyecto_id = proyecto_id
        self.consultor_id = consultor_id
        self.activo = activo

    def create(self):
        BaseRepository.create("asignacion_proyecto", {
            "proyecto_id": self.proyecto_id,
            "consultor_id": self.consultor_id,
            "activo": self.activo
        })

    def update_values(self):
        BaseRepository.update("asignacion_proyecto", {
            "proyecto_id": self.proyecto_id,
            "consultor_id": self.consultor_id,
            "activo": self.activo
        }, {
            "id": self.id
        })
        
    @staticmethod
    def get_all() -> list["Asignacion_proyecto"]:
        resultados = BaseRepository.read_all("asignacion_proyecto")

        return [
            Asignacion_proyecto(
                id=row[0],
                proyecto_id=row[1],
                consultor_id=row[2],
                activo=row[3]
            )
            for row in resultados
        ]


# Convierte un SELECT en objeto Asignacion_proyecto
def create_asignacion_proyecto_object(query: tuple) -> Asignacion_proyecto:
    return Asignacion_proyecto(
        id=query[0],
        proyecto_id=query[1],
        consultor_id=query[2],
        activo=query[3]
    )
