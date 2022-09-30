import simpy
import random
import numpy as np
import matplotlib.pyplot as pp

TIEMPO_TRAMITE = [720, 60, 60, 240, 30, 60, 240, 30, 600, 1200, 480, 240] 
INTERVALO_LLEGADA = 96

tiempo={}
tramites={}

class OficinaTributariaUC(object):
    
    def __init__(self, environment, max_estudiantes, tiempo_tramite):
        self.env=environment
        self.estudiantes = simpy.Resource(environment, max_estudiantes)
        self.tiempo_tramite = tiempo_tramite
        
    def atendiendo_tramite(self, cliente):
        tramite = np.random.choice(TIEMPO_TRAMITE, 1)
        #print(f'{cliente} con un tramite de duracion: {tramite[0]/60}')
        yield self.env.timeout(tramite[0])
        k = tramite[0]/60
        if k in tramites:
            tramites[k]=tramites[k]+1
        else:
            tramites[k]=1
    
 
def llegada_cliente(env, nombre, oficina):
    #print('Llega cliente: %s a la hora %.2f.' % (nombre, env.now/60))
    with oficina.estudiantes.request() as estudiante:
        yield estudiante
        #print('Entra [%s] a la oficina: a la hora %.2f.' % (nombre, env.now/60))
        yield env.process(oficina.atendiendo_tramite(nombre))
        #print('[%s] atendido a las %.2f.' % (nombre, env.now/60))
        
        k=env.now/60
    if k in tiempo:
        tiempo[k]=tiempo[k]+1
    else:
        tiempo[k]=1
    
    
def ejecutar_simulacion(env, max_estudiantes, max_clientes, tiempo_tramite, intervalo):
    oficina=OficinaTributariaUC(env, max_estudiantes, tiempo_tramite)
    for i in range(max_clientes):
        env.process(llegada_cliente(env, 'Cliente-%d'%(i+1),oficina))
    
    while True:
        yield env.timeout(random.randint(intervalo-10, intervalo+10))
        i+=1
        env.process(llegada_cliente(env,'Cliente-%d'%(i+1),oficina))

def run(max_estudiantes, tiempo_pasantia, max_clientes):
    global tiempo
    global tramites
    random.seed(10)

    env=simpy.Environment()
    env.process(ejecutar_simulacion(env, max_estudiantes, max_clientes, TIEMPO_TRAMITE, INTERVALO_LLEGADA))

    print(f'Tiempo de pasantia: {tiempo_pasantia/60}')
    env.run(until = tiempo_pasantia)


    # Generamos la grafica
    datos=sorted(tiempo.items())
    datos_1=sorted(tramites.items())
    #print(tiempo.items())
    x, y =zip(*datos)
    x_1, y_1 =zip(*datos_1)
    print(f'Cantidad de alumnos: {max_estudiantes}')
    print(f'Cantidad minima de clientes: {max_clientes}')
    print(f'Total clientes atendidos: {sum(y)}')# total horas, total clientes
    pp.bar(x,y,width=1,linewidth=2,color='blue')
    #pp.scatter(x,y,color='blue')
    pp.grid(True)
    pp.show()

    pp.bar(x_1,y_1,width=1,linewidth=2,color='red')
    pp.grid(True)
    pp.show()

    #print(x_1,y_1)
    #print(sum(x_1), sum(y_1))

    tiempo={}
    tramites={}
    return max_clientes, sum(y)


