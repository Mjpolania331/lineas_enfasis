from fastapi import FastAPI

app = FastAPI(
    title="API LINEAS-ENFASIS",
    description="Backend para el sistema de inscripción de cursos - Universidad de Medellín",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"mensaje": "Backend funcionando correctamente con FastAPI"}

@app.get("/cursos")
def get_cursos():
    return [{"id": 1, "nombre": "Ingeniería de Software"}, {"id": 2, "nombre": "Inteligencia Artificial"}]