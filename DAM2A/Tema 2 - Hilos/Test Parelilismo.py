from multiprocessing import Process
import time
from threading import Thread


def instrucciones(inicio, fin):
    total = 0
    for i in range(inicio, fin):
        total += i**2

if __name__ == '__main__':

    p = Process(target=instrucciones, args=[0, 10_000_000])

    start = time.perf_counter()

    p.start()
    p.join()

    end = time.perf_counter()

    print(f'1 Proceso ha tardado {end - start } segundos')

    p1 = Process(target=instrucciones, args=[0, 5_000_000])
    p2 = Process(target=instrucciones, args=[5_000_000, 10_000_000])

    start = time.perf_counter()

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.perf_counter()

    print(f'2 Procesos han tardado {end - start} segundos')

    p = Thread(target=instrucciones, args=[0, 10_000_000])

    start = time.perf_counter()

    p.start()
    p.join()

    end = time.perf_counter()

    print(f'1 Hilo ha tardado {end - start} segundos')

    p1 = Thread(target=instrucciones, args=[0, 5_000_000])
    p2 = Thread(target=instrucciones, args=[5_000_000, 10_000_000])

    start = time.perf_counter()

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.perf_counter()

    print(f'2 Hilos han tardado {end - start} segundos')