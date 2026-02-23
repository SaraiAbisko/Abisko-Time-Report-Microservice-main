from DB.crud import BaseRepository

class TipoCobro:
    def __init__(self, id: int, tipo_cobro: str, horas_relacionadas: int):
        self.id = id
        self.tipo_cobro = tipo_cobro
        self.horas_relacionadas = horas_relacionadas

    def create(self):
        BaseRepository.create("tipo_cobro", {
            "tipo_cobro": self.tipo_cobro,
            "horas_relacionadas": self.horas_relacionadas
        })

    def update(self):
        BaseRepository.update("tipo_cobro", {
            "tipo_cobro": self.tipo_cobro,
            "horas_relacionadas": self.horas_relacionadas
        }, {
            "id": self.id
        })

    @staticmethod
    def get_all() -> list["TipoCobro"]:
        resultados = BaseRepository.read_all("tipo_cobro")

        return [
            TipoCobro(
                id=row[0],
                tipo_cobro=row[1],
                horas_relacionadas=row[2]
            )
            for row in resultados
        ]

# Convierte un SELECT en objeto TipoCobro
def create_tipo_cobro_object(query: tuple) -> TipoCobro:
    return TipoCobro(
        id=query[0],
        tipo_cobro=query[1],
        horas_relacionadas=query[2]
    )