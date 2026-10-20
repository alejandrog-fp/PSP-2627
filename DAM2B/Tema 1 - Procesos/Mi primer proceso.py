from multiprocessing import Process
from time import sleep
from os import getpid

def instrucciones(herramienta, lugar):

    print(f"[Hijo] Soy el trabajador {getpid()} y estoy usando un {herramienta} en {lugar}")


if __name__ == '__main__':
    print(f'[Padre] Saludos soy el padre {getpid()}')
    p = Process(target=instrucciones, args=[ 'mi casa', 'martillo'] )
    p2 = Process(target=instrucciones, kwargs=
    {
        'lugar' : 'la oficina',
        'herramienta' : 'cincel'
    })

    p.start()
    p2.start()
    p.join()
    p2.join()

    print('[Padre] Adios desde el padre')