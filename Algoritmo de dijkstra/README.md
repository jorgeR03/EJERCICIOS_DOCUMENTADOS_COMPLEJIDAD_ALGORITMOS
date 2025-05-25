# Algoritmo de Dijkstra: Encontrando el Camino Más Corto

## Introducción: El Problema del Viajero Eficiente

Imaginemos que estamos en la ciudad 'A' y queremos saber la ruta más corta para llegar no solo a un destino, sino a *todos* los demás puntos de interés ('B', 'C', 'D', etc.). Tenemos un mapa que nos indica el "costo" o "distancia" para ir de un punto a otro directamente conectado. Este es, en esencia, el problema que el algoritmo de Dijkstra busca resolver: encontrar el camino de menor costo desde un único punto de origen a todos los demás nodos en una red o grafo.

Fue concebido por el científico de la computación Edsger W. Dijkstra en 1956 y es la base de muchos sistemas de navegación modernos, como los GPS, que calculan la ruta más rápida entre dos lugares.

## El Planteamiento: ¿Cómo se llegó a la solución?

Ante este problema, una primera idea podría ser intentar todas las rutas posibles, sumarlas y quedarnos con la más corta. Sin embargo, en un mapa medianamente complejo, la cantidad de caminos explota exponencialmente, volviendo esta solución impracticable.

Dijkstra propuso un enfoque mucho más inteligente y eficiente, basado en una estrategia "codiciosa" (greedy). La idea es simple pero poderosa: **avanzar siempre por el camino que, hasta el momento, parezca ser el más corto**.

El razonamiento se desenvuelve así:
1.  Comenzamos en nuestro punto de origen (el nodo 'A'). La distancia para llegar a 'A' desde 'A' es, lógicamente, 0. Para todos los demás destinos, como aún no sabemos cómo llegar, asumimos que la distancia es infinita.
2.  Desde 'A', miramos a nuestros vecinos directos ('B' y 'E' en nuestro caso). Anotamos las distancias: a 'B' es 1, a 'E' es 3.
3.  Ahora, de todos los lugares que hemos descubierto (B y E), elegimos el que tiene la menor distancia total desde el origen. En este caso, 'B' (distancia 1) es más prometedor que 'E' (distancia 3). Así que "viajamos" a 'B'.
4.  Una vez en 'B', lo marcamos como un punto ya visitado y definitivo. Desde aquí, exploramos sus vecinos. Al hacerlo, descubrimos nuevos caminos. Por ejemplo, para llegar a 'C', ahora sabemos que podemos hacerlo pasando por 'B', con una distancia total de `1 (A->B) + 2 (B->C) = 3`.
5.  El paso crucial es la **actualización**: si ya conocíamos un camino a un nodo, pero el que acabamos de descubrir a través de nuestro punto actual es más corto, actualizamos nuestra tabla con esta nueva y mejor ruta.
6.  Repetimos el proceso: de toda la "frontera" de nodos que hemos descubierto pero aún no hemos visitado, siempre elegimos el que tenga la menor distancia acumulada desde el origen, y exploramos desde allí.

Este proceso garantiza que, una vez que declaramos un nodo como "visitado", la distancia que hemos encontrado para él es, definitivamente, la más corta posible.

## Las Herramientas: ¿Qué se usó en el código?

Para traducir esta lógica a código, necesitamos las herramientas adecuadas:

* **Para representar el Grafo:** Se utilizó un **diccionario de Python**. Las claves son los nodos (ej. 'A') y los valores son una lista de tuplas, donde cada tupla contiene un vecino y el peso de la arista hacia él (ej. `[('B', 1), ('E', 3)]`). Esta estructura, llamada lista de adyacencia, es ideal para consultar rápidamente los vecinos de cualquier nodo.

* **Para guardar las Distancias:** Un simple **diccionario** (`distancias`) es perfecto. Mapea cada nodo a un número: la distancia más corta encontrada hasta el momento desde el origen. Se inicializa con `infinito` para todos, excepto para el nodo de inicio, que es `0`.

* **Para encontrar el "siguiente paso más barato" eficientemente:** Aquí está la clave del rendimiento del algoritmo. Podríamos buscar en nuestro diccionario de distancias cada vez, pero sería lento. En su lugar, se usa una **Cola de Prioridad (o Min-Heap)**. En Python, esto se implementa con el módulo `heapq`. Esta estructura de datos está optimizada para hacer una cosa muy bien: devolverte siempre el elemento con el valor más bajo (en nuestro caso, la tupla `(distancia, nodo)` con la menor distancia) de forma casi instantánea. Cada vez que encontramos un camino más corto hacia un vecino, lo añadimos a esta cola. Así, en cada paso del bucle principal, simplemente le pedimos a la cola el siguiente destino más prometedor.

