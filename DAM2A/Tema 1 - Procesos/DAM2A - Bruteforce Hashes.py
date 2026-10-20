from multiprocessing import Process, cpu_count, current_process
import hashlib
import base64

N_PROCESS = cpu_count()

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

def break_hashes(hashes: list[str]) -> None:
    for hash in hashes:
        with open('rockyou.txt', 'rt', encoding='latin-1') as file:
            for password in file:
                if generar_sha1_b64(password.strip()) == hash:
                    print(f'[{current_process().name}] {hash} -> {password.strip()}')
                    break

if __name__ == '__main__':

    with open('hashes.txt', 'rt', encoding='utf8') as file:
        hashes = [hash.strip() for hash in file.readlines()]

    # with open('passwords.txt', 'rt', encoding='utf8') as file:
    #     passwords = [password.strip() for password in file.readlines()]

    hashes_trozos = dividir_datos(hashes, N_PROCESS)

    procesos = []
    for i in range(N_PROCESS):
        p = Process(target=break_hashes, name=f'Proceso-{i}', args=(hashes_trozos[i],))
        procesos.append(p)

    for p in procesos:
        p.start()

    print('[Padre] Esperando a que acaben los procesos')
    for p in procesos:
        p.join()