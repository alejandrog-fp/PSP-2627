import time
from multiprocessing import Process, Value, Array

class MiProceso(Process):

    def __init__(self, nombre, lista):
        super().__init__(name = nombre)
        self.lista = lista

    def run(self):
        print(f'[{self.name}] La lista compartido es: {self.lista[:]}')
        for i in range(len(self.lista)):
            self.lista[i] += 1
        print(f'[{self.name}] La lista compartido es: {self.lista[:]}')

if __name__ == '__main__':

    lista = Array('i', [1, 2, 3])

    p1 = MiProceso('Juan', lista)
    p1.start()
    p1.join()

    p2 = MiProceso('Marta', lista)
    p2.start()
    p2.join()

    print(f'[Padre] La lista compartido es: {lista[:]}')
    for i in range(len(lista)):
        lista[i] += 1
    print(f'[Padre] La lista compartido es: {lista[:]}')