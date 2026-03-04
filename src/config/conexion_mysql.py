import mysql.connector
from mysql.connector import Error 


class ConexionMySQL:
    host = "localhost"
    port = 3308
    database = "commerce"
    user = "web"
    password = "web"

def crear_conexion():
    try:
        print("Intentando conectar a la base de datos...")
        conexion = mysql.connector.connect(
            host=ConexionMySQL.host,
            port=ConexionMySQL.port,
            database=ConexionMySQL.database,
            user=ConexionMySQL.user,
            password=ConexionMySQL.password
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None
