# Proceso padre
#
# 1. Genera una lista de 10 números aleatorios del 1 al 10 ( random.randint(1, 10) )
#     OPCIONAL: configura un valor de la seed para obtener siempre los mismos valores.
# 2. Muestra por pantalla un mensaje indicando su PID ( os.getpid() )
# 3. Crea un proceso hijo y le pasa como argumento esa lista de valores
# 4. Espera a que acabe la ejecución del proceso hijo

# Proceso hijo
# 1. Calcula la suma total de los números que recibe como argumento.
# 2. Muestra por pantalla el resultado total junto con su PID.

from multiprocessing import Process
from os import getpid
from random import randint

def instrucciones(numeros):
    print(f'{sum(numeros)} PID: {getpid()}')

if __name__ == "__main__":
    numeros = [randint(1, 10) for _ in range(10)]
    print(f'[Padre] PID: {getpid()}')
    p = Process(target=instrucciones, args=[ numeros ])
    p.start()
    p.join()

    print('[Padre] Fin')