import sys
# Eliminamos la importación local de db_marvel. Ahora somos un cliente externo.
import requests
import json

# Definimos la URL de nuestra API (donde vive Uvicorn)
API_URL = "http://127.0.0.1:8000/api/marvel/personajes"

from Marvel.db_marvel import obtener_personajes_api, crear_personaje_api, borrar_personaje_api


def mostrar_menu():
    print("\n" + "=" * 45)
    print(" 🦸‍♂️ PANEL DE CONTROL: MULTIVERSO MARVEL 🦸‍♀️")
    print("=" * 45)
    print("1. Ver lista de personajes (Top 20)")
    print("2. Añadir un nuevo personaje")
    print("3. Eliminar un personaje (Chasquido)")
    print("4. Salir del sistema")
    print("=" * 45)


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")

        if opcion == '1':
            print("\n--- [GET] LISTA DE PERSONAJES DESDE LA API ---")
            try:
                # 1. Hacemos la petición GET a FastAPI
                respuesta = requests.get(API_URL)

                # 2. Imprimimos los metadatos y encabezados de red
                print(f"📡 Código de Estado HTTP: {respuesta.status_code}")
                print(f"📦 Encabezado Content-Type: {respuesta.headers.get('content-type')}")
                print("-" * 30)

                if respuesta.status_code == 200:
                    personajes = respuesta.json()  # Extraemos el JSON
                    if personajes:
                        for p in personajes:
                            print(
                                f"ID: {p['id_personaje']} | Alias: {p['alias_heroe']:<15} | Bando: {p['bando']:<10} | Poder: {p['nivel_poder']}")
                    else:
                        print("No hay personajes registrados en la API.")
                else:
                    print(f"❌ Error del servidor: {respuesta.text}")

            except requests.exceptions.ConnectionError:
                print("❌ ERROR RED: No se pudo contactar con la API. ¿Está Uvicorn encendido?")

        elif opcion == '2':
            print("\n--- [POST] AÑADIR NUEVO PERSONAJE VÍA API ---")
            try:
                id_personaje = int(input("ID del personaje (número único): "))
                alias = input("Alias del héroe/villano: ")
                nombre = input("Nombre real: ")
                bando = input("Bando (Héroe / Villano / Anti-héroe): ")
                poder = int(input("Nivel de poder (1-100): "))

                # 1. Preparamos el paquete de datos para enviarlo por internet
                datos_personaje = {
                    "id_personaje": id_personaje,
                    "alias_heroe": alias,
                    "nombre_real": nombre,
                    "bando": bando,
                    "nivel_poder": poder
                }

                # 2. Hacemos la petición POST a FastAPI indicando que enviamos JSON
                print("\nEnviando paquete JSON a la API...")
                respuesta = requests.post(API_URL, json=datos_personaje)

                # 3. Imprimimos los metadatos
                print(f"📡 Código de Estado HTTP: {respuesta.status_code}")

                if respuesta.status_code == 200:
                    datos_respuesta = respuesta.json()
                    # Comprobamos si la API nos devolvió su mensaje de éxito o de error
                    if "error" in datos_respuesta:
                        print(f"❌ La API respondió: {datos_respuesta['error']}")
                    else:
                        print(f"✅ La API respondió: {datos_respuesta.get('mensaje')}")
                # El error 422 es típico de FastAPI cuando envías un formato incorrecto
                elif respuesta.status_code == 422:
                    print("❌ Error 422: A la API no le gustó el formato de los datos.")
                else:
                    print(f"❌ Error desconocido: {respuesta.text}")

            except ValueError:
                print("❌ Error de formato: El ID y el nivel de poder deben ser números.")
            except requests.exceptions.ConnectionError:
                print("❌ ERROR RED: No se pudo contactar con la API.")

        elif opcion == '3':
            print("\n--- [DELETE] ELIMINAR PERSONAJE VÍA API ---")
            try:
                id_personaje = int(input("Introduce el ID del personaje que deseas eliminar: "))
                seguro = input(f"⚠️ ¿Estás seguro de que quieres borrar el ID {id_personaje}? (s/n): ")

                if seguro.lower() == 's':
                    # 1. Construimos la URL específica con el ID al final (ej: .../personajes/5)
                    url_borrado = f"{API_URL}/{id_personaje}"

                    print(f"\nDisparando petición DELETE a: {url_borrado}")
                    # 2. Hacemos la petición DELETE
                    respuesta = requests.delete(url_borrado)

                    # 3. Imprimimos los metadatos
                    print(f"📡 Código de Estado HTTP: {respuesta.status_code}")

                    if respuesta.status_code == 200:
                        datos_respuesta = respuesta.json()
                        if "error" in datos_respuesta:
                            print(f"❌ La API respondió: {datos_respuesta['error']}")
                        else:
                            print(f"✅ La API respondió: {datos_respuesta.get('mensaje')}")
                    else:
                        print(f"❌ Error del servidor: {respuesta.text}")
                else:
                    print("Operación cancelada. El personaje está a salvo.")

            except ValueError:
                print("❌ Error de formato: El ID debe ser un número entero.")
            except requests.exceptions.ConnectionError:
                print("❌ ERROR RED: No se pudo contactar con la API.")

        elif opcion == '4':
            print("\nCerrando las puertas del multiverso. ¡Hasta pronto!")
            sys.exit()

        else:
            print("❌ Opción no válida. Por favor, elige un número del 1 al 4.")


if __name__ == "__main__":
    main()

