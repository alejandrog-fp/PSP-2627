from multiprocessing import Process
from threading import Thread

def instrucciones(lista):
    lista.append('mundo')
    print(f'[Hijo] {lista}')

if __name__ == '__main__':

    lista = ['Hola']
    print('----- PROCESS ------')
    p = Process(target=instrucciones , args=[ lista ])
    p.start()
    p.join()

    print(f'[Padre] {lista}')

    print('----- THREAD ------')
    t = Thread(target=instrucciones, args= [ lista ])
    t.start()
    t.join()

    print(f'[Padre] {lista}')