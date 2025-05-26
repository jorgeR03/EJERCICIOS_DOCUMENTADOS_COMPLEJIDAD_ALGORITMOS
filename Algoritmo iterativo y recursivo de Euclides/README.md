## Introducción: El Problema del Máximo Común Divisor

El **Máximo Común Divisor (MCD)** entre dos números enteros es el número más grande que divide a ambos sin dejar residuo. Por ejemplo:

```
MCD(48, 18) = 6
```

Este concepto es fundamental en aritmética, álgebra y criptografía (como en RSA), y uno de los métodos más antiguos y eficientes para calcularlo es el **Algoritmo de Euclides**, formulado hace más de 2.000 años por el matemático griego Euclides.

---

## ¿Cómo Funciona el Algoritmo de Euclides?

La idea básica es muy elegante:

```
MCD(a, b) = MCD(b, a % b)
```

Se repite esta operación hasta que el segundo número se convierte en 0. En ese momento, el primero es el MCD.

Por ejemplo:
```
MCD(48, 18)
-> MCD(18, 48 % 18) = MCD(18, 12)
-> MCD(12, 18 % 12) = MCD(12, 6)
-> MCD(6, 12 % 6) = MCD(6, 0)
-> Resultado: 6
```

---

## Enfoque 1: Algoritmo Recursivo


El algoritmo se expresa naturalmente como una función recursiva.

###  Implementación

```python
def mcd_recursivo(a, b):
    if b == 0:
        return a
    else:
        return mcd_recursivo(b, a % b)
```

###  Ventajas
- Elegante, compacto y matemáticamente puro.
- Ideal para comprender el funcionamiento del algoritmo.

###  Desventajas
- Puede causar desbordamiento de pila con números muy grandes (aunque es raro en la práctica).

---

## Enfoque 2: Algoritmo Iterativo


La versión iterativa elimina la recursión usando un bucle `while`.

###  Implementación

```python
def mcd_iterativo(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

###  Ventajas
- Más eficiente para casos prácticos con grandes números.
- Evita el uso de la pila de llamadas recursivas.

###  Desventajas
- Un poco menos intuitivo desde un punto de vista matemático.

---

## Comparación de Complejidad

| Enfoque        | Tiempo     | Espacio       | Límite por profundidad |
|----------------|------------|---------------|-------------------------|
| Recursivo      | O(log n)   | O(log n) pila | ✅ Sí                   |
| Iterativo      | O(log n)   | O(1)          | ❌ No                   |

> Ambos enfoques tienen la misma eficiencia teórica, pero el iterativo suele ser más robusto para grandes volúmenes de datos.

---

## Código Combinado y Listo para Usar

```python
def mcd_recursivo(a, b):
    if b == 0:
        return a
    else:
        return mcd_recursivo(b, a % b)

def mcd_iterativo(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

---

## Conclusión: Un Clásico que Sigue Siendo Relevante

El **Algoritmo de Euclides** es un ejemplo perfecto de cómo una idea matemática antigua sigue siendo una herramienta esencial en la programación moderna. Su simplicidad, eficiencia y aplicabilidad lo hacen un clásico que todo programador debe conocer.

Ya sea usando recursión o iteración, este algoritmo demuestra que las soluciones más poderosas a menudo nacen de las ideas más simples.