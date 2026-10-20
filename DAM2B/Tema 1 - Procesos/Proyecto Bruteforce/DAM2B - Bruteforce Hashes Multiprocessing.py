import hashlib
import base64
from multiprocessing import Process, cpu_count, current_process

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

def instrucciones(hashes, passwords) -> None:
    for hash in hashes:
        for password in passwords:
            if generar_sha1_b64(password) == hash:
                print(f'[{current_process().name}] {hash} -> {password}')
                break


if __name__ == '__main__':

    N_PROCESS = cpu_count()

    print('[PADRE] Inicio lectura hashes.txt')
    with open('hashes.txt', 'rt', encoding='utf8') as f:
        hashes = [hash.strip() for hash in f.readlines()]
    print('[PADRE] Fin lectura hashes.txt')

    print('[PADRE] Inicio lectura rockyou.txt')
    with open('rockyou.txt' , 'rt', encoding='latin-1') as f:
        passwords = [password.strip() for password in f.readlines()]
    print('[PADRE] Fin lectura rockyou.txt')

    print('[PADRE] Repartimos los hashes')
    hashes_troceados = trocear_lista(hashes, N_PROCESS)

    print(f'[PADRE] Voy a crear {N_PROCESS} procesos')
    procesos = []
    for i in range(N_PROCESS):
        p = Process(target = instrucciones ,
                    args = [hashes_troceados[i], passwords ] ,
                    name = f'Proceso-{i}')
        procesos.append(p)

    print('[PADRE] Los procesos están creados y listos para ejecutarlos.')

    for p in procesos:
        p.start()

    for p in procesos:
        p.join()

    print('[PADRE] Todos los procesos han finalizado correctamente')