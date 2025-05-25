# Heurística del Vecino Más Cercano para el Problema del Viajante (TSP)

## Introducción: El Desafío del Recorrido Óptimo

El Problema del Viajante de Comercio (TSP) es uno de los problemas más famosos en optimización. Dada una lista de ciudades y las distancias entre ellas, busca la ruta más corta que visita cada ciudad exactamente una vez y regresa al origen. Es un problema NP-difícil, lo que significa que encontrar la solución perfecta es computacionalmente inviable para un número grande de ciudades.

Por ello, recurrimos a **heurísticas** como la del "Vecino Más Cercano", que nos proporcionan una solución "suficientemente buena" de manera muy rápida.

## El Planteamiento y las Herramientas

La lógica de esta heurística es "codiciosa" y muy intuitiva:
1.  Se parte de una ciudad inicial.
2.  Desde la ubicación actual, se viaja siempre a la ciudad no visitada que esté más cerca.
3.  Este proceso se repite hasta haber visitado todas las ciudades, y finalmente se regresa al punto de partida.

Para implementar esto, el código utiliza una **Matriz de Distancias** para representar el mapa y listas simples para llevar un registro de la `ruta` actual y los nodos ya `visitados`.


Para lograrlo eficientemente, se usan las siguientes herramientas:
* **Grafo (Lista de Adyacencia):** El código primero transforma la matriz de distancias a un formato de diccionario, más natural para este algoritmo.
* **Cola de Prioridad (`heapq`):** Es la pieza clave que permite obtener casi instantáneamente el siguiente nodo a visitar (el de menor distancia), dándole al algoritmo su eficiencia.
* **Diccionarios (`distancias` y `predecesores`):** Se usan para guardar los resultados: la distancia mínima a cada nodo y el "mapa" para reconstruir el camino hacia atrás.
* **Función `obtener_camino_dijkstra`:** Una vez Dijkstra termina, esta función auxiliar utiliza el mapa de predecesores para trazar la ruta desde cualquier destino de vuelta hasta el origen.

## Análisis de Complejidad
* **Tiempo `O(E log V)`:** Donde `V` es el número de nodos y `E` el de aristas.
* **Espacio `O(V)`:** Para las estructuras de datos que almacenan distancias, predecesores y la cola.


