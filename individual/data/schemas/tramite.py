from pydantic import BaseModel
from typing import Optional, List

class Tramite(BaseModel):
    estudiante_id: int
    duracion_tramite: float
    tramite_seleccionado: str

    class Config:
        orm_mode = True


# class TramiteEstudiante(Tramite):
#     estudiante: Optional[Estudiante] = None

#     class Config:
#         orm_mode = True
