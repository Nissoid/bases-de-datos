Descripción
Este proyecto es un sistema backend diseñado para gestionar y almacenar información sobre los personajes del universo Marvel. Utiliza Python para construir e interactuar con una API que procesa los datos de los personajes y los almacena de forma estructurada en una base de datos Oracle.

🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.x

Base de Datos: Oracle Database (SQL)

Librerías principales: requests (para el consumo y manejo de la API) y el driver de conexión para Oracle.

🚀 Características Principales
Gestión de Personajes: Creación, lectura, actualización y estructuración de los datos de Marvel mediante tablas relacionales.

Sistema de Filtrado: Lógica implementada para clasificar y filtrar resultados, permitiendo búsquedas específicas (por ejemplo, aislando a los personajes con el estatus de "héroe").

Integración de API: Uso de la librería requests de Python para automatizar el flujo de datos hacia la base de datos Oracle.

📋 Requisitos Previos
Para ejecutar este proyecto en local, necesitarás:

Python 3 instalado en tu sistema.

Acceso a una instancia de Oracle Database configurada.

Instalar las dependencias del proyecto:

Bash
pip install requests
# Añadir también el driver de Oracle que estés utilizando (ej. cx_Oracle o oracledb)
⚙️ Configuración y Ejecución
Clona este repositorio en tu máquina local.

Configura las credenciales de conexión a tu base de datos Oracle en el archivo correspondiente (asegúrate de que los datos de conexión no se suban al repositorio público).

Ejecuta el script principal para iniciar la carga y gestión de personajes:

Bash
python main.py
