from .connection import create_connection

class BaseRepository:
    @staticmethod
    def create(table, data: dict):
        conn = create_connection()
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        values = list(data.values())

        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders}) RETURNING id;"

        with conn.cursor() as cursor:
            cursor.execute(query, values)
            inserted_id = cursor.fetchone()[0]
            conn.commit()
            return inserted_id

    @staticmethod
    def read(table, conditions: dict):
        conn = create_connection()
        where_clause = ' AND '.join([f"{k} = %s" for k in conditions.keys()])
        values = list(conditions.values())

        query = f"SELECT * FROM {table} WHERE {where_clause};"

        with conn.cursor() as cursor:
            cursor.execute(query, values)
            return cursor.fetchall()
        
    @staticmethod
    def read_all(table: str):
        conn = create_connection()
        query = f"SELECT * FROM {table};"

        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    @staticmethod
    def update(table, data: dict, conditions: dict):
        conn = create_connection()
        set_clause = ', '.join([f"{k} = %s" for k in data.keys()])
        where_clause = ' AND '.join([f"{k} = %s" for k in conditions.keys()])
        values = list(data.values()) + list(conditions.values())

        query = f"UPDATE {table} SET {set_clause} WHERE {where_clause};"

        with conn.cursor() as cursor:
            cursor.execute(query, values)
            conn.commit()

    @staticmethod
    def delete(table, conditions: dict):
        conn = create_connection()
        where_clause = ' AND '.join([f"{k} = %s" for k in conditions.keys()])
        values = list(conditions.values())

        query = f"DELETE FROM {table} WHERE {where_clause};"

        with conn.cursor() as cursor:
            cursor.execute(query, values)
            conn.commit()

    @staticmethod
    def call_function(sql: str, params: list = None):
        conn = create_connection()
        with conn.cursor() as cursor:
            cursor.execute(sql, params or [])
            return cursor.fetchall()