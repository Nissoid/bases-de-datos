# 🦸‍♂️ Marvel Universe Database Manager

## 📝 Descripción

Este proyecto es un sistema backend en **Python** diseñado para gestionar y almacenar información sobre los personajes del universo Marvel. Interactúa con una base de datos **Oracle** y ofrece un menú interactivo por consola (CLI) para realizar operaciones CRUD (Crear, Leer, Eliminar) junto con la configuración inicial de la estructura de la base de datos de manera eficiente y segura.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+ (Uso de `match-case` para la lógica de control)
* **Base de Datos:** Oracle Database (SQL)
* **Librerías principales:** `oracledb` (driver de conexión) y `python-dotenv` (gestión de variables de entorno).

## 🚀 Características Principales

* **Todo en Uno:** Un único archivo principal que contiene tanto la gestión del CRUD como el script de instalación y creación de tablas en la base de datos (Opción 0 del menú).
* **Menú Interactivo CLI:** Interfaz por consola intuitiva que permite listar, añadir y eliminar personajes del universo Marvel de forma rápida.
* **Gestión Segura de Credenciales:** Implementación de un archivo `.env` para proteger los datos de acceso a Oracle, evitando exponer información sensible en el código fuente.
* **Consultas Seguras:** Uso de variables vinculadas (*bind variables*) en las sentencias SQL y mapeo mediante diccionarios en Python para evitar vulnerabilidades de inyección SQL.

## 📋 Requisitos Previos

Para ejecutar este proyecto en local, necesitarás:

1. Python 3.10 o superior instalado en tu sistema.
2. Acceso a una instancia de Oracle Database configurada y activa.
3. Instalar las dependencias necesarias mediante la consola:
   ```bash
   pip install oracledb python-dotenv
   ```

## ⚙️ Configuración y Ejecución

1. Descarga o clona este repositorio en tu máquina local.
2. Crea un archivo llamado **exactamente** `.env` en la misma carpeta que tu código y añade tus credenciales de acceso a Oracle con el siguiente formato:
   ```env
   DB_USUARIO=tu_usuario
   DB_CONTRASENA=tu_contraseña
   DB_HOST=tu_dsn_o_host
   ```
3. Ejecuta el archivo principal para iniciar el programa:
   ```bash
   python marvel.py
   ```
4. Selecciona la **Opción 0** del menú la primera vez que ejecutes el programa. Esto creará automáticamente la tabla necesaria (`marvel_personajes`) en tu base de datos Oracle para empezar a trabajar.

## 👨‍💻 Autor

**Daniel Avilés Martínez** - Desarrollador de software  
[GitHub: nissoid](https://github.com/nissoid)
