import time
from multiprocessing import Process, Value, Array

class MiProceso(Process):

    def __init__(self, nombre, n):
        super().__init__(name = nombre)
        self.n = n

    def run(self):
        print(f'[{self.name}] El numero compartido es: {self.n.value}')
        self.n.value *= 0.1
        print(f'[{self.name}] El numero compartido es: {self.n.value}')

if __name__ == '__main__':

    numero = Value('d', 3.14)

    p1 = MiProceso('Juan', numero)
    p1.start()
    p1.join()

    p2 = MiProceso('Marta', numero)
    p2.start()
    p2.join()

    print(f'[Padre] El numero compartido es: {numero.value}')
    numero.value *= 0.1
    print(f'[Padre] El numero compartido es: {numero.value}')