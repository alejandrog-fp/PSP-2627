import time
from threading import Thread

def instrucciones():
    print('[Hilo] Saludos desde el hilo')
    time.sleep(3)

if __name__ == '__main__':

    hilo = Thread(target=instrucciones )

    print('[Padre] Iniciamos el hilo')

    hilo.start()

    hilo.join()

    print('[Padre] Se finalizó el hilo')