¿Qué problema resuelve?
Este algoritmo resuelve el problema de encontrar si un valor específico (el objetivo) está presente en una lista, y en caso afirmativo, devuelve la posición en la que se encuentra. Es especialmente útil cuando los datos no están ordenados y no se puede aplicar una búsqueda más eficiente como la binaria.

¿Cómo se llega a la solución?
La solución consiste en recorrer la lista desde el primer elemento hasta el último, comparando uno a uno con el valor buscado. En cuanto se encuentra una coincidencia, se devuelve el índice actual. Si se termina de recorrer toda la lista sin encontrar el valor, se devuelve -1 para indicar que no está presente.

¿Qué herramientas usa el código?
El algoritmo usa un simple bucle for para recorrer la lista, una condición if para comparar cada elemento con el objetivo, y retorna el índice correspondiente o -1. No requiere estructuras adicionales, lo que lo hace sencillo y con una complejidad O(n) en tiempo y O(1) en espacio, siendo adecuado para listas pequeñas o no ordenadas.