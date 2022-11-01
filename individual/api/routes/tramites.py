from fastapi import APIRouter

from data.dao.tramites import obtener_tramites, obtener_tramite

router = APIRouter(
    prefix='/tramites',
    tags=['Tramites'],
)


@router.get('/')
async def listar_simulaciones():
    return obtener_tramites()


@router.get('/{id}')
async def recuperar_simulacion(id: int):
    return obtener_tramite(id)
