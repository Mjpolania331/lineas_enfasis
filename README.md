# Monorepo LINEAS-ENFASIS - Entrega 2

Este proyecto corresponde a la segunda entrega de la materia **LÍNEAS DE ENFASIS** de la Universidad de Medellín. Contiene la arquitectura containerizada del sistema con Frontend (Nginx), Backend (FastAPI con Swagger UI) y Base de Datos (PostgreSQL).

---

## 🚀 Arquitectura del Proyecto

El repositorio está organizado en un monorepo con la siguiente estructura:

* **Frontend:** Servidor web Nginx (Puerto 80).
* **Backend:** API REST construida con FastAPI en Python (Puerto 3000) con documentación automática Swagger (`/docs`).
* **Base de Datos:** PostgreSQL 15 (Puerto 5432).
* **Orquestación:** Docker Compose.

---

## 📋 Historias de Usuario

* **HU01 - Contenedorización e Infraestructura:** Como desarrollador, quiero desplegar los servicios de frontend, backend y base de datos mediante Docker Compose para garantizar entornos homogéneos y portables.
* **HU02 - Documentación de API (Swagger):** Como integrador o evaluador, quiero visualizar e interactuar con la documentación OpenAPI/Swagger en la ruta `/docs` del backend para probar los endpoints de la aplicación.
* **HU03 - Publicación de imágenes:** Como administrador de despliegue, quiero disponer de las imágenes públicas en DockerHub para descargar e instanciar los servicios en cualquier entorno sin reconstruir el código base.

---

## 🐳 Imágenes en DockerHub

Las imágenes de los servicios están disponibles públicamente en los siguientes repositorios:

* **Backend:** `mpolania331/lineas-backend:latest`
* **Frontend:** `mpolania331/lineas-frontend:latest`

---

## ⚙️ Instrucciones de Despliegue Local

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/Mjpolania331/lineas_enfasis.git](https://github.com/Mjpolania331/lineas_enfasis.git)
   cd lineas_enfasis