# Problema B: Age Expression

## Introducción: El Acertijo del Abuelo

El Dr. O, un abuelo con dos nietas llamadas Alyssa y Konari, tiene una forma peculiar de revelar su edad. [cite: 15] En lugar de dar un solo número, presenta un acertijo en forma de expresión matemática. [cite: 16, 17] Su edad se calcula mediante la fórmula:

`(a * edad de Alyssa) + (k * edad de Konari)`

donde `a` y `k` son dos números enteros positivos que él tiene en mente. [cite: 16, 17, 21]

El problema nos pide que, dadas las edades del Dr. O, Alyssa y Konari, determinemos si es posible que existan tales números `a` y `k` que satisfagan la ecuación. [cite: 18] Debemos responder con `1` si es posible o con `0` si no lo es. [cite: 21]

## El Planteamiento: ¿Cómo se llegó a la solución?

La tarea se reduce a resolver la ecuación diofántica lineal `a*A + k*K = O`, donde `A`, `K` y `O` son las edades de Alyssa, Konari y el Dr. O, respectivamente. Dado que las edades están restringidas a un valor máximo de 150[cite: 20], no necesitamos métodos matemáticos complejos. Una búsqueda directa y acotada es la estrategia más clara y eficiente.

El proceso de razonamiento es el siguiente:
1.  **Fijar una variable:** Es difícil buscar dos incógnitas (`a` y `k`) a la vez. La estrategia consiste en fijar una de ellas, por ejemplo `a`, y luego verificar si se puede encontrar un `k` válido.
2.  **Establecer límites para la búsqueda:** Sabemos que `a` y `k` deben ser enteros positivos (mayores o iguales a 1). [cite: 21] Esto nos permite acotar la búsqueda de `a`. Si `k` es como mínimo 1, entonces el término `k*K` es como mínimo `K`. Por lo tanto, el término `a*A` no puede ser mayor que `O - K`. Esto nos da un límite superior claro para el valor de `a`: `a <= (O - K) / A`. El código calcula este límite (`max_a_val`) antes de empezar a buscar, para no realizar iteraciones innecesarias.
3.  **Iterar y Verificar:** Se crea un bucle que prueba cada valor de `a` desde 1 hasta el límite que calculamos. Para cada `a`:
    * Se calcula la "edad restante" que `k*K` debe cubrir: `Restante = O - a*A`.
    * Se comprueban dos condiciones críticas para que exista un `k` válido:
        1.  El `Restante` debe ser un número positivo, ya que `k` y `K` son positivos.
        2.  El `Restante` debe ser perfectamente divisible por `K`, para que `k` sea un número entero.
4.  **Concluir la búsqueda:** Si en alguna de las iteraciones se cumplen ambas condiciones, hemos encontrado un par `(a, k)` válido. No necesitamos seguir buscando; podemos detener el bucle (`break`) y afirmar que la solución existe. Si el bucle termina sin encontrar ningún `a` que funcione, entonces concluimos que no existe ninguna solución.

## Las Herramientas: ¿Qué se usó en el código?

* **`input().split()` y `map(int, ...)`:** Se utilizan para leer eficientemente los tres números de las edades desde una única línea de entrada, convirtiéndolos de texto a enteros. [cite: 19]
* **Bucle `for`:** Es la estructura central que itera a través de los posibles valores de `a`, desde 1 hasta el límite máximo calculado.
* **Aritmética y Lógica Booleana:** Se usan operaciones aritméticas simples (`-`, `*`) y el operador módulo (`%`) para la comprobación de la divisibilidad. Una variable booleana (`found_solution`) actúa como una bandera para recordar si hemos encontrado una solución.

## Análisis de Complejidad

* **Complejidad Temporal: `O(D/A)`** donde `D` es la edad del Dr. O y `A` la de Alyssa. La complejidad está determinada por el bucle que itera sobre los posibles valores de `a`. Dado que las edades están acotadas a 150, este número de iteraciones es muy pequeño, haciendo que el algoritmo sea extremadamente rápido y eficiente para los límites del problema.
* **Complejidad Espacial: `O(1)`** (Constante). El algoritmo solo requiere una cantidad fija de memoria para almacenar las variables de entrada y el contador del bucle, sin depender del tamaño de las edades.

