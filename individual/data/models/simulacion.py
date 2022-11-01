from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, Integer

from ..database import Base, engine


class Simulacion(Base):
    __tablename__ = 'simulaciones'
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=datetime.now())
    clientes_atendidos = Column(Integer)
    meta_clientes = Column(Integer)
    cantidad_estudiantes = Column(Integer)
    clientes_g1 = Column(Integer)
    clientes_g2 = Column(Integer)
    estudiantes_g1 = Column(Integer)
    estudiantes_g2 = Column(Integer)
    estudiantes = relationship(
        'estudiante.Estudiante', back_populates='simulacion')
