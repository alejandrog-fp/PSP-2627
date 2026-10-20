# Lista de passwords: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz
from multiprocessing import cpu_count
from random import sample
import hashlib
import base64

def generar_sha1_b64(texto: str) -> str:
    # 1. Convertir el texto a bytes (UTF-8)
    datos_bytes = texto.encode("utf8")

    # 2. Calcular el hash SHA-1
    hash_sha1 = hashlib.sha1(datos_bytes).digest()

    # 3. Codificar los bytes del hash a Base64 y decodificar a string
    return base64.b64encode(hash_sha1).decode("ascii")

if __name__ == '__main__':

    N_PASSWORDS = 2*cpu_count()

    passwords = []
    with open('rockyou.txt', 'rt', encoding='latin-1') as f:
        for password in f:
            passwords.append( password.strip() )

    sample_passwords = sample(passwords, N_PASSWORDS)
    with open('passwords.txt', 'wt', encoding='utf8') as f:
        for password in sample_passwords:
            f.write(f'{password}\n')

    hashes = [generar_sha1_b64(password) for password in sample_passwords]

    with open('hashes.txt', 'wt', encoding='utf8') as f:
        for hash in hashes:
            f.write(f'{hash}\n')