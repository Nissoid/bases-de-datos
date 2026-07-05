
import os
import sys
import oracledb
from dotenv import load_dotenv

# 1. Cargamos el archivo .env una sola vez al arrancar el programa
load_dotenv()

# 2. Guardamos las credenciales en variables para usarlas en todo el archivo
USUARIO = os.getenv("DB_USUARIO")
CONTRASENA = os.getenv("DB_CONTRASENA")
DSN = os.getenv("DB_HOST")


# --- FUNCIONES DE BASE DE DATOS ---

def obtener_personajes_api():
    """
    Se conecta a Oracle y devuelve una lista de personajes.
    """
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        sql = """
            SELECT id_personaje, alias_heroe, nombre_real, bando, nivel_poder 
            FROM marvel_personajes 
        """
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
        return []
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()


def crear_personaje_api(id_personaje, alias_heroe, nombre_real, bando, nivel_poder):
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
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
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
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
        if 'conexion' in locals(): conexion.close()


# --- MENÚ INTERACTIVO ---

def mostrar_menu():
    print("\n" + "=" * 45)
    print(" 🦸‍♂️ MARVEL UNIVERSE DATABASE MANAGER 🦸‍♂️ ")
    print("=" * 45)
    print("1. 📋 Ver personajes almacenados")
    print("2. ➕ Añadir un nuevo personaje")
    print("3. 🗑️ Borrar un personaje")
    print("4. 🚪 Salir")
    print("=" * 45)


def main():
    while True:
        mostrar_menu()

        try:
            opcion = int(input("Elige una opción (1-4): "))

            match opcion:
                case 1:
                    print("\n[INFO] Consultando la base de datos...")
                    personajes = obtener_personajes_api()

                    if not personajes:
                        print("📭 No hay personajes en la base de datos.")
                    else:
                        print("\n--- 📋 LISTA DE PERSONAJES MARVEL ---")
                        for p in personajes:
                            # Como tu función devuelve diccionarios, accedemos a los datos con las claves
                            print(
                                f"ID: {p['id_personaje']} | Alias: {p['alias_heroe']} | Nombre: {p['nombre_real']} | Bando: {p['bando']} | Poder: {p['nivel_poder']}")

                case 2:
                    print("\n--- ➕ AÑADIR NUEVO PERSONAJE ---")
                    try:
                        id_per = int(input("ID del personaje (número único): "))
                        alias = input("Alias del héroe/villano: ")
                        nombre = input("Nombre real: ")
                        bando = input("Bando o afiliación: ")
                        poder = int(input("Nivel de poder (1-100): "))

                        exito = crear_personaje_api(id_per, alias, nombre, bando, poder)
                        if exito:
                            print(f"\n✅ ¡{alias} añadido correctamente a la base de datos!")
                        else:
                            print("\n❌ Hubo un problema al añadir el personaje. Verifica que el ID no exista ya.")
                    except ValueError:
                        print("\n⚠️ Error: El ID y el nivel de poder deben ser números enteros.")

                case 3:
                    print("\n--- 🗑️ BORRAR PERSONAJE ---")
                    try:
                        id_borrar = int(input("Introduce el ID del personaje a borrar: "))
                        exito = borrar_personaje_api(id_borrar)

                        if exito:
                            print(f"\n✅ Personaje con ID {id_borrar} eliminado correctamente.")
                        else:
                            print(f"\n⚠️ No se ha podido borrar. ¿Seguro que el ID {id_borrar} existe?")
                    except ValueError:
                        print("\n⚠️ Error: El ID debe ser un número entero.")

                case 4:
                    print("\nCerrando el sistema. ¡Hasta pronto! 🦸‍♂️")
                    sys.exit()

                case _:
                    print("\n⚠️ Error: Por favor, introduce un número del 1 al 4.")

        except ValueError:
            print("\n⚠️ Error: Entrada no válida. Debes introducir un número entero.")


if __name__ == "__main__":
    main()