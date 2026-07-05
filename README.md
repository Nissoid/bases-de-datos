# 🦸‍♂️ Marvel Universe Database & API

## 📝 Descripción

Este proyecto es un sistema backend diseñado para gestionar y almacenar información sobre los personajes del universo Marvel. Utiliza **Python** para interactuar con una API que procesa los datos de los personajes y los almacena de forma estructurada en una base de datos **Oracle**.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Base de Datos:** Oracle Database (SQL)
* **Librerías principales:** `requests` (para el consumo de la API) y el driver de conexión para Oracle.

## 🚀 Características Principales

* **Gestión de Personajes:** Creación, lectura y almacenamiento de los datos de Marvel mediante tablas relacionales estructuradas en SQL.
* **Sistema de Filtrado:** Lógica de clasificación implementada para filtrar los resultados de la base de datos (por ejemplo, aislando y consultando específicamente a los personajes con el estatus de "héroe").
* **Integración de API:** Uso de la librería `requests` de Python para automatizar el flujo y la obtención de datos hacia la base de datos Oracle.

## 📋 Requisitos Previos

Para ejecutar este proyecto en local, necesitarás:

1. Python 3 instalado en tu sistema.
2. Acceso a una instancia de Oracle Database configurada y activa.
3. Instalar las dependencias necesarias mediante consola:
   ```bash
   pip install requests
