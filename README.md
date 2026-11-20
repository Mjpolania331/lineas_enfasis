# Sistema de Gestión de Líneas de Énfasis - Universidad de Medellín

Aplicación web full-stack contenerizada y orquestada en Kubernetes (Minikube) con integración y despliegue continuo (CI/CD) mediante GitHub Actions y DockerHub.

## Arquitectura del Sistema
+-------------------+      HTTP :80       +----------------------+     Proxy /api/     +-----------------------+
|  Navegador Web    | ------------------> |   Frontend (Nginx)   | ------------------> |   Backend (FastAPI)   |
| (Estudiante/Coord)|                     |  NodePort :30080     |                     |  ClusterIP :3000      |
+-------------------+                     +----------------------+                     +-----------------------+
                                                                                                  |
                                                                                         SQLAlchemy (TCP :5432)
                                                                                                  v
+-------------------+    GitHub Actions   +----------------------+     Pull Image      +-----------------------+
|  GitHub (main)    | ------------------> |      DockerHub       | ------------------> | PostgreSQL 15 + PVC   |
|  Código + k8s/    |   pytest + build    |  :latest (web/api)   |                     |  Almacenamiento 1Gi   |
+-------------------+                     +----------------------+                     +-----------------------+
- **Frontend (`frontend/`):** Portal web institucional servido con **Nginx** (puerto 80, expuesto vía `NodePort 30080`), con proxy inverso `/api/` hacia el backend.
- **Backend (`backend/`):** API REST desarrollada con **FastAPI** y **SQLAlchemy** (puerto 3000) con endpoints `/cursos`, `/inscripciones` y `/health`.
- **Base de Datos (`k8s/postgres.yaml`):** **PostgreSQL 15** con almacenamiento persistente (`PersistentVolumeClaim` de 1Gi) y gestión de credenciales mediante `Secret` y `ConfigMap`.
- **CI/CD (`.github/workflows/ci.yml`):** Ejecución automática de pruebas unitarias (`pytest`) y publicación de imágenes en DockerHub (`mpolania331/lineas-backend:latest` y `mpolania331/lineas-frontend:latest`).

## Despliegue en Kubernetes (Minikube)

1. Iniciar el clúster local:
   ```bash
   minikube start
   ```
2. Aplicar los manifiestos de infraestructura:
   ```bash
   kubectl apply -f k8s/
   ```
3. Verificar el estado de los pods, servicios y almacenamiento:
   ```bash
   kubectl get pods,svc,pvc
   ```
4. Abrir el portal web en el navegador:
   ```bash
   minikube service frontend-service
   ```

## Credenciales de Prueba
- **Estudiante:** `sistemas@soyudemedellin.edu.co` / Contraseña: `123`
- **Profesor:** `profesor.sistemas@udemedellin.edu.co` / Contraseña: `123`
- **Coordinador:** `coordinador@udem.edu.co` / Contraseña: `123`
   
