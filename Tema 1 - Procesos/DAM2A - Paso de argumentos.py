import os
from multiprocessing import Process

def instrucciones(herramienta, lugar):
    print(f'[HIJO {os.getpid()}] Estoy usando un {herramienta} en {lugar}')

if __name__ == '__main__':

    p1 = Process(target=instrucciones, kwargs={
        'lugar': 'mi casa',
        'herramienta': 'martillo'
    })
    p2 = Process(target=instrucciones, args=['cincel', 'la oficina'])
    p1.start()
    p2.start()