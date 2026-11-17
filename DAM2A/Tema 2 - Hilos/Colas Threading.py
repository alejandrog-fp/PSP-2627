import threading
import queue


class Hilo(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        cola.put('test') # No hace falta pasar la referencia de la cola !!

if __name__ == '__main__':

    cola = queue.Queue()

    h = Hilo()
    h.start()
    h.join()

    print(cola.get())

# Esto no se puede hacer en multiprocesing !!
# import multiprocessing
#
# class Proceso(multiprocessing.Process):
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         cola.put('test')
#
# if __name__ == '__main__':
#
#     cola = multiprocessing.Queue()
#
#     p = Proceso()
#     p.start()
#     p.join()
#
#     print(cola.get())