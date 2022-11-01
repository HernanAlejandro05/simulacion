from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Float

from ..database import Base, engine


class Tramite(Base):
    __tablename__ = 'tramites'
    id = Column(Integer, primary_key=True, index=True)
    duracion_tramite = Column(Float)
    tramite_seleccionado = Column(String)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'))
    estudiante = relationship('Estudiante', back_populates='tramites')

    def __repr__(self):
        return "<Tramite(Tramite='%s')>" % self.tramite_seleccionado
