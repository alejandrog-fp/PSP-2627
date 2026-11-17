import random
import time
from threading import Thread, Lock, current_thread

class Banio:
    def __init__(self):
        self._candado = Lock()

    def usar(self):
        with self._candado:
            print(f'[{current_thread().name}] Estoy usando el baño')
            time.sleep(random.randint(1, 4))
            print(f'[{current_thread().name}] Acabé de usar el baño')

if __name__ == '__main__':

    banio = Banio()

    hilos = []
    for nombre in ['Álvaro', 'Manolo', 'Jacinta', 'Juana']:
        t = Thread(target=banio.usar, name=nombre)
        hilos.append(t)

    for t in hilos:
        t.start()

    for t in hilos:
        t.join()