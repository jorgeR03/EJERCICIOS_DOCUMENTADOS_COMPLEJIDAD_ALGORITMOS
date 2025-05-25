# Colección de Algoritmos Fundamentales en Python

Este script es una compilación de soluciones para varios problemas clásicos de programación. Cada algoritmo aborda un desafío diferente y se implementa utilizando técnicas y estructuras de datos comunes en el desarrollo de software y la programación competitiva.

A continuación se detalla cada uno de los algoritmos incluidos.

---

## 1. Verificador de Números Palíndromos

### El Planteamiento: Simetría Numérica

Un número palíndromo es aquel que posee una simetría especial: se lee de la misma forma de izquierda a derecha que de derecha a izquierda. Números como 121, 4554 o 9 son ejemplos de ello. El desafío es crear un método computacional para detectar esta propiedad.

La forma más ingeniosa y directa de abordar este problema no es a través de complejas operaciones matemáticas, sino mediante un cambio de perspectiva. Si convertimos el número en una **cadena de texto**, podemos aprovechar la facilidad con la que los lenguajes de programación manipulan el texto. Una vez que tenemos el número como una secuencia de caracteres, la pregunta "¿es un palíndromo?" se transforma en "¿es esta cadena de texto igual a su versión invertida?".

### Las Herramientas y la Implementación

* **Conversión a Cadena (`str()`):** Es el primer paso crucial para transformar el problema de un dominio numérico a uno textual.
* **Rebanado de Cadenas (`slicing`):** Python ofrece una sintaxis increíblemente concisa y poderosa para manipular secuencias. La expresión `str_numero[::-1]` crea una nueva cadena que es la versión invertida de la original, de una manera muy eficiente y legible.
* **Comparación Directa:** La solución final es una simple comparación de igualdad (`==`) entre la cadena original y su reverso.

### Complejidad
* **Tiempo `O(n)`:** Donde `n` es el número de dígitos del número. La conversión y el rebanado de la cadena toman un tiempo proporcional a su longitud.
* **Espacio `O(n)`:** Se necesita espacio adicional para almacenar la representación del número como cadena.

---

## 2. Eliminador de Duplicados en una Lista Ordenada

### El Planteamiento: Depuración Eficiente

A menudo nos encontramos con listas que contienen elementos repetidos. Si la lista de entrada ya está ordenada, podemos aprovechar esta propiedad para eliminar los duplicados de una forma muy eficiente. El objetivo es producir una nueva lista que contenga solo una instancia de cada elemento, manteniendo el orden original.

La estrategia es simple y se basa en un único recorrido por la lista.
1.  Se crea una nueva lista de `unicos`, inicializándola con el primer elemento de la lista original (que, por definición, es único hasta ese momento).
2.  Se recorre la lista original a partir del segundo elemento.
3.  En cada paso, se compara el elemento actual con el **último elemento que fue añadido a nuestra lista de `unicos`**.
4.  Si son diferentes, significa que hemos encontrado un nuevo número único, por lo que lo añadimos a nuestra lista de `unicos`. Si son iguales, simplemente lo ignoramos y continuamos.

Las Herramientas y la Implementación
Recorrido Único (`for` loop):** La solución evita la complejidad de múltiples pasadas o búsquedas anidadas.
Acceso al Último Elemento:** Se accede eficientemente al último elemento de la lista de resultados con `unicos[-1]` para realizar la comparación.

### Complejidad
* **Tiempo `O(n)`:** Donde `n` es el número de elementos en la lista, ya que solo la recorremos una vez.
* **Espacio `O(k)`:** Donde `k` es el número de elementos únicos. En el peor de los casos (ningún duplicado), `k` sería igual a `n`.

---

## 3. Removedor de Todas las Ocurrencias de un Elemento

### El Planteamiento: Filtrado de Listas
Este problema es una tarea de filtrado fundamental: dada una lista y un valor específico, crear una nueva lista que contenga todos los elementos de la original **excepto** todas las apariciones del valor a eliminar. La lista de entrada no tiene por qué estar ordenada.

La solución más elegante y "Pythónica" para este tipo de tareas es utilizar una **lista por comprensión** (list comprehension). Esta es una característica del lenguaje que permite construir una nueva lista de forma declarativa y concisa.

### Las Herramientas y la Implementación
* **Lista por Comprensión:** La expresión `[elem for elem in lista_nums if elem != valor_a_eliminar]` se lee casi como en lenguaje natural: "Crea una nueva lista con cada elemento de la lista original, si ese elemento no es igual al valor que queremos eliminar". Es una forma muy eficiente y legible de expresar un bucle y un condicional para la construcción de una lista.

### Complejidad
* **Tiempo `O(n)`:** Se debe iterar sobre cada elemento de la lista de entrada una vez.
* **Espacio `O(k)`:** Donde `k` es el número de elementos que no se eliminan.

---

## 4. Combinaciones de Letras del Teclado Telefónico

### El Planteamiento: Exploración Combinatoria
Este es un problema clásico que nos introduce al mundo de la combinatoria y la recursión. Dado un string de dígitos (ej. "23"), el objetivo es generar todas las posibles combinaciones de letras que esos dígitos podrían representar en un teclado telefónico estándar (2="abc", 3="def", etc.).

Este tipo de problema, donde se deben explorar múltiples decisiones en secuencia para construir un conjunto de soluciones, es un candidato perfecto para un algoritmo de **Backtracking**.

El backtracking es una técnica recursiva que construye una solución candidata de forma incremental. La idea es:
1.  Empezar con una combinación vacía.
2.  Para el primer dígito, probar con su primera letra posible (ej. para el "2", probar con la "a").
3.  Llamarse recursivamente para resolver el resto del problema (los dígitos restantes) con la combinación parcial actual ("a").
4.  Una vez que esa rama de exploración termina (se acaban los dígitos), se "retrocede" (backtrack) y se prueba con la siguiente letra del primer dígito ("b"), y se repite el proceso.
5.  Cuando se han probado todas las letras de todos los dígitos, hemos explorado el árbol completo de posibilidades.

### Las Herramientas y la Implementación
* **Mapeo (Diccionario):** Un diccionario es la herramienta ideal para mapear cada dígito a su correspondiente conjunto de letras.
* **Función Recursiva (Backtracking):** Se define una función auxiliar (anidada o no) que lleva la cuenta de la combinación que se está construyendo y del índice del dígito que se está procesando. El caso base de la recursión es cuando se han procesado todos los dígitos.

