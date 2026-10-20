# Script básico de uso de psutil
# Documentación: https://psutil.readthedocs.io/stable/#processes

import psutil

for p in psutil.process_iter():
    if 'python' in p.name().lower():
        print(f'{p.name()}')
        print(f'\tPID: {p.pid}')
        print(f'\tParent PID: {p.ppid()}')
        print(f'\tCMD: {p.cmdline()}')

pid_kill = int(input('Introduzca el PID del proceso que quieres matar: '))
process_kill = psutil.Process(pid_kill)
process_kill.kill()