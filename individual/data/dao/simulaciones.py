from ..models import Simulacion
from ..database import SessionLocal

from ..schemas.simulacion import Simulacion as EsquemaSimulacion

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


def actualizar_simulacion(simulacion_id: int, simulacion: EsquemaSimulacion):
    db_simulacion = db.query(Simulacion).filter(
        Simulacion.id == simulacion_id).first()
    if db_simulacion:
        db_simulacion.fecha = simulacion.fecha
        db_simulacion.clientes_g1 = simulacion.clientes_g1
        db_simulacion.clientes_g2 = simulacion.clientes_g2
        db_simulacion.meta_clientes = simulacion.meta_clientes
        db_simulacion.estudiantes_g1 = simulacion.estudiantes_g1
        db_simulacion.estudiantes_g2 = simulacion.estudiantes_g2
        db_simulacion.clientes_atendidos = simulacion.clientes_atendidos
        db_simulacion.cantidad_estudiantes = simulacion.cantidad_estudiantes
        db.commit()
        db.refresh(db_simulacion)
        return db_simulacion

    return None


def obtener_simulaciones():
    return db.query(Simulacion).all()
