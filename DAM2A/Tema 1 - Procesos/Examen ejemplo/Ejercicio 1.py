import json
from multiprocessing import Process, Queue, current_process
import os


def instrucciones(numeros: list[int], cola: Queue) -> None:
    resultado = 54
    cola.put( {'nombre' : current_process().name, 'PID': current_process().pid, 'resultado' : resultado})

if __name__ == '__main__':

    with open('data.json', 'r') as file:
        data: dict[str, list[int]] = json.load(file)

    trabajadores = []
    cola = Queue()
    for nombre, numeros in data.items():
        trabajador = Process(target=instrucciones, name=nombre , args= [numeros, cola ])
        trabajadores.append(trabajador)

    for trabajador in trabajadores:
        trabajador.start()

    for trabajador in trabajadores:
        trabajador.join()

    while not cola.empty():
        print(cola.get())