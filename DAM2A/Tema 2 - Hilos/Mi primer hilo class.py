from threading import Thread

class MiPrimerHilo(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print('[Hilo] Saludos desde el hilo')

if __name__ == '__main__':

    hilo = MiPrimerHilo()

    hilo.start()
    hilo.join()