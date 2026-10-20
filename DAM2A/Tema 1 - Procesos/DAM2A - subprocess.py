# Script básico de uso de subprocess
# Documentación: https://docs.python.org/3/library/subprocess.html

import subprocess
import os

print(f'Proceso iniciado PID: {os.getpid()}')
# subprocess.run('python "DAM2A - sleep.py"')
# subprocess.run(['python' , 'DAM2A - sleep.py'])
subprocess.Popen(['python' , 'DAM2A - sleep.py']) # No bloquea la ejecución
print('Proceso finalizado')