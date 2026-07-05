import oracledb
import os
from dotenv import load_dotenv

# Cargamos las credenciales del archivo .env
load_dotenv()
USUARIO = os.getenv("DB_USUARIO")
CONTRASENA = os.getenv("DB_CONTRASENA")
DSN = os.getenv("DB_HOST")

# --- ESCUDO DE SEGURIDAD AÑADIDO ---
# Si alguna de las variables está vacía (None), detenemos el programa antes de que falle Oracle
if not USUARIO or not CONTRASENA or not DSN:
    print("❌ Error crítico: Faltan credenciales.")
    print("Python no ha podido leer tus datos de acceso. Por favor, comprueba que:")
    print("1. Tienes un archivo llamado exactamente '.env' en esta misma carpeta.")
    print("2. Dentro del archivo '.env' están escritas ESTAS variables (revisa mayúsculas):")
    print("   DB_USER=tu_usuario")
    print("   DB_PASSWORD=tu_contraseña")
    print("   DB_DSN=tu_dsn")
    exit(1)  # Salimos del programa con errorS


def crear_estructura_base_datos():
    print("Iniciando el instalador de la base de datos...")

    try:
        # 1. Nos conectamos a Oracle
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        # 2. Definimos la sentencia SQL para crear la tabla de Marvel
        # Hemos limpiado los saltos de línea y espacios invisibles para que Oracle no se confunda
        sql_crear_marvel = "CREATE TABLE marvel_personajes (id_personaje NUMBER PRIMARY KEY, alias_heroe VARCHAR2(100) NOT NULL, nombre_real VARCHAR2(100), bando VARCHAR2(50), nivel_poder NUMBER)"

        print("Creando tabla 'marvel_personajes'...")

        try:
            # Ejecutamos la orden de crear la tabla
            cursor.execute(sql_crear_marvel)
            print("✅ Tabla 'marvel_personajes' creada con éxito en el universo de tu base de datos.")

        except oracledb.DatabaseError as e:
            error_obj, = e.args
            # El código de error 955 significa "El nombre ya está siendo usado por un objeto existente"
            if error_obj.code == 955:
                print("⚠️ La tabla 'marvel_personajes' ya existe. No es necesario crearla.")
            else:
                print(f"❌ Error al crear la tabla: {e}")

    except oracledb.DatabaseError as e:
        print(f"❌ Error de conexión a Oracle: {e}")

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()
        print("Instalación finalizada.")


if __name__ == "__main__":
    # Si te fijas, al final añadimos una confirmación de seguridad
    confirmacion = input("ATENCIÓN: Esto modificará la base de datos. ¿Deseas continuar? (s/n): ")
    if confirmacion.lower() == 's':
        crear_estructura_base_datos()
    else:
        print("Operación cancelada.")