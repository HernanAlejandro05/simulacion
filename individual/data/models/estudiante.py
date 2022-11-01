from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, Float

from ..database import Base, engine


class Estudiante(Base):
    __tablename__ = 'estudiantes'
    id = Column(Integer, primary_key=True, index=True)
    tramites_realizados = Column(Integer)
    tiempo_promedio_por_tramite = Column(Float)
    horas_cumplidas = Column(Float)
    duracion_pasantia = Column(Float)
    simulacion_id = Column(Integer, ForeignKey('simulaciones.id'))
    simulacion = relationship('simulacion.Simulacion',
                              back_populates='estudiantes')
    tramites = relationship('tramite.Tramite', back_populates='estudiante')

    def __repr__(self):
        return "<Estudiante(Horas cumplidas='%d')>" % self.horas_cumplidas
