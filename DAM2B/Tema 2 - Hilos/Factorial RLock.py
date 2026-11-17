from threading import RLock

candado = RLock()

def factorial(n):
    with candado:
        if n == 1:
            return 1
        else:
            return factorial(n - 1) * n

print(factorial(5))
