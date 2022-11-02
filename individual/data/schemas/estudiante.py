from pydantic import BaseModel
from typing import Optional, List

from data.schemas.tramite import TramiteLectura


class EstudianteBase(BaseModel):
    horas_cumplidas: float
    duracion_pasantia: float
    tramites_realizados: int
    tiempo_promedio_por_tramite: float

    class Config:
        orm_mode = True


class Estudiante(EstudianteBase):
    simulacion_id: int


class EstudianteLectura(EstudianteBase):
    id: int


class EstudianteTramites(EstudianteBase):
    tramites: List[TramiteLectura] = []

    class Config:
        orm_mode = True
