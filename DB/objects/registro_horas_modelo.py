from DB.crud import BaseRepository

class RegistroHorasModelo:
    def __init__(self, id_registro: int, fecha_registro: str, total_horas: int, 
                 resumen_trabajo_realizado: str, etapa_proyecto: int, iniciativa_cliente: str, 
                 id_consultor:str, id_proyecto: int, id_servicio: int):
        
        self.id_registro = id_registro
        self.fecha_registro = fecha_registro
        self.total_horas = total_horas
        self.resumen_trabajo_realizado = resumen_trabajo_realizado
        self.etapa_proyecto = etapa_proyecto
        self.iniciativa_cliente = iniciativa_cliente
        self.id_consultor = id_consultor
        self.id_proyecto = id_proyecto
        self.id_servicio = id_servicio
        
        
    @staticmethod
    def get_registros(id_registro: int) -> list["RegistroHorasModelo"]:
        resultados = BaseRepository.read("registro_horas_modelo", {"id_registro": id_registro})

        return [
            RegistroHorasModelo(
                id_registro=row[0],
                fecha_registro=row[1],
                total_horas=row[2],
                resumen_trabajo_realizado=row[3],
                etapa_proyecto=row[4],
                iniciativa_cliente=row[5],
                id_consultor=row[6],
                id_proyecto=row[7],
                id_servicio=row[8]
            )
            for row in resultados
        ]          
        
    @staticmethod
    def get_all_registros() -> list["RegistroHorasModelo"]:
        resultados = BaseRepository.read_all("registro_horas_modelo")

        return [
            RegistroHorasModelo(
                id_registro=row[0],
                fecha_registro=row[1],
                total_horas=row[2],
                resumen_trabajo_realizado=row[3],
                etapa_proyecto=row[4],
                iniciativa_cliente=row[5],
                id_consultor=row[6],
                id_proyecto=row[7],
                id_servicio=row[8]
            )
            for row in resultados
        ]         