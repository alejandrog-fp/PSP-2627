# Crea un proceso que se le pase como argumento una lista con el elemento 'hola' y le añade 'mundo'
# El hijo muestra el contenido de la lista
# Una vez finalizado el proceso hijo, el padre muestra el contenido de la lista.
# Crea un hilo que se le pase como argumento una lista con el elemento 'hola' y le añade 'mundo'
# El hijo muestra el contenido de la lista
# Una vez finalizado el proceso hijo, el padre muestra el contenido de la lista.

from multiprocessing import Process, current_process
from threading import Thread

def instrucciones(lista):
    lista.append('mundo')
    print(f'[{current_process().name}] {lista}')

if __name__ == '__main__':

    lista = ['hola']

    p = Process(target=instrucciones, args=[ lista ])
    p.start()
    p.join()

    print(f'[PADRE] {lista}')

    h = Thread(target=instrucciones, args=[lista])
    h.start()
    h.join()

    print(f'[PADRE] {lista}')