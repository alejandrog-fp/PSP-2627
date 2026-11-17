from threading import Thread, Barrier
import time
import random

def cargar_configuracion():
    time.sleep(random.randint(2, 6))

def cliente():
    cargar_configuracion()
    print('Cliente listo !')
    barrera.wait()
    print('Cliente Funcionando')

def servidor():
    cargar_configuracion()
    print('Servidor Listo !')
    barrera.wait()
    print('Servidor Funcionando')

if __name__ == '__main__':

    barrera = Barrier(2)

    c_hilo = Thread(target=cliente)
    s_hilo = Thread(target=servidor)

    c_hilo.start()
    s_hilo.start()

    c_hilo.join()
    s_hilo.join()

