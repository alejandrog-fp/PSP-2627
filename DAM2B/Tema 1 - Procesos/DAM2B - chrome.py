import subprocess

busqueda = input('¿Que quieres buscar?')

subprocess.run(
    [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
     f'https://www.google.com/search?q={busqueda}'
     ]
)