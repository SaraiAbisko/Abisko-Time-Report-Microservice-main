from DB.crud import BaseRepository

class ConsultorModelo:
    def __init__(self, id_consultor: int, nombre: str, apellido: str, correo_electronico: str, telefono: int):
        self.id_consultor = id_consultor
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        

    @staticmethod
    def get_consultores(id_consultor: int) -> list["ConsultorModelo"]:
        resultados = BaseRepository.read("consultor_modelo", {"id_consultor": id_consultor})

        return [
            ConsultorModelo(
                id_consultor=row[0],
                nombre=row[1],
                apellido=row[2],
                correo_electronico=row[3],
                telefono=row[4]
            )
            for row in resultados
        ]       
        
        
        
    @staticmethod
    def get_all_consultores() -> list["ConsultorModelo"]:
        resultados = BaseRepository.read_all("consultor_modelo")

        return [
            ConsultorModelo(
                 id_consultor=row[0],
                nombre=row[1],
                apellido=row[2],
                correo_electronico=row[3],
                telefono=row[4]
            )
            for row in resultados
        ]     