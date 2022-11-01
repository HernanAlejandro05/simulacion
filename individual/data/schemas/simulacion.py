from datetime import datetime

from pydantic import BaseModel
from typing import List

from data.schemas.estudiante import EstudianteBase


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
    estudiantes: List[EstudianteBase] = []

    class Config:
        orm_mode = True
