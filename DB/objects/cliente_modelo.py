from DB.crud import BaseRepository

class ClientModelo:
    def __init__(self, id_cliente: int, nombre_empresa: str, contacto_principal: str, correo_contacto: str, telefono_contacto: int):
        self.id_cliente = id_cliente
        self.nombre_empresa = nombre_empresa
        self.contacto_principal = contacto_principal
        self.correo_contacto = correo_contacto
        self.telefono_contacto = telefono_contacto

    @staticmethod
    def get_clientes(cliente_id: int) -> list["ClientModelo"]:
        resultados = BaseRepository.read("cliente_modelo", {"id_cliente": cliente_id})

        return [
            ClientModelo(
                id_cliente=row[0],
                nombre_empresa=row[1],
                contacto_principal=row[2],
                correo_contacto=row[3],
                telefono_contacto=row[4]
            )
            for row in resultados
        ]
        
    @staticmethod
    def get_all_clientes() -> list["ClientModelo"]:
        resultados = BaseRepository.read_all("cliente_modelo")

        return [
            ClientModelo(
                id_cliente=row[0],
                nombre_empresa=row[1],
                contacto_principal=row[2],
                correo_contacto=row[3],
                telefono_contacto=row[4]
            )
            for row in resultados
        ]

