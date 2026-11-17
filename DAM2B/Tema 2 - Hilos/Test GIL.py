import time
from threading import Thread


def contar_primos(inicio: int, fin: int) -> int:
    total = 0
    for n in range(max(inicio, 2), fin):
        if all(n % d for d in range(2, int(n ** 0.5) + 1)):
            total += 1
    print(total)
    return total

if __name__ == '__main__':

    N = 400_000
    n_hilos = 4

    print('Vamos a contar cuantos primos hay usando un único hilo')
    start = time.perf_counter()

    contar_primos(2, N)

    end = time.perf_counter()

    print(f'He tardado {end- start} segundos usando un único hilo')

    print(f'Vamos a contar cuantos primos hay usando {n_hilos} hilos')
    hilos = []

    for i in range(n_hilos):
        h = Thread(target=contar_primos, args=[i * (N // n_hilos), (i+1) * (N // n_hilos)])
        hilos.append(h)


    start = time.perf_counter()

    for h in hilos:
        h.start()

    for h in hilos:
        h.join()

    end = time.perf_counter()

    print(f'He tardado {end - start} segundos usando {n_hilos} hilos')