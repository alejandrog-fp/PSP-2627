import time
from multiprocessing import Process
from threading import Thread, RLock, current_thread

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self._candado = RLock()

    def retirar(self, cantidad):
        with self._candado:
            nuevo_saldo = self.saldo - cantidad
            time.sleep(0.1)
            self.saldo = nuevo_saldo
            print(f'[{current_thread().name}] He sacado {cantidad} €')

    def ingresar(self, cantidad):
        with self._candado:
            self.saldo += cantidad

    def transferir(self, otra: CuentaBancaria, cantidad):
        with self._candado:
            self.retirar(cantidad)
            otra.ingresar(cantidad)



if __name__ == '__main__':

    cuenta_bancaria_1 = CuentaBancaria(1_000)
    cuenta_bancaria_2 = CuentaBancaria(600)
    print('Saldos antes de la transferencia.')
    print(f'{cuenta_bancaria_1.saldo=} €')
    print(f'{cuenta_bancaria_2.saldo=} €')

    cuenta_bancaria_1.transferir(cuenta_bancaria_2, 500)

    print('Saldos después de la transferencia.')
    print(f'{cuenta_bancaria_1.saldo=} €')
    print(f'{cuenta_bancaria_2.saldo=} €')