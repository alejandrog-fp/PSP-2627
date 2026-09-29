# Ejercicio propuesto 2 del libro

import subprocess

print('Iniciando Google Chrome')
busqueda = input('¿Que quieres buscar? ')
subprocess.run([r'C:\Program Files\Google\Chrome\Application\chrome.exe',
                f'https://www.google.com/search?q={busqueda}'])
print('Se cerró Chrome')