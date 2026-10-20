# Ejercicio 1

Crea un script que realice las siguientes instrucciones:
1. Cargue la información almacenada en el archivo ``data.json``.
   La manera de cargar dicha información se haría con las siguientes líneas de código:
```python
import json

with open('data.json', 'r') as file:
    data : dict[str, list[int]] = json.load(file)
```
La información está estructurada en un diccionario donde las **claves** son los nombres de los trabajadores y los **valores** son los datos que tienen que procesar.
2. Crear tantos trabajadores (procesos) como elementos haya definido en el diccionario con los datos. Pista: [Loop Dictionaries](https://www.w3schools.com/python/python_dictionaries_loop.asp)
3. Cada trabajador debe recibir **su nombre**, **la lista con los números** que debe procesar y la **cola** que usará para comunicar los resultados.
4. Los trabajadores deberán calcular el producto de todos los números que aparecen en la lista que han recibido. Una vez hecho el cálculo deberán ponerlo en la cola usando un diccionario con la estructura `{'nombre': nombre del trabajador, 'PID': PID del trabajador, 'resultado': producto de todos los números}`
5. Una vez que hayan acabado todos los trabajadores (procesos hijo), el proceso padre obtendrá de la cola todos los resultados, los imprimirá por pantalla y calculará la suma de todos los resultados.

Ejemplo de output:
````commandline
c:\examen> python ejercicio_1.py
El trabajador Trabajador_1 con PID=25308 ha obtenido el resultado 1399934251911313210941532696320000
El trabajador Trabajador_2 con PID=10156 ha obtenido el resultado 366865527694253279852160000000
El trabajador Trabajador_3 con PID=1640 ha obtenido el resultado 8306705423085155226502617492357120
El trabajador Trabajador_4 con PID=25572 ha obtenido el resultado 1751612862296136423493324800000
La suma total es: 9708758153386458827147495673477120
````
# Ejercicio 2

Crea un script que simule una comunicación **bidireccional** entre un **cliente** y un **servidor** en la cual hay un **hacker** interceptando los mensajes. Cada uno de estos agentes será un proceso distinto.
> cliente <-----> hacker <-----> servidor
0. El proceso padre solicita una contraseña que pasará como argumento al proceso **cliente**.
1. El **cliente** envía su contraseña junto con su PID al hacker usando un diccionario con la estructura ``{'PID': pid, 'contrasena': contrasena}``.
2. El **hacker** recibe el mensaje enviado por el **cliente**. Modifica el valor del PID del **cliente** poniendo el suyo y lo envía al **servidor** manteniendo la misma estructura.
3. El **servidor** recibe el mensaje enviado por el **hacker** y muestra la información recibida. Responde al hacker con un mensaje de bienvenida indicando el PID con el que se ha registrado.
4. El **hacker** recibe el mensaje enviado por el **servidor**, modifica el mensaje recibido cambiando el PID del mensaje por el PID del cliente y se lo reenvia al **cliente**.
5. El **cliente** muestra el mensaje que le ha enviado el **hacker**.

Ejemplo de output (entre corchetes se indica que proceso ha ejecutado cada ``print``):
````commandline
c:\examen> python ejercicio_2.py
Introduzca la contraseña con la que se va a registrar el cliente: 1234
[Cliente] El cliente con PID=22948 se va a registrar en el servidor con la contrasena: 1234
[Cliente] Esperando respuesta del servidor
[Hacker] Interceptado mensaje del cliente: {'PID': 22948, 'contrasena': '1234'}
[Hacker] Voy a registrarme en el servidor con mi PID=25652 y la contraseña 1234
[Servidor] Se ha registrado el usuario con PID=25652 y contrasena: 1234
[Hacker] El servidor me ha mandado el siguiente mensaje: [Servidor] Bienvenido usuario con PID=25652
[Hacker] Remplazo mi PID con el PID del cliente y envio el mensaje al cliente.
[Cliente] Respuesta del servidor: [Servidor] Bienvenido usuario con PID=22948
````