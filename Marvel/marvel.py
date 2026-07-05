import sys
# Importamos la logica de base de datos desde el modulo db_marvel
from db_marvel import obtener_personajes_api, crear_personaje_api, borrar_personaje_api

def mostrar_menu():
    print("\n" + "=" * 45)
    print(" GESTOR DE BASE DE DATOS MARVEL ")
    print("=" * 45)
    print("1. Ver personajes almacenados")
    print("2. Añadir un nuevo personaje")
    print("3. Borrar un personaje")
    print("4. Salir")
    print("=" * 45)

def main():
    # Bucle principal de la aplicacion
    while True:
        mostrar_menu()

        try:
            opcion = int(input("Elige una opcion (1-4): "))

            match opcion:
                case 1:
                    print("\n[INFO] Consultando registros...")
                    personajes = obtener_personajes_api()

                    if not personajes:
                        print("La base de datos esta vacia.")
                    else:
                        print("\n--- LISTADO DE PERSONAJES ---")
                        for p in personajes:
                            print(f"ID: {p['id_personaje']} | Alias: {p['alias_heroe']} | Nombre: {p['nombre_real']} | Bando: {p['bando']} | Poder: {p['nivel_poder']}")

                case 2:
                    print("\n--- ALTA DE PERSONAJE ---")
                    try:
                        id_per = int(input("ID (numero unico): "))
                        alias = input("Alias: ")
                        nombre = input("Nombre real: ")
                        bando = input("Bando: ")
                        poder = int(input("Nivel de poder (1-100): "))

                        exito = crear_personaje_api(id_per, alias, nombre, bando, poder)
                        if exito:
                            print(f"\n[OK] Personaje {alias} registrado correctamente.")
                        else:
                            print("\n[ERROR] No se pudo registrar. Verifica que el ID no exista previamente.")
                    except ValueError:
                        print("\n[AVISO] Los campos ID y Nivel de poder requieren valores numericos.")

                case 3:
                    print("\n--- BAJA DE PERSONAJE ---")
                    try:
                        id_borrar = int(input("Introduce el ID del personaje a eliminar: "))
                        exito = borrar_personaje_api(id_borrar)

                        if exito:
                            print(f"\n[OK] Registro con ID {id_borrar} eliminado.")
                        else:
                            print(f"\n[AVISO] No se encontro ningun registro con el ID {id_borrar}.")
                    except ValueError:
                        print("\n[AVISO] El ID introducido no tiene un formato valido.")

                case 4:
                    print("\nCerrando conexion. Fin del programa.")
                    sys.exit()

                case _:
                    print("\n[AVISO] Opcion fuera de rango. Seleccione entre 1 y 4.")

        except ValueError:
            print("\n[AVISO] Entrada no reconocida. Debe introducir un numero.")

if __name__ == "__main__":
    main()
