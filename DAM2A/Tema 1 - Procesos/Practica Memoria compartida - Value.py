import time
from multiprocessing import Process, Value, Array
class MiProceso(Process):

    def __init__(self, nombre, var_compartida):
        super().__init__(name=nombre)
        self.var_compartida = var_compartida

    def run(self):
        print(f'[{self.name}] El valor de la variable compartida es: {self.var_compartida.value}')
        self.var_compartida.value += 1
        print(f'[{self.name}] El nuevo valor de la variable compartida es: {self.var_compartida.value}')

if __name__ == '__main__':

    var_compartida = Value('i', 67)

    MiProceso(nombre='Pepe', var_compartida=var_compartida).start()
    time.sleep(2)
    MiProceso(nombre='Julia', var_compartida=var_compartida).start()
    time.sleep(2)
    print(f'[Padre] El valor final de la variable es {var_compartida.value}')

