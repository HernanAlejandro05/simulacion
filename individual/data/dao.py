from .schemas import EsquemaEstudiante, EsquemaTramite

from .database import SessionLocal
from .models import Simulacion, Estudiante, Tramite

db = SessionLocal()


def registrar_simulacion():
    db_simulacion = Simulacion()
    db.add(db_simulacion)
    db.commit()
    db.refresh(db_simulacion)
    return db_simulacion


def registrar_estudiante(estudiante: EsquemaEstudiante):
    db_estudiante = Estudiante(
        simulacion_id=estudiante.simulacion_id,
        horas_cumplidas=estudiante.horas_cumplidas,
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
