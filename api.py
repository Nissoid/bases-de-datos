from fastapi import FastAPI
from pydantic import BaseModel
# Añadimos la importación de la nueva función
from herramientas_db import obtener_lista_clientes_api, crear_cliente_api

app = FastAPI(title="Mi ERP Corporativo API")


class ClienteNuevo(BaseModel):
    id_cliente: int
    nombre: str
    email: str


@app.get("/api/clientes")
def ruta_obtener_clientes():
    resultado = obtener_lista_clientes_api()
    return resultado


# Actualizamos la ruta POST
@app.post("/api/clientes")
def ruta_crear_cliente(cliente: ClienteNuevo):
    # 1. FastAPI y Pydantic ya han validado que los datos son correctos
    # 2. Se los enviamos a nuestra función de Oracle
    exito = crear_cliente_api(cliente.id_cliente, cliente.nombre, cliente.email)

    # 3. Respondemos a la web dependiendo de lo que haya pasado en Oracle
    if exito:
        return {"mensaje": f"¡Éxito! El cliente '{cliente.nombre}' ha sido guardado en la base de datos."}
    else:
        return {"error": "No se pudo guardar. Es posible que el ID ya exista en Oracle."}