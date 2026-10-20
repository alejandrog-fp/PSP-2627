# Proceso Padre:
# 1. Genera una lista que contiene tantas listas como núcleos tiene el ordenador ( multiprocessing.cpu_count() ).
# Cada una de estas listas internas tiene 5 números enteros generados de manera aleatoria entre 1 y 10 ( random.randint(1, 10) ).
# Ejemplo de datos para 2 núcleos/procesos y 3 números -> [ [1, 3, 5], [2, 4, 6] ]
# 2. Crea tantos procesos hijos como núcleos tiene el ordenador. A cada proceso hijo se le manda una de las listas con números
# 3. Espera a que acaben todos los procesos hijos.

# Procesos hijos: recibe una lista de números enteros e imprime por pantalla la suma, indicando su PID
# PISTA: El pid se puede obtener a partir de la función os.getpid()

from multiprocessing import Process, cpu_count
from random import randint
from os import getpid

def instrucciones(numeros: list) -> None:
    print(f'{sum(numeros)} PID: {getpid()}')

if __name__ == "__main__":

    N_PROCESS = cpu_count()

    lista_numeros = []
    for i in range(N_PROCESS):
        numeros = []
        for j in range(5):
            numeros.append(randint(1, 10))

        lista_numeros.append(numeros)

        # Ejercicio, hacer esto en una unica linea usando list comprehension

    procesos = []
    for i in range(N_PROCESS):
        p = Process(target = instrucciones, args=  [ lista_numeros[i] ]  )
        procesos.append(p)

    for p in procesos:
        p.start()

    for p in procesos:
        p.join()
