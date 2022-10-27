from datetime import datetime

from pydantic import BaseModel
from typing import Optional, List


class EsquemaSimulacion(BaseModel):
    fecha: datetime


class EsquemaEstudiante(BaseModel):
    simulacion_id: int
    horas_cumplidas: float
    tramites_realizados: int
    tiempo_promedio_por_tramite: float

    class Config:
        orm_mode = True


# class EstudianteTramites(Estudiante):
#     traamites: List[Estudiante] = [None]

#     class Config:
#         orm_mode = True


class EsquemaTramite(BaseModel):
    estudiante_id: int
    duracion_tramite: float
    tramite_seleccionado: str

    class Config:
        orm_mode = True


# class TramiteEstudiante(Tramite):
#     estudiante: Optional[Estudiante] = None

#     class Config:
#         orm_mode = True
