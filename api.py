from fastapi import FastAPI
from pydantic import BaseModel

# --- IMPORTACIONES MARVEL ---
# Importamos la nueva función desde la carpeta "marvel."
from Marvel.db_marvel import obtener_personajes_api, crear_personaje_api, borrar_personaje_api

app = FastAPI(title="Universo Marvel")

# ==========================================
# MODELOS DE DATOS (Pydantic)
# ==========================================
class PersonajeMarvel(BaseModel):
    id_personaje: int
    alias_heroe: str
    nombre_real: str
    bando: str
    nivel_poder: int


# ==========================================
# RUTAS DEL UNIVERSO MARVEL
# ==========================================

@app.get("/api/marvel/personajes")
def ruta_obtener_personajes_marvel():
    """
    Devuelve la lista de personajes
    """
    resultado = obtener_personajes_api()
    return resultado

@app.post("/api/marvel/personajes")
def ruta_crear_personaje_marvel(personaje: PersonajeMarvel):
    """Añade un nuevo personaje a la base de datos"""
    exito = crear_personaje_api(
        personaje.id_personaje,
        personaje.alias_heroe,
        personaje.nombre_real,
        personaje.bando,
        personaje.nivel_poder
    )

    if exito:
        return {"mensaje": f"¡Éxito! {personaje.alias_heroe} ha sido registrado en el Multiverso."}
    else:
        return {"error": "No se pudo guardar. Es posible que el ID de personaje ya exista."}

@app.delete("/api/marvel/personajes/{id_personaje}")
def ruta_borrar_personaje_marvel(id_personaje: int):
    """Elimina un personaje de la base de datos"""
    exito = borrar_personaje_api(id_personaje)

    if exito:
        return {
            "mensaje": f"El personaje con ID {id_personaje} ha sido borrado de la existencia (¡Chasquido de Thanos!)."}
    else:
        return {"error": "No se encontró ningún personaje con ese ID."}