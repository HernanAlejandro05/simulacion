from fastapi import APIRouter

from data.schemas.simulacion import SimulacionEstudiantes
from data.dao.simulaciones import obtener_simulaciones, obtener_simulacion

router = APIRouter(
    prefix='/simulaciones',
    tags=['Simulaciones'],
)


@router.get('/')
async def listar_simulaciones():
    return obtener_simulaciones()


@router.get('/{id}',  response_model=SimulacionEstudiantes)
async def recuperar_simulacion(id: int):
    return obtener_simulacion(id)
