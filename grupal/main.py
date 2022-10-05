from sim import *
import random

MAX_CLIENTES = 800
MAX_ESTUDIANTES = 31
TIEMPO_PASANTIA = [9600, 5760]

r = .65
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

# idx = random.randint(0, 1)
# index = [idx, 0 if idx == 1 else 1]


acum_clientes = 0
acum_horas = 0

for i in range(2):
    # print(index[i])
    max_clientes, horas = run(
        estudiantes[i], TIEMPO_PASANTIA[i], clientes[i])
    acum_clientes += max_clientes
    acum_horas += horas

print('\n')
print('-'*50)
print(f'Meta de clientes a atender: {acum_clientes}')
print(f'Total de clientes atendidos: {acum_horas}')
print('-'*50)
