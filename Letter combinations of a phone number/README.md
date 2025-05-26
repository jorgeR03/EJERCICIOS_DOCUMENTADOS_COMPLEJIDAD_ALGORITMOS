Este algoritmo se resolvió utilizando una técnica conocida como backtracking (o retroceso), que es una forma de explorar todas las posibles combinaciones paso a paso. Lo que hacemos es:

Mapear los dígitos a letras, igual que como están en un teclado antiguo.

Usar una función recursiva que va construyendo combinaciones letra por letra.

Cada vez que se completa una combinación (es decir, que tiene tantas letras como dígitos), se guarda en una lista.

El proceso sigue hasta haber probado todas las combinaciones posibles.

El número de combinaciones posibles crece rápidamente. Por ejemplo, para el número "23", cada dígito puede representar 3 letras, lo que da lugar a 3 × 3 = 9 combinaciones. Si tuvieras 4 dígitos, con un promedio de 3 letras por dígito, ya estarías viendo 3⁴ = 81 combinaciones. En términos generales, si cada dígito tiene L letras asociadas y hay N dígitos, el número total de combinaciones es aproximadamente Lⁿ.

Un enfoque de fuerza bruta podría intentar construir todas las combinaciones manualmente, pero esto se vuelve rápidamente inviable a medida que el número de dígitos crece. Para resolver esto de forma elegante, utilizamos un enfoque basado en backtracking.

La Estrategia Recursiva: Pensar como un Árbol 🌳
El algoritmo sigue una estructura lógica y natural inspirada en la forma en que uno explora opciones en una conversación telefónica:

Mapeo de Teclas: Cada dígito del 2 al 9 se asocia con un conjunto de letras, según un teclado telefónico clásico.

Construcción por Niveles: El algoritmo explora letra por letra, avanzando al siguiente dígito solo después de haber elegido una opción para el actual.

Backtracking (Retroceso): Cuando se alcanza una combinación completa, se guarda. Si no, el algoritmo continúa probando diferentes opciones.

Este patrón es extremadamente eficiente para generar combinaciones cuando el orden importa y cada elemento tiene múltiples opciones posibles.

✅ ¿Qué se logra con este algoritmo?
Este algoritmo permite explorar todas las posibles formas en que un número de teléfono se podría traducir a texto, una técnica que se usaba mucho en la personalización de números telefónicos (como 1-800-FLOWERS). Además, es un buen ejemplo de cómo usar recursión para generar combinaciones de forma ordenada y eficiente.