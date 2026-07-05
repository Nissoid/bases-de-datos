import oracledb
import os
from dotenv import load_dotenv

# Carga de variables de entorno al iniciar el modulo
load_dotenv()

USUARIO = os.getenv("DB_USUARIO")
CONTRASENA = os.getenv("DB_CONTRASENA")
DSN = os.getenv("DB_HOST")


def obtener_personajes_api():
    """Ejecuta una consulta SELECT y devuelve una lista de diccionarios con los personajes."""
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        sql = """
            SELECT id_personaje, alias_heroe, nombre_real, bando, nivel_poder 
            FROM marvel_personajes 
        """
        cursor.execute(sql)
        datos = cursor.fetchall()

        # Mapeo de los resultados de Oracle (tuplas) a diccionarios de Python
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
        print(f"[ERROR] Fallo en la base de datos: {e}")
        return []

    finally:
        # Aseguramos el cierre de recursos incluso si hay una excepcion
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()


def crear_personaje_api(id_personaje, alias_heroe, nombre_real, bando, nivel_poder):
    """Inserta un nuevo registro. Retorna True si tiene exito."""
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        # Uso de bind variables para prevenir inyeccion SQL
        sql = """
            INSERT INTO marvel_personajes(id_personaje, alias_heroe, nombre_real, bando, nivel_poder)
            VALUES (:1, :2, :3, :4, :5)
        """
        cursor.execute(sql, [id_personaje, alias_heroe, nombre_real, bando, nivel_poder])
        conexion.commit()

        return True

    except oracledb.DatabaseError as e:
        print(f"[ERROR] No se pudo crear el personaje: {e}")
        return False

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()


def borrar_personaje_api(id_personaje):
    """Elimina un registro por ID. Retorna True si se elimino algo."""
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        sql = "DELETE FROM marvel_personajes WHERE id_personaje = :1"
        cursor.execute(sql, [id_personaje])

        # rowcount nos indica cuantas filas han sido afectadas por el DELETE
        if cursor.rowcount == 0:
            return False

        conexion.commit()
        return True

    except oracledb.DatabaseError as e:
        print(f"[ERROR] Fallo al intentar borrar: {e}")
        return False

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()