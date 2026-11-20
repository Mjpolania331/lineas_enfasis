import os
from contextlib import asynccontextmanager
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "lineas_enfasis")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

if DB_HOST:
    DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
else:
    DATABASE_URL = "sqlite:///./local_test.db"
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class CursoDB(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)


class InscripcionDB(Base):
    __tablename__ = "inscripciones"
    id = Column(Integer, primary_key=True, index=True)
    estudiante = Column(String, nullable=False)
    codigo = Column(String, nullable=False)
    linea_enfasis = Column(String, nullable=False)


class InscripcionCreate(BaseModel):
    estudiante: str
    codigo: str
    linea_enfasis: str
    curso_id: Optional[int] = None


def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(CursoDB).count() == 0:
            iniciales = [
                CursoDB(
                    nombre="Desarrollo de Software",
                    descripcion="Diseña, construye y despliega soluciones web, móviles y empresariales con prácticas modernas de ingeniería."
                ),
                CursoDB(
                    nombre="Analítica de Datos",
                    descripcion="Convierte datos académicos y organizacionales en visualizaciones, modelos predictivos y decisiones accionables."
                ),
                CursoDB(
                    nombre="Ciberseguridad",
                    descripcion="Protege infraestructuras, aplicaciones y datos mediante análisis de riesgos, pruebas y controles de seguridad."
                ),
            ]
            db.add_all(iniciales)
            db.commit()
    finally:
        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="API LINEAS-ENFASIS",
    description="Backend para el sistema de inscripción de cursos - Universidad de Medellín",
    version="2.0.0",
    lifespan=lifespan,
)


@app.get("/")
def read_root():
    return {"mensaje": "Backend funcionando correctamente con FastAPI"}


@app.get("/health")
def health_check():
    return {"status": "ok", "database": "postgresql" if DB_HOST else "sqlite"}


@app.get("/cursos")
def get_cursos():
    db = SessionLocal()
    try:
        cursos = db.query(CursoDB).all()
        return [{"id": c.id, "nombre": c.nombre, "descripcion": c.descripcion} for c in cursos]
    finally:
        db.close()


@app.get("/inscripciones")
def get_inscripciones():
    db = SessionLocal()
    try:
        registros = db.query(InscripcionDB).all()
        return [
            {
                "id": r.id,
                "estudiante": r.estudiante,
                "codigo": r.codigo,
                "linea_enfasis": r.linea_enfasis,
            }
            for r in registros
        ]
    finally:
        db.close()


@app.post("/inscripciones", status_code=201)
def crear_inscripcion(payload: InscripcionCreate):
    db = SessionLocal()
    try:
        nueva = InscripcionDB(
            estudiante=payload.estudiante,
            codigo=payload.codigo,
            linea_enfasis=payload.linea_enfasis,
        )
        db.add(nueva)
        db.commit()
        db.refresh(nueva)
        return {
            "id": nueva.id,
            "estudiante": nueva.estudiante,
            "codigo": nueva.codigo,
            "linea_enfasis": nueva.linea_enfasis,
        }
    finally:
        db.close()
