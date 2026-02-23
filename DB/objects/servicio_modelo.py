from DB.crud import BaseRepository

class ServicioModelo:
    def __init__(self, id_servicio: int, nombre_servicio: str, descripcion_servicio: str,
                 tipo_cobro: str, horas_relacionadas: int):
        self.id_servicio = id_servicio
        self.nombre_servicio = nombre_servicio
        self.descripcion_servicio = descripcion_servicio
        self.tipo_cobro = tipo_cobro
        self.horas_relacionadas = horas_relacionadas
        

    @staticmethod
    def get_servicios(id_servicio: int) -> list["ServicioModelo"]:
        resultados = BaseRepository.read("servicio_modelo", {"id_servicio": id_servicio})

        return [
            ServicioModelo(
                id_servicio=row[0],
                nombre_servicio=row[1],
                descripcion_servicio=row[2],
                tipo_cobro=row[3],
                horas_relacionadas=row[4]
            )
            for row in resultados
        ]       
        
        
        
    @staticmethod
    def get_all_servicios() -> list["ServicioModelo"]:
        resultados = BaseRepository.read_all("servicio_modelo")

        return [
            ServicioModelo(
                id_servicio=row[0],
                nombre_servicio=row[1],
                descripcion_servicio=row[2],
                tipo_cobro=row[3],
                horas_relacionadas=row[4]
            )
            for row in resultados
        ]     