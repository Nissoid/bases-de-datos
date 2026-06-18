import oracledb
import os
from dotenv import load_dotenv
from tabulate import tabulate

# 1. Cargamos el archivo .env una sola vez al arrancar el programa
load_dotenv()

# 2. Guardamos las credenciales en variables para usarlas en todo el archivo
USUARIO = os.getenv("DB_USUARIO")
CONTRASENA = os.getenv("DB_CONTRASENA")
DSN = os.getenv("DB_HOST")


# ==========================================
# MÓDULO DE CLIENTES
# ==========================================

def imprimir_clientes():
    # Ahora usamos las variables en lugar del texto fijo
    conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
    cursor = conexion.cursor()

    cursor.execute("SELECT id_cliente, nombre, email FROM clientes")
    datos = cursor.fetchall()

    cabeceras = ["ID CLIENTE", "EMPRESA", "CORREO ELECTRÓNICO"]
    print(tabulate(datos, headers=cabeceras, tablefmt="grid"))

    cursor.close()
    conexion.close()

def crear_cliente():
    print("\n--- NUEVO CLIENTE ---")
    try:
        id_cli = int(input("ID del cliente (ej. 105): "))
        nombre_cli = input("Nombre de la empresa: ")
        email_cli = input("Correo electrónico: ")
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return

    conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
    cursor = conexion.cursor()

    try:
        sql = "INSERT INTO clientes (id_cliente, nombre, email) VALUES (:1, :2, :3)"
        cursor.execute(sql, [id_cli, nombre_cli, email_cli])
        conexion.commit()
        print(f"¡Éxito! El cliente '{nombre_cli}' ha sido guardado.")

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Error al guardar en BD: {error.message}")

    finally:
        cursor.close()
        conexion.close()

def modificar_cliente():
    print("\n--- MODIFICAR CLIENTE ---")
    try:
        id_cli = int(input("Introduce el ID del cliente que quieres actualizar: "))
        nuevo_nombre = input("Nuevo nombre de la empresa: ")
        nuevo_email = input("Nuevo correo electrónico: ")
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return

    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        sql = "UPDATE clientes SET nombre = :1, email = :2 WHERE id_cliente = :3"
        cursor.execute(sql, [nuevo_nombre, nuevo_email, id_cli])

        if cursor.rowcount == 0:
            print(f"[!] Aviso: No se encontró ningún cliente con el ID {id_cli}.")
        else:
            conexion.commit()
            print(f"¡Éxito! Los datos del cliente {id_cli} han sido actualizados.")

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"\n[!] Error al actualizar: {error.message}")

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()


# ==========================================
# MÓDULO DE EMPLEADOS
# ==========================================

def imprimir_empleados():
    conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
    cursor = conexion.cursor()

    cursor.execute("SELECT id_empleado, nombre, apellido, id_departamento FROM empleados")
    datos = cursor.fetchall()

    cabeceras = ["ID_EMPLEADO", "NOMBRE", "APELLIDOS", "ID_DEPARTAMENTO"]
    print(tabulate(datos, headers=cabeceras, tablefmt="grid"))

    cursor.close()
    conexion.close()

def crear_empleado():
    print("\n--- NUEVO EMPLEADO ---")
    try:
        id_emp = int(input("ID del Empleado (ej. 3): "))
        nombre_emp = input("Nombre del empleado: ")
        apellido_emp = input("Apellido del empleado: ")
        id_dept = input("ID del departamento (10-Ciberseguridad o 20-Desarrollo web): ")
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return

    conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
    cursor = conexion.cursor()

    try:
        sql = "INSERT INTO empleados (id_empleado, nombre, apellido, id_departamento) VALUES (:1, :2, :3, :4)"
        cursor.execute(sql, [id_emp, nombre_emp, apellido_emp, id_dept])
        conexion.commit()
        print(f"¡Éxito! El empleado '{nombre_emp} {apellido_emp}' ha sido guardado.")

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Error al guardar en BD: {error.message}")

    finally:
        cursor.close()
        conexion.close()

def modificar_empleado():
    print("\n--- MODIFICAR EMPLEADO ---")
    try:
        id_emp = int(input("ID del Empleado (ej. 3): "))
        nombre_emp = input("Nombre del empleado: ")
        apellido_emp = input("Apellido del empleado: ")
        id_dept = input("ID del departamento (10-Ciberseguridad o 20-Desarrollo web): ")
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return

    conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
    cursor = conexion.cursor()

    try:
        sql = "UPDATE empleados SET nombre = :1, apellido = :2, id_departamento = :3 WHERE id_empleado = :4"
        cursor.execute(sql, [nombre_emp, apellido_emp, id_dept, id_emp])

        if cursor.rowcount == 0:
            print(f"[!] Aviso: No se encontró ningún empleado con el ID {id_emp}.")
        else:
            conexion.commit()
            print(f"¡Éxito! El empleado '{nombre_emp} {apellido_emp}' ha sido actualizado.")

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Error al guardar en BD: {error.message}")

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()


def obtener_lista_clientes_api():
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        cursor.execute("SELECT id_cliente, nombre, email FROM clientes ORDER BY id_cliente")
        datos = cursor.fetchall()

        # Transformamos las tuplas raras de Oracle en una lista de diccionarios limpios
        lista_clientes = []
        for fila in datos:
            lista_clientes.append({
                "id_cliente": fila[0],
                "nombre": fila[1],
                "email": fila[2]
            })

        return lista_clientes  # ¡IMPORTANTE! Devolvemos los datos, no los imprimimos

    except oracledb.DatabaseError as e:
        return {"error": "No se pudo conectar a la base de datos"}
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()


def crear_cliente_api(id_cli, nombre_cli, email_cli):
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        sql = "INSERT INTO clientes (id_cliente, nombre, email) VALUES (:1, :2, :3)"
        cursor.execute(sql, [id_cli, nombre_cli, email_cli])
        conexion.commit()

        return True  # Indicamos que todo ha ido perfecto

    except oracledb.DatabaseError as e:
        # Si falla (ej. el ID ya existe), lo devolvemos para que la API se entere
        return False

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()

def obtener_lista_empleados_api():
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        cursor.execute("SELECT id_empleado, nombre,apellido, id_departamento FROM empleados ORDER BY id_empleado")
        datos = cursor.fetchall()

        # Transformamos las tuplas raras de Oracle en una lista de diccionarios limpios
        lista_empleados = []
        for fila in datos:
            lista_empleados.append({
                "id_empleado": fila[0],
                "nombre": fila[1],
                "apellido": fila[2],
                "id_departamento": fila[3]
            })

        return lista_empleados  # ¡IMPORTANTE! Devolvemos los datos, no los imprimimos

    except oracledb.DatabaseError as e:
        return {"error": "No se pudo conectar a la base de datos"}
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()

def crear_empleado_api(id_emp, nombre_emp, apellido_emp, id_dep):
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        sql = "INSERT INTO empleados (id_empleado, nombre, apellido, id_departamento) VALUES (:1, :2, :3, :4)"
        cursor.execute(sql, [id_emp, nombre_emp, apellido_emp, id_dep])
        conexion.commit()

        return True  # Indicamos que todo ha ido perfecto

    except oracledb.DatabaseError as e:
        # Si falla (ej. el ID ya existe), lo devolvemos para que la API se entere
        return False

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()


def modificar_cliente_api(id_cli, nuevo_nombre, nuevo_email):
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        sql = "UPDATE clientes SET nombre = :1, email = :2 WHERE id_cliente = :3"
        cursor.execute(sql, [nuevo_nombre, nuevo_email, id_cli])

        # Comprobamos si realmente se ha modificado alguien
        if cursor.rowcount == 0:
            return False  # El cliente no existía

        conexion.commit()
        return True

    except oracledb.DatabaseError:
        return False
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()


def eliminar_cliente_api(id_cli):
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        # Peligro: El WHERE es vital para no borrar toda la tabla
        sql = "DELETE FROM clientes WHERE id_cliente = :1"
        cursor.execute(sql, [id_cli])

        if cursor.rowcount == 0:
            return False

        conexion.commit()
        return True

    except oracledb.DatabaseError:
        return False
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()

def modificar_empleado_api(id_emp, nuevo_nombre, nuevo_apellido, nuevo_id_dep):
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        # Actualizamos nombre, apellido e id_departamento
        sql = "UPDATE empleados SET nombre = :1, apellido = :2, id_departamento = :3 WHERE id_empleado = :4"
        cursor.execute(sql, [nuevo_nombre, nuevo_apellido, nuevo_id_dep, id_emp])

        # Comprobamos si realmente se ha modificado alguien
        if cursor.rowcount == 0:
            return False  # El empleado no existía

        conexion.commit()
        return True

    except oracledb.DatabaseError:
        return False
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()

def eliminar_empleado_api(id_emp):
    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        # Corregido: Ahora apunta a la tabla empleados y usa id_empleado
        sql = "DELETE FROM empleados WHERE id_empleado = :1"
        cursor.execute(sql, [id_emp])

        if cursor.rowcount == 0:
            return False

        conexion.commit()
        return True

    except oracledb.DatabaseError:
        return False
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()