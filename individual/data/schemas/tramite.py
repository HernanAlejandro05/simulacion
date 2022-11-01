from pydantic import BaseModel
from typing import Optional, List


class TramiteBase(BaseModel):
    duracion_tramite: float
    tramite_seleccionado: str

    class Config:
        orm_mode = True


class Tramite(TramiteBase):
    estudiante_id: int


# class TramiteEstudiante(Tramite):
#     estudiante: Optional[Estudiante] = None

#     class Config:
#         orm_mode = True
