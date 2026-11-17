import time
from threading import Thread, Lock, RLock
from multiprocessing import Process


class CuentaCorriente:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.candado = RLock()

    def retirar(self, cantidad):
        with self.candado:
            if cantidad <= self.saldo:
                nuevo_saldo = self.saldo - cantidad
                time.sleep(0.1)
                self.saldo = nuevo_saldo
                print(f'He retirado {cantidad} €')
            else:
                print('No se ha podido retirar el dinero.')

    def ingresar(self, cantidad):
        with self.candado:
            self.saldo += cantidad

    def transferir(self, destino, cantidad):
        with self.candado:
            self.retirar(cantidad)
            destino.ingresar(cantidad)

if __name__ == '__main__':

    mi_cuenta_corriente = CuentaCorriente(1_000)
    otra_cuenta_corriente = CuentaCorriente(500)

    mi_cuenta_corriente.transferir(otra_cuenta_corriente, 100)
    print(f'Tengo {mi_cuenta_corriente.saldo} €')
    print(f'La otra cuenta tiene {otra_cuenta_corriente.saldo} €')

    # hilos = []
    # for i in range(4):
    #     t = Thread(target=mi_cuenta_corriente.retirar, args= [ 500 ])
    #     hilos.append(t)
    #
    # for t in hilos:
    #     t.start()
    # for t in hilos:
    #     t.join()

