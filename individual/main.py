from sim import *
import random

MAX_CLIENTES = 800
MAX_ESTUDIANTES = 30
ESTUDIANTE_POR_TIPO_PASANTIA = 1
TIEMPO_PASANTIA = [9600, 5760]

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

acum_horas = 0

print('CLIENTES>>>', clientes)
print('ESTUDIANTES>>>', estudiantes)

for e in range(2):
    print(f"{'-'*50}>[{estudiantes[e]}]<{'-'*50}")
    for i in range(estudiantes[e]):
        max_clientes, horas = run(
            ESTUDIANTE_POR_TIPO_PASANTIA, TIEMPO_PASANTIA[e], clientes[e])
        # acum_clientes += max_clientes
        acum_horas += horas

        print('\n')
        print('-'*50)
        print(f'Total de clientes atendidos: {acum_horas}')
        print('-'*50)
