from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from data.dao.simulaciones import obtener_simulaciones

router = APIRouter(
    prefix='/simulaciones',
    tags=['Simulaciones'],
)


@router.get('/')
async def listar_simulaciones():
    return obtener_simulaciones()
