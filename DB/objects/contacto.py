from DB.crud import BaseRepository

class Contacto:
    def __init__(self, id: int, nombre_contacto: str, correo_electronico: str, numero_telefono: str, cliente_id: int):
        self.id = id
        self.nombre_contacto = nombre_contacto
        self.correo_electronico = correo_electronico
        self.numero_telefono = numero_telefono
        self.cliente_id = cliente_id

    def create_contact(self):
        BaseRepository.create("contacto", {
            "nombre_contacto": self.nombre_contacto,
            "correo_electronico": self.correo_electronico,
            "numero_telefono": self.numero_telefono,
            "cliente_id": self.cliente_id
        })

    def update_contact(self):
        BaseRepository.update("contacto", {
            "nombre_contacto": self.nombre_contacto,
            "correo_electronico": self.correo_electronico,
            "numero_telefono": self.numero_telefono,
            "cliente_id": self.cliente_id
        }, {
            "id": self.id
        })
        
    @staticmethod
    def get_all() -> list["Contacto"]:
        resultados = BaseRepository.read_all("contacto")

        return [
            Contacto(
                id=row[0],
                nombre_contacto=row[1],
                correo_electronico=row[2],
                numero_telefono=row[3],
                cliente_id=row[4]
            )
            for row in resultados
        ]


# Convierte los datos de un SELECT a un objeto Contacto
def create_contact_object(query: tuple) -> Contacto:
    return Contacto(
        id=query[0],
        nombre_contacto=query[1],
        correo_electronico=query[2],
        numero_telefono=query[3],
        cliente_id=query[4]
    )
