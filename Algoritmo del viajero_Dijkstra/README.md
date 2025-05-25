# Algoritmo de Dijkstra: Encontrando el Camino Más Corto y Cómo Llegar

## Introducción: Más Allá de la Distancia, la Ruta
Ya hemos explorado el genio del algoritmo de Dijkstra para resolver un problema fundamental: calcular la distancia más corta desde un punto de origen a todos los demás en una red. Es como saber que el supermercado está a 500 metros y el parque a 1200 metros.

Pero, ¿y si no solo queremos saber la distancia, sino también las indicaciones exactas para llegar? Esta implementación del algoritmo va un paso más allá. No solo nos dirá el "cuánto", sino también el "cómo", reconstruyendo la secuencia exacta de nodos que forman el camino más corto.

## El Planteamiento: Recordando Nuestros Pasos
El razonamiento fundamental del algoritmo de Dijkstra no cambia: sigue siendo la brillante estrategia "codiciosa" de explorar siempre el nodo alcanzable con la menor distancia acumulada desde el origen. Se avanza paso a paso, actualizando las distancias a los vecinos si se encuentra una ruta más eficiente.

La novedad para reconstruir el camino es añadir una "memoria" al proceso. Además de anotar la distancia más corta a un nodo `V`, también necesitamos recordar cuál fue el nodo `U` que nos permitió encontrar ese camino más corto. A este nodo `U` lo llamamos el **predecesor** de `V`.

Si para cada nodo guardamos quién fue su predecesor en la ruta óptima, al final tendremos una especie de "mapa de migas de pan". Para encontrar el camino a cualquier destino, solo tenemos que empezar en ese destino y seguir las migas de pan hacia atrás, de predecesor en predecesor, hasta que lleguemos de nuevo al punto de partida.

## Las Herramientas: ¿Qué se usó en el código?
Esta versión más completa refina el uso de nuestras herramientas y añade una nueva función para la reconstrucción del camino:

* **Grafo (Diccionario):** Seguimos usando un diccionario como lista de adyacencia para representar el mapa de la red de forma eficiente.

* **Distancias (Diccionario):** Un diccionario para mapear cada nodo a su distancia mínima desde el origen.

* **Cola de Prioridad (`heapq`):** Sigue siendo el motor del algoritmo, garantizando que en cada paso procesemos el nodo más prometedor (el de menor distancia) con una eficiencia logarítmica.

* **Predecesores (Diccionario):** Esta es la adición clave para la reconstrucción. Es un diccionario que guarda, para cada nodo, cuál fue el nodo anterior en el camino más corto. Por ejemplo, si `predecesores['C'] = 'B'`, significa que para llegar a 'C' por la ruta más corta, vinimos desde 'B'.

* **Función `obtener_camino`:** Una vez que Dijkstra ha hecho su trabajo y ha llenado el diccionario de `predecesores`, esta función auxiliar entra en juego. Su lógica es simple:
    1.  Comienza en el nodo `destino`.
    2.  Lo añade a una lista de `camino`.
    3.  Busca su predecesor en el diccionario y salta a él.
    4.  Repite el proceso hasta llegar al nodo `origen`.
    5.  Como esto construye el camino en orden inverso (del destino al origen), al final simplemente se invierte la lista para obtener la secuencia correcta.

## Análisis de Complejidad
La lógica principal del algoritmo no cambia, por lo que la complejidad asintótica se mantiene:

* **Tiempo `O(E log V)`:** Donde `V` es el número de vértices y `E` el de aristas.
* **Espacio `O(V)`:** Para almacenar las distancias, los predecesores y los elementos en la cola.

