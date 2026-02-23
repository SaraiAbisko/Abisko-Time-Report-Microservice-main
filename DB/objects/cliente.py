from DB.crud import BaseRepository
from DB.objects.contacto import Contacto  # Asegúrate que esta clase exista

class Client:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

    def create_client(self):
        BaseRepository.create("cliente", {"nombre": self.nombre})

    def update_values(self):
        BaseRepository.update("cliente", {"nombre": self.nombre}, {"id": self.id})

    def delete_client(self):
        BaseRepository.delete("cliente", {"id": self.id})

    def get_contactos(self) -> list[Contacto]:
        resultados = BaseRepository.read("contacto", {"cliente_id": self.id})
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
        
    @staticmethod
    def get_all() -> list["Client"]:
        resultados = BaseRepository.read_all("cliente")

        return [
            Client(
                id=row[0],
                nombre=row[1]
            )
            for row in resultados
        ]


# Convierte los datos de un SELECT a un objeto Client
def create_client_object(query: tuple) -> Client:
    return Client(id=query[0], nombre=query[1])

# Selecciona todas las instancias de Client registradas en la DB
def get_all_client() -> list[Client]:
    resultados = BaseRepository.read_all("cliente")
    return [create_client_object(row) for row in resultados]