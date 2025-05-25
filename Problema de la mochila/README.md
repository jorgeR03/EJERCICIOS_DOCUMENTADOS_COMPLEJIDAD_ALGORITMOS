# Problema de la Mochila 0/1: La Optimización del Ladrón Inteligente

## Introducción: El Dilema de la Selección Óptima 🎒

Imaginemos a un ladrón que entra en una casa llena de objetos valiosos. Cada objeto tiene un valor (cuánto dinero vale) y un peso. El ladrón lleva una mochila que solo puede soportar una cantidad limitada de peso. Ante esta situación, se enfrenta a un dilema clásico de optimización: **¿qué combinación de objetos debe robar para maximizar el valor total de su botín sin que la mochila se rompa?**

Este es el **Problema de la Mochila**. La variante "0/1" añade una regla crucial: por cada objeto, la decisión es binaria. O lo tomas entero (1) o lo dejas (0). No puedes llevarte la mitad de un televisor o un cuarto de una pintura.

Este problema, aunque parece un juego, es la base de innumerables decisiones en el mundo real, desde la selección de proyectos de inversión con un presupuesto limitado hasta la optimización de la carga en un vehículo de reparto.

## El Planteamiento: ¿Cómo se llegó a la solución?

Una primera idea, la de la "fuerza bruta", sería probar cada posible combinación de objetos. Sin embargo, si hay `N` objetos, existen `2^N` combinaciones posibles. Para una cantidad modesta de objetos (ej. 30), el número de combinaciones ya es astronómico, haciendo esta estrategia imposible de calcular.

Aquí es donde la **Programación Dinámica** se convierte en nuestra herramienta más poderosa. Esta técnica resuelve problemas complejos dividiéndolos en subproblemas más pequeños y simples. La clave está en que la solución óptima a un problema depende de las soluciones óptimas de sus subproblemas.

La estrategia es la siguiente:
1.  **Construir una Tabla de Decisiones:** Imaginemos que creamos una tabla (una matriz) donde las filas representan cada uno de los objetos que podemos elegir y las columnas representan cada posible capacidad de la mochila, desde 0 hasta la capacidad máxima. Llamaremos a esta tabla `dp`.
2.  **Llenar la Tabla Celda por Celda:** Cada celda `dp[i][w]` contendrá la respuesta a una pregunta muy específica: "¿Cuál es el máximo valor que puedo obtener usando solo los primeros `i` objetos, con una mochila que tiene una capacidad exacta de `w`?".
3.  **La Decisión en Cada Celda:** Para llenar cada celda, consideramos el `i`-ésimo objeto y nos hacemos una pregunta fundamental: **¿Nos conviene meter este objeto en la mochila?**
    * **Opción 1: No meter el objeto.** Si decidimos no incluirlo, el valor máximo que podemos obtener es simplemente el que ya habíamos calculado para los `i-1` objetos anteriores con esa misma capacidad `w`. Es decir, `dp[i-1][w]`.
    * **Opción 2: Meter el objeto (si cabe).** Si el peso del objeto actual es menor o igual a la capacidad `w`, podemos meterlo. El valor de esta opción será el valor del objeto actual **más** el valor máximo que podíamos obtener con los `i-1` objetos anteriores en el espacio que nos sobraría en la mochila (`w` menos el peso del objeto actual).
4.  **La Mejor Decisión:** La celda `dp[i][w]` se llena con el valor máximo entre estas dos opciones.

Al terminar de llenar toda la tabla, la celda en la esquina inferior derecha (`dp[numero_de_articulos][capacidad_maxima]`) contendrá la respuesta final a nuestro problema: el valor máximo posible.

## Reconstrucción: ¿Qué hay en la mochila?

Una vez que sabemos el valor máximo, podemos averiguar qué objetos lo componen. Para ello, hacemos un "camino hacia atrás" en nuestra tabla, empezando desde la última celda.
* En cada fila `i`, comparamos el valor de la celda actual con el de la celda de arriba (`dp[i-1][w]`).
* Si los valores son diferentes, significa que el objeto `i` fue indispensable para alcanzar ese valor óptimo. Por lo tanto, ¡lo metimos en la mochila! Lo añadimos a nuestra lista de botín y restamos su peso de la capacidad para seguir revisando hacia atrás con la capacidad correcta.
* Si los valores son iguales, significa que el objeto `i` no fue incluido, y simplemente subimos a la fila anterior.

## Las Herramientas: ¿Qué se usó en el código?
* **Tabla 2D (Lista de Listas):** La estructura de datos central es la tabla de programación dinámica `dp`, implementada como una lista de listas en Python.
* **Bucles Anidados (`for`):** Se utilizan para iterar sistemáticamente sobre cada artículo y cada unidad de capacidad, asegurando que cada celda de la tabla `dp` sea calculada.

## Análisis de Complejidad

* **Complejidad Temporal: `O(N * C)`** donde `N` es el número de artículos disponibles y `C` es la capacidad máxima de la mochila. La complejidad se debe a que debemos llenar cada celda de una tabla de tamaño `N` por `C`.
* **Complejidad Espacial: `O(N * C)`** para almacenar la propia tabla de programación dinámica.

