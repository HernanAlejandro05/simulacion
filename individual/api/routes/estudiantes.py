from fastapi import APIRouter

from data.schemas.estudiante import EstudianteTramites
from data.dao.estudiantes import obtener_estudiantes, obtener_estudiante

router = APIRouter(
    prefix='/estudiantes',
    tags=['Estudiantes'],
)


@router.get('/')
async def listar_estudiantes():
    return obtener_estudiantes()


@router.get('/{id}',  response_model=EstudianteTramites)
async def recuperar_estudiante(id: int):
    return obtener_estudiante(id)
