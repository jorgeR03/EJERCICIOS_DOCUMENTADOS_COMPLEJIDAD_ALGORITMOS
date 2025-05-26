# Problema A: An Easy-Peasy Problem

## Introducción: ¿Qué Hace que un Problema sea "Fácil"?

En el mundo de la programación competitiva, la percepción de la dificultad de un problema puede ser subjetiva. [cite: 3] Este problema nos presenta un escenario concreto: un juez de competencia, Travis, necesita saber si el problema que diseñó califica como "fácil" bajo un criterio específico y objetivo. [cite: 1, 6]

La regla, establecida por los otros jueces, es clara: **un problema es fácil solo si al menos la mitad de los concursantes que lo resolvieron lo hicieron durante la primera mitad del concurso.** [cite: 5]

Para verificar esto, se nos proporcionan dos datos clave: `s1`, el número de soluciones correctas ("solves") al finalizar la primera mitad del concurso, y `s2`, el número total de soluciones al terminar la competencia. [cite: 10] El valor de `s2` ya incluye las soluciones de `s1`. [cite: 9] Nuestra tarea es aplicar la regla y emitir un veredicto: "E" de fácil (Easy) o "H" de difícil (Hard). [cite: 11, 12]

## El Planteamiento: ¿Cómo se llegó a la solución?

Este desafío es un ejercicio de **traducción directa** de una regla a una expresión lógica. El razonamiento inicial nos lleva a la condición `s1 >= s2 / 2`. Esta es una comparación perfectamente válida que resuelve el problema.

Sin embargo, esta versión del código utiliza una formulación matemática alternativa pero equivalente: `s1 * 2 >= s2`. ¿Cómo se llega a ella y por qué podría ser preferible?

1.  **Punto de Partida:** La desigualdad original es `s1 >= s2 / 2`.
2.  **Eliminar Decimales:** La división `/` en Python siempre produce un número de punto flotante (un decimal). Aunque para este problema no representa un inconveniente, en programación a veces es deseable trabajar exclusivamente con números enteros para evitar posibles problemas de precisión.
3.  **Transformación Algebraica:** Para eliminar la división, podemos multiplicar ambos lados de la desigualdad por 2. Al hacerlo, la expresión se transforma en `s1 * 2 >= s2`.

Esta nueva condición es lógicamente idéntica a la original, pero tiene la ventaja de que todas las operaciones se realizan únicamente con números enteros. En lugar de preguntar "¿es s1 mayor o igual que la mitad de s2?", preguntamos "¿es el doble de s1 mayor o igual que s2?". El resultado es el mismo, pero el cálculo es ligeramente diferente.

## Las Herramientas: ¿Qué se usó en el código?

La simplicidad del problema se refleja en las herramientas de Python utilizadas:

* **`input().split()`:** Lee la única línea de entrada que contiene los dos números y los separa en una lista de cadenas.
* **`map(int, ...)`:** Convierte eficientemente las cadenas de texto a números enteros para poder realizar la multiplicación y la comparación.
* **`if/else`:** La estructura de control que evalúa la condición `s1 * 2 >= s2` y ejecuta el bloque de código correspondiente para imprimir "E" o "H".

## Análisis de Complejidad

* **Complejidad Temporal: `O(1)` (Constante).** El programa ejecuta un número fijo de operaciones (lectura, conversión, una multiplicación, una comparación y una impresión). La eficiencia no depende del valor de los números de entrada.
* **Complejidad Espacial: `O(1)` (Constante).** El espacio en memoria utilizado es mínimo, solo para almacenar dos variables numéricas.

