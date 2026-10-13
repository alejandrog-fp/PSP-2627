from multiprocessing import Process, current_process, cpu_count
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

def instrucciones( hashes: list[str] ) -> None:

    for hash in hashes:
        with open('rockyou.txt', 'rt', encoding='latin-1') as f:
            for password in f:
                password = password.strip()
                if generar_sha1_b64(password) == hash:
                    print(f'[{current_process().name}]{hash} -> {password}')
                    break


if __name__ == '__main__':

    # f = open('hashes.txt', 'rt', encoding='utf8')
    # hashes = f.readlines()
    # f.close()
    # Es equivalente a
    with open('hashes.txt', 'rt', encoding='utf8') as f:
        hashes = [ hash.strip() for hash in f.readlines()]
    # Trocear los hashes

    hashes_trozos = dividir_datos(hashes, N_PROCESOS)

    print(f'[{current_process().name}] Se van a iniciar {N_PROCESOS} procesos.')
    # Creación de procesos
    procesos = []
    for i in range(N_PROCESOS):
        p = Process(target=instrucciones ,
                    name=f'Proceso-{i}',
                    args= [ hashes_trozos[i] ] )
        procesos.append(p)

    start = time.time()
    for p in procesos:
        p.start()

    for p in procesos:
        p.join()
    end = time.time()
    print(f'[PADRE] Los procesos hijos acabaron. Tardaron {end-start} segundos')