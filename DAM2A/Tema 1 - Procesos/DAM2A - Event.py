from multiprocessing import Process, Event
from time import sleep

def instrucciones(bandera: Event) -> None:
    print(f'[Proceso 1] El estado de la bandera es {bandera.is_set()}')
    bandera.set()
    sleep(4)
    print(f'[Proceso 1] El estado de la bandera es {bandera.is_set()}')

def instrucciones_2(bandera: Event) -> None:
    sleep(2)
    print(f'[Proceso 2] El estado de la bandera es {bandera.is_set()}')
    bandera.clear()

if __name__ == '__main__':

    bandera = Event()

    p1 = Process(target = instrucciones, args = [bandera])
    p2 = Process(target = instrucciones_2, args = [bandera])

    p1.start()
    p2.start()

    p1.join()
    p2.join()