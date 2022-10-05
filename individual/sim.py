import simpy
import random
import numpy as np
import matplotlib.pyplot as pp

# TIEMPO_TRAMITE = [720, 60, 60, 240, 30, 60, 240, 30, 600, 1200, 480, 240]
TIEMPO_TRAMITE = {
    'Capacitacion temas tributarios': 720,
    'Determinar necesidades del contribuyente': 60,
    'Ingreso de contribuyentes a la base de datos': 60,
    'Asesoramiento individual sobre derechos y oblicgaciones tributarias': 240,
    'Recepcion de documentos tributarios': 30,
    'Analisis de documentos tributarios': 60,
    'Llenado de formularios en el sri': 240,
    'Entrega de declaraciones y documentacion al contribuyente': 30,
    'Determinar los grupos vulnerables': 600,
    'Preparacion de talleres de capacitacion': 1200,
    'Ejecucion de talleres de capacitacion': 480,
    'Promocion de servicios tributarios': 240,
}

INTERVALO_LLEGADA = 96

tiempo = {}
tiempo_pasantia = 0
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
        global tiempo_pasantia
        # tramite = np.random.choice(TIEMPO_TRAMITE, 1)

        self.check_time()

        tramite = np.random.choice(list(TIEMPO_TRAMITE.keys()), 1)[0]
        duracion = TIEMPO_TRAMITE[tramite]/60

        total_tiempo_tramites += duracion
        # if total_tiempo_tramites >= (tiempo_pasantia/60):
        #     end_event = self.env.event()
        #     end_event.succeed()

        contador_de_tramites += 1
        print(
            f'{cliente} entra a realizar: {tramite} y tomara un tiempo de {duracion}hrs.')

        # tipos_de_tramite[tramite[0]] += 1

        yield self.env.timeout(int(TIEMPO_TRAMITE[tramite]))
        k = duracion
        if k in tramites:
            tramites[k] = tramites[k]+1
        else:
            tramites[k] = 1

    def check_time(self):
        duracion = tiempo_pasantia/60
        limite_duracion = duracion-20 if duracion == 160 else duracion-10
        if total_tiempo_tramites >= limite_duracion and 'Capacitacion temas tributarios' \
                in TIEMPO_TRAMITE and 'Preparacion de talleres de capacitacion' in TIEMPO_TRAMITE:

            del TIEMPO_TRAMITE['Capacitacion temas tributarios']
            # del TIEMPO_TRAMITE['Determinar los grupos vulnerables']
            # del TIEMPO_TRAMITE['Ejecucion de talleres de capacitacion']
            del TIEMPO_TRAMITE['Preparacion de talleres de capacitacion']


def llegada_cliente(env, cliente, oficina):
    with oficina.estudiantes.request() as estudiante:
        yield estudiante
        yield env.process(oficina.atendiendo_tramite(cliente))

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


def run(max_estudiantes, duracion_pasantia, max_clientes):
    global tiempo
    global tiempo_pasantia
    global tramites
    global total_tiempo_tramites
    global contador_de_tramites
    random.seed(10)

    tiempo_pasantia = duracion_pasantia

    env = simpy.Environment()
    env.process(ejecutar_simulacion(env, max_estudiantes,
                max_clientes, TIEMPO_TRAMITE, INTERVALO_LLEGADA))

    print('*'*50)
    print(f'Tiempo de pasantia: {duracion_pasantia/60}'.upper())
    env.run(until=duracion_pasantia)

    # Generamos la grafica
    datos = sorted(tiempo.items())
    datos_1 = sorted(tramites.items())
    # print(tiempo.items())
    x, y = zip(*datos)
    x_1, y_1 = zip(*datos_1)
    print(f'Cantidad de alumnos: {max_estudiantes}\n')
    # total horas, total clientes
    print(f'Cantidad de clientes que deberia atender: {max_clientes}\n')
    # total horas, total clientes
    promedio_duracion_tramite = total_tiempo_tramites / contador_de_tramites
    print(f'Cantidad de tramites realizados: {contador_de_tramites}\n')
    print(
        f'Duracion promedio por tramite: {promedio_duracion_tramite:.2f} horas')
    print(f'Horas cumplidas: {total_tiempo_tramites}\n'.upper())
    pp.bar(x, y, width=1, linewidth=2, color='blue')
    # pp.scatter(x,y,color='blue')
    pp.grid(True)
    # pp.show()

    pp.bar(x_1, y_1, width=1, linewidth=2, color='red')
    pp.grid(True)
    # pp.show()

    aux_tramites = contador_de_tramites

    tiempo = {}
    tramites = {}
    total_tiempo_tramites = 0
    contador_de_tramites = 0

    return max_clientes, aux_tramites
