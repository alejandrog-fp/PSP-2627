import time
from threading import Thread, Lock
from multiprocessing import Process


class CuentaCorriente:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.candado = Lock()

    def retirar(self, cantidad):
        with self.candado:
            if cantidad <= self.saldo:
                nuevo_saldo = self.saldo - cantidad
                time.sleep(0.1)
                self.saldo = nuevo_saldo
                print(f'He retirado {cantidad} €')
            else:
                print('No se ha podido retirar el dinero.')

if __name__ == '__main__':

    mi_cuenta_corriente = CuentaCorriente(1_000)
    hilos = []
    for i in range(4):
        t = Thread(target=mi_cuenta_corriente.retirar, args= [ 500 ])
        hilos.append(t)

    for t in hilos:
        t.start()
    for t in hilos:
        t.join()

    print(f'Saldo final: {mi_cuenta_corriente.saldo} €')
