from multiprocessing import Process, current_process, cpu_count, Queue
import hashlib
import base64
import time

N_PROCESOS = cpu_count()

def generar_sha1_b64(texto: str) -> str:
    # 1. Convertir el texto a bytes (UTF-8)
    datos_bytes = texto.encode("utf8")

    # 2. Calcular el hash SHA-1
    hash_sha1 = hashlib.sha1(datos_bytes).digest()

    # 3. Codificar los bytes del hash a Base64 y decodificar a string
    return base64.b64encode(hash_sha1).decode("ascii")

def dividir_datos(datos, n_trozos):

    tamano_trozo = len(datos) // n_trozos
    sobrantes = len(datos) % n_trozos

    datos_troceados = []
    inicio = 0
    for i in range(n_trozos):
        fin = inicio + tamano_trozo + (1 if i < sobrantes else 0)
        datos_troceados.append(datos[inicio:fin])
        inicio = fin

    return datos_troceados

def instrucciones( hash: str, passwords: list[str]) -> None:

    for password in passwords:
        if generar_sha1_b64(password) == hash:
            print(f'[{current_process().name}] {hash} -> {password}')
            break


def instrucciones_queue( hash: str, passwords: list[str], cola: Queue ) -> None:

    for password in passwords:
        if generar_sha1_b64(password) == hash:
            # print(f'[{current_process().name}] {hash} -> {password}')
            cola.put( f'[{current_process().name}] {hash} -> {password}' )
            break

if __name__ == '__main__':

    hash = 'dDrIenB5eYDu55FeW+89uT4AoOw='

    passwords = []
    with open('rockyou.txt', 'rt', encoding='latin-1') as f:
        for password in f:
            passwords.append(password.strip())

    passwords_trozos = dividir_datos(passwords, N_PROCESOS)

    print(f'[{current_process().name}] Se van a iniciar {N_PROCESOS} procesos.')
    # Creación de procesos
    cola = Queue()
    procesos = []
    for i in range(N_PROCESOS):
        p = Process(target=instrucciones_queue ,
                    name=f'Proceso-{i}',
                    args= [ hash, passwords_trozos[i], cola ] )
        procesos.append(p)

    start = time.perf_counter()
    for p in procesos:
        p.start()

    mensaje = cola.get()
    print(mensaje)

    for p in procesos:
        p.kill()

    for p in procesos:
        p.join()
    end = time.perf_counter()
    print(f'[PADRE] Los procesos hijos acabaron. Tardaron {end-start} segundos')

    procesos = []
    for i in range(N_PROCESOS):
        p = Process(target=instrucciones,
                    name=f'Proceso-{i}',
                    args=[hash, passwords_trozos[i]])
        procesos.append(p)

    start = time.perf_counter()
    for p in procesos:
        p.start()

    for p in procesos:
        p.join()
    end = time.perf_counter()
    print(f'[PADRE] Los procesos hijos acabaron. Tardaron {end - start} segundos')