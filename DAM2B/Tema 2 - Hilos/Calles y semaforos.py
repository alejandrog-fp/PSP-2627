# =============================================================================
# EJERCICIO: Control de acceso con threading.Semaphore
# =============================================================================
#
# CONTEXTO
# Una calle está en obras y solo queda abierto un carril estrecho. Por
# seguridad, como máximo pueden circular 3 coches a la vez. Los demás
# tienen que esperar a que salga alguno.
#
# OBJETIVO
# Usar la clase Semaphore del módulo threading para limitar cuántos hilos
# acceden a la vez a un recurso compartido.
#
# REQUISITOS
# 1. Define una clase Calle:
#    - En el constructor (__init__) crea un atributo de tipo
#      threading.Semaphore con capacidad para 3 hilos.
#    - Define un método pasar(self, nombre) que:
#        a) Muestre "<nombre> espera para entrar en la calle".
#        b) Adquiera el semáforo (mejor con la sentencia `with`).
#        c) Muestre "<nombre> ENTRA en la calle".
#        d) Simule el tiempo que tarda en cruzar con time.sleep(),
#           usando un valor aleatorio entre 1 y 3 segundos.
#        e) Muestre "<nombre> SALE de la calle".
#        f) Libere el semáforo (si usas `with`, se libera solo).
#
# 2. En el programa principal:
#    - Crea un único objeto Calle, que compartirán todos los hilos.
#    - Crea 10 hilos (Coche-1, Coche-2, ..., Coche-10). Cada uno debe
#      ejecutar calle.pasar() con su nombre.
#    - Arranca todos los hilos y espera a que terminen con join().
#    - Al final, muestra "Todos los coches han cruzado la calle".
#
# EJEMPLO DE SALIDA (el orden variará en cada ejecución)
#    Coche-1 espera para entrar en la calle
#    Coche-1 ENTRA en la calle
#    Coche-2 espera para entrar en la calle
#    Coche-2 ENTRA en la calle
#    Coche-3 espera para entrar en la calle
#    Coche-3 ENTRA en la calle
#    Coche-4 espera para entrar en la calle
#    Coche-2 SALE de la calle
#    Coche-4 ENTRA en la calle
#    ...
#    Todos los coches han cruzado la calle
#
# COMPRUEBA QUE...
# - Nunca hay más de 3 mensajes "ENTRA" sin su "SALE" correspondiente.
# - Un coche solo entra cuando otro acaba de salir (si ya hay 3 dentro).
#
# AMPLIACIONES (opcionales)
# A) Añade a Calle un contador de coches dentro y muéstralo al entrar
#    y al salir, p. ej.: "Coche-4 ENTRA (dentro: 3)". Para modificar el
#    contador de forma segura, protégelo con un threading.Lock.
# B) Quita el semáforo y vuelve a ejecutar el programa. ¿Qué ocurre?
#    Explícalo con un comentario.
# C) Investiga la diferencia entre Semaphore y BoundedSemaphore. ¿Qué
#    pasa si llamas a release() más veces que a acquire() con cada uno?
# =============================================================================
