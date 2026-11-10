from threading import Thread

class MiHilo(Thread):
    def __init__(self, nombre, x, y):
        super().__init__(name=nombre)
        self.x = x
        self.y = y

    def run(self):
        print(f'[{self.name}] Saludos desde el hilo hijo y se me han pasado los siguientes argumentos {self.x=}, {self.y=}')


if __name__ == '__main__':

    t = MiHilo( nombre='Pepe', x=1, y=2 )

    t.start()

    t.join()

    print(f'[Padre] Saludos desde el hilo principal')
