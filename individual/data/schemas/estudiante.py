from pydantic import BaseModel
from typing import Optional, List


class Estudiante(BaseModel):
    simulacion_id: int
    horas_cumplidas: float
    duracion_pasantia: float
    tramites_realizados: int
    tiempo_promedio_por_tramite: float

    class Config:
        orm_mode = True

# class EstudianteTramites(Estudiante):
#     traamites: List[Estudiante] = [None]

#     class Config:
#         orm_mode = True
