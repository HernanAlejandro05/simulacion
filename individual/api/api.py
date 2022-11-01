from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.tramites import router as tra_router
from routes.estudiantes import router as est_router
from routes.simulaciones import router as sim_router

from data.database import engine
from data.models import estudiante, simulacion, tramite

app = FastAPI(
    title='API Simulación Oficina Tributaria UC',
    description='Esta es una API para consumir los datos generados a través de una simulación \
    que busca emular las prácticas profesionales de los estudiantes de la Universidad de Cuenca.',
    version='0.1.0'
)


origins = []


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crea las tablas e inicializa la basa de datos.
tramite.Base.metadata.create_all(bind=engine)
estudiante.Base.metadata.create_all(bind=engine)
simulacion.Base.metadata.create_all(bind=engine)

app.include_router(tra_router)
app.include_router(est_router)
app.include_router(sim_router)
