from multiprocessing import Process, cpu_count
from math import ceil
from functools import reduce

N_PROCESOS = cpu_count() # 6

def instucciones(numeros: list[int]):
    pass
    # Imprimir por pantalla la suma de todos los numeros
    # ej:
    # instrucciones([1, 2, 3])
    # [Hijo] La suma de [1, 2, 3] es 6
    #
    # Pista: existe la función sum
    # Opción 1
    print(f'{sum(numeros)}')
    # Opción para los amantes de los bucles
    total = 0
    for n in numeros:
        total += n
    print(f'{total}')
    # Opcion para listos
    print(f'{reduce(lambda total, siguiente: total + siguiente, numeros)}')

def dividir_datos(datos, n_trozos):
    # Modificar esta función para que nuca de un trozo vacío
    tamano_trozo = ceil(len(datos) / n_trozos)

    datos_troceados = []

    for i in range(n_trozos):
        inicio = i*tamano_trozo
        fin = inicio + tamano_trozo # = i*tamano_trozo + tamano_trozo = (i+1)*tamano_trozo
        datos_troceados.append( datos[inicio:fin] )

        # datos_troceados.append( datos[i*tamano_trozo:(i+1)*tamano_trozo ])
    # datos_troceados = [ datos[0*tamano_trozo:1*tamano_trozo],
    #                    datos[1*tamano_trozo:2*tamano_trozo],
    #                    datos[2*tamano_trozo:3*tamano_trozo], ...]

    return datos_troceados


if __name__ == '__main__':
    datos = list(range(1024))
    # Generamos lo N_PROCESOS trozos en trozos: list[list[int]]
    datos_troceados = dividir_datos(datos, N_PROCESOS)

    # Creamos N_PROCESOS procesos
    # Idea: guardar los N_PROCESOS en una lista procesos : list[Process]
    procesos = []
    for i in range(N_PROCESOS):
        p = Process(target=instucciones, args=[ datos_troceados[i] ] )
        procesos.append(p)

    # Iniciamos los N_PROCESOS
    for p in procesos:
        p.start()
    # Esperamos a que acaben los N_PROCESOS
    for p in procesos:
        p.join()