import sys
import requests
from tabulate import tabulate

# Las direcciones centrales de nuestra API
URL_CLIENTES = "http://127.0.0.1:8000/api/clientes"
URL_EMPLEADOS = "http://127.0.0.1:8000/api/empleados"


def mostrar_menu():
    print("\n" + "=" * 40)
    print("      SISTEMA ERP - CLIENTE API")
    print("=" * 40)
    print("--- GESTIÓN DE CLIENTES ---")
    print("1. Listar todos los clientes")
    print("2. Añadir un nuevo cliente")
    print("3. Modificar un cliente existente")
    print("4. Eliminar un cliente")
    print("\n--- GESTIÓN DE EMPLEADOS ---")
    print("5. Listar todos los empleados")
    print("6. Añadir un nuevo empleado")
    print("7. Modificar un empleado existente")
    print("8. Eliminar un empleado")
    print("\n9. Salir del sistema")
    print("=" * 40)


# ==========================================
# FUNCIONES DE CLIENTES
# ==========================================

def menu_listar_clientes():
    print("\n--- LISTADO DE CLIENTES ---")
    try:
        respuesta = requests.get(URL_CLIENTES)
        if respuesta.status_code == 200:
            clientes = respuesta.json()
            if not clientes:
                print("No hay clientes registrados.")
                return
            tabla = [[c['id_cliente'], c['nombre'], c['email']] for c in clientes]
            print(tabulate(tabla, headers=["ID", "Nombre Empresa", "Correo Electrónico"], tablefmt="grid"))
        else:
            print(f"Error del servidor: {respuesta.json().get('detail', 'Desconocido')}")
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se pudo conectar con la API. ¿Está el servidor encendido?")


def menu_añadir_cliente():
    print("\n--- AÑADIR NUEVO CLIENTE ---")
    try:
        id_cli = int(input("Introduce el ID del cliente: "))
        nombre = input("Nombre de la empresa: ")
        email = input("Correo electrónico: ")
        datos = {"id_cliente": id_cli, "nombre": nombre, "email": email}

        respuesta = requests.post(URL_CLIENTES, json=datos)
        resultado = respuesta.json()
        if respuesta.status_code == 200 and "mensaje" in resultado:
            print(f"✅ {resultado['mensaje']}")
        else:
            print(f"❌ Error: {resultado.get('error', 'No se pudo crear el cliente')}")
    except ValueError:
        print("El ID debe ser un número entero.")
    except requests.exceptions.ConnectionError:
        print("❌ Error de conexión con la API.")


def menu_modificar_cliente():
    print("\n--- MODIFICAR CLIENTE ---")
    try:
        id_cli = int(input("Introduce el ID del cliente a modificar: "))
        nuevo_nombre = input("Nuevo nombre de la empresa: ")
        nuevo_email = input("Nuevo correo electrónico: ")
        datos = {"id_cliente": id_cli, "nombre": nuevo_nombre, "email": nuevo_email}

        respuesta = requests.put(f"{URL_CLIENTES}/{id_cli}", json=datos)
        resultado = respuesta.json()
        if respuesta.status_code == 200 and "mensaje" in resultado:
            print(f"🔄 {resultado['mensaje']}")
        else:
            print(f"❌ Error: {resultado.get('error', 'No se pudo modificar')}")
    except ValueError:
        print("El ID debe ser un número entero.")
    except requests.exceptions.ConnectionError:
        print("❌ Error de conexión.")


def menu_eliminar_cliente():
    print("\n--- ELIMINAR CLIENTE ---")
    try:
        id_cli = int(input("Introduce el ID del cliente a borrar: "))
        confirmar = input(f"¿Seguro que deseas eliminar al cliente {id_cli}? (s/n): ")
        if confirmar.lower() != 's':
            print("Operación cancelada.")
            return

        respuesta = requests.delete(f"{URL_CLIENTES}/{id_cli}")
        resultado = respuesta.json()
        if respuesta.status_code == 200 and "mensaje" in resultado:
            print(f"🗑️ {resultado['mensaje']}")
        else:
            print(f"❌ Error: {resultado.get('error', 'No se pudo eliminar')}")
    except ValueError:
        print("El ID debe ser un número entero.")
    except requests.exceptions.ConnectionError:
        print("❌ Error de conexión.")


# ==========================================
# FUNCIONES DE EMPLEADOS
# ==========================================

def menu_listar_empleados():
    print("\n--- LISTADO DE EMPLEADOS ---")
    try:
        respuesta = requests.get(URL_EMPLEADOS)
        if respuesta.status_code == 200:
            empleados = respuesta.json()
            if not empleados:
                print("No hay empleados registrados.")
                return
            tabla = [[e['id_empleado'], e['nombre'], e['apellido'], e['id_departamento']] for e in empleados]
            print(tabulate(tabla, headers=["ID", "Nombre", "Apellido", "ID Dept."], tablefmt="grid"))
        else:
            print(f"Error del servidor: {respuesta.json().get('detail', 'Desconocido')}")
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se pudo conectar con la API.")


def menu_añadir_empleado():
    print("\n--- AÑADIR NUEVO EMPLEADO ---")
    try:
        id_emp = int(input("Introduce el ID del empleado: "))
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        id_dep = int(input("ID del Departamento: "))

        datos = {
            "id_empleado": id_emp,
            "nombre": nombre,
            "apellido": apellido,
            "id_departamento": id_dep
        }

        respuesta = requests.post(URL_EMPLEADOS, json=datos)
        resultado = respuesta.json()
        if respuesta.status_code == 200 and "mensaje" in resultado:
            print(f"✅ {resultado['mensaje']}")
        else:
            print(f"❌ Error: {resultado.get('error', 'No se pudo crear el empleado')}")
    except ValueError:
        print("Los IDs (Empleado y Departamento) deben ser números enteros.")
    except requests.exceptions.ConnectionError:
        print("❌ Error de conexión con la API.")


def menu_modificar_empleado():
    print("\n--- MODIFICAR EMPLEADO ---")
    try:
        id_emp = int(input("Introduce el ID del empleado a modificar: "))
        nuevo_nombre = input("Nuevo nombre: ")
        nuevo_apellido = input("Nuevo apellido: ")
        nuevo_id_dep = int(input("Nuevo ID de Departamento: "))

        datos = {
            "id_empleado": id_emp,
            "nombre": nuevo_nombre,
            "apellido": nuevo_apellido,
            "id_departamento": nuevo_id_dep
        }

        respuesta = requests.put(f"{URL_EMPLEADOS}/{id_emp}", json=datos)
        resultado = respuesta.json()
        if respuesta.status_code == 200 and "mensaje" in resultado:
            print(f"🔄 {resultado['mensaje']}")
        else:
            print(f"❌ Error: {resultado.get('error', 'No se pudo modificar')}")
    except ValueError:
        print("Los IDs deben ser números enteros.")
    except requests.exceptions.ConnectionError:
        print("❌ Error de conexión.")


def menu_eliminar_empleado():
    print("\n--- ELIMINAR EMPLEADO ---")
    try:
        id_emp = int(input("Introduce el ID del empleado a borrar: "))
        confirmar = input(f"¿Seguro que deseas eliminar al empleado {id_emp}? (s/n): ")
        if confirmar.lower() != 's':
            print("Operación cancelada.")
            return

        respuesta = requests.delete(f"{URL_EMPLEADOS}/{id_emp}")
        resultado = respuesta.json()
        if respuesta.status_code == 200 and "mensaje" in resultado:
            print(f"🗑️ {resultado['mensaje']}")
        else:
            print(f"❌ Error: {resultado.get('error', 'No se pudo eliminar')}")
    except ValueError:
        print("El ID debe ser un número entero.")
    except requests.exceptions.ConnectionError:
        print("❌ Error de conexión.")


# ==========================================
# BUCLE PRINCIPAL
# ==========================================

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-9): ")

        if opcion == "1":
            menu_listar_clientes()
        elif opcion == "2":
            menu_añadir_cliente()
        elif opcion == "3":
            menu_modificar_cliente()
        elif opcion == "4":
            menu_eliminar_cliente()
        elif opcion == "5":
            menu_listar_empleados()
        elif opcion == "6":
            menu_añadir_empleado()
        elif opcion == "7":
            menu_modificar_empleado()
        elif opcion == "8":
            menu_eliminar_empleado()
        elif opcion == "9":
            print("\n¡Gracias por usar el sistema ERP! Cerrando cliente...")
            sys.exit()
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()