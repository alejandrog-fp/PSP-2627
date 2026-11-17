import random
import time
from threading import Thread, current_thread, Lock, Semaphore


class BaseDatos:
    def __init__(self):
        self.usuarios_conectados = 0
        self.semaforo = Semaphore(2)
        self.print_candado = Lock()

    def conectar(self):
        self.semaforo.acquire()

        self.usuarios_conectados += 1
        with self.print_candado:
            print(f'Se ha conectado el usuario {current_thread().name}')
            print(f'Hay actualmente {self.usuarios_conectados} usuarios conectados a la base de datos')

    def desconectar(self):
        with self.print_candado:
            print(f'Se ha desconectado el usuario {current_thread().name}')
        self.usuarios_conectados -= 1

        self.semaforo.release()

class Cliente(Thread):
    def __init__(self, nombre, bd):
        super().__init__(name=nombre)
        self.bd = bd

    def run(self):
        self.bd.conectar()
        time.sleep(random.randint(1,3))
        self.bd.desconectar()



if __name__ == '__main__':

    bd = BaseDatos()

    hilos = []
    for nombre in ['Pepe', 'Juan', 'Antonia', 'Susana']:
        t = Cliente(nombre= nombre, bd= bd)
        hilos.append(t)

    for t in hilos:
        t.start()

    for t in hilos:
        t.join()