# Crea un proceso que se le pase como argumento una lista con el elemento 'hola' y le añade 'mundo'
# El hijo muestra el contenido de la lista
# Una vez finalizado el proceso hijo, el padre muestra el contenido de la lista.
# Crea un hilo que se le pase como argumento una lista con el elemento 'hola' y le añade 'mundo'
# El hijo muestra el contenido de la lista
# Una vez finalizado el proceso hijo, el padre muestra el contenido de la lista.

def instrucciones(lista):
    lista.append('mundo')
    print(lista)