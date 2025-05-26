# Algoritmo: Encontrando el Valor Mínimo en una Lista

## Introducción: La Búsqueda del Menor Elemento

Una de las tareas más fundamentales en la programación es analizar una colección de datos y extraer información clave. El problema que este algoritmo resuelve es, en apariencia, muy simple: dada una lista de números, ¿cómo podemos encontrar de manera confiable cuál de ellos es el más pequeño?

Aunque para un humano la respuesta pueda parecer obvia al mirar un grupo pequeño de números, una computadora necesita un proceso metódico e infalible para llegar al mismo resultado, sin importar si la lista tiene cinco elementos o cinco millones. Este algoritmo establece precisamente ese proceso.

## El Planteamiento: ¿Cómo se llegó a la solución?

La estrategia para resolver este problema imita la lógica que usaríamos en la vida real. Imaginemos que nos dan una baraja de cartas, cada una con un número, y nos piden encontrar la carta con el valor más bajo sin poder verlas todas a la vez.

El proceso mental sería el siguiente:
1.  **Establecer un Punto de Partida:** Tomamos la primera carta de la baraja y, de manera provisional, declaramos que esa es la más baja que hemos visto hasta ahora. No tenemos más información, así que es nuestra única referencia. Esto corresponde a `minimo = lista[0]`.
2.  **Recorrer y Comparar:** Luego, vamos pasando una por una el resto de las cartas de la baraja. Por cada nueva carta que vemos, la comparamos con la que tenemos en la mano como "la más baja hasta ahora".
3.  **Actualizar al Campeón:** Si la nueva carta tiene un valor menor que nuestra carta "campeona" provisional, la descartamos y nos quedamos con la nueva. Esta nueva carta se convierte en nuestra nueva referencia del valor más bajo encontrado. Esto es lo que hace la línea `if numero < minimo: minimo = numero`.
4.  **Llegar a la Conclusión:** Una vez que hemos revisado todas las cartas de la baraja, la que nos queda en la mano como "la más baja" es, con total certeza, la carta con el valor mínimo de todo el conjunto. Este es el valor que retornamos.

Este método, conocido como **búsqueda lineal**, es simple, robusto y garantiza encontrar el mínimo al asegurar que cada elemento ha sido considerado.

## Las Herramientas: ¿Qué se usó en el código?

La implementación de esta lógica requiere herramientas muy básicas de programación:

* **Variable de Referencia (`minimo`):** Se usa una variable para mantener en memoria el valor más pequeño que se ha encontrado *hasta el momento* en el recorrido de la lista. Su correcta inicialización con el primer elemento de la lista es clave para que las comparaciones posteriores funcionen.
* **Bucle `for`:** Es la estructura que nos permite ejecutar la acción de "recorrer y comparar" para cada uno de los elementos de la lista, sin saltarnos ninguno.
* **Condicional `if`:** Es el centro de la toma de decisiones. En cada paso del bucle, compara el elemento actual con nuestro mínimo de referencia y decide si es necesario actualizarlo.

## Análisis de Complejidad

* **Complejidad Temporal: `O(n)`** donde `n` es el número de elementos en la lista. Esto se debe a que, para garantizar que hemos encontrado el mínimo absoluto, estamos obligados a visitar cada elemento de la lista al menos una vez. El tiempo de ejecución crece de forma lineal con el tamaño de la lista.
* **Complejidad Espacial: `O(1)`** (Constante). El algoritmo es muy eficiente en memoria. Solo necesita espacio para una variable adicional (`minimo`), sin importar si la lista tiene 10 o 10 millones de elementos.

