# Serie de Fibonacci: Explorando su Magia con Algoritmos Recursivos e Iterativos 🌀

## Introducción: La Elegancia Matemática de la Serie de Fibonacci

La **serie de Fibonacci** es una de las secuencias numéricas más conocidas y bellas de la matemática. Fue descrita por primera vez en Occidente por el matemático italiano Leonardo de Pisa, también conocido como Fibonacci, en el siglo XIII. La serie comienza con 0 y 1, y a partir de ahí, **cada número es la suma de los dos anteriores**:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

Esta simple regla ha fascinado a matemáticos, artistas y científicos por siglos, ya que aparece tanto en patrones de la naturaleza como en estructuras algorítmicas. En informática, es una excelente forma de aprender conceptos como **recursión, iteración, eficiencia y optimización**.

## El Problema: ¿Cómo Calcular el n-ésimo Número de Fibonacci?

El desafío es construir una función que reciba un número `n` y devuelva el valor correspondiente al **n-ésimo número** en la secuencia de Fibonacci.

### Ejemplos:
- `fibonacci(0) = 0`
- `fibonacci(1) = 1`
- `fibonacci(5) = 5`
- `fibonacci(7) = 13`

Vamos a resolver este problema usando **dos enfoques** clásicos de programación:

- Un enfoque **recursivo**, que refleja directamente la definición matemática.
- Un enfoque **iterativo**, que es mucho más eficiente computacionalmente.

---

## Enfoque 1: Algoritmo Recursivo — Elegancia Matemática en Código

### 🌱 Filosofía

La recursión consiste en que una función se llama a sí misma para resolver subproblemas más pequeños. En este caso, definimos:

```
fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
```

con los casos base:
```
fibonacci(0) = 0
fibonacci(1) = 1
```

###  Implementación

```python
def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
```

###  Ventajas
- Código limpio y fácil de entender.
- Ideal para aprender recursión.

###  Desventajas
- **Altamente ineficiente para valores grandes de `n`**: repite cálculos una y otra vez.
- La complejidad temporal es exponencial: `O(2^n)`.
- Puede llevar a desbordamiento de pila por exceso de llamadas recursivas.

---

## Enfoque 2: Algoritmo Iterativo — Eficiencia con Simplicidad


En lugar de llamarse a sí misma, la función construye la solución **desde abajo hacia arriba**, acumulando los valores anteriores en variables.

###  Implementación

```python
def fibonacci_iterativo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### ✅ Ventajas
- Muy eficiente: **complejidad lineal `O(n)`**.
- No hay llamadas recursivas, lo cual evita errores de pila.
- Ideal para valores grandes de `n`.

### ❌ Desventajas
- Menos intuitivo desde un punto de vista matemático.
- Requiere control manual del estado (uso de variables temporales).


## Comparación de Complejidad

| Enfoque        | Tiempo        | Espacio       | Reutiliza resultados |
|----------------|---------------|---------------|----------------------|
| Recursivo      | O(2^n)        | O(n) pila     | ❌ No                |
| Iterativo      | O(n)          | O(1)          | ✅ Sí                |

> Nota: Existen mejoras al enfoque recursivo usando **memorización** o **programación dinámica**, que permiten almacenar los resultados intermedios y evitar recomputaciones.



## Código Combinado y Listo para Usar

```python
def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_iterativo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

---

## Conclusión: Dos Caminos, Una Misma Meta

El estudio de la serie de Fibonacci no solo nos permite explorar patrones numéricos bellos, sino que también es una puerta de entrada ideal al pensamiento algorítmico. Ambas soluciones son válidas, pero cada una tiene su lugar:

- La **recursiva** es perfecta para enseñar cómo un problema grande se puede dividir en problemas más pequeños.
- La **iterativa** es lo que uno usaría en producción si busca eficiencia y rendimiento.

Ambos caminos, el elegante y el práctico, nos conducen al mismo destino: el entendimiento profundo del poder del pensamiento computacional.
