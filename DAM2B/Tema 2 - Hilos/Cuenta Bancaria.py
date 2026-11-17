import time
from multiprocessing import Process
from threading import Thread, Lock, current_thread

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self._candado = Lock()

    def retirar(self, cantidad):
        # self._candado.acquire() # Linea bloqueante si el candado está ocupado
        # nuevo_saldo = self.saldo - cantidad
        # time.sleep(0.1)
        # self.saldo = nuevo_saldo
        # self._candado.release()
        # O equivalentemente usando with
        with self._candado:
            nuevo_saldo = self.saldo - cantidad
            time.sleep(0.1)
            self.saldo = nuevo_saldo
            print(f'[{current_thread().name}] He sacado {cantidad} €')



if __name__ == '__main__':

    cuenta_bancaria = CuentaBancaria(1_000)

    hilos= []
    for nombre in ['Álvaro', 'Manolo', 'Jacinta', 'Juana']:
        t = Thread(target=cuenta_bancaria.retirar, args=[ 500 ], name=nombre)
        hilos.append(t)

    for t in hilos:
        t.start()

    for t in hilos:
        t.join()

    print(f'En la cuenta bancaria queda {cuenta_bancaria.saldo} €')
