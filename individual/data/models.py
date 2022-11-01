from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float

from .database import Base, engine


class Simulacion(Base):
    __tablename__ = 'simulaciones'
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=datetime.now())
    clientes_atendidos = Column(Integer)
    meta_clientes =  Column(Integer)
    cantidad_estudiantes =  Column(Integer)
    clientes_g1 =  Column(Integer)
    clientes_g2 =  Column(Integer)
    estudiantes_g1 =  Column(Integer)
    estudiantes_g2 =  Column(Integer)
    estudiantes = relationship('Estudiante', back_populates='simulacion')


class Estudiante(Base):
    __tablename__ = 'estudiantes'
    id = Column(Integer, primary_key=True, index=True)
    tramites_realizados = Column(Integer)
    tiempo_promedio_por_tramite = Column(Float)
    horas_cumplidas = Column(Float)
    duracion_pasantia = Column(Float)
    simulacion_id = Column(Integer, ForeignKey('simulaciones.id'))
    simulacion = relationship('Simulacion', back_populates='estudiantes')
    tramites = relationship('Tramite', back_populates='estudiante')

    def __repr__(self):
        return "<Estudiante(Horas cumplidas='%d')>" % self.horas_cumplidas


class Tramite(Base):
    __tablename__ = 'tramites'
    id = Column(Integer, primary_key=True, index=True)
    duracion_tramite = Column(Float)
    tramite_seleccionado = Column(String)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'))
    estudiante = relationship('Estudiante', back_populates='tramites')

    def __repr__(self):
        return "<Tramite(Tramite='%s')>" % self.tramite_seleccionado


# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
