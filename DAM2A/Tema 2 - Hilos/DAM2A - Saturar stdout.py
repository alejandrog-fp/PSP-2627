from threading import Thread

def instrucciones():
    for _ in range(1024):
        print('b', end='')

if __name__ == '__main__':
    h = Thread(target=instrucciones)
    h.start()

    for _ in range(1024):
        print('A', end='')