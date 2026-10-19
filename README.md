# Monorepo LINEAS-ENFASIS - Entrega 2

Este proyecto corresponde a la segunda entrega del proyecto **LÍNEAS DE ENFASIS** para la materia **Gestión de la Configuración** de la Universidad de Medellín. Contiene la arquitectura containerizada del sistema con Frontend (Nginx), Backend (FastAPI con Swagger UI) y Base de Datos (PostgreSQL).

---

## 🛠️ Tecnologías y Versiones

* **Frontend:** Nginx 1.31.7 (Puerto 80)
* **Backend:** Python 3.10-slim + FastAPI 0.110.0 + Uvicorn (Puerto 3000)
* **Base de Datos:** PostgreSQL 15 (Puerto 5432)
* **Orquestación:** Docker Compose v2+
* **Pruebas:** Playwright (Node.js) / Pytest

---

## 📋 Historias de Usuario y Responsables

| ID | Historia de Usuario | Responsable | Criterio de Aceptación |
| :--- | :--- | :--- | :--- |
| **HU01** | **Contenedorización e Infraestructura:** Como desarrollador, quiero desplegar los servicios mediante Docker Compose para garantizar entornos homogéneos. | M. Polanía | Servicios de Frontend, Backend y PostgreSQL corriendo en contenedores aislados comunicados mediante una red Docker. |
| **HU02** | **Documentación de API (Swagger):** Como integrador, quiero visualizar e interactuar con la documentación OpenAPI/Swagger en `/docs` para probar los endpoints. | M. Polanía | Acceso a `/docs` funcional que expone los endpoints GET/POST de la aplicación. |
| **HU03** | **Pruebas Automatizadas:** Como evaluador, quiero contar con pruebas e2e/unitarias para validar el flujo crítico del sistema. | M. Polanía | Ejecución de scripts de prueba que verifiquen la disponibilidad y respuestas HTTP del frontend y backend. |

---

## 🐳 Imágenes en DockerHub

Las imágenes de los servicios están disponibles públicamente en:

* **Backend:** `mpolania331/lineas-backend:latest`
* **Frontend:** `mpolania331/lineas-frontend:latest`

---

## ⚙️ Instrucciones de Despliegue Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Mjpolania331/lineas_enfasis.git](https://github.com/Mjpolania331/lineas_enfasis.git)
   cd lineas_enfasis
   