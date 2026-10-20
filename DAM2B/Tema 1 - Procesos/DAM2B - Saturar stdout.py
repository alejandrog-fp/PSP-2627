# # Padre:
# 1. Crea el proceso hijo
# 2. Inicia el proceso hijo
# 3. Escribe 1024 'A'
#
# # Hijo
# Escribe 1024 'b'

import multiprocessing as mp

def instrucciones():
    # for _ in range(1024):
    #     print('b', end='')
    print('b' * 1024)

if __name__ == '__main__':

    mp.Process(target=instrucciones).start()
    # for _ in range(1024):
    #     print('A', end='')
    print('A' * 1024)
