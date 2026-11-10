from threading import Thread, current_thread

def instrucciones(x, y):
    print(f'[{current_thread().name}] Saludos desde el hilo hijo y se me han pasado los siguientes argumentos {x=}, {y=}')

if __name__ == '__main__':

    t = Thread(target=instrucciones, name='Pepe', kwargs={'x': 1, 'y' : 2} )

    t.start()

    t.join()

    print(f'[Padre] Saludos desde el hilo principal')

