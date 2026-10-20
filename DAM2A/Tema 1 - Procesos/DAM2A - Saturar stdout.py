from multiprocessing import Process

def instrucciones():
    # Escribe 1024 'b'
    for _ in range(1024*8):
        print('b', end='')

if __name__ == '__main__':

    # Instancia proceso hijo
    p = Process(target=instrucciones )
    # Inicia el proceso hijo
    p.start()
    # Escribe 1024 'A'
    for _ in range(1024*8):
        print('A', end='')