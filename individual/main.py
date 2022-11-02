import random

from sim import *

from data.database import engine
from data.schemas.simulacion import Simulacion
from data.models import estudiante, simulacion, tramite
from data.dao.simulaciones import actualizar_simulacion, registrar_simulacion

# Crea las tablas e inicializa la basa de datos.
tramite.Base.metadata.create_all(bind=engine)
estudiante.Base.metadata.create_all(bind=engine)
simulacion.Base.metadata.create_all(bind=engine)

MAX_CLIENTES = 800
MAX_ESTUDIANTES = 30
ESTUDIANTE_POR_TIPO_PASANTIA = 1
TIEMPO_PASANTIA = [9600, 5760]

if __name__ == '__main__':
    r = .625
    # r = random.random()
    c1 = int(MAX_CLIENTES*r)
    c2 = MAX_CLIENTES - c1

    if c1 > c2:
        clientes = [c1, c2]
    else:
        clientes = [c2, c1]

    e1 = int(MAX_ESTUDIANTES*r)
    e2 = MAX_ESTUDIANTES - e1

    if e1 > e2:
        estudiantes = [e1, e2]
    else:
        estudiantes = [e2, e1]

    clientes_atendidos = 0

    print('CLIENTES>>>', clientes)
    print('ESTUDIANTES>>>', estudiantes)

    simu = registrar_simulacion()

    for e in range(2):
        print(f"{'-'*50}>[{estudiantes[e]}]<{'-'*50}")
        for i in range(estudiantes[e]):
            _, cli = run(
                ESTUDIANTE_POR_TIPO_PASANTIA, TIEMPO_PASANTIA[e], clientes[e], simu.id)
            clientes_atendidos += cli

            print('\n')
            print('-'*50)
            print(f'Total de clientes atendidos: {clientes_atendidos}')
            print('-'*50)

    sim = Simulacion(
        clientes_g1=c1,
        clientes_g2=c2,
        estudiantes_g1=e1,
        estudiantes_g2=e2,
        fecha=simu.fecha,
        meta_clientes=MAX_CLIENTES,
        cantidad_estudiantes=MAX_ESTUDIANTES,
        clientes_atendidos=clientes_atendidos,
    )
    actualizar_simulacion(simu.id, sim)
