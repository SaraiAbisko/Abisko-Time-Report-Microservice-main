from DB.crud import BaseRepository

class Consultor:
    def __init__(self, id: int, nombre: str, coste_hora: float, numero_telefono: str):
        self.id = id
        self.nombre = nombre
        self.coste_hora = coste_hora
        self.numero_telefono = numero_telefono

    def create(self):
        BaseRepository.create("consultor", {
            "nombre": self.nombre,
            "coste_hora": self.coste_hora,
            "numero_telefono": self.numero_telefono
        })

    def update_values(self):
        BaseRepository.update("consultor", {
            "nombre": self.nombre,
            "coste_hora": self.coste_hora,
            "numero_telefono": self.numero_telefono
        }, {
            "id": self.id
        })
        
    @staticmethod
    def get_all() -> list["Consultor"]:
        resultados = BaseRepository.read_all("consultor")

        return [
            Consultor(
                id=row[0],
                nombre=row[1],
                coste_hora=row[2],
                numero_telefono=row[3]
            )
            for row in resultados
        ]


# Convierte un SELECT en objeto Consultor
def create_consultor_object(query: tuple) -> Consultor:
    return Consultor(
        id=query[0],
        nombre=query[1],
        coste_hora=query[2],
        numero_telefono=query[4]
    )

# Obtiene los datos del constructor en base al ID del mismo, normalmente se lo entregaria el AD
def get_consultor_data(consultor_id: int) -> Consultor:
    row = BaseRepository.read("consultor", {"id": consultor_id})
    if not row:
        raise ValueError(f"No se encontró un consultor con id {consultor_id}")
    row = row[0]
    return Consultor(
        id=row[0],
        nombre=row[1],
        coste_hora=row[2],
        numero_telefono=row[4]
    )