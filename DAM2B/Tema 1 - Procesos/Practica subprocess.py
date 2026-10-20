import subprocess
import os

print(os.getcwd())
#subprocess.run('python "Practica sleep.py"')
#subprocess.run(['python', 'Practica sleep.py']) # Bloqueante
subprocess.Popen(['python', 'Practica sleep.py'])
print('Se acabo')