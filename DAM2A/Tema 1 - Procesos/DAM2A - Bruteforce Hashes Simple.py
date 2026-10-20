# from multiprocessing import Process
import hashlib
import base64
import time

def generar_sha1_b64(texto: str) -> str:
    # 1. Convertir el texto a bytes (UTF-8)
    datos_bytes = texto.encode("utf8")

    # 2. Calcular el hash SHA-1
    hash_sha1 = hashlib.sha1(datos_bytes).digest()

    # 3. Codificar los bytes del hash a Base64 y decodificar a string
    return base64.b64encode(hash_sha1).decode("ascii")

if __name__ == '__main__':

    # f = open('hashes.txt', 'rt', encoding='utf8')
    # hashes = f.readlines()
    # f.close()
    # Es equivalente a
    with open('hashes.txt', 'rt', encoding='utf8') as f:
        hashes = [ hash.strip() for hash in f.readlines()]

    print('Se va a iniciar un proceso.')
    start = time.time()
    for hash in hashes:
        with open('rockyou.txt', 'rt', encoding='latin-1') as f:
            for password in f:
                password = password.strip()
                if generar_sha1_b64(password) == hash:
                    print(f'{hash} -> {password}')
                    break
    end = time.time()
    print(f'Tardó {end-start} segundos')