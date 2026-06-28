import oracledb
import os
from dotenv import load_dotenv


# 1. Cargamos el archivo .env una sola vez al arrancar el programa
load_dotenv()

# 2. Guardamos las credenciales en variables para usarlas en todo el archivo
USUARIO = os.getenv("DB_USUARIO")
CONTRASENA = os.getenv("DB_CONTRASENA")
DSN = os.getenv("DB_HOST")


def obtener_personajes_api():
    """
    Se conecta a Oracle y devuelve una lista de personajes.
    Por defecto, devuelve solo los 20 primeros para no saturar la pantalla.
    """
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        # Usamos FETCH FIRST para limitar cuántos traemos
        sql = """
            SELECT id_personaje, alias_heroe, nombre_real, bando, nivel_poder 
            FROM marvel_personajes 
        """

        # Le pasamos el límite como parámetro de seguridad
        cursor.execute(sql)
        datos = cursor.fetchall()

        # Transformamos las tuplas raras de Oracle en diccionarios bonitos de Python
        lista_personajes = []
        for fila in datos:
            lista_personajes.append({
                "id_personaje": fila[0],
                "alias_heroe": fila[1],
                "nombre_real": fila[2],
                "bando": fila[3],
                "nivel_poder": fila[4]
            })

        return lista_personajes

    except oracledb.DatabaseError as e:
        print(f"Error en Oracle: {e}")
        return []  # Devolvemos una lista vacía si algo falla
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()

def crear_personaje_api(id_personaje, alias_heroe, nombre_real, bando, nivel_poder):
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn= DSN)
        cursor = conexion.cursor()

        sql = """
            INSERT INTO marvel_personajes(id_personaje, alias_heroe, nombre_real, bando, nivel_poder)
            VALUES (:1, :2 , :3 , :4, :5)
        """
        cursor.execute(sql, [id_personaje, alias_heroe, nombre_real, bando, nivel_poder])
        conexion.commit()

        return True

    except oracledb.DatabaseError as e:
        print(f"Error al crear personaje en Oracle: {e}")
        return False

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()

def borrar_personaje_api(id_personaje):
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn= DSN)
        cursor = conexion.cursor()

        sql = """
            DELETE FROM marvel_personajes WHERE id_personaje = :1
        """
        cursor.execute(sql, [id_personaje])

        if cursor.rowcount == 0:
            return False
        conexion.commit()
        return True

    except oracledb.DatabaseError as e:
        print(f"Error al borrar personaje en Oracle: {e}")
        return False

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals():conexion.close()