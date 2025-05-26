## Introducción: ¿Qué es el Factorial?

El **factorial** de un número entero positivo `n` (denotado como `n!`) es el producto de todos los números enteros desde `1` hasta `n`.

Por definición:

```
n! = n × (n-1) × (n-2) × ... × 2 × 1
```

Y también por convención:

```
0! = 1
```

El factorial es ampliamente utilizado en combinatoria, matemáticas discretas, probabilidades y análisis de algoritmos. Es un excelente ejemplo para enseñar **recursión**, **iteración**, y **eficiencia computacional**.

---

## El Problema: ¿Cómo Calcular `n!`?

Queremos escribir un algoritmo que reciba un número `n` y devuelva el valor de su factorial `n!`. Resolveremos este problema de dos formas:

- Usando **recursión**, reflejando su definición matemática.
- Usando un **bucle iterativo**, optimizando el rendimiento.

---

## Enfoque 1: Algoritmo Recursivo — Simplicidad Matemática

### 🌱 Filosofía

La recursión consiste en que la función se llama a sí misma para resolver una versión más pequeña del problema. En el caso del factorial:

```
factorial(n) = n × factorial(n-1)
```

con el caso base:

```
factorial(0) = 1
```

###  Implementación

```python
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)
```

###  Ventajas
- Código compacto y directo.
- Buena forma de aprender recursión.

###  Desventajas
- **Puede provocar desbordamiento de pila** para valores grandes de `n`.
- **Complejidad de tiempo:** `O(n)` y **espacio:** `O(n)` (por las llamadas recursivas).

---

## Enfoque 2: Algoritmo Iterativo — Fuerza Controlada

###  Filosofía

En este enfoque, utilizamos un bucle para calcular el producto de todos los números desde `1` hasta `n`, acumulando el resultado en una variable.

###  Implementación

```python
def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
```

###  Ventajas
- Muy eficiente y evita problemas de pila.
- **Complejidad de tiempo y espacio:** `O(n)` y `O(1)` respectivamente.

###  Desventajas
- Menos intuitivo para representar la definición matemática directa.

---

## Comparación de Complejidad

| Enfoque        | Tiempo     | Espacio     | Riesgo de desbordamiento |
|----------------|------------|-------------|---------------------------|
| Recursivo      | O(n)       | O(n) pila   | ✅ Sí                     |
| Iterativo      | O(n)       | O(1)        | ❌ No                     |

---

## Código Combinado y Listo para Usar

```python
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
```

---

## Conclusión: Dos Caminos para una Misma Operación

El cálculo del factorial es una excelente forma de comparar **recursión** e **iteración** en la práctica. Si bien el enfoque recursivo es elegante y fiel a la definición matemática, el iterativo suele ser preferido en aplicaciones reales debido a su eficiencia y menor consumo de memoria.

Ambos enfoques nos enseñan que en programación, hay muchas formas de resolver un problema: lo importante es elegir la más adecuada según el contexto.