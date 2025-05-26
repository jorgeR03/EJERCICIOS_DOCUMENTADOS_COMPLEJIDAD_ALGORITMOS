# Problema A: An Easy-Peasy Problem

## Introducción: ¿Qué Hace que un Problema sea "Fácil"?

En el mundo de la programación competitiva, la percepción de la dificultad de un problema puede ser subjetiva. Este problema nos presenta un escenario concreto: un juez de competencia, Travis, necesita saber si el problema que diseñó califica como "fácil" bajo un criterio específico y objetivo. [cite: 1, 6]

La regla, establecida por los otros jueces, es clara: **un problema es fácil solo si al menos la mitad de los concursantes que lo resolvieron lo hicieron durante la primera mitad del concurso.** [cite: 5]

Para verificar esto, se nos proporcionan dos datos clave: `s1`, el número de soluciones correctas (o "solves") al finalizar la primera mitad, y `s2`, el número total de soluciones al terminar la competencia. [cite: 10] Es importante notar que el total `s2` ya incluye las soluciones de `s1`. [cite: 9] Nuestra tarea es aplicar la regla y emitir un veredicto: "E" de fácil (Easy) o "H" de difícil (Hard). [cite: 11, 12]

## El Planteamiento: ¿Cómo se llegó a la solución?

A diferencia de problemas que requieren algoritmos complejos para encontrar una ruta o un valor óptimo, este desafío es un ejercicio de **traducción directa**. El objetivo no es diseñar un algoritmo complejo, sino convertir una regla expresada en lenguaje humano a una simple expresión lógica en código.

El proceso de razonamiento es el siguiente:

1.  **Identificar los componentes clave de la regla:** La regla es "al menos la mitad de las soluciones totales".
2.  **Traducir cada componente:**
    * "Las soluciones totales" corresponde a nuestra variable `s2`.
    * "La mitad de las soluciones totales" se traduce matemáticamente como `s2 / 2`.
    * La frase "al menos" significa "mayor o igual que", lo que en programación se representa con el operador `>=`.
    * El valor que debemos comparar contra esta mitad es "el número de soluciones en la primera mitad", que corresponde a nuestra variable `s1`.
3.  **Construir la expresión final:** Al unir todas las piezas, la regla completa se convierte en la condición lógica: `s1 >= s2 / 2`.

No se necesitan bucles, recursión ni estructuras de datos complejas. La solución entera se reduce a evaluar esta única condición y tomar una de dos decisiones posibles. Es la forma más pura de la lógica condicional.

