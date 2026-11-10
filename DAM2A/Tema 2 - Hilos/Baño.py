import random
import time
from threading import Thread, current_thread

class Baño:
    def __init__(self):
        pass

    def usar(self):
        print(f'[{current_thread().name}] Está usando el baño')
        time.sleep(random.randint(1, 4))
        print(f'[{current_thread().name}] Acabó de usar el baño')

if __name__ == '__main__':

    baño = Baño()
    personas = ['Jorge', 'Jaime', 'Lucía']

    hilos = []
    for persona in personas:
        t = Thread(target=baño.usar, name=persona)
        hilos.append(t)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()