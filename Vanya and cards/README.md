# Algoritmo: Minimizando Cartas para el Equilibrio

## Introducción: La Búsqueda del Balance Perfecto

Imaginemos un juego de equilibrio. Se nos entrega un conjunto de cartas, cada una con un valor que puede ser positivo (suma puntos) o negativo (resta puntos). Al sumar todas nuestras cartas, obtenemos una puntuación total que probablemente no sea cero.

Nuestro objetivo es alcanzar un balance perfecto, es decir, una suma total de cero. Para lograrlo, se nos da acceso a un mazo especial de cartas de "ajuste", donde cada carta tiene un valor fijo `x`. La pregunta es: **¿cuál es el número mínimo de estas cartas de ajuste que necesitamos usar para anular nuestra puntuación y dejar el total en cero?**

## El Planteamiento: ¿Cómo se llegó a la solución?

La estrategia para resolver este problema es un proceso matemático directo que se puede desglosar en tres pasos lógicos:

1.  **Calcular el Desequilibrio Total:** Lo primero es saber qué tan lejos de cero estamos. Para ello, simplemente sumamos los valores de todas las cartas que tenemos en la mano. El resultado de esta suma es nuestro "desequilibrio". Si la suma es `-35`, significa que tenemos un déficit de 35 puntos. Si es `+42`, tenemos un superávit de 42. En cualquier caso, la magnitud del problema, el "cuánto" necesitamos corregir, es el valor absoluto de esta suma.

2.  **Dividir para Vencer:** Una vez que conocemos el desequilibrio total, necesitamos saber cuántas de nuestras cartas de ajuste de valor `x` se necesitan para cubrirlo. La operación más directa es dividir el desequilibrio total por el valor `x`. Por ejemplo, si nuestro desequilibrio es de 35 y cada carta de ajuste vale 10, la división `35 / 10` nos da `3.5`.

3.  **El Redondeo Crucial (La Lógica del "Techo"):** Este es el paso clave del razonamiento. No podemos usar "media carta". Si necesitamos cubrir 3.5 "unidades de ajuste" y solo usamos 3 cartas (que suman 30), todavía nos faltarían 5 puntos para alcanzar el equilibrio. Por lo tanto, estamos obligados a tomar la siguiente carta entera. Debemos usar 4 cartas (que suman 40) para garantizar que el desequilibrio original sea completamente neutralizado. Esta operación de "siempre redondear hacia arriba al siguiente entero" se conoce en matemáticas como la **función techo (ceiling)**.

El algoritmo implementa precisamente esta lógica, usando `math.ceil` para asegurar que siempre se tome el número mínimo de cartas necesarias para resolver el desequilibrio por completo.

## Las Herramientas: ¿Qué se usó en el código?

* **`sum()`:** Función nativa de Python que calcula de forma eficiente la suma de todos los elementos en la lista de cartas inicial.
* **`abs()`:** Función nativa que devuelve el valor absoluto de un número. Se usa para obtener la magnitud del desequilibrio total, sin importar si es positivo o negativo.
* **`math.ceil()`:** Es la función central de la solución. Proviene de la librería `math` y se encarga de realizar la operación "techo", redondeando cualquier número decimal hacia el siguiente entero superior.
* **`map(int, input().split())`:** La herramienta estándar en Python para leer una línea de texto con múltiples números separados por espacios y convertirlos en una lista de enteros.

## Análisis de Complejidad

* **Complejidad Temporal: `O(N)`** donde `N` es el número de cartas en la lista inicial. La operación dominante es `sum(cards)`, que necesita recorrer cada uno de los `N` elementos una vez para sumarlos. El resto de las operaciones (división, `ceil`) son de tiempo constante.
* **Complejidad Espacial: `O(N)`** para almacenar en memoria la lista inicial de `N` cartas leída de la entrada.

