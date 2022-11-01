from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.simulaciones import router as sim_router

from data.database import engine
import data.models as models

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

models.Base.metadata.create_all(bind=engine)

app.include_router(sim_router)
