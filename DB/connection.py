import psycopg2
from psycopg2 import OperationalError

# Indicaciones: Se debe adaptar la funcion create_connection para que utilice
# los parametros de conexion de la clase ConfigLoader en Utils/config.py

# Crea la conexion con la base de datos
def create_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432", # 2310
            database="time_report_data_qa",
            user="postgres",
            password="Qlik2025*"
        )
        print("[DB] Conexión establecida exitosamente.")
        return conn
    except OperationalError as e:
        print(f"[DB][Error] No se pudo conectar: {e}")
        return None

# Cierra el cursor y la conexión a la base de datos si están abiertos.
def close_connection(connection, cursor=None):
    try:
        if cursor is not None and not cursor.closed:
            cursor.close()
            print("[DB] Cursor cerrado correctamente.")
        if connection is not None and connection.closed == 0:
            connection.close()
            print("[DB] Conexión cerrada correctamente.")
    except Exception as error:
        print(f"[DB][Error al cerrar la conexión]: {error}")