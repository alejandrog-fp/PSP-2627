import time
from multiprocessing import Process, Queue

class MiProceso(Process):

    def __init__(self, cola):
        super().__init__()
        self.cola = cola

    def run(self):
        print('[Hijo] Voy a introducir algo en la cola.')
        time.sleep(5)
        self.cola.put('Hola mundo')

if __name__ == '__main__':

    cola = Queue()

    p = MiProceso(cola)
    p.start()

    print('[Padre] Voy a ver que ha introducido mi hijo en la cola')
    msg = cola.get() # Linea bloqueante si no hay nada en la cola
    print(f'[Padre] Mi hijo ha introducido esto en la cola: {msg}')