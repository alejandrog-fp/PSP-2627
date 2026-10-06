import subprocess
import os

print('Proceso padre:', os.getpid())
p = subprocess.Popen(['python', 'suma_numeros.py'],
                     stdout=subprocess.PIPE,
                     stdin=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     text=True)

print('Proceso hijo', p.pid)
p.stdin.write('1\n')
p.stdin.flush()

p.stdin.write('2\n')
p.stdin.flush()

p.stdin.write('\n')
p.stdin.flush()

print(p.stdout.read())