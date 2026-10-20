from multiprocessing import Process

class ProcesoHijo(Process):

    def __init__(self, nombre, argumento):
        super().__init__(name=nombre)
        self.argumento = argumento

    def run(self):
        print(f'Saludos desde el proceso hijo. Me llamo {self.name} y me has pasado como argumento: {self.argumento}')

if __name__ == '__main__':

    print('Saludos desde el proceso padre.')

    p = ProcesoHijo('Pepe', 'Hola')
    p.start()
