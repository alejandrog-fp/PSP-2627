from multiprocessing import Process
from time import sleep
from os import getpid

def instrucciones():
    hijo_pid = getpid()
    print(f'[HIJO {hijo_pid}] Saludos desde el proceso hijo.')
    sleep(100)
    print(f'[HIJO {hijo_pid}] Hasta luego')

if __name__ == '__main__':

    padre_pid = getpid()
    print(f'[PADRE {padre_pid}] Hola')
    p = Process(target = instrucciones )
    p.start()
    p.join() # Bloquea el proceso padre hasta que acabe el proceso hijo
    print(f'[PADRE {padre_pid}] Adiós')

