import psutil

for p in psutil.process_iter():
    # if 'python.exe' == p.name().lower():
    if 'python' in p.name().lower():
        print(f'{p.name()=}')
        print(f'\t{p.cmdline()=}')
        print(f'\t{p.pid=}')
        print(f'\t{p.ppid()=}')

pid_kill = int(input('¿Que proceso quieres matar? '))
process_kill = psutil.Process(pid_kill)
process_kill.kill()