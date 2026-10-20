import subprocess
import os

print(os.getcwd())
#subprocess.run('python "DAM2B - sleep.py"')
#subprocess.run(['python', 'DAM2B - sleep.py']) # Bloqueante
subprocess.Popen(['python', 'DAM2B - sleep.py'])
print('Se acabo')