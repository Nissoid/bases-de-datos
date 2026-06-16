# Sintaxis mágica: from [nombre_del_archivo_sin_el_py] import [nombre_de_la_funcion]
from herramientas_db import *
while True:
    opcion = input("\nElige una opción:"
               "\n1. Imprimir empleados"
               "\n2. Imprimir clientes"
               "\n3. Crear empleados"
               "\n4. Crear clientes"
               "\n5. Modificar empleados"
               "\n6. Modificar clientes"
               "\n7. Salir\n")

    match opcion:
        case "1":
            imprimir_empleados()

        case "2":
            imprimir_clientes()

        case "3":
            crear_empleado()

        case "4":
            crear_cliente()

        case "5":
            modificar_empleado()

        case "6":
            modificar_cliente()

        case "7":
            print("\nCerrando conexiones... ¡Hasta pronto!")
            break

        case _:
            print("\n[!] Opción no válida. Por favor, escribe un número del 1 al 7.")