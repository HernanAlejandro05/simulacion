from datetime import datetime

from pydantic import BaseModel


class Simulacion(BaseModel):
    fecha: datetime
    meta_clientes: int
    clientes_g1: int
    clientes_g2: int
    estudiantes_g1: int
    estudiantes_g2: int
    clientes_atendidos: int
    cantidad_estudiantes: int
