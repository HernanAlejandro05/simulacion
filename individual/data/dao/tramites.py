from ..database import SessionLocal
from ..models.tramite import Tramite
from ..schemas.tramite import Tramite as EsquemaTramite

db = SessionLocal()


def registrar_tramite(tramite: EsquemaTramite):
    db_tramite = Tramite(
        duracion_tramite=tramite.duracion_tramite,
        estudiante_id=tramite.estudiante_id,
        tramite_seleccionado=tramite.tramite_seleccionado,
    )
    db.add(db_tramite)
    db.commit()
    db.refresh(db_tramite)


def obtener_tramite(id: int):
    return db.query(Tramite).filter_by(id=id).first()


def obtener_tramites():
    return db.query(Tramite).all()
