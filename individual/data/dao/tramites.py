from ..schemas import EsquemaTramite

from ..models import Tramite
from ..database import SessionLocal

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
