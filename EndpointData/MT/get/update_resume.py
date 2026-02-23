from Backend.DB.crud import BaseRepository
import json

def get_updated_stats():
    # Retorna un diccionario con las estadísticas actualizadas
    return {
        "clients": count_rows("cliente"),
        "contacts": count_rows("contacto"),
        "active_projects": count_active_projects(),
        "defined_services": count_rows("servicio"),
        "payments": count_rows("tipo_cobro"),
        "employees": count_rows("consultor"),
        "states": count_rows("estados")
    }

def count_rows(table_name):
    # Cuenta el total de filas de una tabla
    return len(BaseRepository.read_all(table_name))

def count_active_projects():
    # Intenta contar los proyectos activos (requiere campo booleano 'activo')
    # Si no existe, retorna el total de proyectos
    try:
        active = BaseRepository.read("proyecto", {"activo": True})
        return len(active)
    except Exception:
        return count_rows("proyecto")

def save_stats_to_file(filepath="Backend/EndpointData/MT/get/resume.json"):
    # Guarda las estadísticas actualizadas en un archivo JSON
    stats = get_updated_stats()
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4)

if __name__ == "__main__":
    save_stats_to_file()