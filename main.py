from sim import *
import random

MAX_CLIENTES = 800
MAX_ESTUDIANTES = 41
TIEMPO_PASANTIA = [9600, 5760]

r=random.random()
c_1 = int(MAX_CLIENTES*r)
c_2 = MAX_CLIENTES - c_1
clientes=[c_1, c_2]

e_1 = int(MAX_ESTUDIANTES*r)
e_2 = MAX_ESTUDIANTES - e_1
estudiantes=[e_1, e_2]

idx=random.randint(0,1)
index=[idx, 0 if idx == 1 else 1] 


acum_clientes=0
acum_horas=0

for i in range(2):
    print(index[i])
    max_clientes, horas = run(estudiantes[i], TIEMPO_PASANTIA[index[i]], clientes[i])
    acum_clientes += max_clientes
    acum_horas += horas

print('\n\n-----------------------------------------------')
print(f'Meta de clientes a atender: {acum_clientes}')
print(f'Total de clientes atendidos: {acum_horas}')
print('-----------------------------------------------')
