import random
import time
from threading import Thread, current_thread, Lock

class Baño:
    def __init__(self):
        self._candado = Lock()

    def usar(self):
        with self._candado:
            print(f'[{current_thread().name}] Está usando el baño')
            time.sleep(random.randint(1, 4))
            print(f'[{current_thread().name}] Acabó de usar el baño')


class Persona(Thread):
    def __init__(self, nombre, baño):
        super().__init__(name=nombre)
        self.baño = baño

    def run(self):
        self.baño.usar()

if __name__ == '__main__':

    baño = Baño()
    personas = ['Jorge', 'Jaime', 'Lucía']

    hilos = []
    for persona in personas:
        t = Persona(nombre=persona, baño=baño)
        hilos.append(t)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()