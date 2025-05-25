# El Problema de las 8 Reinas: Un Desafío de Ajedrez Resuelto con Evolución Artificial

## Introducción: El Enigma del Tablero ♛

El problema de las 8 Reinas es un rompecabezas clásico del ajedrez que ha intrigado a matemáticos y programadores durante siglos. El desafío es simple de enunciar, pero no tanto de resolver: **¿cómo podemos colocar ocho reinas de ajedrez en un tablero estándar de 8x8 de tal manera que ninguna reina pueda atacar a otra?**

Recordemos que una reina en el ajedrez puede moverse (y, por lo tanto, atacar) cualquier número de casillas en horizontal, vertical o diagonal. Encontrar una configuración donde las ocho reinas coexistan pacíficamente es el objetivo.

## El Planteamiento: ¿Por qué es un Problema Complejo?

Si intentáramos resolver esto por "fuerza bruta", es decir, probando todas las formas posibles de colocar 8 reinas en las 64 casillas, el número de combinaciones sería astronómico (64C8, que es más de 178 mil millones). Incluso si somos un poco más listos y colocamos solo una reina por columna, todavía hay 8^8 (más de 16 millones) de posibilidades. Claramente, necesitamos un enfoque más inteligente.

Aquí es donde entran en juego los **Algoritmos Genéticos**. En lugar de una búsqueda exhaustiva, los algoritmos genéticos se inspiran en la teoría de la evolución por selección natural de Charles Darwin. La idea es "criar" una población de posibles soluciones, permitir que las mejores "se reproduzcan" y, a lo largo de muchas generaciones, observar cómo la población evoluciona hacia una solución óptima.

## La Estrategia Evolutiva: Componentes Clave

Un algoritmo genético tiene varios componentes que imitan los procesos biológicos:

1.  **Individuos (o Cromosomas):** Cada "individuo" representa una posible solución al problema. En nuestro caso, un individuo es una configuración del tablero de ajedrez. Una forma común y eficiente de representarlo es con una lista de 8 números, donde el índice de la lista representa la columna y el valor en ese índice representa la fila donde se encuentra la reina de esa columna. Por ejemplo, `[0, 4, 7, 5, 2, 6, 1, 3]` significa que la reina de la columna 0 está en la fila 0, la de la columna 1 en la fila 4, y así sucesivamente.

2.  **Función de Aptitud (Fitness):** Necesitamos una forma de medir qué tan "buena" es una solución. La función de aptitud evalúa a cada individuo y le asigna una puntuación. Para las 8 Reinas, una buena medida es el **número de pares de reinas que *no* se atacan entre sí**. Un tablero perfecto tendría 28 pares de reinas no atacantes (que es el número total de formas de elegir 2 reinas de 8, o 8C2).

3.  **Población:** Se comienza con una colección de individuos generados aleatoriamente. Esta es nuestra "generación cero".

4.  **Selección:** De la población actual, se eligen los individuos más "aptos" para ser los "padres" de la siguiente generación. Los individuos con mayor puntuación de aptitud tienen más probabilidades de ser seleccionados.

5.  **Cruce (Recombinación):** Dos padres seleccionados se "cruzan" para producir "hijos". Esto imita la reproducción sexual. Una forma común de cruce es elegir un punto de corte aleatorio en los cromosomas de los padres y combinar la primera parte de un padre con la segunda parte del otro para crear un nuevo individuo.

6.  **Mutación:** Para introducir nueva "diversidad genética" y evitar que el algoritmo se estanque en soluciones subóptimas, se aplica una pequeña probabilidad de mutación a los hijos. Una mutación podría ser, por ejemplo, cambiar aleatoriamente la posición de una reina en una columna.

7.  **Nueva Generación:** Los hijos (posiblemente mutados) forman la nueva generación, que reemplaza a la anterior.

Este ciclo de evaluación, selección, cruce y mutación se repite durante muchas generaciones. Con el tiempo, la aptitud promedio de la población tiende a mejorar, y es muy probable que se encuentre una solución óptima (un tablero con 0 ataques).

## Las Herramientas y la Implementación en Python

* **`random`:** Esta librería de Python es fundamental. Se usa para generar la población inicial, seleccionar puntos de cruce, decidir si ocurre una mutación y elegir nuevas posiciones para las reinas durante la mutación.
* **Representación de Individuos:** Como se mencionó, una lista de enteros es una forma eficiente de representar el tablero.
* **Funciones Clave:**
    * `evaluar_aptitud(tablero)`: Calcula cuántos pares de reinas no se atacan. Itera por todos los pares de reinas y verifica conflictos en filas y diagonales.
    * `generar_individuo()`: Crea una lista aleatoria de 8 posiciones de fila (una por columna).
    * `elegir_padres(poblacion)`: Selecciona los individuos con mayor aptitud (en este caso, los 3 mejores).
    * `cruzar(p1, p2)`: Combina dos individuos padres para crear un hijo.
    * `aplicar_mutacion(individuo)`: Introduce cambios aleatorios en un individuo.
    * `resolver_8_reinas()`: Es el motor principal del algoritmo genético. Gestiona la población, las generaciones y el ciclo evolutivo hasta que se encuentra una solución con aptitud perfecta (28).
* **`tkinter` para la Visualización:** Una vez que el algoritmo genético encuentra una solución, es muy útil poder verla. La librería `tkinter` de Python se utiliza para crear una interfaz gráfica simple que dibuja el tablero de ajedrez y coloca los símbolos de las reinas en las posiciones correctas.

## Análisis de Complejidad

Los algoritmos genéticos son heurísticas estocásticas (basadas en la aleatoriedad). No garantizan encontrar la solución óptima en un número fijo de pasos, ni tampoco la misma solución cada vez que se ejecutan (a menos que se fije la semilla del generador aleatorio).

* **Convergencia:** La "complejidad" se mide más en términos de cuántas generaciones se necesitan para converger a una buena solución. Esto depende de muchos factores: el tamaño de la población, las tasas de cruce y mutación, y la naturaleza del problema.
* **Costo por Generación:** El costo de cada generación está dominado por la evaluación de la aptitud de todos los individuos. Si la población tiene `P` individuos y la evaluación de cada uno toma `O(N^2)` tiempo (donde `N` es el número de reinas, 8 en este caso, para verificar todos los pares), entonces una generación cuesta aproximadamente `O(P * N^2)`.

