import hashlib
import base64
from multiprocessing import Process, cpu_count, current_process, Event
import time

def generar_sha1_b64(texto: str) -> str:
    # 1. Convertir el texto a bytes (UTF-8)
    datos_bytes = texto.encode("utf8")

    # 2. Calcular el hash SHA-1
    hash_sha1 = hashlib.sha1(datos_bytes).digest()

    # 3. Codificar los bytes del hash a Base64 y decodificar a string
    return base64.b64encode(hash_sha1).decode("ascii")

def trocear_lista(lista: list, n_trozos: int) -> list[list]:
    tamano_trozo = len(lista) // n_trozos
    sobrantes = len(lista) % n_trozos

    lista_troceada = []
    inicio = 0
    for i in range(n_trozos):
        if i < sobrantes:
            fin = inicio + tamano_trozo + 1
        else:
            fin = inicio + tamano_trozo
        lista_troceada.append( lista[inicio:fin] )
        inicio = fin

    return lista_troceada

def instrucciones(hash, passwords) -> None:
    for password in passwords:
        if generar_sha1_b64(password) == hash:
            print(f'[{current_process().name}] {hash} -> {password}')
            break

def instrucciones_evento(hash, passwords, bandera) -> None:
    nombre = current_process().name
    for i, password in enumerate(passwords):
        # Cada 100 intentos, comprobar si otro proceso ya lo encontró
        if i % 100 == 0 and bandera.is_set():
            print(f'[{nombre}] Otro proceso ha encontrado el password')
            break

        if generar_sha1_b64(password) == hash:
            print(f'[{nombre}] {hash} -> {password}')
            bandera.set()
            break
    else:
        print(f'[{nombre}] Otro proceso ha encontrado el password')
        
if __name__ == '__main__':

    N_PROCESS = cpu_count()

    # print('[PADRE] Inicio lectura hashes.txt')
    # with open('hashes.txt', 'rt', encoding='utf8') as f:
    #     hashes = [hash.strip() for hash in f.readlines()]
    #
    # hash = hashes[0]
    hash = 'dDrIenB5eYDu55FeW+89uT4AoOw='

    # print('[PADRE] Fin lectura hashes.txt')

    print('[PADRE] Inicio lectura rockyou.txt')
    with open('rockyou.txt' , 'rt', encoding='latin-1') as f:
        passwords = [password.strip() for password in f.readlines()]
    print('[PADRE] Fin lectura rockyou.txt')

    print('[PADRE] Repartimos los hashes')
    passwords_troceados = trocear_lista(passwords, N_PROCESS)

    print(f'[PADRE] Voy a crear {N_PROCESS} procesos')
    procesos = []
    bandera = Event()
    for i in range(N_PROCESS):
        p = Process(target = instrucciones_evento ,
                    args = [ hash, passwords_troceados[i], bandera ] ,
                    name = f'Proceso-{i}')
        procesos.append(p)

    print('[PADRE] Los procesos están creados y listos para ejecutarlos.')

    start = time.perf_counter()
    for p in procesos:
        p.start()

    for p in procesos:
        p.join()
    stop = time.perf_counter()
    print(f'[PADRE] Todos los procesos han finalizado correctamente y han tardado {stop-start} segundos')

    print(f'[PADRE] Voy a crear {N_PROCESS} procesos')
    procesos = []

    for i in range(N_PROCESS):
        p = Process(target=instrucciones,
                    args=[hash, passwords_troceados[i]],
                    name=f'Proceso-{i}')
        procesos.append(p)

    print('[PADRE] Los procesos están creados y listos para ejecutarlos.')

    start = time.perf_counter()
    for p in procesos:
        p.start()

    for p in procesos:
        p.join()
    stop = time.perf_counter()
    print(f'[PADRE] Todos los procesos han finalizado correctamente y han tardado {stop - start} segundos')