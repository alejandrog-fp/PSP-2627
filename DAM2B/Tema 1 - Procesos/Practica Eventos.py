import time
from multiprocessing import Process, Event

class MiProceso(Process):
    def __init__(self, bandera: Event):
        super().__init__()
        self.bandera = bandera

    def run(self):
        print(f'[Hijo] La bandera está {self.bandera.is_set()}')
        time.sleep(5)
        print(f'[Hijo] La bandera está {self.bandera.is_set()}')
        self.bandera.clear()

if __name__ == '__main__':

    bandera = Event()

    p = MiProceso(bandera)
    p.start()
    time.sleep(1)

    bandera.set()

    p.join()
    print(f'[Padre] La bandera está {bandera.is_set()}')