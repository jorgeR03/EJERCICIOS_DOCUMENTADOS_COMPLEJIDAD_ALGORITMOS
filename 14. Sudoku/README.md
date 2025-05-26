# Resolviendo Sudokus con Backtracking: Una Búsqueda Inteligente

## Introducción: El Desafío Lógico del Sudoku 🔢

El Sudoku es más que un simple pasatiempo; es un fascinante problema de lógica y satisfacción de restricciones. El objetivo es rellenar una cuadrícula de 9x9 con números del 1 al 9, de tal manera que cada fila, cada columna y cada una de las nueve subcuadrículas de 3x3 contengan cada número exactamente una vez.

El desafío computacional es: dado un tablero parcialmente lleno, ¿podemos diseñar un algoritmo que encuentre la solución completa de manera sistemática y eficiente?

## El Planteamiento: ¿Cómo se llegó a la solución?

La primera idea que podría surgir es la "fuerza bruta": probar todas las combinaciones posibles de números en las casillas vacías. Sin embargo, el número de combinaciones es tan gigantescamente grande que esta estrategia es inviable. Necesitamos un enfoque que sea exhaustivo pero también inteligente, que descarte caminos sin salida lo antes posible.

La técnica perfecta para esto es el **Backtracking**. Podemos imaginar el proceso como si estuviéramos resolviendo un laberinto:
1.  Avanzamos por un camino.
2.  En cada intersección (una casilla vacía), tomamos una de las posibles direcciones (probamos con un número del 1 al 9).
3.  Seguimos avanzando por ese nuevo camino.
4.  Si en algún momento llegamos a un callejón sin salida (un punto donde ninguna de nuestras decisiones es válida), no nos damos por vencidos. Simplemente **"volvemos hacia atrás" (backtrack)** hasta la última intersección donde tomamos una decisión y probamos una dirección diferente.

Así es como se traduce esta analogía al algoritmo para resolver el Sudoku:
1.  **Encontrar un punto de decisión:** El algoritmo escanea el tablero para encontrar la primera casilla vacía.
2.  **Probar una opción:** Una vez encontrada la casilla, intenta colocar un número, empezando por el `1`.
3.  **Verificar la validez:** Antes de colocarlo, se pregunta: "¿Es este movimiento legal?". Se asegura de que el número no exista ya en la misma fila, la misma columna o la misma subcuadrícula de 3x3.
4.  **Avanzar con confianza:** Si el número es válido, lo coloca en el tablero y, aquí está la clave, **se llama a sí mismo recursivamente** para que intente resolver el resto del tablero a partir de este nuevo estado.
5.  **Propagar el éxito:** Si esa llamada recursiva devuelve `True` (¡éxito!), significa que la decisión fue correcta y se encontró una solución completa por ese camino. Entonces, la función actual también devuelve `True` para pasar la buena noticia hacia atrás.
6.  **Aprender del fracaso (Backtrack):** Si la llamada recursiva devuelve `False`, significa que la decisión tomada llevó a un callejón sin salida. Aquí ocurre la magia: el algoritmo **deshace su movimiento** (vuelve a poner un `0` en la casilla) y prueba con el siguiente número (el `2`, luego el `3`, etc.).
7.  **Admitir el callejón sin salida:** Si se prueban todos los números del 1 al 9 en la casilla actual y ninguno conduce a una solución, la función devuelve `False`, informando a la llamada anterior que la decisión que la condujo hasta aquí fue incorrecta, provocando que esa llamada anterior también haga "backtrack".

## Las Herramientas: ¿Qué se usó en el código?

* **Tablero (Lista de Listas):** La cuadrícula del Sudoku se representa de forma natural como una lista de 9 listas, donde cada lista interna es una fila del tablero.
* **Función `es_valido`:** Actúa como el "guardián de las reglas". Es una función auxiliar crucial que, antes de cada movimiento, verifica si colocar un número en una celda viola alguna de las tres reglas del Sudoku. Utiliza una ingeniosa división entera (`//`) para determinar rápidamente en qué subcuadrícula de 3x3 se encuentra cualquier celda.
* **Función `resolver_sudoku` (Recursión):** Es el corazón del algoritmo. Su capacidad para llamarse a sí misma es lo que permite la exploración profunda de las posibilidades. El valor de retorno booleano (`True` o `False`) es el mecanismo de comunicación esencial que permite que la "ola" de éxito o fracaso se propague hacia atrás a través de las llamadas recursivas, guiando el proceso de backtracking.

## Análisis de Complejidad

* **Complejidad Temporal: Exponencial (`O(9^m)`)** donde `m` es el número de casillas vacías. En el peor de los casos, el algoritmo tiene que explorar una gran parte del árbol de búsqueda. Cada una de las `m` casillas vacías puede tener hasta 9 posibilidades. Aunque el backtracking poda (corta) muchas ramas inviables de este árbol, la complejidad sigue siendo exponencial, lo que refleja la dificultad inherente del problema.
* **Complejidad Espacial: `O(m)`** o `O(1)`. El espacio principal utilizado es la pila de llamadas de la recursión, que en el peor de los casos tendrá una profundidad igual al número de casillas vacías (`m`). Si consideramos el tamaño del tablero (81 casillas) como una constante, la complejidad espacial también se puede describir como `O(1)`.

