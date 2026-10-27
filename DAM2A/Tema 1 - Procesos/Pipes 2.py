from multiprocessing import Process, Pipe
from multiprocessing.connection import PipeConnection


class MiProceso(Process):

    def __init__(self, extremo_conn: PipeConnection):
        super().__init__()
        self.extremo_conn = extremo_conn

    def run(self):
        msg = self.extremo_conn.recv()
        while msg:
            print(f'[Hijo] Mi padre me dice: {msg}')
            msg = self.extremo_conn.recv()

        # while msg := self.extremo_conn.recv():
        #     print(f'[Hijo] Mi padre me dice: {msg}')

        print('[Hijo] Adios')

if __name__ == '__main__':

    extremo_hijo , extremo_padre = Pipe(duplex=False)

    p = MiProceso(extremo_hijo)
    p.start()

    while True:
        msg = input('Introduce lo que quieres decirle a tu hijo: ')
        extremo_padre.send(msg)
        if not msg:
            break


    print('[Padre] Adios')