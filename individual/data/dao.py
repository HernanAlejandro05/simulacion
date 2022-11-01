from .schemas import EsquemaEstudiante, EsquemaTramite, EsquemaSimulacion

from .database import SessionLocal
from .models import Simulacion, Estudiante, Tramite

db = SessionLocal()


def registrar_simulacion():
    db_simulacion = Simulacion(
        meta_clientes=0,
        clientes_atendidos=0,
        cantidad_estudiantes=0,
        clientes_g1=0,
        clientes_g2=0,
        estudiantes_g1=0,
        estudiantes_g2=0,
    )
    db.add(db_simulacion)
    db.commit()
    db.refresh(db_simulacion)
    return db_simulacion

def actualizar_simulacion(simulacion_id:int, simulacion:EsquemaSimulacion):
    db_simulacion = db.query(Simulacion).filter(
        Simulacion.id == simulacion_id).first()
    if db_simulacion:
        db_simulacion.fecha=simulacion.fecha
        db_simulacion.clientes_g1=simulacion.clientes_g1
        db_simulacion.clientes_g2=simulacion.clientes_g2
        db_simulacion.meta_clientes=simulacion.meta_clientes
        db_simulacion.estudiantes_g1=simulacion.estudiantes_g1
        db_simulacion.estudiantes_g2=simulacion.estudiantes_g2
        db_simulacion.clientes_atendidos=simulacion.clientes_atendidos
        db_simulacion.cantidad_estudiantes=simulacion.cantidad_estudiantes
        db.commit()
        db.refresh(db_simulacion)
        return db_simulacion
    
    return None


def obtener_simulaciones():
    return db.query(Simulacion).all()


def registrar_estudiante(estudiante: EsquemaEstudiante):
    db_estudiante = Estudiante(
        simulacion_id=estudiante.simulacion_id,
        horas_cumplidas=estudiante.horas_cumplidas,
        duracion_pasantia=estudiante.duracion_pasantia,
        tramites_realizados=estudiante.tramites_realizados,
        tiempo_promedio_por_tramite=estudiante.tiempo_promedio_por_tramite,
    )
    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)

    return db_estudiante


def actualizar_estudiante(estudiante_id: int, estudiante: EsquemaEstudiante):
    db_estudiante = db.query(Estudiante).filter(
        Estudiante.id == estudiante_id).first()
    if db_estudiante:
        db_estudiante.horas_cumplidas = estudiante.horas_cumplidas
        db_estudiante.duracion_pasantia = estudiante.duracion_pasantia
        db_estudiante.tramites_realizados = estudiante.tramites_realizados
        db_estudiante.tiempo_promedio_por_tramite = estudiante.tiempo_promedio_por_tramite
        db.commit()
        db.refresh(db_estudiante)

        return db_estudiante

    return None


def registrar_tramite(tramite: EsquemaTramite):
    db_tramite = Tramite(
        duracion_tramite=tramite.duracion_tramite,
        estudiante_id=tramite.estudiante_id,
        tramite_seleccionado=tramite.tramite_seleccionado,
    )
    db.add(db_tramite)
    db.commit()
    db.refresh(db_tramite)
