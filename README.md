# 🧵 Data Cloth - Backend

**Data Cloth** es una aplicación web diseñada para gestionar el inventario de ropa de forma eficiente. Este repositorio contiene el backend desarrollado con **Python**, utilizando el microframework **Flask** y la ORM **SQLAlchemy** con una base de datos **PostgreSQL**.

## 🚀 Tecnologías

- **Python**
- **Flask**
- **SQLAlchemy**
- **PostgreSQL**
- **Pipenv** para gestión de entornos y dependencias

## 📦 Funcionalidades

- CRUD de productos de ropa (crear, leer, actualizar, eliminar)
- Gestión de categorías de ropa
- Relación entre prendas y categorías
- API RESTful

## ⚙️ Instalación y ejecución

```bash
git clone https://github.com/nath1710/Datacloth-backend.git

pipenv install flask-cors

pipenv install flask-sqlalchemy

pipenv install flask

pipenv shell

export FLASK_APP=run.py

flask run

```
# 🗃️ Endpoints Principales

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/products` | Obtener todos los productos |
| POST | `/products` | Crear un nuevo producto |
| PUT | `/products/<id>` | Actualizar un producto |
| DELETE | `/products/<id>` | Eliminar un producto |


