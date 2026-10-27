import time
from multiprocessing import Process, Manager

class MiProceso(Process):

    def __init__(self, nombre, diccionario):
        super().__init__(name = nombre)
        self.diccionario = diccionario

    def run(self):
        print(f'[{self.name}] El diccionario compartido es: {self.diccionario}')
        self.diccionario[self.name] = f'Hola soy {self.name} y mi PID es {self.pid}'
        print(f'[{self.name}] El diccionario compartido es: {self.diccionario}')

if __name__ == '__main__':

    with Manager() as manager:
        d = manager.dict()

        p1 = MiProceso('Juan', d)
        p1.start()
        p1.join()

        p2 = MiProceso('Marta', d)
        p2.start()
        p2.join()

        print(f'[Padre] El diccionario compartido es: {d}')
