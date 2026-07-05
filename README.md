# 🦸‍♂️ Marvel Universe Database Manager

## 📝 Descripción

Este proyecto es un sistema backend desarrollado en **Python** diseñado para gestionar y almacenar información sobre los personajes del universo Marvel. Interactúa con una base de datos **Oracle** y ofrece un menú interactivo por consola (CLI) para realizar operaciones CRUD (Crear, Leer, Eliminar). Además, cuenta con scripts automatizados para el despliegue inicial de la estructura de datos y la inserción masiva de registros.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+ (Uso de `match-case` para la lógica del menú)
* **Base de Datos:** Oracle Database (SQL)
* **Librerías principales:** `oracledb` (driver de conexión) y `python-dotenv` (gestión de variables de entorno).

## 🚀 Características Principales

* **Arquitectura Modular:** Código dividido lógicamente entre la interfaz de usuario, las operaciones de base de datos, la configuración inicial y la carga de datos masiva.
* **Menú Interactivo CLI:** Interfaz por consola intuitiva que permite listar, añadir y eliminar personajes del universo Marvel.
* **Inserción Masiva (Seed):** Implementación de un script automatizado usando `executemany` para poblar la base de datos con 100 personajes predefinidos con estadísticas calculadas.
* **Gestión Segura de Credenciales:** Implementación de un archivo `.env` con validaciones de seguridad integradas para proteger los datos de acceso a Oracle.
* **Consultas Seguras:** Uso de variables vinculadas (*bind variables*) en las sentencias SQL y mapeo mediante diccionarios en Python para evitar vulnerabilidades.

## 🏗️ Estructura del Proyecto

El repositorio consta de cuatro archivos principales, cada uno con una responsabilidad única:

* `marvel.py`: Punto de entrada de la aplicación. Contiene el bucle principal y el menú interactivo para el usuario.
* `db_marvel.py`: Módulo que concentra la lógica de negocio y las funciones directas de conexión y operaciones CRUD hacia Oracle.
* `setup_db.py`: Script de instalación para crear la tabla `marvel_personajes`. Incluye escudos de seguridad antes de ejecutar comandos DDL.
* `poblar_marvel.py`: Script de inicialización de datos para insertar de golpe 100 personajes en la base de datos y preparar el entorno de pruebas.

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
3. **Paso 1 (Instalación):** Ejecuta el script de configuración para crear la tabla en la base de datos:
   ```bash
   python setup_db.py
   ```
4. **Paso 2 (Opcional - Poblar BD):** Si quieres empezar con 100 personajes ya cargados (como Iron Man, Thanos, Lobezno, etc.), ejecuta:
   ```bash
   python poblar_marvel.py
   ```
5. **Paso 3 (Ejecución):** Inicia la aplicación principal para abrir el menú interactivo:
   ```bash
   python marvel.py
   ```

## 👨‍💻 Autor

**Daniel Avilés Martínez** - Desarrollador de software  
[GitHub: nissoid](https://github.com/nissoid)
