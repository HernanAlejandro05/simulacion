import simpy
import random
import numpy as np
import matplotlib.pyplot as pp

from data.schemas.tramite import Tramite
from data.schemas.estudiante import Estudiante

from data.dao.tramites import registrar_tramite
from data.dao.estudiantes import registrar_estudiante, actualizar_estudiante

# LISTA_TRAMITES = [720, 60, 60, 240, 30, 60, 240, 30, 600, 1200, 480, 240]
LISTA_TRAMITES = {
    '1. Capacitacion temas tributarios': 720,
    '2. Determinar necesidades del contribuyente': 60,
    '3. Ingreso de contribuyentes a la base de datos': 60,
    '4. Asesoramiento individual sobre derechos y oblicgaciones tributarias': 240,
    '5. Recepcion de documentos tributarios': 30,
    '6. Analisis de documentos tributarios': 60,
    '7. Llenado de formularios en el sri': 240,
    '8. Entrega de declaraciones y documentacion al contribuyente': 30,
    '9. Determinar los grupos vulnerables': 600,
    '10. Preparacion de talleres de capacitacion': 1200,
    '11. Ejecucion de talleres de capacitacion': 480,
    '12. Promocion de servicios tributarios': 240,
}

INTERVALO_LLEGADA = 96

tiempo = {}
tramites = {}
estudiante_id = 0
tiempo_pasantia = 0
tipos_de_tramite = {}
lista_de_tramites = {}
contador_tramites = 0
contador_de_tramites = 0
total_tiempo_tramites = 0


class OficinaTributariaUC(object):

    def __init__(self, environment, max_estudiantes, tiempo_tramite):
        self.env = environment
        self.estudiantes = simpy.Resource(environment, max_estudiantes)
        self.tiempo_tramite = tiempo_tramite

    def atendiendo_tramite(self, cliente):
        global lista_de_tramites
        global estudiante_id
        global tiempo_pasantia
        global tipos_de_tramite
        global contador_tramites
        global contador_de_tramites
        global total_tiempo_tramites

        duracion = 0
        self.check_time()

        lista_tareas = list(lista_de_tramites.keys())
        if contador_tramites < len(lista_tareas):
            tramite_seleccionado = lista_tareas[contador_tramites]
            duracion = lista_de_tramites[tramite_seleccionado]/60
        else:
            tramite_seleccionado = np.random.choice(list(lista_de_tramites.keys()), 1)[0]
            duracion = lista_de_tramites[tramite_seleccionado]/60

        total_tiempo_tramites += duracion

        contador_tramites += 1
        contador_de_tramites += 1

        print(
            f'{cliente} entra a realizar: {tramite_seleccionado} y tomara un tiempo de {duracion}hrs.')

        tramite_data = Tramite(
            duracion_tramite=duracion,
            estudiante_id=estudiante_id,
            tramite_seleccionado=tramite_seleccionado
        )

        registrar_tramite(tramite_data)

        yield self.env.timeout(int(lista_de_tramites[tramite_seleccionado]))
        k = duracion
        if k in tramites:
            tramites[k] = tramites[k]+1
        else:
            tramites[k] = 1

    def check_time(self):
        duracion = tiempo_pasantia/60
        limite_duracion = duracion-30 if duracion == 160 else duracion-20
        if total_tiempo_tramites >= limite_duracion and '1. Capacitacion temas tributarios' \
                in lista_de_tramites and '10. Preparacion de talleres de capacitacion' in lista_de_tramites \
                and '11. Ejecucion de talleres de capacitacion' in lista_de_tramites \
                and '9. Determinar los grupos vulnerables' in lista_de_tramites:

            del lista_de_tramites['1. Capacitacion temas tributarios']
            del lista_de_tramites['9. Determinar los grupos vulnerables']
            del lista_de_tramites['11. Ejecucion de talleres de capacitacion']
            del lista_de_tramites['10. Preparacion de talleres de capacitacion']


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


def run(max_estudiantes, duracion_pasantia, max_clientes, simulacion_id):
    global tiempo
    global lista_de_tramites
    global tramites
    global estudiante_id
    global tiempo_pasantia
    global contador_tramites
    global contador_de_tramites
    global total_tiempo_tramites
    random.seed(10)

    print('SIMULACION>>>>>', simulacion_id)

    estudiante_in = Estudiante(
        horas_cumplidas=0.0,
        tramites_realizados=0,
        duracion_pasantia=0.0,
        simulacion_id=simulacion_id,
        tiempo_promedio_por_tramite=0.0,
    )

    estudiante_id = registrar_estudiante(estudiante_in).id

    print('ESTUDIANTE>>>>>', estudiante_id)

    lista_de_tramites = LISTA_TRAMITES.copy()
    tiempo_pasantia = duracion_pasantia

    env = simpy.Environment()
    env.process(ejecutar_simulacion(env, max_estudiantes,
                max_clientes, lista_de_tramites, INTERVALO_LLEGADA))

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
    # print(f'Cantidad de clientes que deberia atender: {max_clientes}\n')
    # total horas, total clientes
    promedio_duracion_tramite = total_tiempo_tramites / contador_de_tramites
    print(f'Cantidad de tramites realizados: {contador_de_tramites}\n')
    print(
        f'Duracion promedio por tramite: {promedio_duracion_tramite:.2f} horas')
    print(f'Horas cumplidas: {total_tiempo_tramites}\n'.upper())

    estudiante_out = Estudiante(
        simulacion_id=simulacion_id,
        duracion_pasantia=(duracion_pasantia / 60),
        horas_cumplidas=total_tiempo_tramites,
        tramites_realizados=contador_de_tramites,
        tiempo_promedio_por_tramite=float(f'{promedio_duracion_tramite:.2f}')
    )

    actualizar_estudiante(estudiante_id, estudiante_out)

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
    contador_tramites = 0
    contador_de_tramites = 0
    total_tiempo_tramites = 0

    return max_clientes, aux_tramites
