# Obtiene los datos desde la base de datos y los retorna en formato JSON
def get_user_data(user_fullname : str) -> dict:
    # El ID no esta presente en el AD, asi que, en su lugar, se comparte el nombre del consultor en conjunto con la DB de consultor
    user_id_query : str = f"SELECT ID FROM CONSULTOR WHERE NAME == {user_fullname};"

    # Consulta la vista registrada para la instancia de consultas al Time Report
    user_register_query : str = f"SELECT * FROM CLIENTE;"

    return {}