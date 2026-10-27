import time
from multiprocessing import Process, Value, Array
class MiProceso(Process):

    def __init__(self, nombre, var_compartida):
        super().__init__(name=nombre)
        self.var_compartida = var_compartida

    def run(self):
        print(f'[{self.name}] El valor de la variable compartida es: {self.var_compartida[:]}')
        for i in range(len(self.var_compartida)):
            self.var_compartida[i] += 1
        print(f'[{self.name}] El nuevo valor de la variable compartida es: {self.var_compartida[:]}')

def instrucciones(lista):
    print(f'[Hijo] El valor de la variable compartida es: {lista}')
    for i in range(len(lista)):
        lista[i] += 1
    print(f'[Hijo] El nuevo valor de la variable compartida es: {lista}')

if __name__ == '__main__':

    var_compartida = Array('i', [1, 2, 3] )

    MiProceso(nombre='Pepe', var_compartida=var_compartida).start()
    time.sleep(2)
    MiProceso(nombre='Julia', var_compartida=var_compartida).start()
    time.sleep(2)
    print(f'[Padre] El valor final de la variable es {var_compartida[:]}')

    # Manera incorrecta de compartir variables
    # l = [1, 2, 3]
    #
    # p1 = Process(target=instrucciones, args=[ l ])
    # p1.start()
    # p1.join()
    #
    # p2 = Process(target=instrucciones, args= [ l ])
    # p2.start()
    # p2.join()
    #
    # print(l)
