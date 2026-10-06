# Proceso Padre:
# 1. Genera una lista que contiene tantas listas como núcleos tiene el ordenador ( multiprocessing.cpu_count() ). Cada una de estas listas internas tiene 10 números enteros generados de manera aleatoria entre 1 y 10 ( random.randint(1, 10) ).
# Ejemplo de datos para 2 núcleos/procesos y 3 números -> [ [1, 3, 5], [2, 4, 6] ]
# 2. Crea tantos procesos hijos como núcleos tiene el ordenador. A cada proceso hijo se le manda una de las listas con números
# 3. Espera a que acaben todos los procesos hijos.

# Procesos hijos: recibe una lista de números enteros e imprime por pantalla la suma, indicando su PID
# PISTA: El pid se puede obtener a partir de la función os.getpid()
