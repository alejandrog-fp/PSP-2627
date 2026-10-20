import time
from multiprocessing import Process, Queue, current_process

def instrucciones(cola):
    cola.put(f'[{current_process().name}] Hola padre. Me voy a dormir.')
    mensaje_padre = cola.get()
    print(f'[{current_process().name}] Mi padre me ha dicho {mensaje_padre}')
    time.sleep(7)
    cola.put(f'[{current_process().name}] Ya me desperté. Buenos días Padre.')

if __name__ == '__main__':

    cola = Queue()

    p = Process(target=instrucciones, name='Hijo', args= (cola, ))
    p.start()

    mensaje_hijo = cola.get()
    print(f'[Padre] He recibido el siguiente mensaje {mensaje_hijo}')

    cola.put(f'[Padre] Buenas noches hijo. Descansa')

    print('[Padre] Esperando a que se despierte mi hijo.')
    mensaje_hijo = cola.get() # Linea bloqueante
    print(f'[Padre] He recibido el siguiente mensaje {mensaje_hijo}')