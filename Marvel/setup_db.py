import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

USUARIO = os.getenv("DB_USUARIO")
CONTRASENA = os.getenv("DB_CONTRASENA")
DSN = os.getenv("DB_HOST")

# Verificacion de dependencias de entorno
if not USUARIO or not CONTRASENA or not DSN:
    print("[ERROR CRITICO] No se encontraron las credenciales.")
    print("Asegurese de configurar el archivo .env con las variables: DB_USUARIO, DB_CONTRASENA, DB_HOST.")
    exit(1)

def crear_estructura_base_datos():
    print("[INFO] Iniciando configuracion DDL...")

    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        # Estructura de la tabla principal
        sql_crear_marvel = """
            CREATE TABLE marvel_personajes (
                id_personaje NUMBER PRIMARY KEY, 
                alias_heroe VARCHAR2(100) NOT NULL, 
                nombre_real VARCHAR2(100), 
                bando VARCHAR2(50), 
                nivel_poder NUMBER
            )
        """

        try:
            cursor.execute(sql_crear_marvel)
            print("[OK] Tabla 'marvel_personajes' creada con exito.")

        except oracledb.DatabaseError as e:
            error_obj, = e.args
            # Control de error ORA-00955 (el objeto ya existe)
            if error_obj.code == 955:
                print("[INFO] La estructura ya existe. No se requiere accion.")
            else:
                print(f"[ERROR] No se pudo crear la tabla: {e}")

    except oracledb.DatabaseError as e:
        print(f"[ERROR CRITICO] Conexion denegada: {e}")

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()
        print("[INFO] Proceso de configuracion finalizado.")

if __name__ == "__main__":
    # Mecanismo de seguridad para evitar ejecuciones accidentales
    confirmacion = input("AVISO: Esta operacion alterara la estructura de la base de datos. Continuar? (s/n): ")
    if confirmacion.lower() == 's':
        crear_estructura_base_datos()
    else:
        print("[INFO] Operacion cancelada por el usuario.")