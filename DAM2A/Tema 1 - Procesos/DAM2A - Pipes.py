import time
from multiprocessing import Process, Pipe

class ProcesoHijo(Process):
    def __init__(self, nombre, extremo_conexion):
        super().__init__(name=nombre)
        self.extremo_conexion = extremo_conexion

    def run(self):
        msg = self.extremo_conexion.recv()
        print(f'[{self.name}] Mi padre me ha dicho: {msg}')
        print(f'[{self.name}] Me voy a dormir 5 segunditos.')
        time.sleep(5)
        self.extremo_conexion.send('Ya me desperté padre. Buenos días')
if __name__ == '__main__':

    extremo_hijo , extremo_padre = Pipe()

    p = ProcesoHijo('Juan', extremo_hijo)
    p.start()
    extremo_padre.send('Hola hijo')

    print('[Padre] Esperando la respuesta de mi hijo')
    res = extremo_padre.recv() # Linea bloqueante
    print(f'[Padre] Mi hijo me ha dicho: {res}')
