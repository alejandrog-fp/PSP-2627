import subprocess

p = subprocess.run(['ping', '127.0.0.1', '-n', '1'], capture_output=True, encoding='cp850')

print(p.stdout)
print(type(p.stdout))

