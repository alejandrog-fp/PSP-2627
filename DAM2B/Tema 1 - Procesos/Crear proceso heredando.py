from multiprocessing import Process

class MiProceso(Process):

    def __init__(self, nombre, argumento):
        super().__init__(name= nombre) # Llamada al constructor de la superclase (Process)
        self.argumento = argumento

    def run(self) -> None:
        print(f'[{self.name}] Saludos desde el proceso hijo con PID: {self.pid}')
        print(f'[{self.name}] Y se me ha pasado el argumento {self.argumento}')

if __name__ == '__main__':

    print('[Padre] Saludos desde el proceso padre')

    p = MiProceso('Juan', 'hola')

    p.start()
    p.join()

    print('[Padre] Adios')