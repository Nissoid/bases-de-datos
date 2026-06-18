from fastapi import FastAPI
from pydantic import BaseModel
# Añadimos las importaciones correctas para empleados
from herramientas_db import (
    obtener_lista_clientes_api,
    obtener_lista_empleados_api,
    crear_empleado_api,
    crear_cliente_api,
    modificar_cliente_api,
    eliminar_cliente_api,
    modificar_empleado_api, # Añadida
    eliminar_empleado_api   # Añadida
)

app = FastAPI(title="Mi ERP Corporativo API")

class ClienteNuevo(BaseModel):
    id_cliente: int
    nombre: str
    email: str

class EmpleadoNuevo(BaseModel):
    id_empleado: int
    nombre: str
    apellido: str
    id_departamento: int

# ==========================================
# RUTAS DE CLIENTES
# ==========================================

@app.get("/api/clientes")
def ruta_obtener_clientes():
    return obtener_lista_clientes_api()

@app.post("/api/clientes")
def ruta_crear_cliente(cliente: ClienteNuevo):
    exito = crear_cliente_api(cliente.id_cliente, cliente.nombre, cliente.email)
    if exito:
        return {"mensaje": f"¡Éxito! El cliente '{cliente.nombre}' ha sido guardado."}
    else:
        return {"error": "No se pudo guardar. Es posible que el ID ya exista."}

@app.put("/api/clientes/{id_cliente}")
def ruta_modificar_cliente(id_cliente: int, cliente: ClienteNuevo):
    exito = modificar_cliente_api(id_cliente, cliente.nombre, cliente.email)
    if exito:
        return {"mensaje": f"Cliente {id_cliente} actualizado correctamente."}
    else:
        return {"error": "No se pudo actualizar. ¿Seguro que el ID existe?"}

@app.delete("/api/clientes/{id_cliente}")
def ruta_eliminar_cliente(id_cliente: int):
    exito = eliminar_cliente_api(id_cliente)
    if exito:
        return {"mensaje": f"Cliente {id_cliente} eliminado para siempre."}
    else:
        return {"error": "No se encontró ningún cliente con ese ID para borrar."}

# ==========================================
# RUTAS DE EMPLEADOS
# ==========================================

@app.get("/api/empleados")
def ruta_obtener_empleados():
    return obtener_lista_empleados_api()

@app.post("/api/empleados")
def ruta_crear_empleado(empleado: EmpleadoNuevo):
    exito = crear_empleado_api(empleado.id_empleado, empleado.nombre, empleado.apellido, empleado.id_departamento)
    if exito:
        return {"mensaje": f"¡Éxito! El empleado '{empleado.nombre} {empleado.apellido}' ha sido guardado."}
    else:
        return {"error": "No se pudo guardar. Es posible que el ID ya exista."}

@app.put("/api/empleados/{id_empleado}")
def ruta_modificar_empleado(id_empleado: int, empleado: EmpleadoNuevo):
    # Corregido: Ahora llama a modificar_empleado_api y pasa el id_departamento
    exito = modificar_empleado_api(id_empleado, empleado.nombre, empleado.apellido, empleado.id_departamento)
    if exito:
        return {"mensaje": f"Empleado {empleado.nombre} {empleado.apellido} actualizado correctamente."}
    else:
        return {"error": "No se pudo actualizar. ¿Seguro que el ID existe?"}

@app.delete("/api/empleados/{id_empleado}")
def ruta_eliminar_empleado(id_empleado: int):
    # Añadida la ruta DELETE que faltaba
    exito = eliminar_empleado_api(id_empleado)
    if exito:
        return {"mensaje": f"Empleado {id_empleado} eliminado de la base de datos."}
    else:
        return {"error": "No se encontró ningún empleado con ese ID."}