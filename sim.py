import simpy
import random
import numpy as np
import matplotlib.pyplot as pp

TIEMPO_TRAMITE = [720, 60, 60, 240, 30, 60, 240, 30, 600, 1200, 480, 240]
INTERVALO_LLEGADA = 96

tiempo = {}
tramites = {}
total_tiempo_tramites = 0
contador_de_tramites = 0
tipos_de_tramite = {}


class OficinaTributariaUC(object):

    def __init__(self, environment, max_estudiantes, tiempo_tramite):
        self.env = environment
        self.estudiantes = simpy.Resource(environment, max_estudiantes)
        self.tiempo_tramite = tiempo_tramite

    def atendiendo_tramite(self, cliente):
        global total_tiempo_tramites
        global contador_de_tramites
        global tipos_de_tramite
        tramite = np.random.choice(TIEMPO_TRAMITE, 1)
        duracion = tramite[0]/60
        # print(f'{cliente} con un tramite de duracion: {duracion}')

        total_tiempo_tramites += duracion
        contador_de_tramites += 1
        # tipos_de_tramite[tramite[0]] += 1

        yield self.env.timeout(tramite[0])
        k = duracion
        if k in tramites:
            tramites[k] = tramites[k]+1
        else:
            tramites[k] = 1


def llegada_cliente(env, nombre, oficina):
    #print('Llega cliente: %s a la hora %.2f.' % (nombre, env.now/60))
    with oficina.estudiantes.request() as estudiante:
        yield estudiante
        #print('Entra [%s] a la oficina: a la hora %.2f.' % (nombre, env.now/60))
        yield env.process(oficina.atendiendo_tramite(nombre))
        #print('[%s] atendido a las %.2f.' % (nombre, env.now/60))

        k = env.now/60
    if k in tiempo:
        tiempo[k] = tiempo[k]+1
    else:
        tiempo[k] = 1


def ejecutar_simulacion(env, max_estudiantes, max_clientes, tiempo_tramite, intervalo):
    oficina = OficinaTributariaUC(env, max_estudiantes, tiempo_tramite)
    for i in range(max_clientes):
        env.process(llegada_cliente(env, 'Cliente-%d' % (i+1), oficina))

    while True:
        yield env.timeout(random.randint(intervalo-10, intervalo+10))
        i += 1
        env.process(llegada_cliente(env, 'Cliente-%d' % (i+1), oficina))


def run(max_estudiantes, tiempo_pasantia, max_clientes):
    global tiempo
    global tramites
    global total_tiempo_tramites
    global contador_de_tramites
    random.seed(10)

    env = simpy.Environment()
    env.process(ejecutar_simulacion(env, max_estudiantes,
                max_clientes, TIEMPO_TRAMITE, INTERVALO_LLEGADA))

    print('*'*50)
    print(f'Tiempo de pasantia: {tiempo_pasantia/60}'.upper())
    env.run(until=tiempo_pasantia)

    # Generamos la grafica
    datos = sorted(tiempo.items())
    datos_1 = sorted(tramites.items())
    # print(tiempo.items())
    x, y = zip(*datos)
    x_1, y_1 = zip(*datos_1)
    print(f'Cantidad de alumnos: {max_estudiantes}\n')
    print(f'cantidad de clientes que atendio: {sum(y)}\n')  # total horas, total clientes
    print(f'Cantidad de clientes que deberia atender: {max_clientes}\n')
    # total horas, total clientes
    promedio_duracion_tramite = total_tiempo_tramites / contador_de_tramites
    print(f'Cantidad de tramites realizados: {contador_de_tramites}\n')
    print(f'Duracion promedio por tramite: {promedio_duracion_tramite:.2f} horas')
    print(f'Horas cumplidas: {total_tiempo_tramites}\n'.upper())
    pp.bar(x, y, width=1, linewidth=2, color='blue')
    # pp.scatter(x,y,color='blue')
    pp.grid(True)
    # pp.show()

    pp.bar(x_1, y_1, width=1, linewidth=2, color='red')
    pp.grid(True)
    # pp.show()

    # print(x_1,y_1)
    #print(sum(x_1), sum(y_1))

    tiempo = {}
    tramites = {}
    total_tiempo_tramites = 0
    contador_de_tramites = 0
    return max_clientes, sum(y)
