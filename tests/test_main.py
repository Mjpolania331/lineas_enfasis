import os
import sys
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))
from main import app


def test_backend_status():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"mensaje": "Backend funcionando correctamente con FastAPI"}


def test_get_cursos():
    with TestClient(app) as client:
        response = client.get("/cursos")
        assert response.status_code == 200
        cursos = response.json()
        assert len(cursos) >= 3
        assert cursos[0]["nombre"] == "Desarrollo de Software"


def test_crear_y_listar_inscripcion():
    with TestClient(app) as client:
        payload = {
            "estudiante": "María José Polanía",
            "codigo": "20261001",
            "linea_enfasis": "Desarrollo de Software",
        }
        post_res = client.post("/inscripciones", json=payload)
        assert post_res.status_code == 201
        assert post_res.json()["estudiante"] == "María José Polanía"

        get_res = client.get("/inscripciones")
        assert get_res.status_code == 200
        assert any(item["codigo"] == "20261001" for item in get_res.json())
