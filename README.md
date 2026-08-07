# 🦸‍♂️ Marvel Universe & ERP API System

## 📝 Descripción

Este proyecto es un sistema **Full-Stack** desarrollado para gestionar y visualizar información sobre el universo Marvel (junto con un módulo ERP corporativo).

El núcleo del sistema es una **API REST construida con FastAPI** que interactúa con una base de datos **Oracle**.

Los usuarios pueden consumir y manipular los datos de dos maneras:

* A través de un **buscador web interactivo**.
* Mediante un **cliente CLI por consola** que realiza peticiones HTTP.

---

## 🛠️ Tecnologías Utilizadas

### Backend & API

* **Python 3.10+**
* **FastAPI**
* **Uvicorn** (Servidor ASGI)
* **Pydantic** (Validación de datos)
* **requests** (Cliente HTTP)

### Base de datos

* **Oracle Database**
* **SQL**
* **oracledb** (driver de conexión)
* **python-dotenv** (gestión de variables de entorno)

### Frontend

* **HTML5**
* **CSS3**
* **JavaScript (Vanilla)**
* **Fetch API** para el consumo asíncrono de la API

---

## 🚀 Características principales

### Arquitectura Desacoplada (Frontend/Backend)

Separación total de responsabilidades.

* El backend sirve datos a través de **endpoints JSON**.
* El frontend se encarga exclusivamente de la **presentación visual**.

### API RESTful Documentada

Servidor robusto y rápido gracias a **FastAPI**, que incluye documentación automática e interactiva mediante **Swagger UI** para probar las rutas:

* `GET`
* `POST`
* `PUT`
* `DELETE`

### Aplicación Web Interactiva

Buscador en el navegador que consume la **API de Marvel en tiempo real**.

Incluye:

* Barra de búsqueda por nombre.
* Filtros por bando:

  * Héroe
  * Villano
  * Anti-héroe
* Opciones de ordenación dinámica:

  * Alfabética
  * Por nivel de poder

### Cliente CLI Evolucionado

El menú por consola original ha sido refactorizado.

Ahora funciona como un **cliente externo** que interactúa con la API mediante peticiones HTTP, mostrando:

* Códigos de estado.
* Encabezados de red.

### Inserción Masiva y Automatización

Scripts especializados para:

* Despliegue de tablas (DDL).
* Poblado de datos (Seed).
* Inserción mediante `executemany`.

Preparando el entorno de pruebas rápidamente.

### Gestión Segura y Consultas Parametrizadas

* Archivo `.env` ignorado en el repositorio para proteger credenciales.
* Uso exclusivo de variables vinculadas (**bind variables**, `:1`) para prevenir inyecciones SQL.

---

## 🏗️ Estructura del Proyecto

El repositorio está dividido en dos grandes bloques para separar el cliente visual del servidor:

```text
frontend/
├── index.html
├── style.css
└── script.js
```

Contiene la interfaz de usuario web y los archivos del buscador interactivo de Marvel.

```text
backend/
├── api.py
├── main.py
├── marvel/
│   └── db_marvel.py
└── erp/
    └── db_erp.py
```

### `frontend/`

Contiene la interfaz de usuario web.

* `index.html`
* `style.css`
* `script.js`

Archivos del buscador interactivo de Marvel.

### `backend/`

Contiene la lógica del servidor y la base de datos.

#### `api.py`

Punto de entrada principal de la API REST (**FastAPI**).

Enruta las peticiones web hacia la base de datos.

#### `main.py`

Cliente de consola interactivo (**CLI**) que consume los endpoints de la API.

#### `marvel/`

Módulo del multiverso Marvel.

* `db_marvel.py` para lógica CRUD.
* Scripts de poblado.
* Scripts de creación de tablas.

#### `erp/`

Módulo corporativo heredado.

* `db_erp.py` para la gestión independiente de clientes y empleados.

---

# 💻 Ejecución en local

Para ejecutar este proyecto en local, necesitarás:

1. **Python 3.10 o superior** instalado en tu sistema.
2. Acceso a una instancia de **Oracle Database** configurada y activa.
3. Instalar las dependencias necesarias mediante la consola:

```bash
pip install oracledb python-dotenv
```

---

## ⚙️ Configuración y Ejecución

### 1. Descargar o clonar el repositorio

Descarga o clona este repositorio en tu máquina local.

### 2. Configurar las variables de entorno

Crea un archivo llamado **exactamente** `.env` en la misma carpeta que tu código y añade tus credenciales de acceso a Oracle con el siguiente formato:

```env
DB_USUARIO=tu_usuario
DB_CONTRASENA=tu_contraseña
DB_HOST=tu_dsn_o_host
```

### 3. Paso 1 — Instalación

Ejecuta el script de configuración para crear la tabla en la base de datos:

```bash
python setup_db.py
```

### 4. Paso 2 — Poblar la base de datos

**Opcional:** si quieres empezar con **100 personajes** ya cargados, como Iron Man, Thanos, Lobezno, etc., ejecuta:

```bash
python poblar_marvel.py
```

### 5. Paso 3 — Ejecución

Inicia la aplicación principal para abrir el menú interactivo:

```bash
python marvel.py
```

---

## 👨‍💻 Autor

**Daniel Avilés Martínez** - Desarrollador de software

[GitHub: nissoid](https://github.com/nissoid)
