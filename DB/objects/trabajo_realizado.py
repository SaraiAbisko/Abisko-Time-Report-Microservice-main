from DB.crud import BaseRepository

class Trabajo_realizado:
    def __init__(self, id: int, nombre_actividad: str, horas_invertidas: int,
                 hora_extra: bool, asignacion_id: int, fecha):
        self.id = id
        self.nombre_actividad = nombre_actividad
        self.horas_invertidas = horas_invertidas
        self.hora_extra = hora_extra
        self.asignacion_id = asignacion_id
        self.fecha = fecha

    def create_trabajo_realizado(self):
        BaseRepository.create("trabajo_realizado", {
            "nombre_actividad": self.nombre_actividad,
            "horas_invertidas": self.horas_invertidas,
            "hora_extra": self.hora_extra,
            "asignacion_id": self.asignacion_id,
            "fecha": self.fecha
        })

    def update_values(self):
        BaseRepository.update("trabajo_realizado", {
            "nombre_actividad": self.nombre_actividad,
            "horas_invertidas": self.horas_invertidas,
            "hora_extra": self.hora_extra,
            "asignacion_id": self.asignacion_id,
            "fecha": self.fecha
        }, {"id": self.id})

    def delete(self):
        BaseRepository.delete("trabajo_realizado", {"id": self.id})

    @staticmethod
    def get_all() -> list["Trabajo_realizado"]:
        resultados = BaseRepository.read_all("trabajo_realizado")

        return [
            Trabajo_realizado(
                id=row[0],
                nombre_actividad=row[1],
                horas_invertidas=row[2],
                hora_extra=row[3],
                asignacion_id=row[4],
                fecha=row[5]
            )
            for row in resultados
        ]

def create_trabajo_realizado_object(query: tuple) -> Trabajo_realizado:
    return Trabajo_realizado(*query)

def get_all_trabajo_realizado() -> list[Trabajo_realizado]:
    resultados = BaseRepository.read_all("trabajo_realizado")
    return [create_trabajo_realizado_object(row) for row in resultados]
