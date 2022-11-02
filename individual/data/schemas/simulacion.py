from datetime import datetime

from pydantic import BaseModel
from typing import List

from data.schemas.estudiante import EstudianteLectura


class SimulacionBase(BaseModel):
    fecha: datetime
    meta_clientes: int
    clientes_g1: int
    clientes_g2: int
    estudiantes_g1: int
    estudiantes_g2: int
    clientes_atendidos: int
    cantidad_estudiantes: int


class Simulacion(SimulacionBase):
    pass


class SimulacionEstudiantes(Simulacion):
    estudiantes: List[EstudianteLectura] = []

    class Config:
        orm_mode = True
