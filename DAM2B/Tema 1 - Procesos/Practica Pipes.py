import time
from multiprocessing import Process, Pipe

class MiProceso(Process):

    def __init__(self, nombre, extremo_pipe):
        super().__init__(name = nombre)
        self.extremo_pipe = extremo_pipe

    def run(self):
        msg = self.extremo_pipe.recv()
        print(f'[{self.name}] He recibido el mensaje: {msg}')
        time.sleep(5)
        self.extremo_pipe.send('Hola padre')

if __name__ == '__main__':

    extremo_hijo, extremo_padre = Pipe(duplex=False)

    p = MiProceso('Hijo', extremo_hijo)
    p.start()

    extremo_padre.send('Hola hijo')
    print('[Padre] Esperando respuesta de mi hijo')
    msg = extremo_padre.recv() # Linea bloqueante
    print(f'[Padre] He recibido el mensaje: {msg}')