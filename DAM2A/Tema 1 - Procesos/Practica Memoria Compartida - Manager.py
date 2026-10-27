
from multiprocessing import Process, Manager
class MiProceso(Process):

    def __init__(self, nombre, var_compartida):
        super().__init__(name=nombre)
        self.var_compartida = var_compartida


    def run(self):
        print(f'[{self.name}] El valor de la variable compartida es: {self.var_compartida}')
        self.var_compartida[self.name] = f'Me llamo {self.name}'
        print(f'[{self.name}] El nuevo valor de la variable compartida es: {self.var_compartida}')

def instrucciones(lista):
    print(f'[Hijo] El valor de la variable compartida es: {lista}')
    for i in range(len(lista)):
        lista[i] += 1
    print(f'[Hijo] El nuevo valor de la variable compartida es: {lista}')

if __name__ == '__main__':

    with Manager() as manager:
        resultados = manager.dict()
        n = manager.Value('i', 0)
        p1 = MiProceso(nombre='Pepe', var_compartida=resultados)
        p1.start()
        p1.join()
        p2 = MiProceso(nombre='Julia', var_compartida=resultados)
        p2.start()
        p2.join()
        print(f'[Padre] El valor final de la variable es {resultados}')