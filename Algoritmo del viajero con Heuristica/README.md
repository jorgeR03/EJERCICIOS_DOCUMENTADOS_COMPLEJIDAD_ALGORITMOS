# Heurística del Vecino Más Cercano para el Problema del Viajante (TSP)

## Introducción: El Desafío del Recorrido Óptimo 🗺️

El Problema del Viajante de Comercio (TSP por sus siglas en inglés) es uno de los problemas más famosos y estudiados en el campo de la optimización. Su planteamiento es engañosamente simple: dada una lista de ciudades y las distancias entre cada par de ellas, ¿cuál es la ruta más corta posible que visita cada ciudad exactamente una vez y regresa al punto de origen?

Este problema aparece en innumerables aplicaciones del mundo real, desde la logística para la entrega de paquetes y la planificación de rutas de transporte, hasta la fabricación de microchips y la secuenciación de ADN.

A pesar de su simpleza aparente, encontrar la solución **óptima** es extremadamente difícil. El número de rutas posibles crece de forma factorial, lo que significa que incluso para un número modesto de ciudades (por ejemplo, 20), la cantidad de rutas a verificar es astronómica, superando la capacidad de cómputo de las computadoras más potentes del mundo. Por esta razón, el TSP es un problema NP-difícil.

## El Planteamiento: ¿Cómo se llegó a la solución?

Dado que encontrar la ruta perfecta es, en la práctica, imposible para muchos casos, recurrimos a **heurísticas**. Una heurística es una especie de "atajo" mental o regla práctica que nos ayuda a encontrar una solución "suficientemente buena" de manera rápida, aunque no tengamos la garantía de que sea la mejor posible.

La **Heurística del Vecino Más Cercano** es una de las más intuitivas y sencillas para abordar el TSP. Su lógica es, una vez más, "codiciosa" (greedy), similar en espíritu a la de Dijkstra, pero aplicada de forma diferente.

El razonamiento es el siguiente:
1.  **Elige un punto de partida:** Comienza en una ciudad cualquiera.
2.  **Mira a tu alrededor:** Desde tu ubicación actual, examina todas las ciudades que aún no has visitado.
3.  **Toma la decisión más fácil:** Viaja a la ciudad más cercana de entre las que te quedan por visitar.
4.  **Actualiza tu posición:** La ciudad a la que acabas de llegar es tu nueva ubicación actual. Márcala como visitada para no volver a pasar por ella.
5.  **Repite:** Continúa este proceso de moverte siempre al vecino no visitado más cercano hasta que hayas recorrido todas las ciudades.
6.  **Vuelve a casa:** Una vez que todas las ciudades han sido visitadas, realiza el viaje final desde la última ciudad de vuelta a la ciudad original para cerrar el ciclo.

Esta estrategia es muy rápida, pero tiene una debilidad: puede tomar decisiones que son buenas a corto plazo pero que te obligan a realizar viajes muy largos al final del recorrido. Por eso, es una heurística; nos da una solución rápida y razonable, pero no necesariamente la óptima.

## Las Herramientas: ¿Qué se usó en el código?

Para implementar esta lógica, las estructuras de datos son bastante directas:

* **Para representar el Grafo:** En lugar de una lista de adyacencia, aquí se usa una **Matriz de Distancias (o Matriz de Adyacencia)**. Es una tabla de dos dimensiones (una lista de listas en Python) donde `matriz[i][j]` contiene la distancia directa entre la ciudad `i` y la ciudad `j`. Esta estructura es muy eficiente cuando el grafo es "denso", es decir, cuando casi todas las ciudades están conectadas entre sí, como es típico en el TSP.

* **Para el seguimiento:**
    * Una lista booleana `visitados_tsp` se usa para marcar las ciudades que ya han sido parte de la ruta. Esto evita visitarlas más de una vez.
    * Una lista `ruta_tsp` simplemente almacena la secuencia de ciudades visitadas en el orden en que se recorren.

El algoritmo consiste en un bucle principal que se repite hasta que todas las ciudades han sido visitadas. Dentro de él, otro bucle anidado busca el vecino más cercano entre los candidatos no visitados.

## Análisis de Complejidad

* **Tiempo `O(V^2)`:** Donde `V` es el número de ciudades (vértices). El bucle principal se ejecuta `V` veces. Dentro de él, para encontrar al vecino más cercano, debemos recorrer una fila de la matriz, lo que toma `V` pasos. Por lo tanto, la complejidad es cuadrática.
* **Espacio `O(V)`:** Se necesita espacio para almacenar la lista de visitados y la ruta, cuyo tamaño es proporcional al número de ciudades.

