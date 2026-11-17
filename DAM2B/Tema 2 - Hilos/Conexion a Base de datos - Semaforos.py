import time
import random
from threading import current_thread, Thread, Semaphore
from multiprocessing import Process

class BaseDatos:
    def __init__(self):
        self.usuarios_conectados = 0
        self._semaforo = Semaphore(4)

    def conectar(self):
        self._semaforo.acquire()
        print(f'{current_thread().name} ha accedido a la base de datos.')
        self.usuarios_conectados += 1
        print(f'Hay {self.usuarios_conectados} usuarios')

    def desconectar(self):
        print(f'{current_thread().name} se ha desconectado de la base de datos.')
        self.usuarios_conectados -= 1
        self._semaforo.release()

class Cliente(Thread):
    def __init__(self, nombre):
        super().__init__(name = nombre)

    def run(self):
        bd.conectar()
        time.sleep(random.randint(2, 5))
        bd.desconectar()

if __name__ == '__main__':
    bd = BaseDatos()

    hilos = []
    for nombre in ['Juan', 'Alicia', 'Paco', 'Fernando', 'Jaime', 'Ana']:
        t = Cliente(nombre)
        hilos.append(t)

    for t in hilos:
        t.start()

    for t in hilos:
        t.join()