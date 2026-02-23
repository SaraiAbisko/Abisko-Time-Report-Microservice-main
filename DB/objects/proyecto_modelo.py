from DB.crud import BaseRepository

class ProyectoModelo:
    def __init__(self, id_proyecto: int, nombre_proyecto: str, cliente_id_cliente: int, fecha_inicio: int, fecha_fin: int, descripcion: str, estado:str):
        self.id_proyecto = id_proyecto
        self.nombre_proyecto = nombre_proyecto
        self.cliente_id_cliente = cliente_id_cliente
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.descripcion = descripcion
        self.estado = estado
        
        
        
    @staticmethod
    def get_proyectos(id_proyecto: int) -> list["ProyectoModelo"]:
        resultados = BaseRepository.read("proyecto_modelo", {"id_proyecto": id_proyecto})

        return [
            ProyectoModelo(
                id_proyecto=row[0],
                nombre_proyecto=row[1],
                cliente_id_cliente=row[2],
                fecha_inicio=row[3],
                fecha_fin=row[4],
                descripcion=row[5],
                estado=row[6]
            )
            for row in resultados
        ]          
        
    @staticmethod
    def get_all_proyectos() -> list["ProyectoModelo"]:
        resultados = BaseRepository.read_all("proyecto_modelo")

        return [
            ProyectoModelo(
                id_proyecto=row[0],
                nombre_proyecto=row[1],
                cliente_id_cliente=row[2],
                fecha_inicio=row[3],
                fecha_fin=row[4],
                descripcion=row[5],
                estado=row[6]
            )
            for row in resultados
        ]         
        